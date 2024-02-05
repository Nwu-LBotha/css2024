# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:42:14 2024

@author: Louise
"""

import streamlit as st
import pandas as pd
#pip install streamlit-option-menu
import sys

sys.path.insert(1, r'C:\Users\Louise\anaconda3\Lib\site-packages\streamlit_option_menu')

from streamlit_option_menu import option_menu
from streamlit_option_menu import option_menu
from PIL import Image
import matplotlib.pyplot as plt

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
    
              
               
 ########################################PUBLICATIONS           
              


if selected == "Publications":
    st.title(f"Repository {selected}")
    st.divider()
      
    st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
    st.write("ABSTRACT:")
    st.write("Density functional theory (DFT) calculations were used to investigate the surface performance of Pt, Ni, Co, and PtxTM1-x (0 ≤ x ≤ 1) alloys, as well as reaction intermediates (O, H, OH, OH + H, H2O) on these surfaces for H2/O2 recombination. The activity of the PtxTM1-x alloys towards H2/O2 recombination reaction was probed using adsorption energies and reaction energies. The Pt3Co, Pt3Ni and PtNi3 alloys were found to be stable along the (111) miller index, with strong surface adsorption occurring on the PtNi3 (111) surface and weaker adsorption on the Pt3Co (111) surface. Enhanced reactivity was observed on the Pt3Ni and Pt3Co (111) surfaces for the (O*  +  H*  →  OH*) reaction step, while the Pt (111) surface was most suited for the (OH*  +  H*  →  H2O) reaction step. The OH* formation reaction step was inhibited on the PtNi3 (111) surface due to the strong surface absorption of the reaction intermediates. Overall, these results suggest that the Pt3Co (111) surface is a promising alternative catalyst for H2/O2 recombination compared to pristine Pt due to its performance in the O + H adsorption and OH* formation steps.") 
    #st.write("DOI: 10.1016/j.susc.2023.122354")
    
    link_url1 = "https://doi.org/10.1016/j.susc.2023.122354"
    link_text1 = "DOI: 10.1016/j.susc.2023.122354"
    link_html1 = f'<a href="{link_url1}" target="_blank">{link_text1}</a>'

    # Render the link
    st.markdown(link_html1, unsafe_allow_html=True)
    artikel1 = Image.open('Recomb_graphic_abstract.jpg')
    st.image(artikel1)
    
    st.divider()
    
    st.header("Ab Initio Study of Structural, Electronic, and Thermal Properties of Pt/Pd-Based Alloys")
    st.write("ABSTRACT:")
    st.write("Alloys are beneficial in numerous applications since they combine the desirable properties of different metals. In this regard, Pt/Pd alloys have been investigated as a replacement for Pt, which is the standard catalyst used in various catalytic processes. However, there are still gaps in our understanding of the structural, mechanical, and thermodynamic properties of Pt/Pd alloys. This study was conducted using density functional theory (DFT) calculations to investigate the electronic, elasticity, mechanical, and thermodynamic properties of Pt/Pd alloys and compared them to pristine Pt and Pd structures. The results indicate that the considered Pt/Pd alloy structures, PtPd3, PtPd, Pt3Pd, and Pt7Pd, are energetically favourable based on their formation energies. These structures also satisfy Born’s stability criteria and are elastically stable. The phonon density of states showed that the considered Pt/Pd alloy structures are dynamically stable, with no imaginary modes present. Additionally, the Pt atom dominates at lower frequencies, while the Pd atom dominates at higher frequencies, as seen in the phonon band structure. The electronic density of states revealed that the considered Pt/Pd alloy structures have a metallic character and are non-magnetic. These findings contribute to a better understanding of the properties and stability of Pt/Pd alloy structures that are relevant in various fields, including materials science and catalysis.")

    link_url2 = "https://doi.org/10.3390/condmat8030076"
    link_text2 = "DOI: 10.3390/condmat8030076"
    link_html2 = f'<a href="{link_url2}" target="_blank">{link_text2}</a>'
    st.markdown(link_html2, unsafe_allow_html=True)
    artikel2 = Image.open('Graphical_abstract_bulkPaper.png')
    st.image(artikel2)



 ########################################Pt/Ni and Pt/Co Catalysts     

if selected == "Data: Pt/Ni & Pt/Co":
    st.title(f"Repository {selected}")
    st.divider()

    st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")

    st.title("Under Construction, Sorry for the Inconvenience!")
    artikel1_data2 = Image.open('nodata.gif')
    st.image(artikel1_data2)
    
# Fig 1 data: Relative energies of a) PtxNi1-x and b) PtxCo1-x primitive structures 
# Fig 2 Data: Top and side view of a) Pt, b) Ni, c) Co, d) Pt3Ni, e) PtNi3, and f) Pt3Co (111) surfaces, where navy is Pt, Green is Ni and light blue is Co.
#Table 1. Comparison of calculated lattice parameters (in Å) against DFT results and interatomic potentials.
#Table 2. Surface energies (γ) were calculated after optimization, for each solid solution along with their work functions (φ) and d-band centers (εd).
#Fig. 3. Partial density of states (PDOS) for the d-electrons and the d-band center of the pristine Pt (111) and PtxTM1-x (111) surfaces, plotted for the up-spin channel, where d-band center value is indicated by the thick black line which is labelled.
#Fig. 4. Comparison of the pristine surfaces and PtxTM1-x (111) surfaces in terms of the d-band centre and the work function
#Table 3. Calculated adsorption energies (Eads) in eV for the adsorbed O*, H*, HO* and H2O*, and co-adsorbed (O* + H*) and (HO* + H*) on the (111) metal surfaces, compared to literature values (indicated as ref).
#Table 4. Work function (Φ), the difference in the work function from the pristine surface and adsorbed surface (Δ Φ), intermolecular distances obtained from H2O and OH adsorption onto the Pt (111), Pt3Co (111), Pt3Ni(111) and the PtNi3(111) surfaces.
#Table 5. Calculated reaction energies (ER) and activation energies (Ea), in eV, for the recombination reaction R2 (O* + H* → HO*) and R4 (HO* + H* → H2O*) on the investigated metal surfaces.
#Fig. 7. Calculated reaction profile for the a) OH formation and b) H2O formation reactions on the PtxTM1- x (111) surfaces, compared to the Pt (111) surface.


 ########################################Pt/Pd bulk profiles    
 
 
 
if selected == "Data: Pt/Pd bulks":
    st.title(f"Repository {selected}")
    st.divider()


    Fig1_paper2 = "Relative energies of PtPd3, PtPd, Pt3Pd, and Pt7Pd alloy structures."
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    st.header("Figure 1: " + Fig1_paper2.translate(SUB))
    
    #Using Pandas to create my dataframe 
    
    fig1_data = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure1',index_col=None)

    # Plot using Matplotlib
    plt.plot(fig1_data['Percentage Pd'], fig1_data['Formation energy'], color='blue', marker='o', linestyle='solid')
    plt.xlabel("Percentage Pd (%)")
    plt.ylabel("Formation energy (eV)")
    plt.title("Figure 1")
    st.pyplot()
    st.caption("Table: Formation energies")
    st.table(fig1_data)


    Fig2_paper2 = "Murnaghan’s fit for the pristine (a) Pt and (b) Pd, as well as (c) PtPd3, (d) PtPd, (e) PtPd (L10), (f) Pt3Pd, and (g) Pt7Pd alloy structures (conventional unit cell structures)"
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    st.header("Figure 2: " + Fig2_paper2.translate(SUB))
    Vol_fig = "A3"
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        
    
    data_fig1 = st.radio("Please select data to see",("a) Pt","b) Pd","c) PtPd3","d) PtPd","e) Pt3Pd","f) Pt7Pd"))
    if data_fig1 == "a) Pt":
###Figure 2. Make pandas dataframe which outputs a Table and gives a plot, if able

    ###A Pt
        fig2_dataA = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_pt',index_col=None)
      
        plt.plot(fig2_dataA['volume'], fig2_dataA['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(a) Pt")
        st.pyplot()
        
        st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
        st.table(fig2_dataA)        

# ###B Pd
    if data_fig1 == "b) Pd":

        fig2_dataB = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_pd',index_col=None)

        plt.plot(fig2_dataB['volume'], fig2_dataB['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(b) Pd")
        st.pyplot()
        st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
        st.table(fig2_dataB)
        
# ###C PtPd3
    if data_fig1 == "c) PtPd3":
        fig2_dataC = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_A',index_col=None)
        plt.plot(fig2_dataC['volume'], fig2_dataC['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(c) PtPd3")
        st.pyplot()
        st.caption("Table: Murnaghan’s fit for the pristine (a) Pt")
        st.table(fig2_dataC)
    

# ###D PtPd
    if data_fig1 == "d) PtPd":
        fig2_dataD = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_B',index_col=None)
        plt.plot(fig2_dataD['volume'], fig2_dataD['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(d) PtPd")
        st.pyplot()
        st.caption("Table: Murnaghan’s fit for the pristine (d) PtPd")
        st.table(fig2_dataD)

# ###E Pt3Pd
    
    if data_fig1 == "e) Pt3Pd":
        fig2_dataE = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_C',index_col=None)
        plt.plot(fig2_dataE['volume'], fig2_dataE['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(e) PtPd")
        st.pyplot()
        st.caption("Table: Murnaghan’s fit for the pristine (e) Pt")
        st.table(fig2_dataE)

# ###F Pt7Pd
    if data_fig1 == "f) Pt7Pd":
        fig2_dataF = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure2_D',index_col=None)
        plt.plot(fig2_dataF['volume'], fig2_dataF['energy'], color='blue', marker='o', linestyle='solid')
        plt.xlabel("Volume "+Vol_fig.translate(SUP))
        plt.ylabel("Energy (eV)")
        plt.title("Figure 2(f) Pt7Pd")
        st.pyplot()
        st.caption("Table: Murnaghan’s fit for the pristine (f) Pt7Pd")
        st.table(fig2_dataF)
        
# ###Figure 3. Make pandas dataframe which outputs a Table and gives a plot, if able

# #Figure 3. Comparison between calculated phonon band spectra and phonon DOS spectra for the pristine Pt and Pd structures.
    Fig3_paper2 = "Comparison between calculated phonon band spectra and phonon DOS spectra for the pristine Pt and Pd structures."
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    st.header("Figure 3: " + Fig3_paper2.translate(SUB))

    data_fig3 = st.radio("Please select Bandstructure data to see",("Pt","Pd","PtPd3","PtPd","Pt3Pd","Pt7Pd"))
    if data_fig3 == "Pt":
        fig3_data_Ptband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band',index_col=None,nrows=3129)
        plt.scatter(fig3_data_Ptband['band'], fig3_data_Ptband['freq (cm-1)'],s=1, color='blue', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure Pt")
        st.pyplot()

        button_band_pt = st.button("Show Table")
        if button_band_pt:
            st.table(fig3_data_Ptband)


    if data_fig3 == "Pd":
        fig3_data_Pdband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band',index_col=None,skiprows=range(2, 3131),nrows=6260)
        plt.scatter(fig3_data_Pdband['band'], fig3_data_Pdband['freq (cm-1)'],s=1, color='black', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure Pd")
        st.pyplot()
        
        button_band_pd = st.button("Show Table")
        if button_band_pd:
            st.table(fig3_data_Pdband)


    if data_fig3 == "PtPd3":
        fig3_data_PtPd3 = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,nrows=4375)
        plt.scatter(fig3_data_PtPd3['band'], fig3_data_PtPd3['freq (cm-1)'],s=1, color='cyan', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure PtPd3")
        st.pyplot()
        
        button_band_PtPd3 = st.button("Show Table")
        if button_band_PtPd3:
            st.table(fig3_data_PtPd3)


    if data_fig3 == "PtPd":
        fig3_data_PtPd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 4376),nrows=4426)
        plt.scatter(fig3_data_PtPd['band'], fig3_data_PtPd['freq (cm-1)'],s=1, color='green', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure PtPd")
        st.pyplot()
        
        button_band_PtPd = st.button("Show Table")
        if button_band_PtPd:
            st.table(fig3_data_PtPd)


    if data_fig3 == "Pt3Pd":
        
        fig3_data_Pt3Pd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 5906),nrows=10255)
        plt.scatter(fig3_data_Pt3Pd['band'], fig3_data_Pt3Pd['freq (cm-1)'], s=1,color='violet', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure Pt3Pd")
        st.pyplot()
        
        button_band_Pt3Pd = st.button("Show Table")
        if button_band_Pt3Pd:
            st.table(fig3_data_Pt3Pd)
            
    if data_fig3 == "Pt7Pd":
        fig3_data_Pt7Pd = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_band_alloys',index_col=None,skiprows=range(2, 10284),nrows=17793)
        plt.scatter(fig3_data_Pt7Pd['band'], fig3_data_Pt7Pd['freq (cm-1)'],s=1, color='red', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure Pt7Pd")
        st.pyplot()
        
        button_band_Pt7Pd = st.button("Show Table")
        if button_band_Pt7Pd:
            st.table(fig3_data_Pt7Pd)
            
#gg

    data_fig3_2 = st.radio("Please select POS data to see",("Pt","Pd","PtPd3","PtPd","Pt3Pd","Pt7Pd"))
    
    if data_fig3_2 == "Pt":
        fig3_2_data_Ptband = pd.read_excel("Paper2_bulkdata.xlsx",sheet_name='figure3_dos',index_col=None,nrows=202)
        plt.plot(fig3_2_data_Ptband['Pt'], fig3_2_data_Ptband['freq cm-1'], color='blue', linestyle='solid')
        plt.xlabel("PDOS (a.u.)")
        plt.ylabel("Frequency (/cm)")
        plt.title("Band structure Pt")
        st.pyplot()

        button2_band_pt = st.button("Show my Table")
        if button2_band_pt:
            st.table(fig3_2_data_Ptband)


    if data_fig3_2 == "Pd":
        st.title("Sorry data not yet updated, please come back another time")
        artikel2_data2 = Image.open('nodata.gif')
        st.image(artikel2_data2)
        

    if data_fig3_2 == "PtPd3":
        st.title("Sorry data not yet updated, please come back another time")
        artikel2_data2 = Image.open('nodata.gif')
        st.image(artikel2_data2)        


    if data_fig3_2 == "PtPd":
        st.title("Sorry data not yet updated, please come back another time")
        artikel2_data2 = Image.open('nodata.gif')
        st.image(artikel2_data2)


    if data_fig3_2 == "Pt3Pd":
        st.title("Sorry data not yet updated, please come back another time")
        artikel2_data2 = Image.open('nodata.gif')
        st.image(artikel2_data2)


    if data_fig3_2 == "Pt7Pd":
        st.title("Sorry data not yet updated, please come back another time")
        artikel2_data2 = Image.open('nodata.gif')
        st.image(artikel2_data2)

# ###Figure 4. Make pandas dataframe which outputs a Table and gives a plot, if able

#     Fig4_paper2 = "Comparison between the calculated phonon band spectra and phonon DOS spectra for the considered PtPd3 alloy structure."
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     st.header("Figure 4: " + Fig4_paper2.translate(SUB))

#Figure 5. Comparison between the calculated phonon band spectra and phonon DOS spectra for the considered Pt3Pd alloy structure.
#Figure 6. Comparison between the calculated phonon band spectra and phonon DOS spectra for the PtPd structures in the hexagonal rhombohedral and L10 phases.

#Figure 7. Comparison between the calculated phonon band spectra and phonon DOS spectra for the considered Pt7Pd alloy structure.
#Figure 8. Calculated temperature dependence of the (a) entropy (S), (b) Helmholtz free energy (F), and (c) constant-volume specific heat capacity (Cv).
#Figure 9. The calculated projected density of states (PDOS) for each atom in the pristine Pt and Pd, as well as the considered Pt/Pd alloy structures.

#Table 1. Calculated equilibrium lattice constants for the conventional cells, in angstroms (Å), Volume in cubic angstroms (Å3), space groups, and formation energies of pristine Pt and Pd, as well as the Pt/Pd alloy structures in electron volt per formula unit (f.u).
#Table 2. The elastic constants (Cij), bulk modulus (B), shear modulus (G), Young modulus (E), and Poisson (v) for pristine Pt and Pd, as well as the Pt/Pd alloy structures. The table shows the minimum and maximum values for G, E and v.   
#Table 3. Atomic charge (q) per atom for the pristine Pt and Pd, as well as for the Pt/Pd alloy structures.


# st.title("Welcome to My data repository!!!!!")
# st.write("This is a Streamlit application that includes data for my latest published papers.")

# col1, col2 = st.columns(2)
# col1.header("Article 1")
# col1.write("Hu")


# col2.header("Article 1")
# col2.write("Hu")


