import streamlit as st
from datetime import datetime  

# Set up the page configuration
st.set_page_config("All-in-One Unit Converter", page_icon="🔄", layout="centered")

# Conversion factors
conversion_factors = {
    "Length": {
        "meters (📏)": 1, 
        "kilometers (🛤️)": 0.001, 
        "miles (🛣️)": 0.000621371, 
        "feet (👣)": 3.28084
    },
    "Weight": {
        "grams (⚖️)": 1, 
        "kilograms (🏋️‍♂️)": 0.001, 
        "pounds (🐂)": 0.00220462
    },
    "Volume": {
        "liters (🧴)": 1, 
        "milliliters (💦)": 1000, 
        "gallons (🛢️)": 0.264172
    },
    "Temperature": {
        "Celsius (🌡️🔥) to Fahrenheit": lambda x: (x * 9/5) + 32,
        "Celsius (🌡️) to Kelvin (❄️)": lambda x: x + 273.15,
        "Fahrenheit (🔥) to Celsius (🌡️)": lambda x: (x - 32) * 5/9,
        "Fahrenheit (🔥) to Kelvin (❄️)": lambda x: (x - 32) * 5/9 + 273.15,
        "Kelvin (❄️) to Celsius (🌡️)": lambda x: x - 273.15,
        "Kelvin (❄️) to Fahrenheit (🔥)": lambda x: (x - 273.15) * 9/5 + 32,
    },
    "Time": {
        "seconds (⏳)": 1, 
        "minutes (⌛)": 60, 
        "hours (⏰)": 3600, 
        "days (📆)": 86400
    },
    "Area": {
        "square meters (📐)": 1, 
        "square feet (🏠)": 10.7639, 
        "acres (🌿)": 0.000247105
    },
    "Pressure": {
        "Pascals (💨)": 1, 
        "Bar (🏗️)": 1e-5, 
        "PSI (⚙️)": 0.000145038
    },
    "Speed": {
        "m/s (🏃‍♂️)": 1, 
        "km/h (🚗💨)": 3.6, 
        "mph (🏎️💨)": 2.23694
    },
    "Energy": {
        "Joules (⚡)": 1, 
        "Calories (🍕)": 0.239006, 
        "kWh (🔋)": 2.7778e-7
    }
}
  
# Custom CSS for styling the app
st.markdown(
    """
    <style>
    /* Page background gradient */
    .stApp {
        background: #082032;
        color: #FFFFFF;
        }
    .custom-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #E90074;
        }
    .custom-subheader {
        font-size: 28px;
        font-weight: bold;
        color: #E53888;
        text-align: center;
        margin-bottom: 20px;
        }

    /* Customize button appearance */
    div.stButton > button {
        background-color: #E53888;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        transition: 0.3s;
        padding: 10px 20px;
        width: 100%;
        margin-top:14px;
        }
    
    div.stButton > button:hover {
        background-color: #FF4191;
        transform: scale(1.05);
        color: white;
        font-size: 18px;
        font-weight: bold;
        }

    .Conversion_history{
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top:14px;
        margin-bottom:10px;
        color: #FFFFFF;
        }

    .record_history{
        text-align: center;
        font-size: 18px;
        margin: 4px;
        color: #FFFFFF;
 
       }

    .custom-result {
        font-size: 24px;
        font-weight: bold;
        color: #EC7FA9;
        text-align: center;
        margin-top: 20px;
        }    

    .empty_msg{
        text-align: center;
        font-size: 18px;
        color: #FFFFFF;

        }
    
    . /* Custom labels for widgets */
    .custom-label {
        color: #FFFFFF;
        font-size: 16px;
        margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Function to perform unit conversion
def unit_convert(value, category, unit_from, unit_to):
    if category == "Temperature":
        try:
            if unit_from in conversion_factors["Temperature"] and unit_to in conversion_factors["Temperature"]:
                # Directly convert from source to target unit
                return conversion_factors["Temperature"][unit_to](value)
        except Exception as e:
            return f"Error in conversion: {str(e)}"
        return "Conversion not supported"
        
    # Handling other category 
    if category in conversion_factors and unit_from in conversion_factors[category] and unit_to in conversion_factors[category]:
        return value * (conversion_factors[category][unit_to] / conversion_factors[category][unit_from]) 
    else:
        return "Conversion not supported"
  
# streamlit setapp
st.markdown(f"<div class='custom-title'>All-in-One Unit Converter</div>", unsafe_allow_html=True)
st.markdown(f"<div class='custom-subheader'>Convert between different units easily! 🚀</div>", unsafe_allow_html=True)

# Dropdown to select conversion category
st.markdown("<div class='custom-label'>Select Conversion Type:</div>", unsafe_allow_html=True)
category = st.selectbox("", list(conversion_factors.keys()), label_visibility="collapsed")

# Two equal columns for unit selection
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='custom-label'>Convert from:</div>", unsafe_allow_html=True)
    unit_from = st.selectbox("", list(conversion_factors[category].keys()), label_visibility="collapsed")

with col2:
    st.markdown("<div class='custom-label'>Convert to:</div>", unsafe_allow_html=True)
    unit_to = st.selectbox("", [u for u in conversion_factors[category].keys() if u != unit_from], label_visibility="collapsed")


st.markdown("<div class='custom-label'>Enter a value you want to convert:</div>", unsafe_allow_html=True)
value = st.number_input("", min_value=1.0, step=1.0, label_visibility="collapsed")


# Initialize session state for conversion history if not already created
if "history" not in st.session_state:
    st.session_state.history = [] # Stores past conversion records


# Convert button logic
if st.button("🔄 Convert"):
    # Input validation
    if value < 0 and category != "Temperature":
        st.error("Value cannot be negative for this category.")
    elif category == "Temperature" and unit_to.startswith("Kelvin") and value < 0:
        st.error("Kelvin cannot be negative.")
    else:
        result = unit_convert(value, category, unit_from, unit_to)

        if isinstance(result, (int, float)):
            # Dynamic precision based on category
            precision = 2 if category == "Temperature" else 5
            st.markdown(f"<div class='custom-result'>Converted Value: {result:.{precision}f} {unit_to}</div>", unsafe_allow_html=True)
        else:
            st.success(result)

        # Format the conversion record and store it in session state
        precision = 2 if category == "Temperature" else 5  # Reuse precision for history
        timestamp = datetime.now().strftime("%Y-%m-%d   %H:%M   ")
        conversion_record = f"{timestamp}: \t {value} {unit_from} ➝ {result:.{precision}f} {unit_to}"
        st.session_state.history.append(conversion_record)

# Display conversion history in the
st.markdown(f"<div class='Conversion_history'>📜 Conversion History</div>",unsafe_allow_html=True)

if st.session_state.history:
    for record in st.session_state.history[-5:]: # Show last 5 conversions
        # Replace tab (\t) with HTML spaces (&emsp;) for proper rendering
        record_html = record.replace("\t", "&emsp;&emsp;")
        st.markdown(
            f"<div class='record_history'>{record_html}</div>", 
            unsafe_allow_html=True
        )
       
    # Clear history button (only appears when there's history)
    if st.button("🗑️ Clear History", key="clear_history_btn"):
         # Set a session state variable to show the confirmation checkbox
        st.session_state.show_clear_confirmation = True

    # Show the confirmation checkbox if the session state variable is True
    if st.session_state.get("show_clear_confirmation", False):
        if st.checkbox("Are you sure you want to clear the history?",key="clear_confirmation_checkbox"):
            st.session_state.history.clear()  # Clear the history
            st.session_state.show_clear_confirmation = False  # Reset the confirmation state
            st.rerun() # 🔄Force Streamlit to refresh the UI after clearing history
else:
    st.markdown(
        "<div class='empty_msg'>Your conversion history is empty.</div>", 
        unsafe_allow_html=True
    )