import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Day'] = data['Timestamp'].dt.date
data['Month'] = data['Timestamp'].dt.strftime('%Y/%m')
# Ensure only numeric columns are included in the aggregation
numeric_data = data.select_dtypes(include=['number'])
Month_group_crs = data.groupby(['Month', 'Course Name'])[numeric_data.columns].mean().unstack()
#Month_group_crs = data.groupby(['Month', 'Course Name'])[numeric_data.columns].count().unstack()
#Month_group_crs[:20]

#change to areaspline to spline
#change to legend floating: true        to      false
chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2024'
    },
    subtitle: {
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor:
             '#FFFFFF'
    },
    xAxis: {
        // Highlight the last years where moose hunting quickly deminishes
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'john',
        data:
            [3,4,3,5,4,10,12]
    }, {
        name: 'jane',
        data:
            [1,3,4,3,3,5,4]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analisys of Course Reviews",classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analisys")
    hc = jp.HighCharts(a=wp,options=chart_def)
    #print(hc.options.title.text)                   #verify about type data then change this
    hc.options.title.text = "Averange Rating by Month by Course"
    hc.options.subtitle = ""

    hc.options.xAxis.categories = list(Month_group_crs.index)
    hc_data = [{"name":v1,"data":[v2 for v2 in Month_group_crs[v1]]}for v1 in Month_group_crs.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)