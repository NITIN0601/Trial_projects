import streamlit as st


def launch_option0(options):
    st.title(options)
    cont()


def launch_option1(options):
    st.title(options)
    cont()


def launch_option2(options):
    st.title(options)
    cont()


def cont():
    # Create a dictionary of buttons with unique keys
    buttons = {
        'Model 1': 'button1',
        'Model 2': 'button2',
        'Model 3': 'button3',
        'Model 4': 'button4'
    }

    # Create a layout using columns
    cols = st.columns(len(buttons))

    # Iterate over the buttons dictionary
    selected_button = None
    for i, (button_text, button_key) in enumerate(buttons.items()):
        if cols[i % len(cols)].button(button_text, key=button_key):
            selected_button = button_text

    st.markdown(
        """
        <style>
        .stAlert {
            max-width: 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the selected button
    st.success(selected_button)

    return


def side_bar1():
    with st.sidebar:
        options = ['Transcript', 'Resume', 'Code Optimization']
        selected_option = st.radio('Select an service', options)
        st.success(selected_option)

    option_actions = {
        options[0]: lambda: launch_option0(options[0]),
        options[1]: lambda: launch_option1(options[1]),
        options[2]: lambda: launch_option2(options[2])
    }

    if selected_option in option_actions:
        option_actions[selected_option]()

def side_bar2():
    linked_list = {
        "Tone": ["Formal", "Casual", "Informative", "Persuasive"],
        "Format": ["Essay", "Bullet Points", "Outline", "Dialog"],
        'Act as': ["Expert", "Critic", "Enthusiast"],
        'Objective': ["Inform", "Persuade", "Entertain"],
        'Context': ["Background Information", "Data", "Context Information"],
        'Scope': ["Range of Topic"],
        'Keywords': ["Phrases"],
        'Limitations': ["Character Count", "Word Count"],
        'Examples': ["Desired Style", "Structure", "UnStructure", "Content"],
        'Deadline': ["Time Frame", "Time-Sensitive"],
        'Audience': ["Tailored"],
        'Language': ["English"],
        'Citations': ["Count of Citations"],
        'Point of view': ["AI", "Human"],
        'Counterarguments': ["True", "False"],
        'Terminology': ["Industry Specific", "Generic"],
        'Analogies': ["Concepts"],
        'Quotes': ["Yes", "No"],
        'Statistics': ["Data Type"],
        'Visual Elements': ["Charts", "Graphs", "Images"],
        'Call to action': ["Next Step", "Clear"],
        'Sensitivity': ["More sensitive", "less sensitive"]
    }

    for category, options in linked_list.items():
        checkbox_selected = st.sidebar.checkbox(category)

        if checkbox_selected:
            radio_option = st.sidebar.radio("select the option", options, index=0, horizontal=True)
        else:
            radio_option = "Default Option"


def side_bar():
    st.sidebar.markdown('## Services Offered')
    side_bar1()

    st.sidebar.markdown('## Prompt Guide')
    side_bar2()

    st.sidebar.markdown('## test Guide')
    return


side_bar()
