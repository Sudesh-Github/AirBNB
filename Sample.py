import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def datafr():
    df= pd.read_csv("Airbnb_data.csv")
    return df

df= datafr()

with st.sidebar:
    select= option_menu("Main Menu", ["Home", "Data Exploration","Tips to Improve","About"])

if select == "Home":

    image1= Image.open("airbnb_icon.jpg")
    st.image(image1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


if select == "Data Exploration":
    tab1, tab2, tab3, tab4, tab5= st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])
    with tab1:
        st.title("**PRICE DIFFERENCE**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["address.country"].unique())

            df1= df[df["address.country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores.review_scores_value","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores.review_scores_value"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)
            
                
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique())

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host.host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host.host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)

        with col1:

            
            hostresponsetime= st.selectbox("Select the host_response_time",df4["host.host_response_time"].unique())

            df5= df4[df4["host.host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            

            st.plotly_chart(fig_do_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

    with tab2:

        def datafr():
            df_a= pd.read_csv("Airbnb_data.csv")
            return df_a

        df_a= datafr()

        st.title("**AVAILABILITY ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Select the Country_a",df_a["address.country"].unique())

            df1_a= df[df["address.country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","address.location.is_location_exact_True"], values="availability.availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","address.location.is_location_exact_True"], values="availability.availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","address.location.is_location_exact_True"], values="availability.availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","address.location.is_location_exact_True"], values="availability.availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
        
        roomtype_a= st.selectbox("Select the Room Type_a", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host.host_response_time")[["availability.availability_30","availability.availability_60","availability.availability_90","availability.availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host.host_response_time', y=["availability.availability_30","availability.availability_60","availability.availability_90","availability.availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)


    with tab3:

        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("Airbnb_data.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country_l",df_l["address.country"].unique())

        df1_l= df_l[df_l["address.country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property_type_l",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)


        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["address.street","host.host_location","host.host_neighbourhood"],y="address.market", title="MARKET",
                    hover_data= ["name","host.host_name","address.market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

 
    with tab4:

       st.title("GEOSPATIAL VISUALIZATION")
       st.write("")

       fig_4 = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', color='price', size='accommodates',
                      color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                      zoom=1)
       fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
    st.plotly_chart(fig_4)   


    with tab5:

        country_t= st.selectbox("Select the Country_t",df["address.country"].unique())

        df1_t= df[df["address.country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host.host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host.host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host.host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host.host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host.host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host.host_location", "total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "total_price", y= "host.host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host.host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)


if select == "Tips to Improve":
        df = pd.read_csv("Airbnb_data.csv")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["***PRICE ANALYSIS***", "***AVAILABILITY ANALYSIS***", "***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])

        with tab1:
            st.title("**PRICE DIFFERENCE**")
            col1, col2 = st.columns(2)

            with col1:
                country = st.selectbox("Select the Country", df["address.country"].unique(), key="price_country")
                df1 = df[df["address.country"] == country]
                df1.reset_index(drop=True, inplace=True)

                room_ty = st.selectbox("Select the Room Type", df1["room_type"].unique(), key="price_room_type")
                df2 = df1[df1["room_type"] == room_ty]
                df2.reset_index(drop=True, inplace=True)

                df_bar = pd.DataFrame(df2.groupby("property_type")[["price", "review_scores.review_scores_value", "number_of_reviews"]].sum())
                df_bar.reset_index(inplace=True)

                fig_bar = px.bar(df_bar, x='property_type', y="price", title="PRICE FOR PROPERTY_TYPES", hover_data=["number_of_reviews", "review_scores.review_scores_value"], color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
                st.plotly_chart(fig_bar)

                st.info("### Tips for Price Optimization")
                st.info("Hosts should consider setting competitive prices based on the most common property types in their area. For instance, if apartments tend to be priced higher, adjusting prices for other property types might attract more bookings.")
                st.write("")



            with col2:
                proper_ty = st.selectbox("Select the Property_type", df2["property_type"].unique(), key="price_property_type")
                df4 = df2[df2["property_type"] == proper_ty]
                df4.reset_index(drop=True, inplace=True)

                df_pie = pd.DataFrame(df4.groupby("host.host_response_time")[["price", "bedrooms"]].sum())
                df_pie.reset_index(inplace=True)

                fig_pi = px.pie(df_pie, values="price", names="host.host_response_time",
                                hover_data=["bedrooms"],
                                color_discrete_sequence=px.colors.sequential.BuPu_r,
                                title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                                width=600, height=500)
                st.plotly_chart(fig_pi)
                st.write("")
                st.write("")



                st.info("### Tips for Host Response Time")
                st.info("Encourage hosts to improve their response times. Faster response times are associated with higher prices and potentially better reviews, which can lead to more bookings.")
                st.write("")
                st.write("")

            col1, col2 = st.columns(2)

            with col1:
                hostresponsetime = st.selectbox("Select the host_response_time", df4["host.host_response_time"].unique(), key="price_host_response_time")
                df5 = df4[df4["host.host_response_time"] == hostresponsetime]

                df_do_bar = pd.DataFrame(df5.groupby("bed_type")[["minimum_nights", "maximum_nights", "price"]].sum())
                df_do_bar.reset_index(inplace=True)

                fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'],
                                    title='MINIMUM NIGHTS AND MAXIMUM NIGHTS', hover_data="price",
                                    barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)

                st.plotly_chart(fig_do_bar)

                st.info("### Tips for Minimum and Maximum Nights")
                st.info("Adjust the minimum and maximum night requirements based on bed type to optimize booking rates. For example, properties with certain bed types that are underbooked might benefit from shorter minimum night stays.")

            with col2:
                df_do_bar_2 = pd.DataFrame(df5.groupby("bed_type")[["bedrooms", "beds", "accommodates", "price"]].sum())
                df_do_bar_2.reset_index(inplace=True)

                fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'],
                                    title='BEDROOMS AND BEDS ACCOMMODATES', hover_data="price",
                                    barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=600, height=500)

                st.plotly_chart(fig_do_bar_2)

                st.info("### Tips for Bedrooms and Beds")
                st.info("This chart indicates how different bed types correlate with the number of bedrooms, beds, and accommodates. Hosts can use this information to optimize their property setup to attract more guests.")

        with tab2:
            st.title("**AVAILABILITY ANALYSIS**")
            col1, col2 = st.columns(2)

            with col1:
                country_a = st.selectbox("Select the Country", df["address.country"].unique(), key="availability_country")
                df1_a = df[df["address.country"] == country_a]
                df1_a.reset_index(drop=True, inplace=True)

                property_ty_a = st.selectbox("Select the Property Type", df1_a["property_type"].unique(), key="availability_property_type")
                df2_a = df1_a[df1_a["property_type"] == property_ty_a]
                df2_a.reset_index(drop=True, inplace=True)

                df_a_sunb_30 = px.sunburst(df2_a, path=["room_type", "bed_type", "address.location.is_location_exact_True"], values="availability.availability_30", width=600, height=500, title="Availability_30", color_discrete_sequence=px.colors.sequential.Peach_r)
                st.plotly_chart(df_a_sunb_30)

                st.info("### Tips for Seasonal Availability")
                st.info("Identify patterns of low and high availability and adjust pricing or marketing strategies accordingly. For example, if a property has low availability in the next 30 days, it might benefit from last-minute discounts or promotions.")

            with col2:
                df_a_sunb_60 = px.sunburst(df2_a, path=["room_type", "bed_type", "address.location.is_location_exact_True"], values="availability.availability_60", width=600, height=500, title="Availability_60", color_discrete_sequence=px.colors.sequential.Blues_r)
                st.plotly_chart(df_a_sunb_60)

            col1, col2 = st.columns(2)

            with col1:
                df_a_sunb_90 = px.sunburst(df2_a, path=["room_type", "bed_type", "address.location.is_location_exact_True"], values="availability.availability_90", width=600, height=500, title="Availability_90", color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
                st.plotly_chart(df_a_sunb_90)

            with col2:
                df_a_sunb_365 = px.sunburst(df2_a, path=["room_type", "bed_type", "address.location.is_location_exact_True"], values="availability.availability_365", width=600, height=500, title="Availability_365", color_discrete_sequence=px.colors.sequential.Greens_r)
                st.plotly_chart(df_a_sunb_365)

            roomtype_a = st.selectbox("Select the Room Type", df2_a["room_type"].unique(), key="availability_room_type")
            df3_a = df2_a[df2_a["room_type"] == roomtype_a]

            df_mul_bar_a = pd.DataFrame(df3_a.groupby("host.host_response_time")[["availability.availability_30", "availability.availability_60", "availability.availability_90", "availability.availability_365", "price"]].sum())
            df_mul_bar_a.reset_index(inplace=True)

            fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host.host_response_time', y=["availability.availability_30", "availability.availability_60", "availability.availability_90", "availability.availability_365"],
                                    title='AVAILABILITY BASED ON HOST RESPONSE TIME', hover_data="price",
                                    barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_df_mul_bar_a)

            st.info("### Tips for Host Response Time and Availability")
            st.info("Encourage hosts to respond more quickly to booking inquiries, as faster response times correlate with higher availability and potential earnings.")

        with tab3:
            
            st.title("**LOCATION ANALYSIS**")
            country_l = st.selectbox("Select the Country", df["address.country"].unique(), key="location_country")

            df1_l = df[df["address.country"] == country_l]
            df1_l.reset_index(drop=True, inplace=True)

            proper_ty_l = st.selectbox("Select the Property Type", df1_l["property_type"].unique(), key="location_property_type")

            df2_l = df1_l[df1_l["property_type"] == proper_ty_l]
            df2_l.reset_index(drop=True, inplace=True)

            # Visualization for Price Distribution
            st.subheader("Price Distribution")
            fig_price = px.histogram(df2_l, x='price', nbins=30, title='Price Distribution', color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(fig_price)

            # Visualization for Number of Reviews
            st.subheader("Number of Reviews Distribution")
            fig_reviews = px.histogram(df2_l, x='number_of_reviews', nbins=30, title='Number of Reviews Distribution', color_discrete_sequence=px.colors.sequential.Magma)
            st.plotly_chart(fig_reviews)

            # Visualization for Room Types
            st.subheader("Room Types Distribution")
            fig_room_type = px.pie(df2_l, names='room_type', title='Room Types Distribution', color_discrete_sequence=px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig_room_type)

            # Visualization for Property Types
            st.subheader("Property Types Distribution")
            fig_property_type = px.pie(df2_l, names='property_type', title='Property Types Distribution', color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig_property_type)

            # Visualization for Reviews per Month
            st.subheader("Reviews per Month Distribution")
            fig_reviews_per_month = px.histogram(df2_l, x='reviews_per_month', nbins=30, title='Reviews per Month Distribution', color_discrete_sequence=px.colors.sequential.Sunset)
            st.plotly_chart(fig_reviews_per_month)

            # Visualization for Accommodates
            st.subheader("Accommodates Distribution")
            fig_accommodates = px.histogram(df2_l, x='accommodates', nbins=15, title='Accommodates Distribution', color_discrete_sequence=px.colors.sequential.Burg)
            st.plotly_chart(fig_accommodates)

            # Visualization for Beds
            st.subheader("Beds Distribution")
            fig_beds = px.histogram(df2_l, x='beds', nbins=15, title='Beds Distribution', color_discrete_sequence=px.colors.sequential.Burgyl)
            st.plotly_chart(fig_beds)

            # Visualization for Bathrooms
            st.subheader("Bathrooms Distribution")
            fig_bathrooms = px.histogram(df2_l, x='bathrooms', nbins=15, title='Bathrooms Distribution', color_discrete_sequence=px.colors.sequential.PuBu)
            st.plotly_chart(fig_bathrooms)

            st.info("### Tips for Price Range Segmentation")
            st.info("Segment properties into different price ranges and tailor marketing strategies accordingly. For example, lower-priced properties could target budget travelers, while higher-priced properties might focus on luxury experiences.")

            st.info("### Tips for Accommodates and Features")
            st.info("Optimize property features to match guest capacity. For instance, ensure that properties accommodating more guests have adequate bedrooms and beds.")

        with tab4:
            st.title("**GEOSPATIAL VISUALIZATION**")
            fig = px.scatter_mapbox(df, lat="Latitude",
                                    lon="Longitude",
                                    hover_name="price", hover_data=["property_type", "room_type"],
                                    color_discrete_sequence=["fuchsia"], zoom=3, height=600)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)

            st.info("### Tips for Geographic Distribution")
            st.info("Use geographic data to identify underserved areas where new listings could be added. Focus on high-demand locations with fewer listings to capture untapped markets.")

        with tab5:
            st.title("**TOP CHARTS**")
            col1, col2 = st.columns(2)

            with col1:
                country_t = st.selectbox("Select the Country", df["address.country"].unique(), key="top_charts_country")
                df1_t = df[df["address.country"] == country_t]
                df1_t.reset_index(drop=True, inplace=True)

                df_bar_t_1 = pd.DataFrame(df1_t.groupby("address.suburb")[["price", "review_scores.review_scores_value", "number_of_reviews"]].sum())
                df_bar_t_1.reset_index(inplace=True)

                fig_bar_t_1 = px.bar(df_bar_t_1, x='address.suburb', y="price", title="PRICE PER SUBURB",
                                    hover_data=["review_scores.review_scores_value", "number_of_reviews"], color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
                st.plotly_chart(fig_bar_t_1)

                st.info("### Tips for Neighborhood Pricing")
                st.info("Adjust prices based on neighborhood trends. Properties in popular neighborhoods should consider premium pricing, while those in less popular areas might benefit from competitive pricing or added amenities to attract guests.")

            with col2:
                df_bar_t_2 = pd.DataFrame(df1_t.groupby("host.host_location")[["price", "review_scores.review_scores_value", "number_of_reviews"]].sum())
                df_bar_t_2.reset_index(inplace=True)

                fig_bar_t_2 = px.bar(df_bar_t_2, x='host.host_location', y="price", title="PRICE PER HOST LOCATION",
                                    hover_data=["review_scores.review_scores_value", "number_of_reviews"], color_discrete_sequence=px.colors.sequential.Burg, width=600, height=500)
                st.plotly_chart(fig_bar_t_2)

            col1, col2 = st.columns(2)

            with col1:
                df_bar_t_3 = pd.DataFrame(df1_t.groupby("room_type")[["price", "review_scores.review_scores_value", "number_of_reviews"]].sum())
                df_bar_t_3.reset_index(inplace=True)

                fig_bar_t_3 = px.bar(df_bar_t_3, x='room_type', y="price", title="PRICE PER ROOM TYPE",
                                    hover_data=["review_scores.review_scores_value", "number_of_reviews"], color_discrete_sequence=px.colors.sequential.Darkmint, width=600, height=500)
                st.plotly_chart(fig_bar_t_3)

                st.info("### Tips for Room Type Performance")
                st.info("Evaluate which room types perform best in specific areas and adjust listings accordingly. For example, if private rooms are more popular in urban areas, focus on optimizing these types of listings.")

            with col2:
                df_bar_t_4 = pd.DataFrame(df1_t.groupby("property_type")[["price", "review_scores.review_scores_value", "number_of_reviews"]].sum())
                df_bar_t_4.reset_index(inplace=True)

                fig_bar_t_4 = px.bar(df_bar_t_4, x='property_type', y="price", title="PRICE PER PROPERTY TYPE",
                                    hover_data=["review_scores.review_scores_value", "number_of_reviews"], color_discrete_sequence=px.colors.sequential.Brwnyl, width=600, height=500)
                st.plotly_chart(fig_bar_t_4)

            st.write("**TOP 100 PRICE LISTINGS**")
            df_bar_t_5 = df1_t.nlargest(100, "price")

            fig_bar_t_5 = px.bar(df_bar_t_5, x='price', y=['minimum_nights', 'maximum_nights', 'accommodates'],
                                title='TOP 100 PRICE LISTINGS',
                                barmode='group', color_discrete_sequence=px.colors.sequential.PuBu, width=1000, height=500)

            st.plotly_chart(fig_bar_t_5)

            st.info("### Tips for Top 100 Listings")
            st.info("Analyze the characteristics of top-performing listings (e.g., minimum nights, maximum nights, accommodates) and replicate these features in other listings to improve performance.")


if select == "About":

    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')


