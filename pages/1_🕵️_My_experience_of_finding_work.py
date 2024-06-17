# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from my_funcs import *
import plotly.express as px
import base64
# Side bar info and page config
st.set_page_config(
    page_title="My experience of finding work",
    layout="centered",
    page_icon="🕵️",

)
st.sidebar.header("My experience of finding work")
st.sidebar.markdown("This section looks at my experience of finding work, including three interview case studies.")

# Content
st.title('My experience of finding work 🕵️')
st.warning('The following information might be triggering for some people.',icon="⚠️")

# Intro
st.markdown('## A bit about me')
st.markdown('''Hello!  My name is Alex, and I was diagnosed with Asperger's Syndrome in 2012, aged 27.  I've worked in retail, \
insurance, audit, financial services, training, and B2B marketing roles, and the purpose \
    of this section is for me to provide you with some examples of what it's like to apply/interview for employment as an autistic person.  \
        I will focus on three case studies where I was unsuccessful, for various reasons, to illustrate some the of the obstacles autistic people \
            face.
    ''')
st.markdown('''## Case study assumptions made 🤔
Where possible I try to be transparent, so I'll preclude the case studies I prepared by stating the following:
1. I've done my utmost to anonymise the organisations featured. All three are in some way connected with the public sector.
2. Where possible, I'll use gender-neutral pronouns to try and mitigate the effects of unconscious bias.
3. The ethnicity and genders of the interviewers are diverse, but I will do my best \
            to avoid calling out those differences in order to avoid offence.

***

### Notes on metrics 🖊️
In an attempt to visualise my experience, I will be using metrics of my own design in order to compare the interviews. \
    They are defined below:

''')
metrics = {'Metric':
    {'Location 🗺️': 'Measures time taken to commute to/from the office location, as well as time taken to access commercial facilities. \
        A shorter distance for both relates to a higher score.',
    'Environment 🏢🌱' : 'Measures how the office would affect me from a sensory perspective (5 - minimally, 1 - horrifically)',
    'Timekeeping ⏱️' : 'Measures punctuality.  On time would score a 5, more than 10 minutes late would score a 1',
    'Communication 💬' : 'Measures the language used and the questions posed.  Lack of context when posing questions and verbosity were penalised',
    'Affability 😊' : 'Measures whether I believe the interviewer to be likeable (5), tolerable (3), or someone I\'d sooner avoid (1).'
    }
}
st.write(metrics)

st.markdown('''
Every organisation starts off with full marks.

***
''')

st.markdown('''## Organisation Interview Scores 📊

The chart below shows the scores awarded to each organisation for each of the metrics defined, above.''')
# Define data
organisation=['A','B','C']
location=[4,4,5]
environment=[3,2,3]
timekeeping=[3,1,2]
communication=[3,1,2]
affability=[2,2,1]
x_axis = np.arange(len(organisation))
width = 0.15

# Multi bar Chart
fig, ax = plt.subplots(figsize=(10,5))

# Hide the right and top spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Plot the data
plt.bar(x_axis-.3 , location, width, label = 'Location')
plt.bar(x_axis-.15 , environment, width, label = 'Environment')
plt.bar(x_axis, timekeeping, width, label = 'Timekeeping')
plt.bar(x_axis + .15, communication, width, label = 'Communication')
plt.bar(x_axis + .3, affability, width, label = 'Affability')

def valuelabel(x_axis,location, environment, timekeeping, communication, affability):
    for i in range(len(x_axis)):
        plt.text(i-.3,location[i],location[i], ha = 'center', va = 'bottom')
        plt.text(i-.15,environment[i],environment[i], ha = 'center', va = 'bottom')
        plt.text(i,timekeeping[i],timekeeping[i], ha = 'center', va = 'bottom')
        plt.text(i+.15,communication[i],communication[i], ha= 'center', va = 'bottom')
        plt.text(i+.3,affability[i],affability[i], ha = 'center', va = 'bottom')
# calling the function to add value labels
valuelabel(x_axis, location, environment, timekeeping, communication, affability)

# Label the x-axis and show title
plt.xlabel('Organisation')
plt.title('Organisation Interview Scores', size = 18)

# Xticks
plt.xticks(x_axis, organisation)
plt.yticks([])
plt.tick_params(bottom = False)

# Add legend
plt.legend()

# Display
plt.show()
st.pyplot(fig, ax)
st.caption('Fig 4: Bar chart showing the interview scores I gave to organisations A, B, and C.')
st.markdown('''It can be seen from Fig 4, above, that with the exeception of the Location metric, none of the \
    organisations scored particularly well.  With a total score of 15 out of 25, Organisation A scored highest overall.\
  For those who don't trust my arithmetic skills, I've reproduced the chart, above, in tabular form including total scores:
            ''')

def color_positive_green(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: green'` for positive
    strings, gray for netural strings, and black otherwise.
    """

    if val >= 4:
        color = 'green'
    elif val == 3:
        color = 'gray'
    else: color = 'red'
    return 'color: % s' % color

df = pd.DataFrame(list(zip(location,environment,timekeeping, communication, affability)),
                  columns=['Location','Environment','Timekeeping','Communication','Affability'],
                  index=organisation)

df['Total Score'] = df.sum(axis=1)
slice_ = ['Location','Environment','Timekeeping','Communication','Affability']
st.write(df.style.applymap(color_positive_green, ['Location','Environment','Timekeeping','Communication','Affability']))




st.caption('Table 1: Organisation Scores')

st.markdown('''Continue reading to find out why I awarded those scores.

***''')

st.subheader('Case Study One: Organisation A')

st.markdown('''
I managed to secure this interview for a data analyst position via a recruitment agency.  It was an overcast day and the interview took place in \
    person on the organisation's premises in an industrial estate, about a 20 minute walk from where I lived at the time; \
        the nearest shops were a further 10 mins away (Location score = 4).\
        I arrived early and sat patiently in the reception, which was sparsely furnished and dimly lit.

The interviewer arrived in a hurry, five minutes after the interview was due to start (Timekeeping score = 3), and led me to a corner office in a room that was about 10m long by about 5m wide.  The decor was dated and it stank of sweat, but it was bearable (Environemt score = 3).
The first thing I noticed about the interviewer was a nasty gash on the side of their face.  They explained that\
    they had been playing with their dog and it was their carelessness (or words to that effect) which led to the dog clawing at\
    their face.  They asked me what autism was and how it affected me, so I gave them a synposis.  Their response was,
>"So you can give it, but you can't take it."

For those of you who didn't graduate magna cum loud-arse from the Clown College for the Comedically Challeged, \
                that was a joke, or at least I hope it was because they certainly found it amusing.  I managed not to roll my eyes at their ignorance (Affability score = 2).

They proceeded to describe themselves as an "intermediate Excel user" (😕 Communication score = 3) before asking me how I dealt with messy data.  My confidence had been shaken by their earlier remark, so my answer \
    wasn't as polished as it might have been.  They seemed concerned that I wouldn't be able cope with the noise because, allegedly, the \
        the office became rather loud when everyone was in (we were the only two present at the time).  I guess that they
weren't aware of noise cancelling headphones 🤦.  Needless to say, I wasn't offered the role.  Ableism prevailed, but it was their loss.
''')

# Plotting for org A
a = pd.DataFrame(dict(
    r=[4,3,3,3,2],
    theta=['Location','Environment','Timekeeping','Communication','Affability']))
fig2 = px.line_polar(a, r='r', theta='theta', line_close=True,range_r = [0,5],title='Organisation A Scores',color_discrete_sequence=px.colors.sequential.Pinkyl_r, template='plotly_dark')
fig2.update_traces(fill='toself')
st.plotly_chart(fig2)

st.subheader('Case Study Two: Organisation B')
st.markdown('''
I applied for this GDPR compliance role (I can't remember the exact title) via the organisation's careers portal.  \
    The process was pretty arduous, involving copying and pasting my CV line-by-line before answering essay based questions. \
        There was no way for me to upload my CV, which would have reduced the time taken significantly. \
        I ticked the box stating that I was disabled, which enabled me to get an interview because I matched the job criteria.

This organisation was based in a city centre, about a 15 minute train ride from where I lived at the \
    time (Location score = 4).  Unfortunately, it was a massive open-plan office with meeting offices on one side and no designated waiting area. \
        I was asked to wait in a narrow connecting corridor adjacent to another which lead to a stairwell.  It was a sunny day, which made the lighting \
            redundant, bordering on oppressive (Environment score = 2).  The interview started fifteen minutes late (Timekeeping score = 1).

When I was invited into the glass-panelled office there were two interviewers present.  One of them asked me to make myself comfortable.  If I had \
    interpreted that literally, I would have taken my suit, tie and shirt off, before sitting down in my underpants (I'm not a big fan of clothes). \
        Wisely, I chose to sit down in the chair provided, which was functional and comfortable enough.  The meeting room was far too bright, to the point where \
the blinds served no real purpose.  To begin with, the questions were straightforward enough.  Then they asked me, "How are you detail-orientated?"
''')

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.markdown("![Man shaking his head in disbelief](https://media.giphy.com/media/tPdYQaW6oCIOA/giphy.gif)")
    st.caption('[GIF available here](https://media.giphy.com/media/tPdYQaW6oCIOA/giphy.gif)')

st.markdown('''At this point I was raging on the inside.  In response, I asked them what they meant by that, before telling them that the cracks \
    on the plaster on the wall behind them were distracting, as were the boxes pilled haphazardly behind where they were sat. \
    Moreover, the lights were too bright, and the floor wasn't level.  I then asked if that answered their question (Communication score = 1).\
        One of them grew increasingly amused and smug as I spoke.  I couldn't get out of there fast enough for my liking (Affability score = 2).  \
            The feedback I received was that they had no doubt I could do the job, but there was a stronger candidate. \
                My feedback for the interview panel consists of two words: foxtrot oscar (or words to that effect)!''')

# Plotting for org B
b = pd.DataFrame(dict(
    r=[4,2,1,1,2],
    theta=['Location','Environment','Timekeeping','Communication','Affability']))
fig3 = px.line_polar(b, r='r', theta='theta', line_close=True,range_r = [0,5],title='Organisation B Scores', color_discrete_sequence=px.colors.sequential.Pinkyl_r, template='plotly_dark')
fig3.update_traces(fill='toself')
st.plotly_chart(fig3)

st.subheader('Case Study Three: Organisation C')

st.markdown('''This interview was for the role of Power BI Data Anaylst, located about a ten minute walk from where I live \
(Location score = 5).  The interview consisted of a PowerPoint presentation followed by questions from an interview
panel, all conducted over Zoom.

The application process was one of those where one has to enter all of their contact \
    information, education, work experience, etc., on to a webform, before answering essay questions.  I ticked the box \
    which would guarantee an interview if I met the minimum requirements.  I stipulated that I was autistic and that I may \
    need questions to be rephrased, so you can imagine my surprise when, 5 minutes late to join the call (Timekeeping = 2), the \
    the lead interviewer (whom was one of three) stated that they wouldn\'t be rephrasing any questions (Communication = 2). \
    I suppose that at least they were explicitly ableist.

I noticed quite early on that I was only being interviewed because I checked that box.  I made my presentation and none \
    of the interview panel asked any questions.  I've delivered autism training to over 1,000 delegates, and in my experience there are \
    usually questions once I've finished presenting.  Of the three people on the interview panel, only the lead interviewer asked any questions during the interview; the other \
    two mumbled "No thanks", or words to that effect, when asked if they had anything to say.  They looked bored and disengaged and didn't seem \
    to be worried who knew about it.  I got feedback that I had shown 'adequate' skills for the role.  I wonder what score I would have achieved \
    if their interview skills were equivalent.  Further, I dare to suggest they would have been more engaged with me if the interview was conducted in person.
'''
)

# Plotting for org C
c = pd.DataFrame(dict(
    r=[5,3,2,2,1],
    theta=['Location','Environment','Timekeeping','Communication','Affability']))
fig4 = px.line_polar(c, r='r', theta='theta', line_close=True,range_r = [0,5],title='Organisation C Scores', color_discrete_sequence=px.colors.sequential.Pinkyl_r, template='plotly_dark')
fig4.update_traces(fill='toself')
st.plotly_chart(fig4)

st.markdown('***')

st.subheader('What did I take away from these experiences?')
st.markdown('''
Ultimately, I concluded that none of these organisations were not suitable for me.  If I have to fight for my rights based on the Equality Act 2010 and the [Autism Act 2009](https://www.legislation.gov.uk/ukpga/2009/15/contents) each day \
    then I'll have less time to do my actual work.

In each case it wasn't my ability to do the role that was in question so much as it was the interviewers' inability to \
    communicate in a manner that I could understand.  Consequently, the interviews were effective in telling me that I wouldn't have enjoyed working for any of \
    those organisations.

To find out how you can be less like those interviewers, read the next sections of the app.
''')
