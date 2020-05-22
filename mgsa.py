from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)


# TODO Offload this to JSON file
# Hardcoded positions, sizes, and links for art in galleries
artwork = {
    # Room #: [Artwork, Width, Height, Top, Left]
    "room1": [  
        ["No Diving, 50x44", 22, 40, 25, 25], 
        ["Kenny and Co., 16x20", 9, 18, 40, 65],
        ["Ryan, 24x36", 9, 24, 38, 85]
    ],
    "room2": [
        ["Beauty Parlor, 52x44", 22, 50, 17, 15],
        ["Ye Ye and Nai Nai, 24x36", 12, 35, 28, 48],
        ["Dan-Anh, 24x36", 12, 35, 25, 74]
    ],
    "room3": [
        ["Untitled, 42x38", 20,40,25,2],
        ["Untitled, 16x20", 10,20,40,28],
        ["Untitled, 16x28", 15,20,40,45],
        ["Untitled, 24x36", 12,30,35,68],
        ["Untitled, 20x40", 10,35,32,86]
    ],
    "room4": [
        ["Anxiety, (9)8x10", 30,55,30,10],
        ["Stores of Moldy Food, 16x18", 12,30,40,55],
        ["Sad, Sole, Fridge, 16x22", 15,25,40,80]
    ],
    "room5": [
        ["Systematic Discrepancies, 33x33", 25,55,22,6],
        ["Disposable Bodies, 16x22", 12,32,34,43],
        ["Nostalgia, (9)8x10", 27,50,25,70]
    ],
    "room6": [
        ["From Outside, 36x48", 23,40,30,3],
        ["From Inside, 36x48", 20,30,35,50]
    ],
    "room7": [
        ["Projected, 48x60", 35,70,12,5],
        ["Broken Medicine Cabinet, 13x16", 10,20,42,48],
        ["From Both Outside and Inside, 36x48", 32,48,28,65]
    ],
    "room8": [
        ["Stop Series 1, 18x24", 10,28,45,5],
        ["Stop Series 2, 18x24", 10,22,48,20],
        ["Stop Series 3, 18x24", 8,18,50,33],
        ["“Shut up!” ,18x24", 6,15,51,45],
        ["The Spirit of the Forest, 16x20", 6,15,51,55],
        ["Untitled, 3x3", 15,30,42,65],
        ["Isolation, 18x24", 8,25,47,85]
    ],
    "links": {
        "Untitled, 3x3": "../static/artwork/shannon 2.jpg", 
        "Isolation, 18x24": "../static/artwork/shannon 3.jpg", 
        "The Spirit of the Forest, 16x20": "../static/artwork/shannon 1.jpg",
        "Disposable Bodies, 16x22": "../static/artwork/desiree 4.jpg", 
        "Sad, Sole, Fridge, 16x22": "../static/artwork/desiree 1.jpg",
        "Stores of Moldy Food, 16x18": "../static/artwork/desiree 2.jpg",
        "Systematic Discrepancies, 33x33": "../static/artwork/desiree 3.jpg",
        "Nostalgia, (9)8x10": "../static/artwork/sera 1.jpg", 
        "Anxiety, (9)8x10": "../static/artwork/sera 2.jpg",
        "No Diving, 50x44": "../static/artwork/lauren 1.jpg", 
        "Beauty Parlor, 52x44": "../static/artwork/lauren 2.jpg",
        "Untitled, 16x28": "../static/artwork/jon 3.jpg",
        "Untitled, 20x40": "../static/artwork/jon 2.jpg",
        "Untitled, 16x20": "../static/artwork/jon 4.jpg", 
        "Untitled, 24x36": "../static/artwork/jon 1.jpg", 
        "Untitled, 42x38": "../static/artwork/jon 5.jpg",
        "From Outside, 36x48": "../static/artwork/bri 1.jpg",
        "From Inside, 36x48": "../static/artwork/bri 2.jpg",
        "From Both Outside and Inside, 36x48": "../static/artwork/bri 3.jpg",
        "Broken Medicine Cabinet, 13x16": "../static/artwork/liz 1.jpg", 
        "Projected, 48x60": "../static/artwork/liz 2.jpg",
        "Stop Series 1, 18x24": "../static/artwork/giancarlo 1.jpg",
        "Stop Series 2, 18x24": "../static/artwork/giancarlo 2.jpg",
        "Stop Series 3, 18x24": "../static/artwork/giancarlo 3.jpg",
        "“Shut up!” ,18x24": "../static/artwork/giancarlo 4.jpg",
        "Kenny and Co., 16x20": "../static/artwork/david 2.jpg",
        "Ryan, 24x36": "../static/artwork/david 4.jpg", 
        "Dan-Anh, 24x36": "../static/artwork/david 1.jpg",
        "Ye Ye and Nai Nai, 24x36": "../static/artwork/david 3.jpg",
    },
    "artists": {
        "Untitled, 3x3": "Shannon Heylin", 
        "Isolation, 18x24": "Shannon Heylin", 
        "The Spirit of the Forest, 16x20": "Shannon Heylin",
        "Disposable Bodies, 16x22": "Deziree Jordyn", 
        "Sad, Sole, Fridge, 16x22": "Deziree Jordyn",
        "Stores of Moldy Food, 16x18": "Deziree Jordyn",
        "Systematic Discrepancies, 33x33": "Deziree Jordyn",
        "Nostalgia, (9)8x10": "Serafina Kennedy", 
        "Anxiety, (9)8x10": "Serafina Kennedy",
        "No Diving, 50x44": "Lauren Krasnoff", 
        "Beauty Parlor, 52x44": "Lauren Krasnoff",
        "Untitled, 16x28": "Jon Lewis",
        "Untitled, 20x40": "Jon Lewis",
        "Untitled, 16x20": "Jon Lewis", 
        "Untitled, 24x36": "Jon Lewis", 
        "Untitled, 42x38": "Jon Lewis",
        "From Outside, 36x48": "Briana Mclaurin",
        "From Inside, 36x48": "Briana Mclaurin",
        "From Both Outside and Inside, 36x48": "Briana Mclaurin",
        "Broken Medicine Cabinet, 13x16": "Liz Pope", 
        "Projected, 48x60": "Liz Pope",
        "Stop Series 1, 18x24": "Giancarlo Venturini",
        "Stop Series 2, 18x24": "Giancarlo Venturini",
        "Stop Series 3, 18x24": "Giancarlo Venturini",
        "“Shut up!” ,18x24": "Giancarlo Venturini",
        "Kenny and Co., 16x20": "David Yang", 
        "Ryan, 24x36": "David Yang", 
        "Dan-Anh, 24x36": "David Yang", 
        "Ye Ye and Nai Nai, 24x36": "David Yang"
    }
}

# TODO Offload this to JSON file
# Hardcoded names, bios, artwork, instagrams
profiles = [
    {
        "name": "Shannon Heylin",
        "bio": "Color is a predominant aspect of my art. Highly saturated colors are placed next to each other to vibrate and excite the viewer. The canvas becomes a depth of space in a desert or a forest. I am attracted to these natural landscapes because they show the vastness of the natural world. In my paintings the figure is huge but the landscape always dominates in the end. The enlarged figures represent the empowerment of women but also how small we are compared to the world. I use that to give myself perspective and a point of contemplation. Similar to how the figure and the viewer never fully make eye contact. Forcing the viewer to contemplate what the women are thinking about. I want to bring relatable moments like swimming in a lake or walking in the forest but exaggerating those feelings in my paintings by altering the scale. Creating a surrealist scene but still maintaining the connection to the viewer. Looking at my paintings should foster feelings of stillness and wonder.",
        "artwork": ["Untitled, 3x3", "Isolation, 18x24", "The Spirit of the Forest, 16x20"],
        "instagram": "shaaeylin",
        "picture": "../static/headshots/Shannon Heylin.jpeg"
    },
    {
        "name": "Deziree Jordyn",
        "bio": "My series is a response to the circumstances occurring due to COVID-19. From food shortages because of impulse hoarding to displacement of families for various reasons. Topics such as displacement and comfort (or lack thereof) are being explored. I am curious about the cause and the effect of people who are considering solely themselves in a time such as right now. As well as what’s happening to those that don’t have control over their situation for reasons of but not limited to status, class, and race. Privilege and systematic issues are exposed during nationwide hardships but rarely ever addressed and worked on. Considering how to expose such issues in a way that becomes easy to talk about is necessary. In turn it would allow for structured conversations about what could and should be done. Issues like literal tons of food going to waste while families are starving. There is a growing rate of homelessness while hotels and motels remain closed from lack of business. Why are there so many discrepancies that allow for human neglect?",
        "artwork": ["Disposable Bodies, 16x22", "Sad, Sole, Fridge, 16x22", "Stores of Moldy Food, 16x18", "Systematic Discrepancies, 33x33"],
        "instagram": "dezireejordyn",
        "picture": "../static/headshots/Deziree Jordyn.png"
    },
    {
        "name": "Serafina Kennedy",
        "bio": "My paintings are psychological representations of my home, allowing me to translate my internal process through the objects and patterns that are around me during quarantine. The pandemic and the resulting quarantine is obviously a historic and tragic moment.  People will cope with the COVID-19 pandemic in a variety of ways, and my intention with this body of work was to demonstrate and track the evolution of my feelings during this time. I approached each painting in these installations as a part of my visual diary depicting the spaces around me. In this method of documentation, I include objects, patterns, and images from my childhood that I feel a personal connection to. This body of work represents my experiences during quarantine.",
        "artwork": ["Nostalgia, (9)8x10", "Anxiety, (9)8x10"],
        "instagram": "serafina_kennedy",
        "picture": "../static/headshots/Serafina Kennedy.jpeg"
    },
    {
        "name": "Lauren Krasnoff",
        "bio": "My work often depicts my experiences through group portraiture. These two recent paintings explore the irony of group portraits during a time of social distancing. Made while in quarantine, they satirize the present moment as well as society at large. Being isolated has intensified the way I experience visual culture, social media, and the millennial narcissism that goes along with it. We rely on our virtual existence for validation and the false sense of closeness it provides. It feels like social media’s illusion of connectivity already impacted our relationships and created social distancing before all of this. Just like the appearances we keep up, my paintings exist in a space somewhere between real life and a fictional reality. The narratives in my work reference both memory and art history. These pieces present the contemporary action of posing attractively “for the camera” coupled with a historical display of the standards of beauty. By depicting a lack of human interaction, I want to ironically stress the importance of physical and personal connection.",
        "artwork": ["No Diving, 50x44", "Beauty Parlor, 52x44"],
        "instagram": "lauren.krasnoff",
        "picture": "../static/headshots/Lauren Krasnoff.PNG"
    },
    {
        "name": "Jon Lewis",
        "bio": "Informed by art history, queer theory, and feminist critique, my work as a visual artist function as vessels for contradiction, questioning identity and my own relationship with abstraction. I work primarily in painting, although drawing and its inherent immediacy is always considered, to investigate the physicality of the medium and its eagerness to interact with the body within space. Through explorations in color, form, and space, I am constantly searching for a balance between the planned and spontaneous, how to create structures that not only leave enough room for mistakes, but embrace them. While engaging with the modernist canon of abstraction and challenging the rigidity of a predetermined formalism, it’s my hope to make work that can reject the notion of objectivity and subvert traditional heterosexual masculine conventions. I am interested in creating my own visual vocabulary that can both communicate historically self-constructed queer aesthetics and help to navigate my own relationship with these histories. Camp becomes important to the work, as is the high/low relationship between the convention I am referencing and the queerness of my distortion to it. It is at this intersection of high and low, personal and political, masculine and feminine, that my work exists.",
        "artwork": ["Untitled, 16x28", "Untitled, 20x40", "Untitled, 16x20", "Untitled, 24x36", "Untitled, 42x38"],
        "instagram": "jonlewz",
        "picture": "../static/headshots/Jon Lewis.jpeg"
    },
    {
        "name": "Briana Mclaurin",
        "bio": "As an artist, the goal of my work is to tell a story; to tell a story that is otherwise difficult to put into words. The goal is to tackle meaningful subjects and ideas and create something that would personify whatever I envision in my head. I generally paint intimate portraits of my family members, experimenting with the various colors in their brown skin. In most of my work, the central motifs are the expressive and colorful palette, along with the thick application of paint to represent texture in certain areas. The inspiration for my art primarily stems from artists such as Beauford Delaney, Jacob Lawrence, Barkley L. Hendricks, Amy Sherald, Kerry James Marshall, and Jordan Casteel. The way that each artist used their colors to create such beautiful and inspiring images is truly fascinating. Their ability to manipulate and experiment with color and texture is one thing that I will always aim to build upon and continue in my own work.",
        "artwork": ["From Outside, 36x48", "From Inside, 36x48", "From Both Outside and Inside, 36x48"],
        "instagram": "briana_mclaurin",
        "picture": "../static/headshots/Briana McLaurin.jpg"
    },
    {
        "name": "Liz Pope",
        "bio": "With my paintings I like to use the human figure to convey feelings through body language, bodily textures, or things that appear on the surface of the body like scrapes and bruises. I think the human figure is a really important part of art and my work specifically, but in hopes to expand my language in painting I’ve been working on adding more subjects in my pieces to interact with the figures I paint. My two recent pieces Projected and Broken Medicine Cabinet are two ways I feel anxiety. Projected depicts a person projecting two figures using a projector. The figure connected to the head is infested with moths that are prevented from spreading to the figure connected to the heart through the smoke of a cigarette the person is smoking. I painted this piece thinking about the fear of my anxiety being made up in my head and bad habits I developed trying to soothe the anxiety. Broken Medicine Cabinet depicts a person standing in front of a medicine cabinet with the handle broken off looking into a fogged up mirror with two figures emerging from behind the shower curtain. The person has the figure’s arms enveloping her and a moth standing on her throat. I painted this piece thinking about the effects of not taking my medication and the similar feeling it has to horror movie tropes. With these two pieces I wanted to figure out a way to make a non visual ailment visual through the use of symbolism.",
        "artwork": ["Broken Medicine Cabinet, 13x16", "Projected, 48x60"],
        "instagram": "lizzzpope",
        "picture": "../static/headshots/Liz Pope.jpg"
    },
    {
        "name": "Giancarlo Venturini",
        "bio": "Giancarlo Venturini is a visual artist from a small town named Boonton, New Jersey. Through painting and sculpture Giancarlo has created works surrounding his experience that stems from the camaraderie of small town life. Having the opportunity to befriend so many diverse people growing up, he started to take an interest in their cultures. In high school one of his best friends started teaching him Polish and this sparked great interest for him. Doing daily lessons, this led him to travel to and learn the language of Poland. Giancarlo now works to promote and preserve a culture that he has admired through painting and sculpture in an attempt to educate while still being humorous. Giancarlo went on to receive his B.F.A. from Rutgers University in 2021. He continues to create work and show in exhibitions.",
        "artwork": ["Stop Series 1, 18x24", "Stop Series 2, 18x24", "Stop Series 3, 18x24", "“Shut up!” , 18x24"],
        "instagram": "gian_venturini",
        "picture": "../static/headshots/Giancarlo Venturini.jpg"
    },
    {
        "name": "David Yang",
        "bio": "Growing up I was often made to feel not quite American enough for my white friends and classmates, yet not quite Asian enough for my family. I think in the past, this sort of otherness has led me to withdraw from meaningful social interaction, straining my relationships with both my family members and my peers. Now, however, with the rise of racially charged violence against Asians due to COVID-19, I seek to try and empower those who look like me and have experienced the same things as me in any way possible. These portraits are a way for me to voice my pride in the unique and important status of being a first generation Asian American.",
        "artwork": ["Kenny and Co., 16x20", "Ryan, 24x36", "Dan-Anh, 24x36", "Ye Ye and Nai Nai, 24x36"],
        "instagram": "idem.paris",
        "picture": "../static/headshots/David Yang.jpg"
    }
]

@app.route('/')
@app.route('/room/<id>')
def gallery(id=1):
    return render_template('gallery.html', page = int(id), totalpages = 8, background=f"../static/galleries/room {id}.jpg", artwork=artwork)

@app.route('/mobile')
def mobile():
    return render_template('mobile.html', artwork=artwork)

@app.route('/artists')
def artists():
    return render_template('artists.html', profiles=profiles, artwork=artwork)

@app.route('/artwork/<art>')
def art(art):
    return render_template('art.html', art=art, profiles=profiles, artwork=artwork)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)