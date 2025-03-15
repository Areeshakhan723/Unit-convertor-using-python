# Unit-Convertor built with Python, UV, and Streamlit.

A simple and intuitive unit convertor built with Python, UV, and Streamlit. Convert between various units of length, weight, volume, temperature, time, area, pressure, speed, and energy with ease!

## 🚀 Features
Multiple Categories: Convert units across 9 categories, including Length, Weight, Volume, Temperature, Time, Area, Pressure, Speed, and Energy.

Dynamic Precision: Results are displayed with appropriate precision (e.g., 2 decimal places for Temperature, 5 for others).

Conversion History: View and clear the last 5 conversions.

User-Friendly UI: Clean and modern interface with custom styling.

## 🛠️ Installation

### 1️⃣ Install UV

First, install UV (if not already installed):

curl -LsSf https://astral.sh/uv/install.sh | sh

For Windows:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Verify installation:

uv --version

### 2️⃣ Create and Initialize the Project

uv init unit-convertor

cd unit-convertor

### 3️⃣ Install Sreamlit (Dependency)

uv add streamlit

### 4️⃣ Activate UV Virtual Environment (Windows)

.venv\Scripts\activate

### 5️⃣ Run Unit Convertor

streamlit run unit_convertor.py

🎉 That’s it! Your Unit Convertor is ready to use 🚀

## 🖥️ Usage

Select a Category: Choose the type of unit you want to convert (e.g., Length, Weight, Temperature).

Choose Units: Select the source unit (Convert from) and the target unit (Convert to).

Enter Value: Input the value you want to convert.

Convert: Click the 🔄 Convert button to see the result.

View History: Check the 📜 Conversion History section to see the last 5 conversions.

Clear History: Use the 🗑️ Clear History button to remove all history.

