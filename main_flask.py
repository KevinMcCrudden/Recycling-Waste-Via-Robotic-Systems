



# Example function to create models
def create_models():
    # Your code to create new models goes here
    # For example, creating new Tabs
    Locations_Panel = TabPanel(child=plots_Locations, title="WPI Recycling Locations") 
    Monthly_panel = TabPanel(child=plots_monthly, title="22 WPI Recycling Monthly")
    Academic_Year_panel = TabPanel(child=academic_year, title="WPI Recycling Academic Year")
    Robot_panel = TabPanel(child=Robot_Rate_Layout, title="Robot Calculation")

    tabs = Tabs(tabs=[Locations_Panel, Monthly_panel, Academic_Year_panel, Robot_panel])
    return tabs

# Updated modify_doc function
def modify_doc(doc):
    tabs = create_models()
    doc.add_root(tabs)
