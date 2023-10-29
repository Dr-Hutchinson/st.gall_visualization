import base64
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

with open("annotated_gall_plan.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode()

img_path = "data:image/png;base64," + base64_image

# Create the initial figure
fig = go.Figure()

# Add background image
fig.add_layout_image(
    dict(
        x=0,
        sizex=850,
        y=1000,
        sizey=850,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source=img_path)
)

annotation_points = [
    {'name': 'The Basilica', 'x': 300, 'y': 550, 'text': 'The Basilica'},
    {'name': 'Health Care and Healing', 'x': 225, 'y': 875, 'text': 'Health Care and Healing'},
    {'name': 'Education and Hospitality', 'x': 175, 'y': 625, 'text': 'Education and Hospitality'},
    {'name': 'Pens and Stables', 'x': 525, 'y': 300, 'text': 'Pens and Stables'},
    #{'name': 'Area 3', 'x': 258.98, 'y': 426.89, 'text': 'Area 3: New Explanation'},
    #{'name': 'Area 3', 'x': 300, 'y': 550, 'text': 'Area 3: New Explanation'},
    {'name': 'Crafts and Artisans', 'x': 725, 'y': 525, 'text': 'Crafts and Artisans'},
    {'name': 'The Orchard, Cemetery, Vegetable Garden, and Livestock Pens', 'x': 615, 'y': 900, 'text': 'The Orchard, Cemetery, Vegetable Garden, and Livestock Pens'}
    #{'name': 'Area 5', 'x': 300, 'y': 900, 'text': 'Area 5: New Explanation'}
]

scatter_points = {
    'x': [point['x'] for point in annotation_points],
    'y': [point['y'] for point in annotation_points],
    'text': [point['text'] for point in annotation_points],
}

# Add scatter plot for annotations
fig.add_trace(
    go.Scatter(
        x=scatter_points['x'],
        y=scatter_points['y'],
        text=scatter_points['text'],
        mode="markers+text",
        textposition="bottom center",
        marker=dict(size=10, color='red'),
        hoverinfo="text"
    )
)

# Streamlit app
st.title("Interactive St. Gall Plan")

with st.expander("How to Navigate the App:", expanded=True):
    st.write("""
    ### How to Navigate the Image
    **Quick Navigation**: Use the dropdown menu labeled "Quick Navigate to" to instantly zoom into specific areas of interest. The sliders below will automatically adjust to the selected area.

    **Manual Zoom:**

    Horizontal Position (Zoom): Slide to move the view left and right across the image.\n
    Vertical Position (Zoom): Slide to move the view vertically up and down the image.\n

    **Reset View:**

    To reset the view to the full image, set both sliders to 0 and select "None" from the Quick Navigate menu.\n

    **Hover Information**: Hover over the red markers on the image to see additional information about different areas.
    """)

zoom_to_area = False
default_x_range = 0
default_y_range = 0

if not isinstance(default_x_range, int):
    default_x_range = int(default_x_range[0])  #

if not isinstance(default_y_range, int):
    default_y_range = int(default_y_range[0])  # or any other logic to convert it to int

# Dropdown for quick navigation
selected_area = st.selectbox('Quick Navigate to:', ['None'] + [point['name'] for point in annotation_points])

content_to_display = []

basilica_text_1 = """**Welcome to the St. Gall Monastery's Basilica - An Architectural Marvel**\n\nAs you stand in the center of this remarkable architectural representation, imagine yourself between the East and West Paradises of the St. Gall Plan. You are about to embark on a journey through a basilica that, while never built, reflects the intricacies and sanctity of monastic life during the medieval period."""
basilica_text_2 = """Below these towers, the main entrance offers a welcoming message: "Here all the arriving crowd will find their entry." (Adueniens adytum populus hic cunctus habebit) This entrance serves as the only gateway to the vast monastic complex, ensuring controlled access. Visitors would then proceed to a semi-circular atrium where their paths diverged based on social standing—echoing the societal hierarchies of the Middle Ages.\n\nStep inside the basilica, and you'll notice it's strategically divided. Columns and railings aren't just architectural features; they dictate movement. The majority of the church, including its transept, presbytery, nave, and dual apses, is reserved exclusively for monks. Lay visitors, including many of you, are restricted to the side aisles, baptismal font area, and the crypt, emphasizing the distinction between the secular and the sacred."""
basilica_text_3 = """As you wander through the side aisles, pay special attention to the array of altars, each dedicated to specific saints. These altars aren't just places of worship but also a reflection of the religious veneration of the time. From Saints Lucia and Cecilia in the northern aisle to Saints Agatha and Agnes in the southern aisle, each altar has its own story, deeply rooted in Christian lore."""
basilica_text_4 = """Throughout the tour, consider how the basilica, even in its unbuilt state, draws from genuine medieval monastic designs. The St. Gall Plan beautifully marries function with faith, creating a tapestry of architectural brilliance and religious devotion. If you ever get a chance, compare this design with extant medieval monasteries to appreciate the similarities and differences in their architectural choices."""

pens_stables_text_1 = """**Pens and Stables**\n\nIn a monastery setting, especially during the medieval period, self-sustainability was vital. The St. Gall Plan, with its emphasis on providing for the community's needs, showcases several areas dedicated to animal husbandry—a practice intrinsic to the monastic way of life."""
pens_stables_text_2 = """**Sheep:** Often reared for their wool, which was a crucial resource for making garments and bedding. The monastery would have likely had its own weavers turning this wool into valuable textiles.\n\n**Goats:** Besides their meat, goats were also kept for their milk which could be consumed directly or transformed into cheese, another staple in the monastic diet.\n\n**Cows:** Predominantly reared for their milk, which was essential for producing butter and cheese. Beef might have also been consumed during specific periods, but was generally less common due to the cost and effort of raising cattle.\n\n**Swine:** Pigs were valuable for their meat. Their efficient feed-to-meat conversion rate made them a popular choice in monastic settings. Pork could be preserved as ham or bacon, ensuring provisions during winter months."""
pens_stables_text_3 = """**Brood Mares and Foals - Horse Breeding Area:**\n\nMonasteries often played a pivotal role in maintaining and improving local livestock breeds. The inclusion of a dedicated area for breeding mares and foals suggests an interest in horse husbandry. Horses were indispensable, not just for transportation, but also for various labor-intensive tasks around the monastery, such as plowing fields or hauling goods."""
pens_stables_text_4 = """**Residence for Servants**:\n\nThis area denotes the housing for the monastic estate's labor force. Many of these individuals were likely serfs, bound to the land and the service of the monastery. The nature of serfdom in the medieval period meant that peasants, while not wholly owned by the monastery, were obligated to provide labor in exchange for the right to live on and farm a portion of the monastic lands. This relationship was multifaceted: while serfs had certain obligations to the monastery, the religious institution also had duties of protection and spiritual guidance toward them. The proximity of the servants' residence to the livestock areas is indicative of their roles in ensuring the day-to-day operation of the monastery's agricultural and animal husbandry practices."""

crafts_text_1 = """**Craftsmanship and Labor in the St. Gall Plan**\n\nThe intricate planning evident in the St. Gall Monastery showcases its ambition to be more than just a spiritual hub; it aimed to be a self-sustaining community, thriving on the diverse skills of its inhabitants. Here's a deeper dive into the various roles and facilities dedicated to craftsmanship and labor within the monastery:"""
crafts_text_2 = """**Crafts**:\n\n**Fuller:** These individuals played a vital role in treating and refining woolen cloth, making it thicker and more suitable for garments.\n\n**Shieldmaker:** As the name suggests, shieldmakers were responsible for crafting shields, potentially indicating that the monastery had its own security forces or catered to the needs of traveling knights or soldiers.\n\n**Goldsmith:** With their expertise in working with precious metals, goldsmiths were crucial for creating religious artifacts, jewelry, and sometimes coinage.\n\n**Blacksmith:** The backbone of many medieval communities, blacksmiths forged tools, agricultural implements, weapons, and other metal goods, ensuring the smooth functioning of everyday monastic life.\n\n**Grinders:** These craftsmen were likely involved in sharpening tools and weapons, a service that would be essential for both the monastery's craftsmen and its agricultural workers.\n\n**Turner:** Specializing in shaping wood using a lathe, turners would produce items like bowls, spindles, and other cylindrical wooden objects.\n\n**Cooper:** Coopers specialized in making wooden casks, barrels, and other staved containers. Their products were crucial for storage and transportation of liquids like water, beer, and wine."""
crafts_text_3 = """**Food Storage and Production:**\n\n**Storeroom for grain:** Grain was a staple diet and a valuable commodity. Proper storage ensured the monastery had a consistent food supply and could also trade surplus grain.\n\n**Bakery and Brewery:** Bread and beer were dietary staples in the medieval era. The monastery's dedicated bakery would produce daily bread, while the brewery catered to the monks' consumption needs and also produced beverages for guests and trading.\n\n**Mill:** Essential for grinding grain into flour, the mill was a critical component of the monastery's food production process.\n\n**Granary:** A larger storage facility, the granary ensured that harvested grain was kept dry and safe from pests, guaranteeing food security for the community.\n\nThe presence of such a diverse range of craftspeople and facilities underlines the monastery's aspiration to be a self-contained community. Not only did this ensure the monks' needs were met, but it also positioned the monastery as a hub of trade and craftsmanship in the region. Such extensive planning exemplifies the monastic commitment to labor as a form of devotion, blending spiritual pursuits with the practical needs of day-to-day life."""

health_text_1 = """**Medical Care in Monastic Communities During Medieval Times:**\n\nIn the medieval era, monastic communities played a pivotal role in healthcare. These establishments were not merely spiritual havens; they were also centers of healing, knowledge, and medical innovation. Many monasteries harbored a wealth of medical expertise, often grounded in ancient texts and traditions, serving both their monastic residents and the surrounding populace."""
health_text_2 = """**Medical Herb Garden:** Renowned for their herbal expertise, monastic communities cultivated gardens teeming with plants, which were meticulously harnessed to create remedies. This garden symbolizes the monastery's commitment to natural healing, with herbs addressing ailments ranging from minor discomforts to severe diseases.\n\n**Physician's Residence:** Near the herb garden lies the Physician's Residence, a clear indicator of the monastery's dedicated healthcare approach. Here, the resident physician, well-versed in both spiritual and medical realms, attended to the monks, guests, and peasants. The closeness to the medical herb garden reaffirms the intrinsic link between nature and healing."""
health_text_3 = """**Bloodletting Room:**\n\nVenturing further, we encounter the Bloodletting Room. This practice, deeply influenced by the theories of the ancient Greek physican Galen, aimed at balancing the body's four humors: blood, phlegm, yellow bile, and black bile. An imbalance was believed to cause illness. Thus, bloodletting, whether via leeches or instruments, sought to restore this harmony."""
health_text_4 = """**Rooms for the Critically Ill:**\n\nNearby, the rooms for the critically ill accentuate the monastery's comprehensive care ethos. Here, those with acute conditions were tended to in isolation, both to prevent contagion and to ensure a serene recovery environment.\n\n**Warming Rooms and Sleeping Rooms:** The adjacent Warming Rooms and Sleeping Rooms encapsulate the monastery's philosophy that healing is multifaceted, encompassing warmth, comfort, and restful repose.\n\n**Cloisters of the Sick & Novitiate:** At the heart of this healthcare hub is the Cloisters of the Sick and the Novitiate. This serene space provided solace to the ailing while also serving as a formative ground for novices— those individuals at the threshold of their monastic journey. A novice embarked on a period of intense spiritual and practical training, post which they would take their monastic vows and be fully integrated into the monastic community."""
health_text_5 = """**Refectory and Store Rooms:** The Refectory stands as a testament to the monastery's holistic approach to life. More than just a dining hall, it was a space of communion and reflection where monks gathered for communal meals, emphasizing the integration of physical sustenance with spiritual nourishment. The medieval monastic diet was modest but nutritious, primarily consisting of grains like barley and rye, legumes, vegetables from the garden, and fruits from the orchard. On special occasions or for those requiring it, the diet could be supplemented with dairy products from cows and goats, and eggs from the chickens. Pigs provided a source of meat, though meat consumption was often limited due to religious observances. The presence of the pens for goats, cows, pigs, and chickens, alongside an orchard and vegetable garden in the St. Gall Plan, exemplifies a self-sustaining community, ensuring a balanced diet for its inhabitants."""

orchard_text_1 = """**Sustenance and Serenity: The Orchard, Cemetery, Vegetable Garden, and Livestock**: As we journey to the upper right-hand corner of the St. Gall Plan, we are invited into the monastery's verdant realm, where the rhythms of nature and human endeavor harmoniously intertwine. This section unveils the monastery's dedication to self-sustainability, showcasing how each plot of land and every creature held a vital role in sustaining the community. From the tranquil repose of the departed in the Cemetery to the bustling activities in the Vegetable Garden and livestock quarters, this quadrant of the complex is a testament to the monastery's profound connection to the earth and its bounties. Join us as we delve deeper into this interplay of life, death, and daily sustenance."""
orchard_text_2 = """**Orchard & Cemetery:** Directly adjoining each other, the Orchard and the Cemetery signify the delicate balance between life and death within the monastery. The Orchard, brimming with fruit-bearing trees, provided the community with fresh produce and symbolized life's bounty and nourishment. On the other hand, the Cemetery served as the final resting place for the departed, marking the end of life's journey, in a location that ensured their spirits would rest amid nature's serenity."""
orchard_text_3 = """**Vegetable Garden:** Just to the right of the Cemetery, the Vegetable Garden is a testament to the monastery's self-sufficiency. Here, a variety of vegetables essential for the monastic diet were cultivated. This garden not only fed the community but also served as a place of labor, contemplation, and connection to the earth. Vegetables grown here formed the backbone of the daily meals in the Refectory, emphasizing fresh and seasonal produce."""
orchard_text_4 = """**Geese Enclosure:** The Geese Enclosure, located at the very top-right corner, played multiple roles. Geese provided feathers for bedding and quills, meat for consumption, and eggs for both eating and use in baking. Additionally, geese often served as an early warning system due to their loud honks when strangers approached, indirectly bolstering the monastery's security.\n\n**Fowl Keeper's Residence:** Next to the Geese Enclosure is the residence of the Fowl Keeper. Tasked with tending to various birds within the monastery, the Fowl Keeper ensured their health, managed their breeding, and oversaw the collection of eggs. This position was crucial, given the significance of poultry in the monastic diet and economy.\n\n**Hen Pen:** The Hen Pen represents another pillar of the monastery's self-sustainability. Hens were invaluable for their consistent egg production, and their presence ensured a steady supply of protein for the community."""

education_text_1 = """**Scholarship, Stewardship, and Shelter: Education and Hospitality at St. Gall**\n\nIn the medieval era, monasteries weren't solely dedicated to worship; they also served as beacons of education and welcoming hospitality. The St. Gall Plan's meticulous design prominently features spaces that catered to both the mind, body, and the soul, especially evident in the western sections of the monastery."""
education_text_2 = """**School:** At the core of the monastic educational journey was the school. Here, young monks and novices didn't only receive foundational religious education but were also introduced to diverse subjects like Latin, mathematics, and music. A key text that students would have encountered, and which is also present in this app's curriculum, is the "Colloquy of Aelfric." This Old English text was not just a language-learning tool but also a window into the daily life, occupations, and societal structures of the time. Such texts exemplify how monastic schools were hubs of comprehensive learning, blending spiritual teachings with broader educational content."""
education_text_3 = """**House for Guests and Pilgrims:** Embodying the Benedictine ethos of hospitality, the House for Guests was a testament to the monastery's commitment to welcoming all. Whether they were scholars seeking knowledge, travelers looking for shelter, or pilgrims on a spiritual journey, the monastery doors were always open. This practice of open-hearted welcome finds its roots in the "Rule of St. Benedict," which admonishes: "All guests who present themselves are to be welcomed as Christ, for he himself will say: I was a stranger and you welcomed me (Matt 25:35)." This quote underscores the profound reverence with which guests were regarded, seeing in them the very image of Christ."""
education_text_4 = """**The Abbot's House:** The Abbot's House, prominently situated near the school and guest accommodations on the St. Gall Plan, stands as a testament to the abbot's paramount role in the monastery. As the spiritual and administrative leader, the abbot held divinely mandated authority, acting as Christ's representative within the community. Chosen for virtue and wisdom, he ensured adherence to the Rule of St. Benedict, oversaw the monastery's daily affairs, arbitrated disciplinary matters, and represented the institution in external interactions with nobility and the church. Moreover, embodying the Benedictine ethos of hospitality, the abbot's residence often welcomed guests, pilgrims, and those seeking counsel, making it a bastion of faith and benevolence in the medieval era."""

# Check if an area is selected Education and Hospitality at St. Gall= '\n\nIn the medieval era, monasteries weren't solely dedicated to worship; they also served as beacons of education, knowledge dissemination, and welcoming hospitality. The St. Gall Plan's meticulous design prominently features spaces that catered to both the mind and the soul, especially evident in the western sections of the monastery.one':
zoom_to_area = True
for point in annotation_points:
    if point['name'] == selected_area:
        zoom_x_range = [point['x'] - 200, point['x'] + 200]
        zoom_y_range = [point['y'] - 200, point['y'] + 200]
        default_x_range = int(point['x']) - 200  # Set slider default to selected area
        default_y_range = int(point['y']) - 200  # Set slider default to selected area

        if selected_area == "The Basilica":
            # Text Section 1
            content_to_display.append({'type': 'text', 'content': basilica_text_1})
            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_0.png'})
            # Text Section 2
            content_to_display.append({'type': 'text', 'content': basilica_text_2})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_2.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': basilica_text_3})

            # Image 3
            content_to_display.append({'type': 'image', 'content': 'app_images/image_4.png'})

            # Text Section 4
            content_to_display.append({'type': 'text', 'content': basilica_text_4})

        elif selected_area == "Pens and Stables":

            # Text Section 1
            content_to_display.append({'type': 'text', 'content': pens_stables_text_1})

            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_6.png'})

            # Text Section 2
            content_to_display.append({'type': 'text', 'content': pens_stables_text_2})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_7.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': pens_stables_text_3})

            # Image 3
            content_to_display.append({'type': 'image', 'content': 'app_images/image_8.png'})

            # Text Section 4
            content_to_display.append({'type': 'text', 'content': pens_stables_text_4})

        elif selected_area == "Crafts and Artisans":
            # Text Section 1
            content_to_display.append({'type': 'text', 'content': crafts_text_1})

            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_9.png'})

            # Text Section 2
            content_to_display.append({'type': 'text', 'content': crafts_text_2})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_10.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': crafts_text_3})

        elif selected_area == "Health Care and Healing":
            # Text Section 1
            content_to_display.append({'type': 'text', 'content': health_text_1})

            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_11.png'})

            # Text Section 2
            content_to_display.append({'type': 'text', 'content': health_text_2})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_12.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': health_text_3})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_13.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': health_text_4})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_14.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': health_text_5})

        elif selected_area == "The Orchard, Cemetery, Vegetable Garden, and Livestock Pens":
            # Text Section 1
            content_to_display.append({'type': 'text', 'content': orchard_text_1})

            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_15.png'})

            # Text Section 2
            content_to_display.append({'type': 'text', 'content': orchard_text_2})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_16.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': orchard_text_3})

            # Image 2
            content_to_display.append({'type': 'image', 'content': 'app_images/image_17.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': orchard_text_4})

        elif selected_area == "Education and Hospitality":
            # Text Section 1
            content_to_display.append({'type': 'text', 'content': education_text_1})

            # Image 1
            content_to_display.append({'type': 'image', 'content': 'app_images/image_18.png'})

            # Text Section 2
            content_to_display.append({'type': 'text', 'content': education_text_2})

            # Image 2
            #content_to_display.append({'type': 'image', 'content': 'app_images/image_16.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': education_text_3})

            # Image 2
            #content_to_display.append({'type': 'image', 'content': 'app_images/image_17.png'})

            # Text Section 3
            content_to_display.append({'type': 'text', 'content': education_text_4})

        break

# Sliders for zooming
x_range = st.slider('Horizontal Position (Zoom)', 0, 850, default_x_range, 50, key='x_slider')

# Debug statements to check the type and value of default_y_range
#st.write("Before Streamlit y-slider - Type of default_y_range:", type(default_y_range))
#st.write("Before Streamlit y-slider - Value of default_y_range:", default_y_range)

    # Debug statements to check the application of constraints
#st.write("Applying constraints...")
default_x_range = max(0, default_x_range)
default_y_range = max(0, default_y_range)
#st.write("After applying constraints - default_y_range:", default_y_range)
y_range = st.slider('Vertical Position (Zoom)', 0, 850, default_y_range, 50, key='y_slider')

# Update figure based on input
if x_range != 0 or y_range != 0:
    fig.update_xaxes(range=[x_range, x_range + 400])
    fig.update_yaxes(range=[y_range, y_range + 400])
elif zoom_to_area:
    fig.update_xaxes(range=zoom_x_range)
    fig.update_yaxes(range=zoom_y_range)
else:
    fig.update_xaxes(range=[0, 1000])
    fig.update_yaxes(range=[0, 1000])

# Update layout properties
fig.update_layout(
    width=700,
    height=700,
    autosize=False,
    margin=dict(l=0, r=0, b=0, t=0),
    template="plotly_white",
)

# Display the Plotly figure with both annotations and zoom
st.plotly_chart(fig)

# Display the text at the bottom, underneath the visualization
for item in content_to_display:
    if item['type'] == 'text':
        st.write(item['content'])
    elif item['type'] == 'image':
        image = Image.open(item['content'])
        st.image(image)
