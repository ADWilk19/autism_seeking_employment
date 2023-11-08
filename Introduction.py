# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from my_funcs import *

# Page Setup
st.set_page_config(
    page_title="Autistic and Seeking Employment",
    page_icon="🧐",
    layout="wide"
)
# Sidebar
st.sidebar.header("Autistic and Seeking Employment")
st.sidebar.markdown('''This section outlines the purpose of this paper; attempts to define what autism is; and looks at autism prevalence and employment statistics.
''')

# Page Content
    # Introduction
st.header("Autistic and Seeking Employment 🧐")
st.warning('The following information might be triggering for some people.',icon="⚠️")
st.write('''Imagine you are carrying a mirror in front of you, at arms’ length, wherever you go.\
    Its about 2.13m/7’ tall and 1.52m/5’ wide, and, rather than reflecting you as a person, \
    it only highlights your difficulties; it is designed so that you receive continuous, distorted, \
    fragmented feedback as you do your best to understand, let alone meet, the expectations of the time \
    and space that you occupy.  Assuming its thickness is 0.625cm/0.25”, its weight could be estimated at \
    around 51.4kg /113.4lbs, although depending on the situation it can feel much heavier.\
    Would you want to engage with that mirror so that you can become what it expects you to be? \
    Would you be able to process and understand the feedback it provides?  Would you even be able to lift it? \
    Now imagine that this mirror is in fact society, with dimensions larger than your mind can fathom, each of \
    which offers too much information to process.  This is how I felt as an autistic adult looking for work.''')
st.image('visuals/luis-villasmil-gzb4RKX-pdc-unsplash.jpg', caption=None,
width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.caption("Photo of a mirror by [Luis Villasmil](https://unsplash.com/@villxsmil?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/mirror?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)")
st.markdown('''The purposes of me creating this app are threefold:
1.	To share my experience of applying for work, including three case studies;
2.	To highlight some of the barriers to entry for autistic people seeking employment; and
3.	To propose strategies which might facilitate hiring managers, agency recruiters, HR personnel and colleagues working with autistic people to help them find and/or keep employment.

Before I do that, let’s take a look at what autism is, how prevalent it is, and the current employment status of the autism population (i.e., those people diagnosed with autism).
''')
st.markdown('***')
st.subheader("What is autism? 🤔")
st.write('''
            Autism can be viewed from the [medical or the social model of disability](https://www.disabilitynottinghamshire.org.uk/index.php/about/social-model-vs-medical-model-of-disability/), and as such,
            there are many different ways of defining it.  According to [Autistica](https://www.autistica.org.uk/what-is-autism/what-is-autism),
            autism “…affects the way people communicate and experience the world around them.”  Similarly,
            the [National Autistic Society](https://www.autism.org.uk/advice-and-guidance/what-is-autism) defines Autism as “…a lifelong developmental disability which affects how people communicate and interact with the world.”

Personally, I like this one by Dr Luke Beardon, Senior Lecturer at The Autism Centre at Sheffield Hallam University:

>“Autism refers to a neurotype that leads to a cognition that is qualitatively different from that of the PNT\
 [Predominant Neuro-Type, or non-autistic people] in the way that information specific to communication, social\
 interpretation and interaction is processed and understood; and to a perceptual reality of the sensory environment\
 that differs considerably from one individual to the next.” ([Beardon, 2017](https://www.amazon.co.uk/Autism-Adults-Luke-Beardon/dp/152937541X/ref=sr_1_2?keywords=luke+beardon+autism&qid=1664368608&qu=eyJxc2MiOiIzLjIyIiwicXNhIjoiMi43OCIsInFzcCI6IjIuODIifQ%3D%3D&sprefix=luke+baer%2Caps%2C284&sr=8-2))

It is worth noting that there have been multiple theories regarding autism.  Click [here](https://www.spectrumnews.org/features/legacy-special-reports/theories-of-autism/) for a list of articles explaining 7 of them \
    (there are more, but I don't want to go into too much detail).

There is a joke in the autism community which goes like this:
>When you've met one autistic person, you've met one autistic person.

Consequently, it's very difficult to be universally autism-friendly.\
    I've worked with autistic people whose sensory profile differs significantly from my own. \
I'm photosensitive, so I often wear sunglasses when in meetings.  One autistic person I worked with didn't like this \
    because they couldn't see my eyes.  In the end I took off my sun glasses to appease that person.  That was not a \
    reasonable adjustment.  It was my choice, I decided to do it, and my eyes stung for the duration of the meeting. \
    Other autistic people may not be as accomodating.  It's their choice.''')

st.markdown('''Given that:
1. Autism has [genetic](https://www.spectrumnews.org/news/autism-genetics-explained/) and environemntal causes;
2. Research into those causes are on-going; and
3. Autism is diagnosed by observing [behaviour](https://www.nhs.uk/conditions/autism/getting-diagnosed/how-to-get-diagnosed/);
4. It's no wonder that there is so much heterogeneity (i.e., difference) among those of us whom are autistic.''')
st.warning("As such, some of the strategies I offer here may not be appropriate for the autistic person with whom \
           you interact.",icon='⚠️')

# Neurodiversity
st.markdown('#### A note on Neurodiversity ♾️')

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.image('visuals/rsz_stockvault-brain-connections-creativity-and-intelligence-concept193493.jpg', caption=None,
width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption('Picture of a human brain by Jack Moreh, available from [stockvault](https://www.stockvault.net/photo/193493/brain-connections-creativity-and-intelligence-concept#)')
st.markdown('''Please be mindful that **everyone is neurodiverse**.  That's the opinion of Judy Singer, the sociologist who \
    coined the term back in the late 90s.  Read this [blog post](https://neurodiversity2.blogspot.com/p/what.html) for proof.  \
    According to Singer, Neurodiversity:
* is a feature of Earth as a whole, since humans have colonized all Earth's ecosystems;
* refers specifically to the limitless variability of human cognition and the uniqueness of each human mind;
* was coined, [Judy believes], by [herself] in the 1990s, as a political term to argue for the importance of including all neurotypes \
for a thriving human society.

Furthermore, the neurodiversity movement is "an evolving, decentralized and leaderless social movement".  Judy's book, [NeuroDiversity: \
The Birth of an Idea](https://www.amazon.com/NeuroDiversity-Birth-Idea-Judy-Singer-ebook/dp/B01HY0QTEE/), is a thought-provoking read for those of \
        you whom prefer to go into more detail on the origins of neurodiversity.

Bearing all of this in mind, when someone refers to their "neurodiverse colleagues", to whom are they referring?''')
q1 = st.text_input("Type your answer here. 💡HINT: it's a one-word answer💡")
if q1.lower() == 'everyone':
    st.success('Correct', icon='✅')
elif q1 == '':
    pass
else:
    st.error('The correct answer is **everyone**', icon='❌')
st.markdown('''Personally, I have misgivings about the neurodiversity movement.  Whilst I agree that everyone has a story \
    to tell and should have the opportunity to participate in society, for some the harsh \
    reality is that they won't be able to do that without significant on-going support and, as things stand, UK society has multiple issues to consider:
* there's an on-going [cost of living crisis]('https://www.theguardian.com/business/cost-of-living-crisis');
* the cost of one war is significant, in terms of lives and resources, so getting involved in two for whatever reason will be \
costly ([the UK only paid off its WWII debt in 2006](https://www.nytimes.com/2006/12/28/business/worldbusiness/28iht-nazi.4042453.html));
* as of June 2023 there's a [£28.5 billion trade deficit]('https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/apriltojune2023') \
            that will need to be paid to residents outside of the UK;
* the NHS is overburdened; and
* many more besides.

For me, advocates for the neurodiversity movement try \
        to accentuate the positives of difference, which is great, but I've come to sympathise with parents and/or  neurodivergent people whom feel \
        misrepresented and even more marginalised as a consequence.

I spent the first 26 years of my life trying to be something/someone that I wasn't designed to be, and my mental health \
    suffers to this day as result.  In spite of this, I'm able to recognise that there are other people out there whose needs far outweigh my own. \
    Unfortunately life isn't fair, so I encorage you to be mindful that for every [Elon Musk](https://www.axios.com/2022/04/15/elon-musk-aspergers-syndrome), \
    there might be hundreds of thousands of people who can't make themselves understood (I'm talking about autistic people in this context and \
    it's a conservative guess on my part); that won't change unless everyone learns to communicate respectfully in a manner which \
       can be understood by their audience.  I'm willing to take that challenge on.  Are you?

***''')


# Autism Prevalence Map

st.subheader("Autism prevalence 📈")
st.write('The chart below is interactive and is my attempt to replicate the one available [here](https://worldpopulationreview.com/country-rankings/autism-rates-by-country). \
    Hover over the countries to see autism prevalence per 10,000 people.')
# Load both datasets
file = 'raw_data/world_autism_prevalence/autism_world_prevalence.csv'
file2 = 'raw_data/world_autism_prevalence/country_coords.csv'
aut_prev = pd.read_csv(file)
coords = pd.read_csv(file2)
# change ISO_A3 column name to iso_a3 in the coords dataframe
coords.rename(columns = {'ISO_A3':'iso_a3'}, inplace = True)
# Perform a left join on iso_a3 to get latitude and longitude
map_df = pd.merge(aut_prev,coords, on='iso_a3', how='left')
# Drop duplicate name_y column and rename name_x column
map_df.drop('name_y',axis=1,inplace=True)
map_df.rename(columns= {'name_x':'name'}, inplace=True)
# Sort by values
map_df = map_df.sort_values(by=['est_autism_prevalence_per_10k'], ascending=False)

# Plot map
fig = go.Figure(data=go.Choropleth(
    locations = map_df['iso_a3'],
    z = map_df['est_autism_prevalence_per_10k'],
    text = map_df['name'],
    colorscale = 'Viridis',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Prevalence per 10,000',
))
# Change ocean colour, map layout, and annotations
fig.update_geos(
    resolution=50,
    showocean=True, oceancolor="LightBlue",
)
fig.update_layout(
    width=1000,
    height=800,
    paper_bgcolor='#FFFFFF',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth'
    ),
    title={
        'text': '<b>Autism prevalence is highest in the Middle East 📈</b>',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    },
    title_font_color='#000000',
    title_font_size=20,
    font=dict(
        family='Arial',
        size=12,
        color='#000000'
    ),
    annotations = [dict(
        x=0.5,
        y=0.01,
        xref='paper',
        yref='paper',
        text='Source:<a href="https://worldpopulationreview.com/country-rankings/autism-rates-by-country">\
            Autism rates by country (2023)</a>',
        showarrow = False,
    )]
)
# Plot the fig
st.plotly_chart(fig,use_container_width=True)
st.caption('Fig 1: World autism prevalence map.')

    # Narrative
st.markdown('''There are many factors which affect a person's ability to receive an autism diagnosis, including but not exclusive to: \
gaining access to dianostic services; the ethnicity and/or gender of the individual seeking diagnosis; \
and/or the attitudes of the people in a position to diagnose.  As at 01 June, 2023, the number  \
of open "suspected autism" referrals in England stood at \
    [143,119](https://app.powerbi.com/view?r=eyJrIjoiYTNmZmEwNWYtYzcyYS00MDIwLTgxYmYtMGVjZDYwNDM0NWMyIiwidCI6IjUwZjYwNzFmLWJiZmUtNDAxYS04ODAzLTY3Mzc0OGU2MjllMiIsImMiOjh9).''')

# Top 5 countries
st.subheader('The 5 countries where autism is most prevalent are in the Middle East')
# Set figsize
fig2, ax = plt.subplots(figsize=(10,5))
# Declare x and y before plotting
x = map_df['name'].iloc[0:5]
y = map_df['est_autism_prevalence_per_10k'].iloc[0:5]
plt.barh(x, y,color=['#440154','#24898d','#20998a','#20998a','#2bac80']) # Specify the color of the bars

# Adding labels to the bars
for index, value in enumerate(y):
    plt.text(value, index,
             str(value))

# Formatting
plt.title('Top 5 countries by autism prevalence per 10,000 people',size = 18, loc='left')
ax.set_xticks([])
ax.set_xticklabels([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.invert_yaxis()
plt.xlabel('Prevalence per 10,000 people', size = 13)
plt.ylabel('Country', size = 13)

st.pyplot(fig2, ax)
st.caption('Fig 2: Top 5 countries with the highest autism prevalence.')


    # Bottom 5 countries
st.subheader('The 5 countries where autism is least prevalent are in Europe')
fig3, ax2 = plt.subplots(figsize=(10,5))
# Declare x and y before plotting
x = map_df['name'].iloc[193:]
y = map_df['est_autism_prevalence_per_10k'].iloc[193:]
plt.barh(x, y,color=['#e8e427','#e8e427','#e8e427','#e8e427','#fde725'])
# Adding labels to the bars
for index, value in enumerate(y):
    plt.text(value, index,
             str(value))
# Formatting

plt.title('Bottom 5 countries by autism prevalence per 10,000 people',size = 18, loc='left')
plt.xlabel('Prevalence per 10,000 people', size = 13)
plt.ylabel('Country', size = 13)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_xticks([])
ax2.set_xticklabels([])
ax2.invert_yaxis()
plt.show()

st.pyplot(fig3, ax2)
st.caption('Fig 3: Bottom 5 countries with the lowest autism prevalence.')
st.markdown('***')

# Employment
st.subheader('Autism and employment 💼')
st.write('''Part of the [national strategy for autistic children, young people and adults: \
            2021 to 2026](https://www.gov.uk/government/publications/national-strategy-for-autistic-children-young-people-and-adults-2021-to-2026/the-national-strategy-for-autistic-children\-young-people-and-adults-2021-to-2026#supporting-more-autistic-people-into-employment-1),\
         a policy paper last updated by the Department of Education and the Department of Health & Social Care in July 2021,\
            refers to supporting more autistic people into employment:
>"By 2026, we want data to show that we have made progress on closing the employment gap for autistic people, drawing on the Labour Force Survey. \
    We want more autistic people who can and want to work to do so, and to ensure that those who have found a job are \
        less likely to fall out of work. We also want to show that employers have become more confident in hiring and \
        supporting autistic people, and that autistic people’s experience of being in work has improved."

This is promising news, but what is the current state of employment?''')

st.subheader('Percentage of people in employment by disability status: Q3 2021 📈')
st.write('''The following statistics were taken from the [Office of National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/disability/articles/outcomesfordisabledpeopleintheuk/2021), \
and show the employment rates of non-disabled, disabled, and autistic people aged 16 to 64 years \
    living in the UK, for the quarter ending September 2021. The numbers in green represent the change year on year.''')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Non-Disabled',81.6,0.3)

with col2:
    st.metric('Disabled',53.5,1.4)

with col3:
    st.metric('Autistic',29,7.2)

st.caption('''Sources for [2020 Data](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/disability/articles/outcomesfordisabledpeopleintheuk/2020#employment)
           and [2021 Data](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/disability/articles/outcomesfordisabledpeopleintheuk/2021)''')
st.markdown('''These statistics look promising, with the number of autistic people in employment having increased by 7.2 percentage points between Q3 2020 and Q3 2021. \
            As an autistic person seeking continued employment, however, I hope that these figures continue to increase. 7 out of 10 (71% of) autistic people between 16 and 64 are out of employment.\
            This represents a huge opportunity for recruitment agents to increase their fees, given that:
1. According to Office of National Statistics data, [nearly two-thirds (64.1%) of the population in 2021 (that's 38.2 million people) were aged 15 to 64 years](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/populationandhouseholdestimatesenglandandwales/census2021#age-and-sex-of-the-population).
2. Autism prevalence in the UK is ~78.1 per 10,000, meaning ~298,000 of those people aged 15-64  will have an autism diagnosis.''')
equation_1 = st.expander('Show/hide calculations')
with equation_1:
    st.latex('''Autistic\ and\ aged\ 15-64 = Proportion\ of\ autistic\ people\ \\times Population\ aged\ 15-64''')
    st.latex('''\Rightarrow \\frac{78.1}{10,000}\\times 38,200,000''')
    st.latex('''\Rightarrow 0.00781\\times 38,200,000''')
    st.latex('''= 298,342''')
st.markdown('''3. 7 out of 10 (~71%) of those 298,342 people will be unemployed (~211,822):''')
equation_2 = st.expander('Show/hide calculations')
with equation_2:
    st.latex('''
    Autistic\ and\ unemployed\ aged\ 15-64 = 0.71 \\times 298,342 = 211,822.82
            ''')
st.markdown('''4. The UK National Living Wage for those working full-time (based on [£10.42](https://www.gov.uk/government/publications/the-national-minimum-wage-in-2023/the-national-minimum-wage-in-2023) per hour x 37.5 hours a week) is £20,319.
5. Recruitment costs can be between [15% and 20% of a candidate's first annual salary](https://www.agencycentral.co.uk/articles/2016-10/how-recruitment-agencies-get-paid.htm), going up to 30% for harder \
    to fill positions; ergo
6. If another 7.2% (~15,251) of the autistic working age population were successfully hired on a full-time basis at a fee of 17.5%, this would mean that \
    there are roughly **£54.2m** worth of recruitment fees to be earned:''')
equation_3 = st.expander('Show/hide calculations')
with equation_3:
    st.latex('''
            Potential\ recruitment\ fees\ = Number\ of\ autistic\ people\ \\times  National\ Living\ Wage\ annual\ salary\ \\times recruitment\ fee\ percentage\
            ''')
    st.latex('''
            \Rightarrow 15,251 \\times  £ 20,319 \\times 0.175
            ''')
    st.latex('''
\Rightarrow £54,229,887.08 \\approxeq £54.2m''')

st.markdown('''Even a small proportion of that could help a few of you to heat your homes during the winter. 😉

***

So, what are you waiting for? Explore the rest of this app to find out how you can support someone like me to find employment.
         ''')
