import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vehicleList = pd.read_csv("data/vehicle_list.csv")
vehicleData = pd.read_csv("data/BC 12 CD 3456.csv")

st.selectbox("Manufacturer", vehicleList['Manufacturer'].unique())
st.selectbox("Model", vehicleList['Model'])
st.selectbox("Subsystem", ["Fuel", "Air", "Oil",
             "Powertrain", "ECU", "Brakes"])
st.image("data//images//Background MH 12 PQ 5841.png")
st.image("data//images//Component Layout.png")


data = pd.read_csv('data/BC 12 CD 3456.csv')
vehicleData = data.copy()
col = vehicleData.columns.values.tolist()
master_row_id = vehicleData['master_row_id'].unique()
new_df = pd.DataFrame(columns=col)


def errorRate(actualValue, predicatedValue):
    errorRate = (predicatedValue - actualValue)/actualValue
    return errorRate.mean()


X = []
y_of_iq = []
y_of_rp = []
y_of_mu = []

for i in master_row_id:
    modelNumber = vehicleData.loc[vehicleData['master_row_id'] == i]
    for j in col[2:]:
        modelNumber[j] = modelNumber[j].replace(0, modelNumber[j].mean())
        new_df = pd.concat([modelNumber, new_df])
    X.append(i)
    y_of_iq.append(errorRate(new_df['iq'], new_df['iq_pred']))
    y_of_rp.append(errorRate(new_df['rp'], new_df['rp_pred']))
    y_of_mu.append(errorRate(new_df['mu'], new_df['mu_pred']))


if st.button('IQ line chart'):
    fig, ax = plt.subplots()
    ax.plot(X, y_of_iq)
    plt.title("IQ line chart")
    st.pyplot(fig)

if st.button('RP line chart'):
    fig, ax = plt.subplots()
    ax.plot(X, y_of_rp)
    plt.title("RP line chart")
    st.pyplot(fig)

if st.button('MU line chart'):
    fig, ax = plt.subplots()
    ax.plot(X, y_of_mu)
    plt.title("MU line chart")
    st.pyplot(fig)
