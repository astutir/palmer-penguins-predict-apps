import streamlit as st
import importlib.util
import os

# Function to load a module from a file
def load_page(page):
    if not os.path.isfile(page):
        st.error(f"File not found: {page}")
        return None
    
    spec = importlib.util.spec_from_file_location("module.name", page)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    st.sidebar.title('Welcome to this Apps!')
    page = st.sidebar.selectbox('Select a page below:', ['Home', 'Data Info', 'Prediction'])
    
    page_file = None
    if page == 'Home':
        page_file = 'pages/0_Home.py'
    elif page == 'Data Info':
        page_file = 'pages/Data_Info.py'
    elif page == 'Prediction':
        page_file = 'pages/Prediction.py'
    
    if page_file:
        page_module = load_page(page_file)
        if page_module:
            if hasattr(page_module, 'main'):
                page_module.main()
            else:
                st.error(f"The selected page '{page}' does not have a 'main' function.")
                
if __name__ == "__main__":
    main()
