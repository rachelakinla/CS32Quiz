import streamlit as st

# Displaying image
st.image("logo.png", width= 800)

#COUNTERS AND DEFINITIONS
counters = {"SUP_counter": 0, "ADULT_counter": 0, "ADVO_counter": 0, "HH_counter": 0, "MENT_counter": 0, "AFTERSCHOOL_counter": 0, "INSCHOOL_counter": 0, "SHELTER_counter":0 } 

all_questions_submitted = False
questions_answered_counter = 0

def updateCounter(question, response, counters):
    """ Updates the counters by adding 1 (or not) based on the question. It categorizes the response per program and if the answer hints towards an interest in it, the function adds a point to that program. """
    if question == 1:
        if response == "Morning":
            counters["ADULT_counter"] += 1
            counters["INSCHOOL_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif response == "Afternoon":
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif response == "Evening":
            counters["ADULT_counter"] += 1
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1

    if question == 2 and int(response) > 5:
        counters["MENT_counter"] += 1
        counters["AFTERSCHOOL_counter"] += 1
        counters["INSCHOOL_counter"] += 1

    if question == 3 and int(response) > 5:
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1
    if question == 4:
        if 'Youth Enrichment' in response:
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1
        elif 'Education' in response:
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1
        elif 'Immigrant Services' in response:
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
        elif 'Housing' in response:
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif 'Elderly Services' in response:
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
        elif 'Legal Services' in response:
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
        elif 'Special Needs' in response:
            counters["HH_counter"] += 1

    if question == 5:
        if response == "Somewhat":
            counters["ADULT_counter"] += 1
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif response == "Very":
            counters["ADVO_counter"] += 1
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1        
    if question == 6:
        if response == "Yes":
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
            
    
    if question == 7:
        if response == "No":
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif response == "Yes":
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1

    if question == 8:
        if response == "No":
            counters["ADULT_counter"] += 1
            counters["ADVO_counter"] += 1
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1
        elif response == "Yes":
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1

    if question == 9:
        if response == "No":
            counters["ADVO_counter"] += 1
            counters["HH_counter"] += 1
            counters["SHELTER_counter"] += 1
        elif response == "Yes":
            counters["ADULT_counter"] += 1
            counters["MENT_counter"] += 1
            counters["AFTERSCHOOL_counter"] += 1
            counters["INSCHOOL_counter"] += 1   
    return None
    
#TALLYING
def display_results(counters):
    '''Calculates and displays the results of the exam by finding the program with the most points within counters, and their respective amount of points'''

    st.title("Quiz Results")

    max_value = max(counters.values())
    highest_counters = [key for key, value in counters.items() if value == max_value] #list for counters w/ highest numbers
    highest_values = [counters[key] for key in highest_counters] 
    return highest_counters,highest_values
    

#QUESTION 1
question = 1
st.subheader("Question 1 : ") 
with st.form("question1"):
    options = [" "]+ ["Morning"] + ["Afternoon"] + ["Evening"]
    selection = st.selectbox("What time of day are you most available?", options=options)
    st.form_submit_button()
    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == "Morning" or selection == "Afternoon" or selection == "Evening":
        questions_answered_counter +=1
        st.write ("Most available in the ", selection)
        updateCounter(question, selection, counters)
        

#QUESTION 2
question = 2
st.subheader("Question 2 : ")
with st.form("question2"):
    kid_comfort = st.slider("From 1-10, 10 being the most comfortable, how comfortable are you with working with kids?", 0, 10,0)
    st.form_submit_button()
    questions_answered_counter +=1
    st.write("I'm a", kid_comfort, 'out of 10')
    updateCounter(question, kid_comfort, counters)

#QUESTION 3
question = 3
st.subheader("Question 3 : ")
with st.form("question3"):
    adult_comfort = st.slider("From 1-10, 10 being the most comfortable, how comfortable are you with working with adults?", 0, 10,0)
    st.form_submit_button()
    questions_answered_counter +=1
    st.write("I'm a", adult_comfort, 'out of 10')
    updateCounter(question, adult_comfort, counters)

#QUESTION 4
question = 4
st.subheader("Question 4 : ")
with st.form("question 4"):
        interests = st.multiselect(
            'What are you passionate about? Please select all that interest you.',
            ['Youth Enrichment', 'Education', 'Immigrant Services', 'Housing','Elderly Services', 'Legal Services','Special Needs'])
        st.form_submit_button()
        questions_answered_counter +=1
        #finds number of items selected
        listlen = 0
        for item in interests:
            if isinstance(item, str):
                listlen += 1
        st.write(listlen, "item(s) selected")
        updateCounter(question, interests, counters)

#QUESTION 5
question = 5
st.subheader("Question 5 : ")
with st.form("question5"):
    options = [" "]+ ["Not at All"] + ["Somewhat"] + ["Very"]
    selection = st.selectbox("How important is direct community engagement to you?", options = options)
    st.form_submit_button()
    
    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == selection == "Not at All" or selection == "Somewhat" or selection == "Very":
        questions_answered_counter +=1
        st.write("Direct community engagement is", selection, "important to me.")
        updateCounter(question, selection, counters)

#QUESTION 6
question = 6
st.subheader("Question 6 : ")
with st.form("question6"):
    options = [" "]+ ["Yes"] + ["No"]
    selection = st.selectbox("Would you be interested in doing active advocacy work for social justice issues as a volunteer?", options = options)
    st.form_submit_button()

    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == "Yes" or selection == "No":
        questions_answered_counter +=1
        st.write("You answered:", selection)
        updateCounter(question, selection, counters)

#QUESTION 7
question = 7
st.subheader("Question 7 : ")
with st.form("question7"):
    options = [" "]+ ["Yes"] + ["No"]
    selection = st.selectbox("Would you want to work in an educational setting?", options = options)
    st.form_submit_button()

    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == "Yes" or selection == "No":
        questions_answered_counter +=1
        st.write("You answered:", selection)
        updateCounter(question, selection, counters)

#QUESTION 8
question = 8
st.subheader("Question 8: ")
with st.form("question8"):
    options = [" "]+ ["Yes"] + ["No"]
    selection = st.selectbox(" Are you interested in volunteering to address homelessness and housing issues?", options = options)
    st.form_submit_button()

    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == "Yes" or selection == "No":
        questions_answered_counter +=1
        st.write("You answered:", selection)
        updateCounter(question, selection, counters)

#QUESTION 9
question = 9
st.subheader("Question 9: ")
with st.form("question9"):
    options = [" "]+ ["Yes"] + ["No"]
    selection = st.selectbox("Are you comfortable providing emotional support to program participants?", options = options)
    st.form_submit_button()

    if selection== " ":
        st.write ("Please enter valid response!")
    elif selection == "Yes" or selection == "No":
        questions_answered_counter +=1
        st.write("You answered:", selection)
        updateCounter(question, selection, counters)


#Check if all questions are answered
if questions_answered_counter == 9:
    all_questions_submitted = True

#Display quiz results
if all_questions_submitted:
    show_results_button = st.button("Show Results")
    if show_results_button:
        results, values = display_results(counters)
        st.subheader("PHBA PROGRAM(S) THAT BEST FITS YOU:")
        for key in results:
            #Find the index of the first occurrence of ':'
            index = key.find(":") + 1
            # Find the substring starting from index and match with counter
            program_counter = key[index:]
            if program_counter == "ADULT_counter":
                program_result = "Adult Services Programs"
                st.subheader(program_result)
                st.image("adult_graphic.png", width=600)

            elif program_counter == "ADVO_counter":
                program_result = "Advocacy Programs"
                st.subheader(program_result)
                st.image("advo_graphic.png", width=600)

            elif program_counter == "HH_counter":
                program_result = "Health and Housing Programs"
                st.subheader(program_result)
                st.image("HH_graphic.png", width=600)

            elif program_counter == "MENT_counter":
                program_result = "Mentoring Programs"
                st.subheader(program_result)
                st.image("ment_graphic.png", width=600)
                
            elif program_counter == "AFTERSCHOOL_counter":
                program_result = "Afterschool Programs"
                st.subheader(program_result)
                st.image("afterschool_graphic.png", width=600)


            elif program_counter == "INSCHOOL_counter":
                program_result = "In School Programs"
                st.subheader(program_result)
                st.image("inschool_graphic.png", width=600)
                
            elif program_counter == "SHELTER_counter":
                program_result = "Shelter Programs"
                st.subheader(program_result)
                st.image("shelter_graphic.png", width=600)
                

        st.link_button("Click Here to Learn More!", "https://www.pbha.org/program-directory")
    
    
