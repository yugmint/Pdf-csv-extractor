# Import Lib:

import streamlit as st
import pandas as pd
import pdfplumber as plumber
import re

#title:
st.title("Lets Extract data from Report PDF to CSV...!!")

# File uploader for multiple files
files = st.file_uploader("Upload your report files", accept_multiple_files=True)

# Processing each uploaded file
for file in files:
    if file:
        # Opening PDF file
        data = plumber.open(file)

#Extracing Data from report texts:

        Obs_mass=[]
        sam_pos=[]
        flp=[]
        
        for i in range(len(data.pages)):
            page_no=data.pages[i]
            txt=page_no.extract_text().split()
            for j, x in enumerate(txt):
                if x == "(Da)":
                    ind_1=j+10
                    ind_temp=ind_1+5
                    if len(txt[ind_temp]) == 9 and "." in txt[ind_temp]:
                        Obs_mass.append([txt[ind_1],txt[ind_temp]])
                    else:
                        Obs_mass.append(txt[ind_1])

                    ind_2= j-8
                    sam_pos.append(txt[ind_2])
                    
                    ind_3= j+12
                    flp.append(txt[ind_3])
                else:
                    pass

    #Creating DataFrames from lists:
        df=pd.DataFrame({"Sample Position" : sam_pos,
                    "Observed Mass (Da)": Obs_mass,
                    "FLP UV % Area" : flp})
        
    #Refining Extracted Texts:    
        df["Sample Position"]=df["Sample Position"].apply(lambda x: x[:-1])

    #Finding cells with Nulls.
        data_1=data

        position=[]
        for i in range(len(data_1.pages)):
            try:
                table=data_1.pages[i].extract_table()
                if table[0][2] == 'Sample type':
                    position.append(table[1][-2])
                else:
                    pass
            except IndexError:
                continue
            except TypeError:
                continue

    #Creating DataFrames from lists:
        sample_df=pd.DataFrame({"Sample Position" : position})

    #Merging DataFrames:
        df_new = pd.merge(df, sample_df, on="Sample Position", how='outer')

    #Cleaning / Dropping Typo Errors:
        df_new.drop(df_new.loc[df_new["Sample Position"].str.len()<5].index, inplace=True)    

    #Sorting As Per Requiried:
        def custom_sort_logic(value):
            match = re.match(r'(\d+)\s*:\s*(\w+)\s*,\s*(\d+)', value)
            if match:
                section1 = int(match.group(1))
                section2 = match.group(2)
                section3 = int(match.group(3))
                return (section1, section3, section2)
            else:
                return (float('inf'), '', float('inf'))

        def sort_dataframe(df, column_name):
            df_sorted = df.sort_values(by=column_name, key=lambda x: x.apply(custom_sort_logic))
            
            return df_sorted
        sorted_df = sort_dataframe(df_new, 'Sample Position')

        # Generate CSV file name based on uploaded PDF file name
        pdf_filename = file.name
        csv_filename = f"Updated_{pdf_filename}.csv"

        # Exporting to CSV
        st.write(f"Exporting the file into {csv_filename}")
        csv_data = sorted_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=csv_filename,
            mime="text/csv"
        )

