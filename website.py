import streamlit as st
st.set_page_config(page_icon="❤️", layout='centered', page_title="Merry Christmas")

st.title('Elizabeth Sarah McNaughton')

container = st.container()

(container.write('my description of her'))

Memories, Inside_Jokes = st.tabs(["Memories", "Inside Jokes"])

with Memories:

    col1, col2, col3 = st.columns(3)

    with col1:

        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg',caption ="Lizzy's First Appearance on Camera Roll", width= 200)
        st.image('D677062A-24CD-42AE-80B2-680571D608CE_1_105_c.jpeg', caption="Our First Met Date",
                 width=200)
        st.image('F7102E66-F614-4BEF-B54F-62381E3D17FD_1_105_c.jpeg', caption="Lizzy's First Time Meeting My Dad",
                 width=200)
        st.image('F6DCB01B-6F34-481A-B0C6-3728D14769A3_1_105_c.jpeg', caption="Pre Bryant Park",
                 width=200)
        #need to replace
        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg', caption="Lizzy's First Appearance on Camera Roll",
                 width=200)

        st.image('B34A68A1-6706-4CB9-87E2-FD24CE011B27_1_105_c.jpeg', caption ='Lizzy somehow smiling after learning '
                                                                               'about the oddities of Kaleb')
        st.image('A25AEF46-CC8B-4197-9C25-2CC8E4BF75DE_1_105_c.jpeg', caption="First of Many Jefferson Coffee Dates",
                 width=200)
        st.image('3286420A-551D-41F8-95BB-809008615974.jpeg', caption="First Dinner With Familia",
                 width=200)
    with col2:

        st.image('D1D508D3-1F08-46E4-A27D-873474688308_1_105_c.jpeg', caption="Beating Lizzy At Chess. Thankfully, She Didn't Have My Mom's Reaction!",
                 width=200)

        st.image('E56EF88E-5ECC-4EFC-AEC8-D7ED704D5178_1_105_c.jpeg', caption="I LOVE KNOCKING ON DOORS",
                 width=200)

        st.image('0A9E7DFA-BD3E-456F-AE8D-1B37ECFE30C8_1_105_c.jpeg', caption="Brooklyn Time",
                 width=200)

        st.image('A727011D-E97E-467A-AE42-B8D67EC36502_1_102_o.jpeg', caption ='Lizzy Carrying At Hot To Go',
                 width =200)
        st.image('7125D8A4-05A6-476D-8177-3CD0DD36AA91.jpeg', caption ='Hard at Work. Or Hardly Working', width = 200)

        st.image('A9BDCCFF-D743-4911-91DB-43E8C661FE05_1_105_c.jpeg', caption="Costco Date!",
                 width=200)
    with col3:
        st.image('0A9E7DFA-BD3E-456F-AE8D-1B37ECFE30C8_1_105_c.jpeg', caption="An Unwarranted Middle Figer (GO IU!)",
                 width=200)

        st.image('F9659469-FEF7-43B2-86CA-0897B32D52AD_1_105_c.jpeg', caption = 'I phew up', width = 200)

        st.image('7D0C9F30-C53E-43AD-A568-03CD219A93E5_1_105_c.jpeg', caption="Our First Ever Concert",
                 width=200)

        st.image('91EA5FB5-DC75-484A-BE9B-B235F2A42868_1_105_c.jpeg', caption="Saturday Night In",
             width=200)

        st.image('840A7B8B-7EFC-41B4-8B7A-8F32C7C5CD4C_1_105_c.jpeg', caption="No Women Knew What Was Going On In the Bagel Store",
             width=200)

        st.image('49567F8A-1040-45B9-A590-EFD3E3B1D295_1_105_c.jpeg', caption="The Best View Wasn't the WTC. It was right next to Matt",
             width=200)
        st.image('74049FE1-D2AE-4E11-B12F-FA11B4CA8B92_1_105_c.jpeg', caption="One of my Favorite Photos",
                 width=200)

with Inside_Jokes:
    st.header('Unhinged Elizabeth Quotes')
    st.write('RIP Compliance Cow')
    SFW_Quotes, NSFW_Quotes = st.tabs(["SFW Quotes", "NSFW Quotes"])

    with SFW_Quotes:
        st.markdown('- It sounds like a Cookie Monster Eating a Burger')
        st.markdown('- I have a coughy every morning')
        st.markdown("- Me!!!!! I'm the Feral Little Wolf")
        st.markdown("- That's My Dead Rabbit, Bitches")
        st.markdown("- I'm good at jumping. Its One of My Talents")
        st.markdown('- You Missed the part in Barbie Where they Shoot the CEO')
        st.markdown("- I'm going to go with the bombing of cambodia")

    with NSFW_Quotes:
        st.markdown("- I'm really good at going down")
        st.markdown('- I sucked your dck to this song. The song was 365')
        st.markdown('- Now I understand why Rockets are so phallic')
        st.markdown('- While Kissing: JOSHIE THE SCUMBUG')
        st.markdown('- I wish they put stuff about penises on the AP Physics Test')
        st.markdown("- You're Never Fully Dressed Without a boner")
        st.markdown('- (Proudly) Im going to make Jello Penises')
        st.markdown('- I feel like its the Lizzy Dick List (2x)')
        st.markdown('- [Talking about Acme], the dick out discount')
        st.markdown('- This is good; its helping my cooch')



