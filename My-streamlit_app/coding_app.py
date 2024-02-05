# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:42:14 2024

@author: Louise
"""

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image  
import matplotlib.pyplot as plt


#import streamlit as st
#st.image('sunrise.jpg', caption='Sunrise by the mountains')
# c:\users\louise\anaconda3\lib\site-packages
#c:\users\louise\anaconda3\lib\site-packages

st.set_option('deprecation.showPyplotGlobalUse', False)

# The side bar menu code. 
#1. Make a sidebar with a name such as contents.

#st.sidebar.header("Contents") # Nag not needed

#3. Lets give topics for the app which will be handy for navigation.
#4. I want stuff to happen when selecting the options in the side bar.


with st.sidebar:
    selected = option_menu(menu_title="Contents", options=["About Me","Publications","Data: Pt/Pd bulks","Data: Pt/Ni & Pt/Co"])


########################################ABOUT ME

if selected == "About Me": 
    st.header("Dr Louise Botha")
    st.divider() 
    # st.title(f"you have selected {selected}") #we will see
    col1, col2 = st.columns(2)


#Column 1 Stuff

        # Replace the URL with the raw URL of your image file on GitHub
    image_url = 'https://github.com/Nwu-LBotha/css2024/raw/main/My-streamlit_app/media/lm_botha.PNG'

    # Display the image using st.image
    with col1:
       st.image(image_url, caption='LM Botha Image', use_column_width=True)

    #img= Image.open('media/undraw_Chat_bot_re_e2gj.png')
    #col1.image('lm_botha.png',caption= 'Dr LM Botha')
    #louise = Image.open('lm_botha.png')
    col1.caption("email: louise.botha@nwu.ac.za") #Nah, will see 
  
    with col1:
      st.link_button("ORCID ID: 0000-0002-1249-2706", "https://orcid.org/0000-0002-1249-2706")


    col1.header("Qualifications")           
    col1.write("Ph.D Chemistry – NWU (2020)")          
    col1.write("M.Sc Chemistry – NWU (2016)")
    col1.write("B.Sc Hons. Chemistry – NWU (2013)")
    col1.write("B.Sc Chemistry & IT – NWU (2012)")


#Column 2 Stuff

 # #Column 2 Stuff

    col2.header("Current position?") 
    col2.write("Currently a Postdoctoral Research Fellow at Hydrogen South Africa. My research focuses on using Density Functional Theory (DFT) to investigate alternative metal Catalysts used in Passive Autocatalytic Recombiners (PARs).")
    col2.divider()    
    col2.header("Hydrogen South Africa?") 
     
         # Replace the URL with the raw URL of your image file on GitHub
    hysa_url = 'https://github.com/Nwu-LBotha/css2024/blob/main/My-streamlit_app/media/HYSA.PNG?raw=true'

     # Display the image using st.image
    with col2:
        st.image(hysa_url, caption='HySA', use_column_width=True)    
     
    col2.write("The Department of Science and Technology of South Africa developed the National Hydrogen and Fuel Cells Technologies (HFCT) Research, Development and Innovation (RDI) Strategy. The National Strategy was branded Hydrogen South Africa (HySA). The overall goal of HySA is to develop and guide innovation along the value chain of hydrogen and fuel cell technologies in South Africa. The overall vision of the HFCT RDI strategy is to bring about wealth, jobs and IPR creation through the initiation of new high-technology industries based on minerals found on South African soil, especially Platinum Group Metals (PGMs)")
   
    with col2:
       st.link_button("Go to HYSA website", "https://hysainfrastructure.com")
    
             
               
 ########################################PUBLICATIONS           

if selected == "Publications":
    st.title(f"Repository {selected}")
    st.divider()
      
    st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
    st.write("ABSTRACT:")
    st.write("Density functional theory (DFT) calculations were used to investigate the surface performance of Pt, Ni, Co, and PtxTM1-x (0 ≤ x ≤ 1) alloys, as well as reaction intermediates (O, H, OH, OH + H, H2O) on these surfaces for H2/O2 recombination. The activity of the PtxTM1-x alloys towards H2/O2 recombination reaction was probed using adsorption energies and reaction energies. The Pt3Co, Pt3Ni and PtNi3 alloys were found to be stable along the (111) miller index, with strong surface adsorption occurring on the PtNi3 (111) surface and weaker adsorption on the Pt3Co (111) surface. Enhanced reactivity was observed on the Pt3Ni and Pt3Co (111) surfaces for the (O*  +  H*  →  OH*) reaction step, while the Pt (111) surface was most suited for the (OH*  +  H*  →  H2O) reaction step. The OH* formation reaction step was inhibited on the PtNi3 (111) surface due to the strong surface absorption of the reaction intermediates. Overall, these results suggest that the Pt3Co (111) surface is a promising alternative catalyst for H2/O2 recombination compared to pristine Pt due to its performance in the O + H adsorption and OH* formation steps.") 
    #st.write("DOI: 10.1016/j.susc.2023.122354")
   
    st.link_button("Click to Go to Publication Journal", "https://doi.org/10.1016/j.susc.2023.122354")

    # Render the link
    #st.image('Recomb_graphic_abstract.jpg',caption='Grapahical abstract')
    AA_url = 'https://github.com/Nwu-LBotha/css2024/blob/main/My-streamlit_app/media/Recomb_graphic_abstract.jpg?raw=true'
    st.image(AA_url, caption='Graphical Abstract', use_column_width=True) 
        
    st.divider()
    
    st.header("Ab Initio Study of Structural, Electronic, and Thermal Properties of Pt/Pd-Based Alloys")
    st.write("ABSTRACT:")
    st.write("Alloys are beneficial in numerous applications since they combine the desirable properties of different metals. In this regard, Pt/Pd alloys have been investigated as a replacement for Pt, which is the standard catalyst used in various catalytic processes. However, there are still gaps in our understanding of the structural, mechanical, and thermodynamic properties of Pt/Pd alloys. This study was conducted using density functional theory (DFT) calculations to investigate the electronic, elasticity, mechanical, and thermodynamic properties of Pt/Pd alloys and compared them to pristine Pt and Pd structures. The results indicate that the considered Pt/Pd alloy structures, PtPd3, PtPd, Pt3Pd, and Pt7Pd, are energetically favourable based on their formation energies. These structures also satisfy Born’s stability criteria and are elastically stable. The phonon density of states showed that the considered Pt/Pd alloy structures are dynamically stable, with no imaginary modes present. Additionally, the Pt atom dominates at lower frequencies, while the Pd atom dominates at higher frequencies, as seen in the phonon band structure. The electronic density of states revealed that the considered Pt/Pd alloy structures have a metallic character and are non-magnetic. These findings contribute to a better understanding of the properties and stability of Pt/Pd alloy structures that are relevant in various fields, including materials science and catalysis.")

    st.link_button("Click to Go to Publication Journal", "https://doi.org/10.3390/condmat8030076")
  #   st.image('Graphical_abstract_bulkPaper.png',caption='Graphical Abstract')
    BB_url = 'https://github.com/Nwu-LBotha/css2024/blob/main/My-streamlit_app/media/Graphical_abstract_bulkPaper.png?raw=true'
    st.image(BB_url, caption='Graphical Abstract', use_column_width=True) 


 ########################################Pt/Ni and Pt/Co Catalysts     

if selected == "Data: Pt/Ni & Pt/Co":
    st.title(f"Repository {selected}")
    st.divider()
    st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
    st.title("Under Construction, Sorry for the Inconvenience!")
    no_url = 'https://github.com/Nwu-LBotha/css2024/blob/main/My-streamlit_app/media/nodata.gif?raw=true'
    st.image(no_url, use_column_width=True)  
    

 ########################################Pt/Pd bulk profiles    

if selected == "Data: Pt/Pd bulks":
    st.title(f"Repository {selected}")
    st.divider()
    st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
    st.title("Under Construction, Sorry for the Inconvenience!")
    no_url = 'https://github.com/Nwu-LBotha/css2024/blob/main/My-streamlit_app/media/nodata.gif?raw=true'
    st.image(no_url, use_column_width=True)  
