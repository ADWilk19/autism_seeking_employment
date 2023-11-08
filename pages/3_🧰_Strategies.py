# Imports
import streamlit as st
import pandas as pd

# Side bar and page config info
st.set_page_config(
    page_title="Strategies to help autistic people find and keep employment",
    page_icon="🧰",
    layout="wide"
)
st.sidebar.header("Strategies to help autistic people find and keep employment")
st.sidebar.markdown("This section offers some strategies for helping autistic people to find, and keep employment.")

# Content
st.markdown("# Strategies to help autistic people find and keep employment 🧰")
st.warning("These strategies are **not** universal! REMEMBER: When you've met one autistic person, you've met one autistic person!",icon="⚠️")

st.markdown('''
    Below are a few tips that might help you to work more effectively with autistic people.  It's designed to be a starting point from which you \
        can do more research as opposed to a catchall enumerating the secrets to life, the universe and everything.

***''')

# Communication
st.subheader('1. Watch your mouth 👀👄')
st.markdown(
'''
Autistic people tend to interpret words [literally](https://autism-all-stars.org/autistic-literal-thinking/).  As such, \
    you will need to be explicit, rather than implicit, when communicating one's thoughts and \
    instructions to autistic people. The subheader above is an example of figurative language, which is poor practice when communicating \
    with autistic people.

Things you should do ✅:
* Agree how you will communicate with the autistic person, for example via
    * telephone 📱,
    * video call 📹,
    * email 📧,
    * messaging 💬, or
    * in person 👫
* Create a step-by-step plan of the interview process, ideally including questions, so that the autistic \
    person knows what to expect. 🤔
* Avoid asking open-ended questions where possible. 👐🤫
* Allow the autistic person time to process what you have said. This includes emails and LinkedIn messages. 🕛
* Encourage questions. 💬❔
* If in doubt, check their understanding of what you have said.
***''')

# Consistency
st.subheader('2. Be consistent 💯')
st.markdown(
'''I believe it should go without saying that it can be difficult to work with autistic people, espcially if you're inconsistent in your actions. I'm not saying that \
    you have to get everything correct 100% of the time.  Further, I'm not saying that you should treat everyone the same way; everyone is different and has individual needs. \
    With that in mind: **Manage epxectations wisely**. 🔮

* Don't say you will do something unless you can guarantee it.
* If you make plans to do something but an event occurs which causes a delay then be sure to inform the \
        autistic person as soon as possible.
* Be clear and concise about what assistance, if any, you'll be able to provide to the autistic person before you agree to do anything.
* Be honest, especially when you don't know the answer!
* Avoid last-minute changes unless absolutely necessary.
* Share pictures of meeting places so that the autistic person knows what to expect (and don't be surprised if they tell you that the meeting place doesn't resemble the picture \
    you sent). Finally...
* **Be accountable for your actions!** Everyone makes mistakes, but we can't learn if we don't recognise and take ownership of them.

***''')

# Reasonable Adjustments
st.subheader('3. Make Reasonable Adjustments 🎛️')
st.markdown('''According to [Citizens Advice](https://www.citizensadvice.org.uk/law-and-courts/discrimination/check-what-type-of-discrimination-youve-experienced/duty-to-make-reasonable-adjustments-for-disabled-people/), \
    employers have a duty to make reasonable adjustments for disabled people as defined by the the Equality Act 2010.  Click on the hyperlink in the previous sentence in order to gain a better \
    overview of what that entails.

From a high level, there are three ways in which reasonable adjustments can be made:

1️⃣ - **Change the way things are done**

2️⃣ - **Change a physical feature**

3️⃣ - **Provide extra aids or services**

I encourage you to do your own research in this regard.  As a starting point, the University of Nottingham have published [a toolkit for reasonable adjustments](https://www.nottingham.ac.uk/edi/documents/case-studies-for-reasonable-adjustments.pdf).
***

''')

# Sensory differences
st.subheader('4. Be Mindful of Sensory Differences 🖐️👅👁️🦻👃💪')
st.markdown('''Everyone experiences the world differently.  According to research done by Autistica, around [8 in 10 autistic people process sensory information differently](https://www.autistica.org.uk/what-is-autism/anxiety-and-autism-hub/sensory-differences).
''')
st.image('visuals/OIUH6F0.jpg', width=500)
st.caption('Image by macrovector on Freepik: https://www.freepik.com/free-vector/infographic-with-gears-five-senses_1048636.htm')
st.markdown('''
In addition to the five senses in the image, above, there are two other senses to consider:
* Proprioception or body awareness; and
* Vestibular, or balance.

When it comes to sensory differences, people may be hyper-sensitive (over-sensitive) to certain senses and hypo-sensitive (under-sensitive) to others.

I'm hyper-sensitive to touch, light and sounds that are high-pitched. As a consequence, I try to give people personal space in the hope that they reciprocate; \
    I sometimes wear sunglasses 😎 to take the worst of the glare from office lighting; and if I really need to concentrate I might wear noise-cancelling \
    headphones. 🎧  I'm also hypo-sensitive to my vestibular and proprioception senses, which basically means that my balance is quite poor and I always have the urge to move.
***
''')


# Seek further autism training
st.subheader('5. Seek further Autism training 🎓')
st.markdown('''
Since 1 July 2022, all registered health and social care providers are required to provide training for their staff in learning disability and autism.  This legal requirement \
    was introduced by the [Health and Care Act 2022](https://www.legislation.gov.uk/ukpga/2022/31/section/181/enacted).  That means that, in most cases, people are not \
    required to receive autism training.

That said, I believe that in order to gain the most from the autistic person with whom you interact it would be a good idea for you to receive some formal autism training. \
    When picking a training provider, I encourage you to choose an organisation that employs autistic individuals to deliver the training themselves.  One such example is [Aspie Trainers](https://www.aspietrainers.co.uk/), \
    a training organisation which I co-founded back in 2014.

If the idea of formal training is not to your liking then there are a plethora of YouTube videos and autism blogs to explore.  If in doubt, ask the person with whom \
    you are working to sign-post you to one (or as many as) they recommend.
***

Ok, that's all I have to share with you at this time.  If you have any questions or comments you can reach me on LinkedIn [here](https://www.linkedin.com/in/adwilkinson19/)''')
