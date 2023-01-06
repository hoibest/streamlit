import streamlit as st

st.title("Uveitis App")
st.header("Clinical presentation")
st.write("Select the patient's clinical presentation")
anatLoc = st.radio("Anatomical location",["Anterior","Intermediate","Posterior","Panuveitis"]) 


course = st.radio("Course",["Acute, monophasic","Acute, recurrent","Chronic"]) 

if course == "Acute, recurrent":
    laterality = st.radio("Laterality",["Unilateral","Unilateral, alternating","Bilateral"]) 
else:
    laterality = st.radio("Laterality",["Unilateral","Bilateral"]) 

granulomatous = st.radio("Granulomatous",["Granulomatous","Nongranulomatous"])



dictPicture = {
    "Acute, monophasic": "AM",
    "Acute, recurrent": "AR",
    "Chronic": "C",  
    "Unilateral": "UL",
    "Unilateral, alternating": "ULA",
    "Bilateral": "BL",
    "Granulomatous": "G",
    "Nongranulomatous": "NG"
}

dictDisease = {
    'AMULG':['CMV','HSV','VZV','Syphilis','TB','Sarcoidosis'],
    'AMULNG':['CMV','HSV','VZV','Syphilis','HLA-B27','Sarcoidosis'],
    'AMBLG':['Syphilis','TB','Sarcoidosis'],
    'AMBLNG':['Syphilis','TINU','Sarcoidosis'],
    'ARULG':['CMV','HSV','VZV','Syphilis','TB','Sarcoidosis'],
    'ARULNG':['CMV','HSV','VZV','Syphilis','HLA-B27','Sarcoidosis'],
    'ARULAG':['Syphilis','TB','Sarcoidosis'],
    'ARULANG':['Syphilis','HLA-B27','Sarcoidosis'],
    'ARBLG':['Syphilis','TB','Sarcoidosis'],
    'ARBLNG':['Syphilis','TINU','Sarcoidosis'],
    'CULG':['CMV','HSV','VZV','Syphilis','TB','Sarcoidosis','FUS'],
    'CULNG':['CMV','HSV','VZV','Syphilis','HLA-B27','Sarcoidosis','FUS','JIA'],
    'CBLG':['Syphilis','TB','Sarcoidosis'],
    'CBLNG':['Syphilis','HLA-B27','JIA','TINU','Sarcoidosis']
}

dictAttribute = {
    'CMV': "Diffuse iris atrophy or endotheliitis, nodular, coin-shaped endothelial lesion",
    'HSV': " Sectoral iris atrophy, keratitis",
    'VZV': "Sectoral iris atrophy, dermatomal zoster",
    'FUS': "Heterochromia, diffuse iris atrophy, stellate kp, exclude (endotheliitis, nodular, coin-shaped endothelial lesion)",
    'JIA': "Age (< 16), JIA arthritis",
    'HLA-B27': "Back problem, diagnosed spondyloarthritis",
    'TINU': "Systemic conditions (fever, weight loss, anorexia, arthralgias, myalgias, rash) , tubulointerstitial nephritis",
    'Sarcoidosis': "Sarcoidosis",
    'Syphilis': "Syphilis",
    'TB' : 'TB'
}

def sentencify(list):
    st.success("These are possible differential diagnosis")
    for dis in list:
        st.write(dis)


button1 = st.button('Done')
if st.session_state.get('button') != True:
    st.session_state['button'] = button1 # Saved the state
if st.session_state['button'] == True:
    oneLine = dictPicture[course]+dictPicture[laterality]+dictPicture[granulomatous]
    sentencify(dictDisease[oneLine])
    st.success("Use for further diagnosis")
    attList = []
    for dis in dictDisease[oneLine]:
        attList.append(dictAttribute[dis])
    choice = st.radio("Which clinical presentation most fit the patient?", tuple(attList))
    st.write("Likely diagnosis of the patient is "+list(dictAttribute.keys())[list(dictAttribute.values()).index(choice)])
    st.success("Check for further investigation")


