# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:42:14 2024

@author: Louise
"""

import streamlit as st
import pandas as pd

st.header("Dr Louise Botha")
st.divider() 
# st.title(f"you have selected {selected}") #we will see
col1, col2 = st.columns(2)


#Column 1 Stuff

louise = Image.open('lm_botha.png')
# st.image(img)
col1.image(louise)
col1.caption("ORCID ID: 0000-0002-1249-2706") #Nah, will see 
col1.caption("email: louise.botha@nwu.ac.za") #Nah, will see 


#Column 2 Stuff

#col2.header("ORCID ID")
#col2.write("0000-0002-1249-2706")  
#col2.divider()  
      
  

col2.header("Qualifications")           
col2.write("Ph.D Chemistry – NWU (2020)")          
col2.write("M.Sc Chemistry – NWU (2016)")
col2.write("B.Sc Hons. Chemistry – NWU (2013)")
col2.write("B.Sc Chemistry & IT – NWU (2012)")
 

col2.write("Currently a Postdoctoral Research Fellow at Hydrogen South Africa. Research focus is towards using Density Dunctional Theory to investigate metals for usage in Catalytic Applications. ")
col2.divider()    
col2.header("Vision of HYSA") 
hysa = Image.open('HYSA.png')
col2.image(hysa)
col2.write("The Department of Science and Technology of South Africa developed the National Hydrogen and Fuel Cells Technologies (HFCT) Research, Development and Innovation (RDI) Strategy. The National Strategy was branded Hydrogen South Africa (HySA). The overall goal of HySA is to develop and guide innovation along the value chain of hydrogen and fuel cell technologies in South Africa. The overall vision of the HFCT RDI strategy is to bring about wealth, jobs and IPR creation through the initiation of new high-technology industries based on minerals found on South African soil, especially Platinum Group Metals (PGMs)")
link_url_hysa = "https://hysainfrastructure.com/"
link_text_hysa = "Go to hysainfrastructure.com"
link_html_hysa = f'<a href="{link_url_hysa}" target="_blank">{link_text_hysa}</a>'
col2.markdown(link_html_hysa, unsafe_allow_html=True)
    
              
 