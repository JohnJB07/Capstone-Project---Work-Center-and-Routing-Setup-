import streamlit as st
import pandas as pd
import numpy as np
import json
import os
from pathlib import Path

def main():
    st.title("📊 Display Work Center & Routing Data")

    # Move Back to the Capstone directory and print out to see 
    os.chdir(os.path.join(os.path.join(Path(__file__).parent, ".."), "json"))
    if Path(os.getcwd()).resolve() == Path(__file__).parent.resolve():
        st.info("Changing directory to homepage directory", icon="ℹ️")
    else:
        st.info("At homepage directory", icon="ℹ️")
    
    json_folder = os.getcwd()

    # User inputs filename
    file_name = st.text_input("Enter the JSON file name (without .json):")

    if file_name:
        file_path = json_folder + f"\{file_name}.json"
        
        if os.path.exists(file_path):
            st.success(f"✅ Found file: {file_name}.json")
            
            # Load JSON
            with open(file_path, "r") as f:
                data = json.load(f)

            # Convert to DataFrames
            work_centers_df = pd.DataFrame(data.get("work_centers", []))
            routing_df = pd.DataFrame(data.get("routing", []))
            quantity = data.get("quantity", None)

            # Display Work Centers
            st.subheader("🏭 Work Centers")
            if not work_centers_df.empty:
                st.dataframe(work_centers_df)
            else:
                st.info("No work center data found.")

            # Display Routing
            st.subheader("🔄 Routing Steps")
            if not routing_df.empty:
                st.dataframe(routing_df)
            else:
                st.info("No routing data found.")

            # Display Quantity
            st.subheader("📦 Production Quantity")
            st.write(quantity)

            # Example: summary using numpy
            if not work_centers_df.empty:
                try:
                    costs = np.array(work_centers_df["cost_per_hour"], dtype=float)
                    st.subheader("📈 Summary Stats")
                    st.write(f"Total Cost/hr: {np.sum(costs)}")
                    st.write(f"Average Cost/hr: {np.mean(costs):.2f}")
                except Exception:
                    st.warning("⚠️ Could not compute stats, check data types.")
        else:
            st.error(f"❌ File '{file_name}.json' not found in {json_folder}")

main()