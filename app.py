import streamlit as st
import pickle
import numpy as np

# Load the model
with open('flight_price_gbr.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the function for prediction
def predict_fare(*airline_source_destination, journey_day, journey_month, Total_stops, dep_hrs, dep_mins):
    # Prepare the input array (scaling and preprocessing should match your model's training data)
    input_data = np.array([Total_stops, journey_day, journey_month, dep_hrs, dep_mins] + list(airline_source_destination)).reshape(1, -1)
    return model.predict(input_data)[0]

# Streamlit UI
st.title('Flight Fare Prediction')
st.subheader('Enter Details Below:')


# Boolean features for airlines, sources, and destinations
st.subheader('Airlines')
Airlines = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers', 
            'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy']

airline_values = []
for i in range(0, len(Airlines), 3):
    cols = st.columns(3)  # Create 3 columns for row-wise display
    for idx, airline in enumerate(Airlines[i:i+3]):
        airline_values.append(cols[idx].checkbox(airline))

st.subheader('Departure')
Departure = ['Chennai', 'Delhi', 'Kolkata', 'Mumbai']

source_values = []
cols = st.columns(4)  # Display sources in a single row
for idx, source in enumerate(Departure):
    source_values.append(cols[idx].checkbox(source))

st.subheader('Arrival')
Arrival = ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi']

destination_values = []
cols = st.columns(5)  # Display destinations in a single row
for idx, destination in enumerate(Arrival):
    destination_values.append(cols[idx].checkbox(destination, key=destination))


    # Input fields
total_stops = st.number_input('Total Stops', min_value=0, max_value=4, value=0)
journey_date = st.date_input('Journey Date')
dep_time = st.time_input('Departure Time')


# Prediction button
if st.button('Predict Fare'):
    journey_day = journey_date.day
    journey_month = journey_date.month
    
    dep_hour = dep_time.hour
    dep_min = dep_time.minute
    result = predict_fare(
        *airline_values, *source_values, *destination_values,
        journey_day=journey_day, journey_month=journey_month,
        Total_stops=total_stops, dep_hrs=dep_hour, dep_mins=dep_min
    )
    st.success(f'Predicted Flight Fare: ₹ {result:.2f}')

# Developer details
st.write('***Built by:*** Baizeed Ibrahim K')
st.write('***Github***: [Baizeed Ibrahim K](https://github.com/baizeedk)')
st.write('***LinkedIn***: [Baizeed Ibrahim K](https://www.linkedin.com/in/baizeed-ibrahim-k-7047182a7)')
