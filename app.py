import streamlit as st

st.set_page_config(layout="wide", page_title="Carbon Footprint Calculator")
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Gluten:wght@100..900&family=Raleway:ital,wght@0,100..900;1,100..900&family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# Function to create a navigation bar
def create_navbar():
    # Add your team name on the left
    st.markdown('<h1 style="text-align: left; color: maroon; font-family: Raleway, sans-serif;">ATLAS</h1>', unsafe_allow_html=True)

    # Add navigation links on the right
    st.markdown(
        """
        <style>
            .navbar {
                display: flex;
                flex-wrap: wrap;
                align-content: center;
                justify-content: center;
                background-color: #333;
                font-family: 'Poppins', sans-serif;
            }

            .navbar a {
                display: block;
                color: white;
                text-align: center;
                padding: 11px;
                text-decoration: none;
                font-size: 1rem;
            }

            .navbar a:hover {
                background-color: #ddd;
                color: black;
            }

            .navbar > :nth-child(4) {
                background-color: #097969;
            }
            html {
                scroll-behavior: smooth;
                scroll-padding: 2.2rem;
            }                       
            section {
                padding-top: 15px;
            }
        </style>
        <div class="navbar"> 
            <a href="#section1">What</a>      
            <a href="#section2">Why</a>
            <a href="#section3">How</a>
            <a href="#section4">Carbon Calculator</a>
            <a href="#section5">FAQs</a>
        </div>        
        """,
        unsafe_allow_html=True
    )

def section1():
    col1, col2 = st.columns(2)

    # Add text content to the left column
    with col1:
        st.markdown(
            """
            <div>
                <p style = "font-size: 1rem; font-family: 'Poppins', sans-serif;">A Carbon Footprint is the total amount of greenhouse gases (including carbon
                 dioxide and methane) that are generated by our actions. The average carbon 
                 footprint for a person in the United States is 16 tons, one of the highest 
                 rates in the world. Globally, the average carbon footprint is closer to 4 
                 tons. To have the best chance of avoiding a 2℃ rise in global temperatures, 
                 the average global carbon footprint per year needs to drop to under 2 tons 
                 by 2050. Lowering individual carbon footprints from 16 tons to 2 tons doesn’t
                  happen overnight! By making small changes to our actions, like eating less 
                  meat, taking fewer connecting flights and line drying our clothes, we can 
                  start making a big difference.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        button()

    # Add image to the right column
    with col2:
        st.image(
            "./images/image1.jpg",
            # caption="Carbon Footprint",
            use_column_width=True,
            # style={"border-radius": "10px", "box-shadow": "2px 2px 5px rgba(0, 0, 0, 0.2)"}
        )

def section2():
    # Split the page into two columns
    col1, col2 = st.columns(2)

    # Add the image to the left column
    with col1:
        st.image("./images/image2.jpeg", use_column_width=True)

    # Add the text to the right column
    with col2:
        st.markdown(
            """
            <div>
                <p style = "font-size: 1rem; font-family: 'Poppins', sans-serif;">Understanding your carbon footprint is like looking in the mirror and realizing your impact on the world. 
                It's about recognizing how every action, from turning on a light to driving a car, contributes to the 
                greenhouse gases that warm our planet. By calculating your carbon footprint, you gain clarity on your 
                environmental footprint, enabling you to make more mindful choices. It's not just about reducing emissions; 
                it's about taking responsibility for our planet's health and ensuring a brighter future for generations to come. 
                So, let's take that first step, quantify our impact, and embark on a journey towards sustainability together.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        button()

def section3():
    # st.markdown('<p style="text-align: justify;">To ascertain our carbon footprint employing the prescribed method, we initially acquired pivotal data: daily distance traveled by transportation, monthly electricity consumption, daily meals consumed, and weekly waste production. Subsequently, these values were input into the system.</br> We have incorporated these four significant factors that contribute to an individual carbon emissions. These factors are sourced from the Greenhouse Gas Protocol (<a href="https://ghgprotocol.org/">GHG Protocol</a>), a comprehensive global standardization framework for measuring and managing greenhouse gas (GHG) emissions across private and public sector operations, value chains, and mitigation efforts. These factors were selected specifically for India.</p>', unsafe_allow_html=True)

    # st.divider()
    
    # First row with two columns
    row1_col1, row1_col2 = st.columns(2, gap="large")

    # Populate first row columns
    with row1_col1:
        st.subheader("Transportation")
        st.markdown('<p style="color: #2E8B57; text-align: left; font-weight:bold; font-family: "Poppins", sans-serif;">The emission factor for transportation is 0.14 kgCO2/km. </p><p style="text-align: left;"> Transportation contributes significantly to carbon emissions, particularly through the burning of fossil fuels in vehicles. By quantifying the distance traveled annually and multiplying it by the emission factor for transportation, we can estimate the carbon emissions associated with our mobility. </p> ', unsafe_allow_html=True)

    with row1_col2:
        st.subheader("Electricity Consumption")
        st.markdown('<p style="color: #2E8B57; text-align: left; font-weight:bold; font-family: "Poppins", sans-serif;">The emission factor for electricity consumption is 0.82 kgCO2/kWh. </p><p style="text-align: left;">Electricity usage is a major contributor to carbon emissions, mainly due to the reliance on fossil fuels for electricity generation. By determining the amount of electricity consumed annually and multiplying it by the emission factor for electricity, we can approximate the carbon emissions attributable to our energy consumption.</p> ', unsafe_allow_html=True)

    st.divider()
    # Second row with two columns
    row2_col1, row2_col2 = st.columns(2, gap="large")
    
    # Populate second row columns
    with row2_col1:
        st.subheader("Waste Production")
        st.markdown('<p style="color: #2E8B57; text-align: left; font-weight:bold; font-family: "Poppins", sans-serif;">The emission factor for wastage is 0.1 kgCO2/kg. </p><p style="text-align: left">Waste disposal contributes to carbon emissions primarily through landfilling and incineration. The emission factor for waste represents the carbon emissions per kilogram of waste disposed of, reflecting the environmental impact of waste management practices. By multiplying this factor by our yearly waste production, we can estimate the emissions stemming from waste disposal.</p> ', unsafe_allow_html=True)

    with row2_col2:
        st.subheader("Food/Daily Meals")
        st.markdown('<p style="color: #2E8B57; text-align: left; font-weight:bold; font-family: "Poppins", sans-serif;">The emission factor for transportation is 1.25 kgCO2/meal. </p><p style="text-align: left;">Our dietary habits have a significant impact on our carbon footprint due to the energy-intensive nature of food production and distribution. By multiplying this factor by our yearly meal consumption, we can assess the environmental impact of our dietary choices.</p> ', unsafe_allow_html=True)
    st.divider()

def section4():
     # Define emission factors (example values, replace with accurate data)
    EMISSION_FACTORS = {
        "India": {
            "Transportation": 0.14,  # kgCO2/km
            "Electricity": 0.82,  # kgCO2/kWh
            "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
            "Waste": 0.1  # kgCO2/kg
        }
    }
    # User inputs
    st.subheader("🌍 Your Country:")
    country = st.selectbox("Select", ["India"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💡Monthly electricity consumed (in kWh)")
        st.markdown("Please input your monthly electricity consumed in KWh. The monthly consumption averages are between 100 and 200 kWh in India.")
        electricity = st.slider("Electricity", 0.0, 500.0, key="electricity_input")
        
        st.subheader("🚗 Daily commute distance (in km)")
        st.markdown("Please input your average daily travel distance in km.")
        distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    with col2:
        st.subheader("🗑️ Waste generated per week (in kg)")
        st.markdown("Please input the average amount of waste your household generates in a week. The average is around 400kg in one week.")
        waste = st.slider("Waste", 0.0, 100.0, key="waste_input")
        
        st.subheader("🍽️ Number of meals per day")
        st.markdown("Please input the number of meals you consume in a day.")
        meals = st.number_input("Meals", 0, key="meals_input")
        

    # Normalize inputs
    if distance > 0:
        distance = distance * 365  # Convert daily distance to yearly
    if electricity > 0:
        electricity = electricity * 12  # Convert monthly electricity to yearly
    if meals > 0:
        meals = meals * 365  # Convert daily meals to yearly
    if waste > 0:
        waste = waste * 52  # Convert weekly waste to yearly

    # Calculate carbon emissions
    transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
    electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
    diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
    waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

    # Convert emissions to tonnes and round off to 2 decimal points
    transportation_emissions = round(transportation_emissions / 1000, 2)
    electricity_emissions = round(electricity_emissions / 1000, 2)
    diet_emissions = round(diet_emissions / 1000, 2)
    waste_emissions = round(waste_emissions / 1000, 2)

    # Calculate total emissions
    total_emissions = round(
        transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
    )
    

    if st.button("Calculate CO2 Emissions"):

        # Display results
        st.header("Results")

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Carbon Emissions by Category")
            st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
            st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
            st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
            st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

        with col4:
            st.subheader("Total Carbon Footprint")
            if total_emissions<=7:
                st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
                st.balloons()
            elif total_emissions>7:
                st.error(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
            # st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
            st.warning("In 2021, CO2 emissions per capita for India was 1.9 tons of CO2 per capita. Between 1972 and 2021, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 9.41% in 2021")
     
def section5():    
    faq_items = {
        # "What is a carbon footprint?": "A carbon footprint is the total amount of greenhouse gases, such as carbon dioxide and methane, emitted directly or indirectly by human activities. It measures the impact of these activities on the environment in terms of their contribution to climate change.",        
        "Why is it important to calculate your carbon footprint? ✔️": "Calculating your carbon footprint is important because it helps you understand the environmental impact of your lifestyle choices. By knowing how much carbon you emit, you can identify areas where you can make changes to reduce your impact on the environment. This can include reducing energy consumption, using renewable energy sources, minimizing waste, and adopting sustainable transportation options.",
        "How can I reduce my carbon footprint? ↘️": "There are many ways to reduce your carbon footprint, including:\n\n1. **Reduce energy consumption:** Use energy-efficient appliances, turn off lights when not in use, and adjust your thermostat to conserve energy.\n\n2. **Use renewable energy:** Switch to renewable energy sources such as solar or wind power to reduce reliance on fossil fuels.\n\n3. **Minimize waste:** Reduce, reuse, and recycle materials whenever possible. Compost organic waste to divert it from landfills.\n\n4. **Choose sustainable transportation:** Walk, bike, carpool, or use public transportation instead of driving alone. Consider electric or hybrid vehicles.\n\n5. **Eat a plant-based diet:** Reduce your consumption of meat and dairy products, which have high carbon footprints.\n\n6. **Support carbon offset projects:** Invest in projects that reduce or offset greenhouse gas emissions, such as reforestation or renewable energy initiatives.",
        "What are some examples of activities that contribute to a carbon footprint? 🧐": "Activities that contribute to a carbon footprint include:\n\n- Driving gasoline-powered vehicles\n- Using electricity generated from fossil fuels\n- Heating or cooling homes with non-renewable energy sources\n- Flying in airplanes\n- Manufacturing and transportation of goods\n- Consuming products with high carbon emissions in their production process, such as beef and dairy products",    
        "Is it possible to have a carbon-neutral lifestyle? 🌳": "Achieving a completely carbon-neutral lifestyle may be challenging, but it's possible to significantly reduce your carbon footprint by adopting sustainable practices. This includes reducing energy consumption, using renewable energy sources, minimizing waste, and supporting carbon offset projects. While it may not be feasible for everyone to eliminate all carbon emissions, individuals and organizations can strive to minimize their impact on the environment.",        
        "How accurate are carbon footprint calculators? 💯": "Carbon footprint calculators provide estimates based on average data and assumptions. While they can give you a general idea of your carbon footprint, actual emissions may vary depending on individual circumstances and behaviors. Factors such as location, lifestyle choices, and consumption habits can influence the accuracy of the calculations. It's important to use carbon footprint calculators as a tool for awareness and guidance rather than relying solely on their results. Additionally, choosing a reputable calculator that considers a wide range of factors can improve accuracy."
    }

    for question, answer in faq_items.items():
        with st.expander(f'**{question}**'):
            st.write(f'<div style="font-family: Poppins;">{answer}</div>', unsafe_allow_html=True)

def button():
    st.markdown(
        """
        <style>
            .button {
                display: flex;
                height: 3rem;
                width: 15rem;
                background-color: #D3D3D3;              
                justify-content: center;
                align-items: center;
                font-family: "Poppins", sans-serif;
                border: 1px solid #097969;
                border-radius: 20px;
            }
            .button a{
                font-size: 1.4rem;
                text-decoration:none;
                color:#097969;                
                padding:5px;
            }
            .button a:hover{
                text-decoration:underline;
                color:midnightblue;   
            }           
        </style>
        <div class="button">            
            <a href="#section4">Calculate Now.🌳</a>
        </div>  
        """,
        unsafe_allow_html=True
    )
    
def create_sections():
    st.markdown(
        """
        <style>
            #Home-container {
                font-family: 'Poppins', sans-serif;
                display: flex;
                justify-content: center; 
                align-items: center;
                height: auto;
                background-color: #7393B3;
                padding: 1rem;
                color: white !important;
                text-align: center;
                border: 1px solid black;
            }
            #Home-container h3 {
                color: white;
                font-size: 2rem;
                font-weight: bold;
            }
            .sections {
                margin: 2rem;
                text-align: center;
                color: #013220;
                font-size: 3rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use the defined CSS ID in your HTML content
    st.write('<div id="Home-container"><h3>Use our interactive calculator to learn your Carbon Footprint.</h3></div>', unsafe_allow_html=True)

    st.markdown('<section class="sections" id="section1"><h1>What is a Carbon Footprint?</h1></section>', unsafe_allow_html=True)
    section1()
    st.markdown("---")

    st.markdown('<section class="sections" id="section2"><h1>Why to calculate your Carbon Footprint?</h1></section>', unsafe_allow_html=True)
    section2()
    st.markdown("---")

    st.markdown('<section class="sections" id="section3"><h1>How to calculate your Carbon Footprint?</h1></section>', unsafe_allow_html=True)
    section3()
    
    st.markdown('<section class="sections" id="section4"><h1>Personal Carbon Calculator 🌍</h1></section>', unsafe_allow_html=True)   
    st.markdown("<a id='section4'></a>", unsafe_allow_html=True) 
    section4()
    st.markdown("---")
          
    st.markdown('<section class="sections" id="section5"><h1>Frequently Asked Questions</h1></section>', unsafe_allow_html=True)
    section5()

def create_footer():
    st.markdown("---")   
    st.markdown(
        """
        <style>
            .footer {
                background-color: #097969; 
                font-family: Poppins;
                color: white;             
                text-align:center; 
                padding: 1rem; 
                border: 2px solid black;                        
            }
            .footer a{
                text-decoration:none;
                color:white;                
                padding:5px;
            }
            .footer a:hover{
                text-decoration:underline;
                color:#fccafa;   
            }
            #made-with{  
                font-size: 1.3rem;            
            }
            .st-emotion-cache-z5fcl4 {
                width: 90%;
                padding: 1rem 1rem 2rem;
            }
        </style>
        <div class="footer">   
            <p id="made-with">Made with ❤️ by Team ATLAS</p>     
            <p>Connect with the Developers:</p>            
            <a href="https://www.linkedin.com/in/payalnarwal/"> Payal 🌐</a>
            <a href="https://www.linkedin.com/in/tech-explorer-riyaaa/"> Riya Ahlawat 🌐</a>
            <a href="https://www.linkedin.com/in/samriddhi-tiwari-837aaa261/"> Samriddhi Tiwari 🌐</a>        
            <p>© 2024 ATLAS. All rights reserved.</p>
        </div>  
        """,
        unsafe_allow_html=True
    )


# Main function to build the app layout
def main():
    create_navbar()
    create_sections()
    create_footer()

if __name__ == "__main__":
    main()
