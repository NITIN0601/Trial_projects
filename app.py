import streamlit as st
import requests
import urllib.parse
import subprocess
from fastapi import FastAPI

options = ["model", "n", "presence_penalty", "frequency_penalty","user"]
input_values = []
app = FastAPI()


def retrieve_url_response(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return st.write("No Data found")

@app.get("/url/")
def handle_url_request(**kwargs):
    # Perform any necessary operations with the received data
    # For demonstration purposes, let's just return the received data as a response
    return kwargs


def parm_val(options, input_values):
    st.write("select parameters")

    number = int(st.number_input("Enter a number", max_value=4, value=0, step=1))
    for i in range(int(number)):
        input_value = st.text_input(f"Parameter Key {i + 1}")
        options.append(input_value)

    selected_options = st.multiselect("Select options", options)

    for option in selected_options:
        input_value = st.text_input(f"Enter input for {option}")
        input_values.append(input_value)

    st.write("Selected options and input values:")
    for option, value in zip(selected_options, input_values):
        st.write(f"{option}: {value}")

    url_construct(selected_options, input_values)
    return


def url_construct(selected_options, input_values):
    base_url = "http://localhost:8080/"

    # Constructing the URL parameters
    params = []
    for option, value in zip(selected_options, input_values):
        encoded_option = urllib.parse.quote(option)
        params.append(f"{encoded_option}={value}")

    url = f"{base_url}?{'&'.join(params)}"

    st.write("Generated URL:")
    st.write(url)
    st.write(retrieve_url_response(url))
    return


def main():
    st.title("JSON Key to URL Converter")
    st.write("Enter a JSON key to get the corresponding URL:")
    parm_val(options,input_values)

if __name__ == "__main__":
    subprocess.Popen(["streamlit", "run", "your_script.py", "--browser.serverAddress=0.0.0.0", "--server.port=8501",
                      "--allow-websocket-origin=*"])
    main()
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)





