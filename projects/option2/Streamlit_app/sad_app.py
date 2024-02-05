# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:42:14 2024

@author: Louise
"""

import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Repository")
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


