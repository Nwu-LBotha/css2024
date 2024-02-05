# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:42:14 2024
@author: Louise

# Heed my words: 
# Is this app useful for none computational scientist....No
# Is this app useful for those who want to use my data.....Yes
# Is this app useful for myself....Yes, I lose data
# Did I enjoy making this app.....Yes and No

"""
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from PIL import Image 

# c:\users\louise\anaconda3\lib\site-packages
# c:\users\louise\anaconda3\lib\site-packages
st.set_page_config(layout="wide")

st.set_option('deprecation.showPyplotGlobalUse', False)

# The side bar menu code. 
#1. Make a sidebar with a name such as contents.
#2. If the options are slected the page changes on the right.

with st.sidebar:
    selected = option_menu(menu_title="Contents", options=["About Me","Publications","Data: Pt/Pd bulks","Data: Pt/Ni & Pt/Co"])

######################################## The about me section Code

if selected == "About Me": 
    st.header("Dr LM Botha 🌟")
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

#maybe add todays date, Nah too much work

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
 
# ######################################## The PUBLICATIONS code           
              
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


#  ######################################## The Pt/Ni and Pt/Co Catalysts data    

# # This is data to input later when I use this app for my work.
# # Since I have not added this data, a 404 error is obtained with a cute image and a header.

# if selected == "Data: Pt/Ni & Pt/Co":
#     st.title(f"Repository {selected}")
#     st.divider()
#     st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
#     st.title("Under Construction, Sorry for the Inconvenience!")
#     st.image('nodata.gif')
    
#  ######################################## The Pt/Pd bulk profiles data    

# if selected == "Data: Pt/Pd bulks":
#     st.title(f"Repository {selected}")
#     st.divider()

#     Fig1_paper2 = "Relative energies of PtPd3, PtPd, Pt3Pd, and Pt7Pd alloy structures."
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     st.header("Figure 1: " + Fig1_paper2.translate(SUB))
    
#     #Inserting the data using Pandas to create dataframe 
    
#     fig1_data = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure1',index_col=None)

#     # Plot using Matplotlib
#     plt.plot(fig1_data['Percentage Pd'], fig1_data['Formation energy'], color='blue', marker='o', linestyle='solid')
#     plt.xlabel("Percentage Pd (%)")
#     plt.ylabel("Formation energy (eV)")
#     plt.title("Figure 1")
#     st.pyplot()
#     st.caption("Table: Formation energies")
#     st.table(fig1_data)

#     Fig2_paper2 = "Murnaghan’s fit for the pristine (a) Pt and (b) Pd, as well as (c) PtPd3, (d) PtPd, (e) PtPd (L10), (f) Pt3Pd, and (g) Pt7Pd alloy structures (conventional unit cell structures)"
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     st.header("Figure 2: " + Fig2_paper2.translate(SUB))
#     Vol_fig = "A3"
#     SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        
#     data_fig1 = st.radio("Please select data to see",("a) Pt","b) Pd","c) PtPd3","d) PtPd","e) Pt3Pd","f) Pt7Pd"))
#     if data_fig1 == "a) Pt":

# ###Figure 2. Make pandas dataframe which outputs a Table and gives a plot, if able

#     ###Data for the A selection (Pt)
#     ###The axis lable has a subscript value so the Vol_fig.translate(SUP) code fixes that
#     ###Plots the table with captions and titles.
    
#         fig2_dataA = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_pt',index_col=None)
      
#         plt.plot(fig2_dataA['volume'], fig2_dataA['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(a) Pt")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
#         st.table(fig2_dataA)        

#     #### Data for the B selection (Pd)
#     if data_fig1 == "b) Pd":

#         fig2_dataB = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_pd',index_col=None)

#         plt.plot(fig2_dataB['volume'], fig2_dataB['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(b) Pd")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
#         st.table(fig2_dataB)
        
#         #### Data for the C selection (PtPd3)
#     if data_fig1 == "c) PtPd3":
#         fig2_dataC = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_A',index_col=None)
#         plt.plot(fig2_dataC['volume'], fig2_dataC['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(c) PtPd3")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
#         st.table(fig2_dataC)
    

#     #### Data for the D selection (PtPd)
#     if data_fig1 == "d) PtPd":
#         fig2_dataD = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_B',index_col=None)
#         plt.plot(fig2_dataD['volume'], fig2_dataD['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(d) PtPd")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (d) PtPd")
#         st.table(fig2_dataD)

# #### Data for the E selection (Pt3Pd)
    
#     if data_fig1 == "e) Pt3Pd":
#         fig2_dataE = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_C',index_col=None)
#         plt.plot(fig2_dataE['volume'], fig2_dataE['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(e) PtPd")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (e) Pt")
#         st.table(fig2_dataE)

# ####Data for the F selection Pt7Pd

#     if data_fig1 == "f) Pt7Pd":
#         fig2_dataF = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_D',index_col=None)
#         plt.plot(fig2_dataF['volume'], fig2_dataF['energy'], color='blue', marker='o', linestyle='solid')
#         plt.xlabel("Volume "+Vol_fig.translate(SUP))
#         plt.ylabel("Energy (eV)")
#         plt.title("Figure 2(f) Pt7Pd")
#         st.pyplot()
#         st.caption("Table: Murnaghan’s fit for the pristine (f) Pt7Pd")
#         st.table(fig2_dataF)
        

# ########################################################################################

# #####Figure 3. Comparison between calculated phonon band spectra and phonon DOS spectra for the pristine Pt and Pd structures.
# ## Ads the headers supscript, like previous code.

#     Fig3_paper2 = "Comparison between calculated phonon band spectra and phonon DOS spectra for the pristine Pt and Pd structures."
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     st.header("Figure 3: " + Fig3_paper2.translate(SUB))

#     #Ads a radio botton for the slection to reduce clunkyness
#     #Import dataframe for the correct sheet using a defined datarange using skiprows and nrows.

#     data_fig3 = st.radio("Please select Bandstructure data to see",("Pt","Pd","PtPd3","PtPd","Pt3Pd","Pt7Pd"))
#     if data_fig3 == "Pt":
#         fig3_data_Ptband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band',index_col=None,nrows=3129)
#         plt.scatter(fig3_data_Ptband['band'], fig3_data_Ptband['freq (cm-1)'],s=1, color='blue', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure Pt")
#         st.pyplot()

#         button_band_pt = st.button("Show Table")
#         if button_band_pt:
#             st.table(fig3_data_Ptband)


#     if data_fig3 == "Pd":
#         fig3_data_Pdband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band',index_col=None,skiprows=range(2, 3131),nrows=6260)
#         plt.scatter(fig3_data_Pdband['band'], fig3_data_Pdband['freq (cm-1)'],s=1, color='black', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure Pd")
#         st.pyplot()
        
#         button_band_pd = st.button("Show Table")
#         if button_band_pd:
#             st.table(fig3_data_Pdband)

# # Import dataframe for the correct sheet using a defined datarange using skiprows and nrows.
# #nrows shows the number of rows used. 
# #PLots the data using scatter, small size and colour of green.
# #Ads titles to the axis and the graph,
# #Draws the plot

#     if data_fig3 == "PtPd3":
#         fig3_data_PtPd3 = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,nrows=4375)
#         plt.scatter(fig3_data_PtPd3['band'], fig3_data_PtPd3['freq (cm-1)'],s=1, color='cyan', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure PtPd3")
#         st.pyplot()
        
#         button_band_PtPd3 = st.button("Show Table")
#         if button_band_PtPd3:
#             st.table(fig3_data_PtPd3)

# #Skiprows, skips the previous data which is between 2 and  4376
# #nrows shows the number of rows used. This after the skipriws so it is from 4376 to 4426
# #PLots the data using scatter, small size and colour of green.
# #Ads titles to the axis and the graph,
# #Draws the plot 

#     if data_fig3 == "PtPd":
#         fig3_data_PtPd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 4376),nrows=4426)
#         plt.scatter(fig3_data_PtPd['band'], fig3_data_PtPd['freq (cm-1)'],s=1, color='green', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure PtPd")
#         st.pyplot()

# #The button is used to show the table data. This is due to the massive long data so users can hurt themselves.
# # Maybe add a save button for the data whihc exports to csv file????

        
#         button_band_PtPd = st.button("Show Table")
#         if button_band_PtPd:
#             st.table(fig3_data_PtPd)

# #Skiprows, skips the previous data which is between 2 and  5906
# #nrows shows the number of rows used. This after the skipriws so it is from 5907 to 10255
# #PLots the data using scatter, small size and colour of green.
# #Ads titles to the axis and the graph,
# #Draws the plot

#     if data_fig3 == "Pt3Pd":
        
#         fig3_data_Pt3Pd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 5906),nrows=10255)
#         plt.scatter(fig3_data_Pt3Pd['band'], fig3_data_Pt3Pd['freq (cm-1)'], s=1,color='violet', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure Pt3Pd")
#         st.pyplot()
        
#         button_band_Pt3Pd = st.button("Show Table")
#         if button_band_Pt3Pd:
#             st.table(fig3_data_Pt3Pd)
            
#     if data_fig3 == "Pt7Pd":
#         fig3_data_Pt7Pd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 10284),nrows=17793)
#         plt.scatter(fig3_data_Pt7Pd['band'], fig3_data_Pt7Pd['freq (cm-1)'],s=1, color='red', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure Pt7Pd")
#         st.pyplot()
        
#         button_band_Pt7Pd = st.button("Show Table")
#         if button_band_Pt7Pd:
#             st.table(fig3_data_Pt7Pd)
            
# #This is the second set of data which I added for fun. It is however not coplete since it is a lot of data to add.

#     data_fig3_2 = st.radio("Please select POS data to see",("Pt","Pd","PtPd3","PtPd","Pt3Pd","Pt7Pd"))
    
#     if data_fig3_2 == "Pt":
#         fig3_2_data_Ptband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_dos',index_col=None,nrows=202)
#         plt.plot(fig3_2_data_Ptband['Pt'], fig3_2_data_Ptband['freq cm-1'], color='blue', linestyle='solid')
#         plt.xlabel("PDOS (a.u.)")
#         plt.ylabel("Frequency (/cm)")
#         plt.title("Band structure Pt")
#         st.pyplot()

#         button2_band_pt = st.button("Show my Table")
#         if button2_band_pt:
#             st.table(fig3_2_data_Ptband)


# # This data is not finished so a sorry icon will be displayed with a header.

#     if data_fig3_2 == "Pd":
#         st.title("Sorry data not yet updated, please come back another time")
#         st.image('nodata.gif')
        

#     if data_fig3_2 == "PtPd3":
#         st.title("Sorry data not yet updated, please come back another time")
#         st.image('nodata.gif')     


#     if data_fig3_2 == "PtPd":
#         st.title("Sorry data not yet updated, please come back another time")
#         st.image('nodata.gif')


#     if data_fig3_2 == "Pt3Pd":
#         st.title("Sorry data not yet updated, please come back another time")
#         st.image('nodata.gif')


#     if data_fig3_2 == "Pt7Pd":
#         st.title("Sorry data not yet updated, please come back another time")
#         st.image('nodata.gif')
