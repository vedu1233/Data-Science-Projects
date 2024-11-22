import streamlit as st

# Custom CSS for the animated button
button_css = """
<style>
.animated-button {
    display: inline-block;
    font-size: 16px;
    font-weight: bold;
    color: #fff;
    background-color: #4CAF50;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    box-shadow: 0 4px #999;
    transition: all 0.3s ease;
}

.animated-button:hover {
    background-color: #45a049;
    transform: translateY(-5px);
    box-shadow: 0 6px #666;
}

.animated-button:active {
    background-color: #3e8e41;
    box-shadow: 0 4px #999;
    transform: translateY(2px);
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(button_css, unsafe_allow_html=True)

# Create an HTML button
if st.markdown('<button class="animated-button">Click Me</button>', unsafe_allow_html=True):
    st.write("You clicked the button!")

# Streamlit button
clicked = st.button("Streamlit Default Button")
if clicked:
    st.write("Default Streamlit button clicked!")
