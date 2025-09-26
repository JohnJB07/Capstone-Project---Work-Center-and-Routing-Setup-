import streamlit as st
import json
import os
from pathlib import Path
import time

class Main:
    def __init__(self):
        # Save text
        self.save_text = "Saving to JSON. Please wait."

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

        # Dictionary Initialization
        if "work_center_data" not in st.session_state:
            st.session_state.work_center_data = {
                "work_centers": [], 
                "routing": [], 
                "quantity": None
                }

        # If user selected save to json
        if "save_to_json" not in st.session_state:
            st.session_state.save_to_json = None
                   
    def run(self):
        # Title and Extra Information
        st.title("Work Center and Routing Setup")        
        st.markdown(
        """
        Please input the following details:\n
        \t> Work center name, capacity (hrs/day), cost/hr\n
        \t> Routing steps (operation name, time/unit, assigned work center)\n
        \t> Production quantity\n
        """
        )
        
        # Sidebar text
        st.sidebar.success("Choose the page you want to visit.")

        # Form
        with st.form("form_data", enter_to_submit=False):
            # User input
            self.work_center_name = st.text_input("Input Details Below.", 
                placeholder="Work Center Name")
            self.capacity = st.text_input("", 
                placeholder="Capacity", label_visibility="hidden")
            self.cost_per_hour = st.text_input("", 
                placeholder="Cost Per Hour", label_visibility="hidden")

            # Routing Data
            self.operation = st.text_input("", 
                placeholder="Operation", label_visibility="hidden")
            self.assigned_work_center = st.text_input("", 
                placeholder="Assigned Work Center", label_visibility="hidden")
            self.time_per_unit = st.text_input("", 
                placeholder="Time Per Unit", label_visibility="hidden")

            # Production Quantity  
            self.quantity = st.text_input("", placeholder="Quantity", label_visibility="hidden")

            # Submit button and check if user has submitted the info
            self.submitted = st.form_submit_button("Submit")                
            if self.submitted: 

                # If the user has filled up the form
                if (self.work_center_name and 
                    self.capacity and 
                    self.cost_per_hour and 
                    self.operation and 
                    self.assigned_work_center and 
                    self.time_per_unit and 
                    self.quantity):
                    
                    # Add information to work_center_data dict
                    st.session_state.work_center_data["work_centers"].append({
                        "name": self.work_center_name, 
                        "capacity": int(self.capacity), 
                        "cost_per_hour": float(self.cost_per_hour)
                        })
                    st.session_state.work_center_data["routing"].append({
                        "operation": self.operation,
                        "assigned_work_center": self.assigned_work_center, 
                        "time_per_unit": float(self.time_per_unit)
                        })
                    st.session_state.work_center_data["quantity"] = int(self.quantity)

                    st.text("Form successfully submitted.")                            

                # Form is incomplete
                else:
                    st.text("Please fill up the form completely.")
            
        # Check to see if the user didn't input anything / dictionary is empty
        self.dictionary = st.session_state.work_center_data
        self.check: bool = (
            len(self.dictionary["work_centers"]) == 0) and (
            len(self.dictionary["routing"]) == 0) and not (
            self.dictionary["quantity"])

        if not (self.check):
            # Ask user if they want to save, display the data in json format, or no
            self.ask = st.text("Save to JSON file?")
            self.yes, self.no, self.display = st.columns([0.1, 0.1, 0.8])
            if st.session_state.save_to_json == None or st.session_state == False:
                with self.yes:
                    if st.button("yes"):
                        st.empty()
                        st.session_state.save_to_json = True

                with self.no:
                    if st.button("no"):
                        st.session_state.save_to_json = False

                with self.display:
                    # Button Independent From Hiding the Text Field
                    if st.button("Display results"):
                        if self.check:
                            st.warning("Currently, there is no data found in work_center_data.", icon="⚠️")
                        else:
                            st.success('Successfully displayed data!', icon="✅")
                        st.json(self.dictionary, expanded=2)
        else:
            pass

        # User has selected to save the information
        if st.session_state.save_to_json == True:
            self.note_1 = st.info("NOTE: Data will be saved to JSON.", icon="ℹ️")      
            with st.form("save_json", enter_to_submit=False):
                self.file_name = st.text_input("Input below.", placeholder="File name")
                self.save_file = st.form_submit_button("Submit")

                # Save the data to a json folder
                if self.save_file:
                    try:
                        # JSON Data + JSON File name
                        self.json_data = st.session_state.work_center_data
                        self.full_json_fname = self.file_name + ".json"

                        # Change directory to JSON folder and check if file name already exists
                        os.chdir(os.path.join(Path(__file__).parent, "json"))
                        if os.path.exists(self.full_json_fname):
                            st.warning("File name already exists!", icon="⚠️")
                        else:
                            with open(self.full_json_fname, "w") as file_write:
                                json.dump(self.json_data, file_write, indent=4)
                            
                            # Progress bar
                            if bool((len(self.file_name) > 0)) == True:
                                self.note_1.empty()
                                self.note_2 = st.info(f"Now saving {self.file_name}.json", icon="ℹ️")
                                self.progbar = st.progress(0, self.save_text)

                                for p_complete in range(100):
                                    time.sleep(0.01)
                                    self.progbar.progress(p_complete + 1, text=self.save_text)
                                                    
                                self.note_2.empty()
                                time.sleep(1)
                                st.success("Successfully saved JSON File", icon="✅")
                                self.progbar.empty()
                    except Exception as e:
                        st.error(f"Failed to save data to JSON File: {e}", icon="🚨")                
                else:
                    st.warning("File name is empty!", icon="⚠️")
        else:
            if st.session_state.save_to_json is None:
                pass
            else:
                st.info("NOTE: Data will not be saved to JSON.", icon="ℹ️")   
             
# Run the main function
if __name__ == '__main__':
    main = Main()
    main.run()