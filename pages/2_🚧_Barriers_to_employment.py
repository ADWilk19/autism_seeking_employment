# Imports
import streamlit as st
import pandas as pd

# Side bar info
st.set_page_config(
    page_title="Barriers to employment for autistic job seekers",
    page_icon="🚧",
    layout="wide"
)
st.sidebar.header("Barriers to employment for autistic job seekers")
st.sidebar.markdown("This section looks at some of the factors which adversely affect autistic people seeking employment.")
st.markdown("# Barriers to employment for autistic job seekers 🚧")
st.warning('The following information might be triggering for some people.',icon="⚠️")

# Page Content
st.markdown('Below are five of the barriers to entry for autistic people seeking employment.')

st.header('🚧 1: The application and hiring processes are too long ⌛')

# Application Example
st.markdown('''>Great news, you've found an advert for a job role that is neither non-specific, nor too verbose, and you feel \
     that you would be a good fit for the role.  You have a CV which you have worked on, extensively, to highlight \
     your career achievements.  You even have a cover letter template curated so that you can tweak it and get the \
    application sent without too much extra effort.  You click on the apply button on the company's website and thereafter a blank form loads \
    which asks you to enter all of the information on your CV (there's a button which allows you to link your LinkedIn \
    profile, but it doesn't fill the form properly.  Uploading your CV yields similar results).  You spend 30 minutes filling in the form, before you make a start \
    on the essay questions, ensuring that the answers to all of the questions provide information in accordance with the job/person spec, thus \
    demonstrating your capability to do the role.  You land on the final page of the form, which concerns your \
    Equality and Diversity information.  You click on the box to say that you consider yourself disabled, then \
    rather than having a list of conditions and associated reasonable adjustments which you could tick, the form asks you to provide\
    as much information as you can about any reasonable adjustments you may need should you get through the to interview stage.\
    You're autistic and have been doing your utmost to get this form filled; you've spent hours on this application, reliving \
    your career up to this point.  That includes positive experiences, but copius negative experiences, too. \
    You feel emotionally drained and don't really feel like writing about reasonable adjustments when there's no way to know \
    what they will be; having never set foot on the property of the business, nor having met any of its staff, its difficult to ascertain \
    how much knowledge they have about autism, let alone whether they can actually apply it in the real world. So, you declare your autism \
    and submit the form.  You receive an automated email thanking you for your application.  You might get another form \
    to fill in regarding your application experience.  If you are fortunate enough to get through to the next round, you might hear back from \
    a real person after the submission date closes, but only if you're lucky.  That's one job application done, two more to do today.  \
    Meanwhile, the company's algorithm scans your application for key words in a matter of seconds and will progress your application in accordance with \
    some boolean logic.  The closing date passes and you assume you've been unsuccessful; companies usually notify you \
    when they invite you to interview, right?  Oh well, onto the next applications...''')

st.markdown('''The example above has been a common experience for me when applying for work.  [Indeed](https://www.indeed.com/career-advice/interviewing/interview-timeline)\
    states that the job application process for one job can take place upto eight weeks before an offer of employment is issued.  This is a long time to wait for anyone, and it isn't helped \
    when hiring managers take longer than expected to feedback, or go on leave midway through the hiring process.  I had an in-person interview in September 2018 for which I still haven't \
    received any feedback (today's date is Saturday, 21 October 2023).  I stopped working with the recruitment agency that convinced me to go for the interview after that.  \
    There's a vast difference between conducting due diligence on a candidate, and taking liberties.''')

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.image('visuals/office-space-job-application-meme.jpeg')
    st.caption('Meme found [here](https://tolerosolutions.com/what-are-your-employees-really-doing-at-work/)')

st.markdown('''***
## 🚧 2: Communication ✍️🗣️''')
st.markdown('''Consider the following phrases:

1. A long shot.
2. Back to the drawing board.
3. To corner the market.
4. Hands are tied.
5. Up in the air.
6. Learn the ropes.
7. A learning curve.
8. By the book.

What do they have in common?''')
answers = st.selectbox('Choose an option from the dropdown list, below:', ('',  'These phrases should not be interpreted literally.',
                                                          'These phrases are part of a list which everyone working in business in the UK should know, according to Europe Language Jobs.',
                                                          'These phrases are idioms.',
                                                          'All of the above are true.'))


if answers == '': pass
elif answers == 'All of the above are true.':
    st.success('Congratulations! That is the correct answer! 🎉',icon='✅')
else:
    st.error("Bad luck, try again!",icon='❌')

st.markdown('''Those eight phrases are idioms.  I'm going to make a _gigantic_ assumption and state that I believe you could *precisely* define each of them \
    (you can find the definitions [here](https://www.europelanguagejobs.com/blog/17-Business-English-idioms), just in case you \
    want to be honest with yourself 😉).  Consequently, if someone were to use one of those idioms then you would be able to work out the context of what \
    s/he meant.  This won't be true for most autistic people, who tend to be very literal when interpretting information. \
    I've personally taken the time to download and read a book on idioms.  Was that a reasonable adjustment on my part? \
    Given that similes, metaphors, alusions and irony, all of which are examples of figurative language that \
    **cannot** be easilly understood by a lot of autistic indiviudals (I wouldn't be so rude \
    as to pass judgement on you, dear reader 😉), how would you answer that question (bearing in mind that rhetoric is another form of \
    figurative language)?  For the record, no, I'm not being sarcastic (on this occassion).

***''')

st.markdown('## 🚧 3: Lack of work experience 📉')
st.markdown('''One thing that you need to realise about autistic people is that we're honest; \
    if you find it hard to take criticism, you are likely to find little joy working with most autistic people, especially if you \
    can't "walk the walk", i.e, "show that something is true by your actions rather than your words".

Personally, I found it particularly annoying when my colleagues overstated their capabilities and expected me \
    to fill any gaps in their knowledge without properly explaining anything to me.  When this happened to me in the past my \
    performance suffered and my contract was terminated.  As a result, I've not got an awful lot of work experience because it \
    takes me time to assess where things went wrong, which in turn prevents me from applying for more work, \
    which leads to longer unemployment gaps on my CV...

Let's not forget that having two years worth of experience working in a role means nothing in isolation.  For example,\
    stating you have two years of SQL experience when you've just been running the same queries, originally written by your manager, at the end of \
    each month, doesn't mean you understand how to create temporary tables in order to calculate churn rates. Yet some employers \
    insist on that level of experience for junior roles.  For me, that makes about as much sense as this meme:''')
col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image('visuals/62306ec38c3b9.jpeg')
    st.caption('This meme was found [here](https://www.memedroid.com/memes/detail/3638431/Do-you-have-any-experiences?refGallery=tags&page=1&tag=experience).')
st.markdown('***')

st.markdown('## 🚧 4: Sensory differences 👁️👃👂✋👅')
st.markdown('Interviews can be stressful for everyone, even when technology works (has anyone else \
    been invited to interview over Zoom, just to find out that the call link is broken five minutes beforehand?).  When \
    someone is autistic, there are often sensory differences which can drastically affect their experience at interview. \
    The video below from the National Autistic Society provides one such example: ')
st.video('https://www.youtube.com/watch?v=GAehvcnFjmI')
st.markdown('''Unfortunately, most employers rely on us to divulge any sensory differences we have, which makes us vulnerable because of our communication differences. \
Assuming the interviewers had a vague understanding of how we experience the world, and they were able to interpret our description *literally*, \
reasonable adjustments could be made to aid the individual (more on that, later).

***''')

st.markdown('''## 🚧 5: Lack of Planning Skills 📋''')

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.markdown("![Man planning on a whiteboard](https://media.giphy.com/media/usz0fqhUiVxSs6IUKB/giphy.gif)")
    st.caption('[GIF available here](https://media.giphy.com/media/usz0fqhUiVxSs6IUKB/giphy.gif)')

st.markdown('''I once worked with an autistic person who had a high IQ (~140) and was a member of Mensa.  In spite of that, \
    this person had no formal qualifications, and it often took them 45 minutes to make a slice of toast because \
    they were unable to plan; in effect, each time they made a slice of toast they were doing it for the first time. \
    Despite this, with the right support they were able to get paid to deliver autism training, which enabled them \
    to share their experience.  All of the training delegates believed that their message was the most powerful.

Another autistic person I knew was the facilitator of a self-advocacy group.  One day we were meeting to discuss \
    the ground rules for the group.  Upon realising that they needed to leave instantly so that they could catch their \
    train, they left the group's laptop on the table, still logged-in, before leaving the meeting without saying another word \
    (I shut down the laptop and returned it to the office upstairs after they had left).  Subsequent training was provided \
    to ensure that this scenario was not repeated.

As for me, my planning skills are better than most, given that I've co-ordinated and minuted meetings for a FTSE 250 company in \
    the financial services sector (when I left the company, my line manager said that they couldn't have done my role).  The \
    reason I was able to do this is that I tried to be as flexible as possible, often re-submitting the meeting papers due to late submissions/last-minute agenda items, and \
    doing my best to realise that last-minute changes are to be expected.  In other words, I expect things to go wrong and plan accordingly. \
    This only works because I expect people to say one thing and do another.  Most autistic people will take you at your word, however, and will not \
    be able to cope with rapid and unexpected change.

***
''')
st.markdown('''## 🚧 6: Lack of Social Skills 💬''')
st.image('visuals/pexels-photo-3184360.webp')
st.caption('Photo by fauxels from Pexels: https://www.pexels.com/photo/group-of-people-gathered-around-wooden-table-3184360/')
st.markdown('''Think of the conversations that you had at work this week.  How many of them were specific to your job \
    and how many of them revolved around small talk - the weather, sports, TV programmes, pets, etc.?  \
    Now imagine that you're autistic and you were trying to write a report for your line manager which \
    could have a bearing on your performance review at the end of the year.  People come to your work island \
    and begin talking about *Bake Off*, even though you work for a telecomms company, don't enjoy baking, and have \
    never indicated otherwise.  You find it distracting, but don't know how to explain this to your colleagues \
    without being told that you are rude.  This scenario, and others similar to it, is why some autistic people \
    struggle to keep work.  Whilst I realise that some people talk to alleviate stress or because they enjoy social interaction \
    (I wonder what that's like), when I go to work, I go to *work*.  The sad reality is that most non-autistic people cannot appreciate \
    just how disruptive they can be (assuming that they actually care about how they're perceived...).

***

Ok, that's enough regarding barriers to employment.  Read on to see which strategies may prove useful when working alongside autistic people.
''')
