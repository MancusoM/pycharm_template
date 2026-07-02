import streamlit as st
from pathlib import Path
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

current_script_path = Path(__file__).resolve()
parent_directory = current_script_path.parent
from const import messages

audio_folder = f"{parent_directory}/memos"

st.set_page_config(page_icon="❤️", layout="centered", page_title="Merry Christmas")

st.title("Elizabeth Sarah McNaughton")

container = st.container()

container.write(
    "Lizzy, everyday I see you, that's my Pocketful of Happiness for the Day"
)

Memories, Inside_Jokes,Happy_Birthday,Merry_Xmas, Job, purdue = st.tabs(["Memories", "Inside Jokes",'Happy Birthday',"Merry Christmas!","First Day On the Job", "Felix Cumpleaños!"])

def return_audio(audio_file):
    st.audio(f"{audio_folder}/{audio_file}")

def display_image(file_path:str,caption:str,width:int):
    return st.image(f"images/{file_path}",caption,width)

def write_markdown(string:str):
    return st.markdown(f"- {string}")

with Memories:
    col1, col2, col3 = st.columns(3)

    with col1:

        display_image(
            file_path= "FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg",
            caption="Lizzy's First Appearance on Camera Roll",
            width =200,
        )

        display_image(
            file_path="D677062A-24CD-42AE-80B2-680571D608CE_1_105_c.jpeg",
            caption="Lizzy's First Appearance on Camera Roll",
            width=200,
        )
        display_image(
            "D677062A-24CD-42AE-80B2-680571D608CE_1_105_c.jpeg",
            caption="Our First Met Date",
            width=200,
        )

        display_image(
            "F7102E66-F614-4BEF-B54F-62381E3D17FD_1_105_c.jpeg",
            caption="Lizzy's First Time Meeting My Dad",
            width=200,
        )

        display_image(
            "F6DCB01B-6F34-481A-B0C6-3728D14769A3_1_105_c.jpeg",
            caption="Pre Bryant Park",
            width=200,
        )
        display_image(
            "B34A68A1-6706-4CB9-87E2-FD24CE011B27_1_105_c.jpeg",
            caption="Lizzy somehow smiling after learning about the oddities of Kaleb",
            width =200
        )
        display_image(
            "A25AEF46-CC8B-4197-9C25-2CC8E4BF75DE_1_105_c.jpeg",
            caption="First of Many Jefferson Coffee Dates",
            width=200,
        )
        display_image(
            "3286420A-551D-41F8-95BB-809008615974.jpeg",
            caption="First Dinner With Familia",
            width=200,
        )

        display_image(
            "IMG_7749.jpeg",
            caption="Is She Beauty or is She Beast? " "Answer:Both",
            width=200,
        )
        display_image(
            'burger.jpeg',
            caption="Lizzy's Alwaays A Happy Girl When She Has A Burger",
            width = 200
        )
        display_image(
            'coffee.jpeg',
            caption = 'NYC Coffee Date Pre NYC Library Date',
            width =200
        )
        display_image(
            'purdue.jpeg',
            caption='Lizzy Bringing Matt to His First Purdue Game',
            width=200
        )
        display_image(
            'Museum.jpeg',
            caption='Babys First Whitney Trip',
            width=200
        )
        display_image(
            'pigeon.jpeg',
            caption="Do you really live in the tristate area if you haven't seen a massive pigeon",
            width=200
        )
        display_image(
            "mets.jpeg",
            caption="Lizzy Taking in the Wise Words of the Captain",
            width=200
        )
        display_image(
            "mtn.jpeg",
            caption="The scenery was gorgeous, but the best view was next to Matt",
            width=200
        )
        display_image(
            "allan.jpg",
            caption="Lizzy's Favorite Man?",
            width=200
        )
        display_image(
            "pigeon.jpeg",
            caption="Big-Ass pigeon",
            width=200
        )

    with col2:
        display_image(
            "D1D508D3-1F08-46E4-A27D-873474688308_1_105_c.jpeg",
            caption="Beating Lizzy At Chess. Thankfully, She Didn't Have My Mom's Reaction!",
            width=200,
        )

        display_image(
            "E56EF88E-5ECC-4EFC-AEC8-D7ED704D5178_1_105_c.jpeg",
            caption="I LOVE KNOCKING ON DOORS",
            width=200,
        )

        display_image(
            "A727011D-E97E-467A-AE42-B8D67EC36502_1_102_o.jpeg",
            caption="Lizzy Carrying At Hot To Go",
            width=200,
        )
        display_image(
            "7125D8A4-05A6-476D-8177-3CD0DD36AA91.jpeg",
            caption="Hard at Work. Or Hardly Working",
            width=200,
        )

        display_image(
            "A9BDCCFF-D743-4911-91DB-43E8C661FE05_1_105_c.jpeg",
            caption="Costco Date!",
            width=200,
        )

        display_image(
            "EEE8A07D-4A00-4FAE-AB61-69213AE417E0_1_105_c.jpeg",
            caption="String Bean Waiting For Monkey",
            width=200,
        )
        display_image(
            'art_show.jpeg',
            caption= "Lizzy Attending John's Art Show",
            width = 200
        )
        display_image(
            'diva.jpeg',
            caption = 'Da Diva',
            width = 200
        )
        display_image(
            'hangry.jpeg',
            caption ='Better Feed Lizzy Or She Will Eat You',
            width = 200
        )
        display_image(
            'middle.jpeg',
            caption = 'What Did I Do To Deserve This???',
            width = 200
        )
        display_image(
            'playground.jpeg',
            caption='playground? Playground',
            width=200
        )
        display_image(
            'purdue.jpeg',
            caption='Mets Win with Lizzy in attendance: Wizzy',
            width=200
        )
        display_image(
            "camera.jpeg",
            caption="LizBert celebrating Julia's birthday",
            width =200
        )
        display_image(
            "dippy.jpeg",
            caption="I see Favoritism!",
            width=200
        )
        display_image(
            "camera.jpeg",
            caption="The Group™️ice-staking",
            width=200
        )
        #display_image(
            #nyc.jpg",
            #caption="This is all Manhattan?",
            #width=200
        #)
        #display_image(
            #maryland.jpg",
            #caption="Go Purdue! Don't Go Amtrak!",
            #width=200
        #)

    with col3:
        display_image(
            "0A9E7DFA-BD3E-456F-AE8D-1B37ECFE30C8_1_105_c.jpeg",
            caption="An Unwarranted Middle Figer (GO IU!)",
            width=200,
        )

        display_image(
            "F9659469-FEF7-43B2-86CA-0897B32D52AD_1_105_c.jpeg",
            caption="I phew up",
            width=200,
        )

        display_image(
            "7D0C9F30-C53E-43AD-A568-03CD219A93E5_1_105_c.jpeg",
            caption="Our First Ever Concert",
            width=200,
        )

        display_image(
            "91EA5FB5-DC75-484A-BE9B-B235F2A42868_1_105_c.jpeg",
            caption="Saturday Night In",
            width=200,
        )

        display_image(
            "840A7B8B-7EFC-41B4-8B7A-8F32C7C5CD4C_1_105_c.jpeg",
            caption="No Women Knew What Was Going On In the Bagel Store",
            width=200,
        )

        display_image(
            "49567F8A-1040-45B9-A590-EFD3E3B1D295_1_105_c.jpeg",
            caption="The Best View Wasn't the WTC. It was right next to Matt",
            width=200,
        )
        display_image(
            "74049FE1-D2AE-4E11-B12F-FA11B4CA8B92_1_105_c.jpeg",
            caption="Halloween Night",
            width=200,
        )
        display_image(
            "angry.jpeg",
            caption = '😲',
            width =200
        )
        display_image(
            'snow.jpeg',
            caption = 'No Good Weather During Our First Vacation? No Problem!',
            width = 200
        )
        display_image(
            'valentine.jpeg',
            caption ="A Wonderful Valentine's Day Celebration",
            width = 200
        )
        display_image(
            'zoo.jpeg',
            caption='Great Day for Lizzys Branding',
            width=200
        )
        display_image(
            'IMG_2442.jpeg',
            caption='One Benefit To the Hive: # Of Dogs',
            width=200
        )
        display_image(
            'IMG_0870.jpeg',
            caption='Lizzy (left) with Her Spirit Animal',
            width=200
        )
        display_image(
            "snowman.jpeg",
            caption="An engineer at work (truly)",
            width=200
        )
        display_image(
            "walking.jpeg",
            caption="An engaging walk on a rainy day",
            width=200
        )
        display_image(
            "toronto.jpg",
            caption="A great vacation in Toronto",
            width=200
        )
        #display_image(
            #puppy.jpg",
            #caption="Puppy soon :) ",
            #width=200
        #)

with Inside_Jokes:
    st.header("Unhinged Elizabeth Quotes")
    st.write("RIP Compliance Cow")
    SFW_Quotes, NSFW_Quotes = st.tabs(["SFW Quotes", "NSFW Quotes"])

    with SFW_Quotes:
        
        write_markdown("It sounds like a Cookie Monster Eating a Burger")
        write_markdown("I have a coughy every morning")
        write_markdown("Me!!!!! I'm the Feral Little Wolf")
        write_markdown("That's My Dead Rabbit, Bitches")
        write_markdown("I'm good at jumping. Its One of My Talents")
        write_markdown("You Missed the part in Barbie Where they Shoot the CEO")
        write_markdown("It’s a fine line between supporting the gays and holiday spirit ")
        write_markdown("I'm going to go with the bombing of cambodia")
        write_markdown("These are the gayest brownies this side of the Mississippi ")
        write_markdown("Pack the gun no grabbing buns")
        write_markdown("When I want to be in safe feminine space I go to the nfl")
        write_markdown("Wart girls lips taste like pepperoni")
        write_markdown("You don’t know what a pond is")


    with NSFW_Quotes:
        write_markdown("I'm really good at going down")
        write_markdown("I sucked your dck to this song. The song was 365")
        write_markdown("Now I understand why Rockets are so phallic")
        write_markdown("*While Kissing*: JOSHIE THE SCUMBUG")
        write_markdown("I wish they put stuff about penises on the AP Physics Test")
        write_markdown("You're Never Fully Dressed Without a boner")
        write_markdown("(Proudly) Im going to make Jello Penises")
        write_markdown("I feel like its the Lizzy Dick List (2x)")
        write_markdown("[Talking about Acme], the dick out discount")
        write_markdown("What do you want to do first: me or the Spinach balls?")
        write_markdown("I had to text my grandma so I couldn’t vote cum stain ")
        write_markdown("[In front of friends]:  I’m going to stick in my mouth")
        write_markdown("Do you have your penis (referred to as little Matt) write python code")
        write_markdown("Take it. It has chlamydia on it.")
        write_markdown("[impersonating The General from Insurance] I wanna fuck you so bad I’m so hard")
        write_markdown("You would want that Steve cohenussy")
        write_markdown("I have the dog in the bag with the condoms")
        write_markdown("He’s thrusting in reggaeton ")
        write_markdown("You can’t talk about penis then go right back to credit cards")
        write_markdown("I didn’t take you as a thong guy")
        write_markdown("Purdussy")
        write_markdown("Imagine your husband acts zesty in a soup porno")
        write_markdown("You don’t lactate")
        write_markdown("I did not just describe a boner in typescript")
        write_markdown("Wait until I describe it in rust. It would be a memory safe function")
        write_markdown("Having sex is embedded programming ")
        write_markdown("Imagine dating me bc im cute and boom wartboy ussy")
        write_markdown("Wart girls lips taste like pepperoni")
        write_markdown("They’re all mech engineers. We tell them to fuck up some gears then we go fuck upstairs")
        write_markdown("He just stared at my boobs and then emailed the government of Alaska")
        write_markdown("My boobs are like bop it")
        write_markdown("I don’t wanna work at Meta. I get mad dick")
        write_markdown("I used to like cookies more than sex. Then I started having good sex")
        write_markdown("I thought Denmark was made up in Shakespeare")
        write_markdown("Reverse cowgirl so I can work on my code")
        write_markdown("Can you send nut master to me")
        write_markdown("You want that Steve Jobsussy")
        write_markdown("You did not do “hot to go” about your erection")
        write_markdown("I wonder how much men are going to watch the Minecraft movie instead of getting any modicum of pussy")
        write_markdown("It’s a fine line between a boys hangout and public masturbation")
        write_markdown("We have black guys")
        write_markdown("It’s a Ben & Jerry’s flavor. Orgasm swirl")
        write_markdown("Bunny on my boobs")
        write_markdown("The gods of my period")
        write_markdown("I just want to be licked, topped, and loved")
        write_markdown("I need to get the screenshot of the porn book club")
        write_markdown("Pinky, turn around. Mommy’s having fun")
        write_markdown("What happens if you get pulled into the Spiderverse during sex")
        write_markdown("Now that I’ve seen Pete and his voluptuous ass, I'm going to sign up for bare tomorrow")
        write_markdown("They were fucking. There are dragons. What more could you want")
        write_markdown("Moomoo sex is sex that sponsors the Mets")
        write_markdown("Your abortion talk convinced me to go to Pilates tomorrow")
        write_markdown("Locksmith roleplay")
        write_markdown("Even bad bitches gotta take a poopy sometime")
        write_markdown("Mozart said. Gobble me swallow me drip down the side of me")
        write_markdown("I’m black")
        write_markdown("Lindor’s bisexual")
        write_markdown("We either need to peg harder or peg smarter")
        write_markdown("Octopus in my pussy?")
        write_markdown("Is the cow in the udder?")
        write_markdown("Can we watch the sensory fruit video before sex")
        write_markdown("There’s nothing less erotic than grilled cheese")
        write_markdown("I can still pretend to be in the Klan if you want")
        write_markdown("I want you to celebrate our anniversary by taking a shit in my toilet")
        write_markdown("I got mad dick when I had LinkedIn premium")
        write_markdown("(Talking about stuffies) I don’t want them to fuck")
        write_markdown("Greater than or equal to you fucking bitch")
        write_markdown("Good. You should be discriminated against")
        write_markdown("I feel like a furry")
        write_markdown("I want to be cumt ruffle’s grandmother")
        write_markdown("I’m going to make Pearl Harbor look like the Boston tea party")
        write_markdown("I’m sound tracking your piss")

with Happy_Birthday:
    write_markdown('Happy Birthday, my darling')
    write_markdown('https://youtube.com/shorts/FZELFihDJoA?feature=share')

with Merry_Xmas:
    write_markdown('Happy Xmas!')
    write_markdown('https://www.youtube.com/shorts/8jMfNlA2ukU')

with Job:
    audio_folder = f"{parent_directory}/memos"
    file_names = [f for f in os.listdir(audio_folder) if os.path.isfile(os.path.join(audio_folder, f))]

    stuffies_folder = f"{parent_directory}/images/stuffies"
    stuffie_names = [f for f in os.listdir(stuffies_folder) if os.path.isfile(os.path.join(stuffies_folder, f))]

    start =0

    try:
        for file in file_names:
            images_list = [key for key in messages.keys() if "PNG" in key]
            names = [value for value in messages.values()]

            specific_image = images_list[start]

            display_image(f"stuffies/{specific_image}", " ", 100)
            return_audio(file)
            start +=1
    except IndexError:
        st.write("")
with purdue:
    write_markdown('Happy Birthday, my dear')
    write_markdown('https://tinyurl.com/WhatIsThisQuestion')