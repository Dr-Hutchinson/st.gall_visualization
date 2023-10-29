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
    {'name': 'Area 1', 'x': 135, 'y': 900, 'text': 'Area 1: New Explanation'},
    #{'name': 'Area 2', 'x': 523.26, 'y': 138.33, 'text': 'Area 2: New Explanation'},
    {'name': 'Area 2', 'x': 525, 'y': 300, 'text': 'Area 2: New Explanation'},
    #{'name': 'Area 3', 'x': 258.98, 'y': 426.89, 'text': 'Area 3: New Explanation'},
    #{'name': 'Area 3', 'x': 300, 'y': 550, 'text': 'Area 3: New Explanation'},
    {'name': 'Area 4', 'x': 725, 'y': 525, 'text': 'Area 4: New Explanation'},
    #{'name': 'Area 5', 'x': 504.38, 'y': 835.45, 'text': 'Area 5: New Explanation'}
    {'name': 'Area 5', 'x': 300, 'y': 900, 'text': 'Area 5: New Explanation'}
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




# Check if an area is selected from the dropdown
if selected_area != 'None':
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

            elif selected_area == "Area 1":
                content_to_display.append({'type': 'text', 'content': basilica_text_1 })
            elif selected_area == "Area 2":
                content_to_display.append({'type': 'text', 'content': 'Placeholder text'})
            elif selected_area == "Area 3":
                content_to_display.append({'type': 'text', 'content': 'Placeholder text'})
            elif selected_area == "Area 4":
                content_to_display.append({'type': 'text', 'content': 'Placeholder text'})
            elif selected_area == "Area 5":
                content_to_display.append({'type': 'text', 'content': 'Placeholder text'})

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
