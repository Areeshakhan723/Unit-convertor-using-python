# Unit-Convertor built with Python, UV, and Streamlit.

A simple and intuitive unit convertor built with Python, UV, and Streamlit. Convert between various units of length, weight, volume, temperature, time, area, pressure, speed, and energy with ease!

## 🚀 Features
𝗠𝘂𝗹𝘁𝗶𝗽𝗹𝗲 𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝗶𝗲𝘀: Convert units across 9 categories, including Length, Weight, Volume, Temperature, Time, Area, Pressure, Speed, and Energy.

𝗗𝘆𝗻𝗮𝗺𝗶𝗰 𝗣𝗿𝗲𝗰𝗶𝘀𝗶𝗼𝗻: Results are displayed with appropriate precision (e.g., 2 decimal places for Temperature, 5 for others).

𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗶𝗼𝗻 𝗛𝗶𝘀𝘁𝗼𝗿𝘆: View and clear the last 5 conversions.

𝗨𝘀𝗲𝗿-𝗙𝗿𝗶𝗲𝗻𝗱𝗹𝘆 𝗨𝗜: Clean and modern interface with custom styling.

## 🖥️ Usage

𝗦𝗲𝗹𝗲𝗰𝘁 𝗮 𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝘆: Choose the type of unit you want to convert (e.g., Length, Weight, Temperature).

𝗖𝗵𝗼𝗼𝘀𝗲 𝗨𝗻𝗶𝘁𝘀: Select the source unit (Convert from) and the target unit (Convert to).

𝗘𝗻𝘁𝗲𝗿 𝗩𝗮𝗹𝘂𝗲: Input the value you want to convert.

𝗖𝗼𝗻𝘃𝗲𝗿𝘁: Click the 🔄 Convert button to see the result.

𝗩𝗶𝗲𝘄 𝗛𝗶𝘀𝘁𝗼𝗿𝘆: Check the 📜 Conversion History section to see the last 5 conversions.

𝗖𝗹𝗲𝗮𝗿 𝗛𝗶𝘀𝘁𝗼𝗿𝘆: Use the 🗑️ Clear History button to remove all history.

## Live Demo: 
https://areeshakhan723-unit-convertor-using-pytho-unit-convertor-aoylfz.streamlit.app/
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
