from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Electricity Consumption Analysis</title></head>
    <body style="margin:0; padding:0; text-align:center; background-family:sans-serif;">
        <h1 style="padding:20px; margin:0; background:#1f4e79; color:white;">Electricity Consumption Analysis Dashboard</h1>
        <iframe src="https://public.tableau.com/app/profile/kalagotla.charmi/viz/ElectricityConsumption_17830639783270/StoryonelectricityConsumptioninindia?:showVizHome=no&:embed=true" width="100%" height="850px" frameborder="0"></iframe>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
