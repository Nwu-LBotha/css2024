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

col1.caption("ORCID ID: 0000-0002-1249-2706") #Nah, will see 
col1.caption("email: louise.botha@nwu.ac.za") #Nah, will see 


#Column 2 Stuff
  

col2.header("Qualifications")           
col2.write("Ph.D Chemistry – NWU (2020)")          
col2.write("M.Sc Chemistry – NWU (2016)")
col2.write("B.Sc Hons. Chemistry – NWU (2013)")
col2.write("B.Sc Chemistry & IT – NWU (2012)")
 

col2.write("Currently a Postdoctoral Research Fellow at Hydrogen South Africa. Research focus is towards using Density Dunctional Theory to investigate metals for usage in Catalytic Applications. ")
col2.divider()    
col2.header("Vision of HYSA") 
col2.write("The Department of Science and Technology of South Africa developed the National Hydrogen and Fuel Cells Technologies (HFCT) Research, Development and Innovation (RDI) Strategy. The National Strategy was branded Hydrogen South Africa (HySA). The overall goal of HySA is to develop and guide innovation along the value chain of hydrogen and fuel cell technologies in South Africa. The overall vision of the HFCT RDI strategy is to bring about wealth, jobs and IPR creation through the initiation of new high-technology industries based on minerals found on South African soil, especially Platinum Group Metals (PGMs)")
link_url_hysa = "https://hysainfrastructure.com/"
link_text_hysa = "Go to hysainfrastructure.com"
link_html_hysa = f'<a href="{link_url_hysa}" target="_blank">{link_text_hysa}</a>'
col2.markdown(link_html_hysa, unsafe_allow_html=True)


st.header("Publications:")

st.header("Hydrogen and oxygen recombination reaction on Pt–Ni and Pt–Co based alloys using density functional theory")
st.write("ABSTRACT:")
st.write("Density functional theory (DFT) calculations were used to investigate the surface performance of Pt, Ni, Co, and PtxTM1-x (0 ≤ x ≤ 1) alloys, as well as reaction intermediates (O, H, OH, OH + H, H2O) on these surfaces for H2/O2 recombination. The activity of the PtxTM1-x alloys towards H2/O2 recombination reaction was probed using adsorption energies and reaction energies. The Pt3Co, Pt3Ni and PtNi3 alloys were found to be stable along the (111) miller index, with strong surface adsorption occurring on the PtNi3 (111) surface and weaker adsorption on the Pt3Co (111) surface. Enhanced reactivity was observed on the Pt3Ni and Pt3Co (111) surfaces for the (O*  +  H*  →  OH*) reaction step, while the Pt (111) surface was most suited for the (OH*  +  H*  →  H2O) reaction step. The OH* formation reaction step was inhibited on the PtNi3 (111) surface due to the strong surface absorption of the reaction intermediates. Overall, these results suggest that the Pt3Co (111) surface is a promising alternative catalyst for H2/O2 recombination compared to pristine Pt due to its performance in the O + H adsorption and OH* formation steps.") 
#st.write("DOI: 10.1016/j.susc.2023.122354")

link_url1 = "https://doi.org/10.1016/j.susc.2023.122354"
link_text1 = "DOI: 10.1016/j.susc.2023.122354"
link_html1 = f'<a href="{link_url1}" target="_blank">{link_text1}</a>'

# Render the link
st.markdown(link_html1, unsafe_allow_html=True)

st.divider()

st.header("Ab Initio Study of Structural, Electronic, and Thermal Properties of Pt/Pd-Based Alloys")
st.write("ABSTRACT:")
st.write("Alloys are beneficial in numerous applications since they combine the desirable properties of different metals. In this regard, Pt/Pd alloys have been investigated as a replacement for Pt, which is the standard catalyst used in various catalytic processes. However, there are still gaps in our understanding of the structural, mechanical, and thermodynamic properties of Pt/Pd alloys. This study was conducted using density functional theory (DFT) calculations to investigate the electronic, elasticity, mechanical, and thermodynamic properties of Pt/Pd alloys and compared them to pristine Pt and Pd structures. The results indicate that the considered Pt/Pd alloy structures, PtPd3, PtPd, Pt3Pd, and Pt7Pd, are energetically favourable based on their formation energies. These structures also satisfy Born’s stability criteria and are elastically stable. The phonon density of states showed that the considered Pt/Pd alloy structures are dynamically stable, with no imaginary modes present. Additionally, the Pt atom dominates at lower frequencies, while the Pd atom dominates at higher frequencies, as seen in the phonon band structure. The electronic density of states revealed that the considered Pt/Pd alloy structures have a metallic character and are non-magnetic. These findings contribute to a better understanding of the properties and stability of Pt/Pd alloy structures that are relevant in various fields, including materials science and catalysis.")

link_url2 = "https://doi.org/10.3390/condmat8030076"
link_text2 = "DOI: 10.3390/condmat8030076"
link_html2 = f'<a href="{link_url2}" target="_blank">{link_text2}</a>'
st.markdown(link_html2, unsafe_allow_html=True)

 