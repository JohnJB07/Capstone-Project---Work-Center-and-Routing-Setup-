# Need to install module if you dont have it yet
import streamlit as st
import numpy # not used yet
import pandas # not used yet

# Included with Python
import json # not used yet aswell.

class Main:
    def __init__(self):
        # Work Center Data
        self.work_center_name: str = None
        self.capacity: int = None
        self.cost_per_hour: float = None

        # Routing Data
        self.operation: str = None
        self.assigned_work_center: str = None
        self.time_per_unit: float = None

        # Production Quantity   
        self.quantity: int = None

        # I dont wanna fucking invoke this shit no more
        self.run()

    def run(self):
        # TITLE
        st.title("Work Center and Routing Setup")
        st.markdown(
        """
        Please input the following details:\n
        Work center name, capacity (hrs/day), cost/hr\n
        Routing steps (operation name, time/unit, assigned work center)\n
        Production quantity\n
        """
        )

        # TEXT FIELDS
        # Work Center Data (INPUT)
        self.work_center_name = st.text_input("Input Below.", placeholder="Work Center Name")
        self.capacity = st.text_input("", placeholder="Capacity", label_visibility="hidden")
        self.cost_per_hour = st.text_input("", placeholder="Cost Per Hour", label_visibility="hidden")

        # Routing Data
        self.operation = st.text_input("", placeholder="Operation", label_visibility="hidden")
        self.assigned_work_center = st.text_input("", placeholder="Assigned Work Center", label_visibility="hidden")
        self.time_per_unit = st.text_input("", placeholder="Time Per Unit", label_visibility="hidden")

        # Production Quantity  
        self.quantity = st.text_input("", placeholder="Quantity", label_visibility="hidden")

        # Submit button
        if st.button("Submit"): 
            # Completed Form :D
            if (self.work_center_name and self.capacity and self.cost_per_hour and self.operation
                and self.assigned_work_center and self.time_per_unit and self.quantity):
                # Add functionality to add all the details to a JSON File
                st.text("Form successfully submitted.")
            # They fucking passed the form..(INCOMPLETE tf?)
            else:
                st.text("Please fill up the form completely.")
                pass
        
# Run the main function
if __name__ == '__main__':
    Main()

# Testing code below
"""
if "test_val" not in st.session_state:
    st.session_state.test_val = {"Values": []}

x = st.text_input("Input name")

if st.button("Test button") and x:
    st.text("Test", help="Tooltip", width="content")
    st.session_state.test_val["Values"].append(x)
    print(st.session_state.test_val)
    print(f"Test_Val Value: {st.session_state.test_val}\nX Value: {x}")    
"""