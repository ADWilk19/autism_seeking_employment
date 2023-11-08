#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def int_map():
    # Load both datasets
    file = '/Users/alexwilkinson/code/ADWilk19/autism_employment/raw_data/world_autism_prevalence/autism_world_prevalence.csv'
    file2 = '/Users/alexwilkinson/code/ADWilk19/autism_employment/raw_data/world_autism_prevalence/country_coords.csv'
    aut_prev = pd.read_csv(file)
    coords = pd.read_csv(file2)
    # change ISO_A3 column name to iso_a3 in the coords dataframe
    coords.rename(columns = {'ISO_A3':'iso_a3'}, inplace = True)
    coords.columns
    # Perform a left join on iso_a3 to get latitude and longitude
    map_df = pd.merge(aut_prev,coords, on='iso_a3', how='left')
    # Drop duplicate name_y column and rename name_x column
    map_df.drop('name_y',axis=1,inplace=True)
    map_df.rename(columns= {'name_x':'name'}, inplace=True)
    fig2 = go.Figure(data=go.Choropleth(
        locations = map_df['iso_a3'],
        z = map_df['est_autism_prevalence_per_10k'],
        text = map_df['country'],
        colorscale = 'Viridis',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'Prevalence per 10,000',
    ))
    fig2.update_layout(
        width=1000,
        height=620,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='natural earth'
        ),
        title={
            'text': '<b>Autism prevalence per 10,000 people by country</b>',
            'y':0.9,
            'x':0.5,
            'xanchor': 'right',
            'yanchor': 'top',
        },
        title_font_color='#525252',
        title_font_size=20,
        font=dict(
            family='Heebo',
            size=12,
            color='#525252'
        ),
        annotations = [dict(
            x=0.5,
            y=0.01,
            xref='paper',
            yref='paper',
            text='Source:<a href="https://worldpopulationreview.com/country-rankings/autism-rates-by-country">\
                Autism rates by country (2022)</a>',
            showarrow = False
        )]
    )
    fig2.show()

def bar_chart():
    # Define data
    organisation=['A','B','C']
    location=[4,4,5]
    environment=[3,3,2]
    punctuality=[3,3,2]
    communication=[3,1,2]
    affability=[2,2,1]
    x_axis = np.arange(len(organisation))
    width = 0.15

    # Multi bar Chart
    plt.figure(figsize=(10,6))
    plt.bar(x_axis-.3 , location, width, label = 'Location')
    plt.bar(x_axis-.15 , environment, width, label = 'Environment')
    plt.bar(x_axis, punctuality, width, label = 'Punctuality')
    plt.bar(x_axis + .15, communication, width, label = 'Communication')
    plt.bar(x_axis + .3, affability, width, label = 'Affability')
    plt.xlabel('Organisation')
    plt.ylabel('Score out of 5')
    plt.title('Organisation Interview Scores')

    # Xticks

    plt.xticks(x_axis, organisation)

    # Add legend

    plt.legend()

    # Display

    plt.show()
