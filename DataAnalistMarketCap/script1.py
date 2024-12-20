from flask import Flask, render_template


app=Flask(__name__)

@app.route('/finance/')
def finance():
    import yfinance as yf
    import datetime
    import pandas as pd
    from bokeh.plotting import figure, show, output_file
    import numpy as np
    from bokeh.embed import components
    from bokeh.resources import CDN
    start = datetime.datetime(2018, 3, 1)
    end = datetime.datetime(2018, 3, 18)

    # Download data from Yahoo Finance
    df = yf.download("GOOG", start=start, end=end)

    # Create the 'Status' column
    df['Status'] = np.where(df['Close'] > df['Open'], 'increase',
                            np.where(df['Close'] < df['Open'], 'decrease', 'equal'))

    # Calculate the middle values
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)
    hours_12 = 12 * 60 * 60 * 1000  # 12 hours in milliseconds

    # Plotting with Bokeh
    p = figure(x_axis_type='datetime', width=1000, height=300,sizing_mode='scale_width')
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    # Create rectangles for days with increase and decrease
    increase_df = df[df['Status'] == "increase"]
    decrease_df = df[df['Status'] == "decrease"]

    # Draw the high-low segments
    p.segment(df.index, df["High"], df.index, df["Low"], color="Black")

    # Plot the rectangles for increase
    p.rect(increase_df.index, increase_df["Middle"],
        hours_12, increase_df["Height"], 
        fill_color="#CCFFFF", line_color="black")

    # Plot the rectangles for decrease
    p.rect(decrease_df.index, decrease_df["Middle"],
        hours_12, decrease_df["Height"], 
        fill_color="#CC3333", line_color="black")

    script1, div1= components(p)
    cdn_js=CDN.js_files[0]
    cdn_css = CDN.css_files[0] if CDN.css_files else None
    return render_template("finance.html",script1=script1,div1=div1,cdn_css=cdn_css,cdn_js=cdn_js)

    # Save and show the plot
    #output_file("CS.html")
    #show(p)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__== "__main__":
    app.run(debug=True)