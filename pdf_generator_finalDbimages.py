from pymongo import MongoClient
from datetime import datetime
from io import BytesIO
from PIL import Image
from fpdf import FPDF
import base64
import os
from flask import Flask,request, jsonify
client = MongoClient(host='10.236.76.215', port= 27017)
db = client['locobotDB']
collection = db['pdfData']
data = collection.find()

app = Flask(__name__)

@app.route('/generatePdf', methods=['POST'])
def create_Pdf_with_fetched_records():
    data = request.json
    filter = data.get('user_data')
    print("filter ",filter)
    # fetched = collection.find_one(filter)
    fetched = collection.find_one(filter)
    for i in fetched['observations']:
        print('observation ---- ', i)

    class PDF(FPDF):
        def __init__(self):
            super().__init__()

        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 12, '5G Tech Mobile Robot Reporting', 1, 1, 'C')
            self.image("./5glogo4.png", 10, 8, 0, 15)
            self.image('Capgemini-Logo.png',25, 8, 0, 16)
            pdf.ln(7)

        def footer(self):
            # Set the position of the footer
            self.set_y(-15)
            # Set the font and size for the footer
            self.set_font('Arial', 'I', 8)
            # Add a page number
            self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'R')


    pdf = PDF()  # Instance of custom class
    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)  # Set auto page break with a margin of 15mm

    pdf.image("./servicecentercar.jpg", 7, 50, w=190, h=40, type="jpg")
    pdf.ln(15)

    date = datetime.today().now()
    pdf.set_font('Arial', '', 12)

    # Giving title
    pdf.set_font('Times', 'UB', 12)
    pdf.cell(w=0, h=-0.5, txt="Damage Report", ln=1, align='C')

    # Printing Today's date & Client Name
    pdf.set_font('Arial', '', 14)
    pdf.cell(w=150, h=120, txt="Date Of Issue: ", ln=0)
    pdf.cell(w=30, h=120, txt=str(date.strftime("%d %b %Y")), ln=1)
    pdf.cell(w=100, h=10, txt="Billed To: ", ln=0)

    # printing Multiline User Details & Address
    addtxt = """  Max Smith
                  5Th Avenue, Boulevard 4
                  City : Austin
                  state : Texas
                  Zipcode : 102010"""
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(w=0, h=9, txt=addtxt, align="R")
    pdf.ln(30)

    # printing Small info on auto pdf creation
    pdf.set_font('Arial', '', 12)

    text = """
     * This report is generated with 5G Tech Mobile Robot Reporting
     * In inspection it has detected damages and missing Rim's, 
     * please find the damage images and details below """

    pdf.multi_cell(w=0, h=9, txt=text, border=1)
    pdf.ln(70)

    # Creating Table...
    # pdf.set_font('Arial', 'B', 10)
    # table_Data = [
    #     ['Damaged part', 'Car Model', 'Owner', 'Quantity', 'Cost'],
    #     ['Headlights', 'Honda City', 'Max Smith', '2', '$24.99'],
    #     ['Bumper front', 'Honda City', 'Max Smith', '1', '$38.86'],
    #     ['Bumper Back', 'Honda City', 'Max Smith', '1', '$26.99'],
    #     ['Front Wheel', 'Honda City', 'Max Smith', '1', '$157.76']
    # ]
    # for row in table_Data:
    #     for item in row:
    #         pdf.cell(38, 10, txt=item, border=1, align='C')
    #     pdf.ln(10)

    pdf.ln(20)
    pdf.set_font('Times', 'B', 12.0)  # Font
    pdf.set_fill_color(200, 220, 255)  # Background color
    pdf.cell(0, 6, "Detected damage Images: -", 1, 1, 'L', 1)  # title
    pdf.ln(15)

    #initial values for x & y coordinates, width(w), height(h) and spacing after every loop
    x = 20
    spacing = 60
    y = pdf.get_y() + spacing / 3
    w = 25
    h = 30
    count = 0

    if fetched is not None:
        fetched['_id'] = str(fetched['_id'])

        #loop through observations
        for ind, k in enumerate(fetched['observations']):
            # reset x for next column
            if ind >= 0:
                x = 30
                #for key(i) values(v) in k.items
                for i, v in k.items():
                    count = count + 1
                    #save the images temporary in the folder to display on pdf
                    saveing = f'detectedImages/theimage{count}.jpg'

                    #check key(i) and perform the respective operation
                    if i == 'Side':
                        pdf.set_font('Times', 'UB', 12.0)
                        #change color to blue
                        pdf.set_text_color(0, 0, 255)
                        pdf.text(x-20, y - 20, f'Side:- {v.capitalize()}')
                        # change color back to black
                        pdf.set_text_color(0, 0, 0)

                    elif i == 'Car_image':
                        image = BytesIO(base64.b64decode(v[23:]))
                        imagedata = Image.open(image)
                        imagedata.save(saveing)
                        print('saved after car save image is ', saveing)
                        pdf.image(saveing, x=x - 10, y=y, w=w*2, h=h)
                        pdf.text(x, y - 5, i.capitalize())

                    elif i == 'Damage_images':
                        if len(v) ==0:
                            dh = h
                            x = x + spacing
                            pdf.set_font('Times', 'B', 12)
                            pdf.text(x+5, y-5, i)
                            pdf.image('no_damage1.png', x=x+7, y=y+5, w=w, h=h -10)
                            pdf.text(x+5, y + h+10, 'No Damage detected')
                        elif len(v) == 1:
                            dh = h / len(v)
                            dy = y
                            x = x + spacing
                            # if damage is single key value
                            image = BytesIO(base64.b64decode(v[0][23:]))
                            imagedata3 = Image.open(image)
                            imagedata3.save(saveing)
                            print('saved after damage save image is ', saveing)
                            pdf.image(saveing, x=x-5, y=dy, w=w + 12, h=dh - 18)
                            pdf.text(x, dy - 5, i.capitalize())
                            dy = dy + dh + 5
                            count = count + 1

                        else:
                            dh = h / len(v)
                            dy = y
                            x = x + spacing
                            # if damage is multi key value
                            for damage in v:
                                if damage:
                                    image = BytesIO(base64.b64decode(damage[23:]))
                                    print(image)
                                    imagedata3 = Image.open(image)
                                    imagedata3.save(saveing)
                                    print('saved after damage save image is ', saveing)
                                    pdf.image(saveing, x=x, y=dy, w=w+7, h=dh - 5)
                                    pdf.text(x, dy - 5, i.capitalize())
                                    dy = dy + dh + 5
                                    count = count + 1

                    elif i == 'Rim_images':
                        #for rim
                        if len(v) <1:
                            ry = y
                            x = x + spacing
                            pdf.set_font('Times', 'B', 12)
                            pdf.text(x+5, y-5, i)
                            pdf.image('no_damage1.png', x=x+5, y=ry+5, w=w, h=h-10)
                            pdf.text(x+5, ry + h+10, 'No missing Rim ')
                        elif v:
                            for rim in v:
                                rh = h / len(v)
                                ry = y
                                x = x + spacing
                                image = BytesIO(base64.b64decode(rim[23:]))
                                imagedata = Image.open(image)
                                imagedata.save(saveing)
                                print('saved after rim save image is ', saveing)
                                pdf.image(saveing, x=x, y=ry, w=w+5, h=rh - 5)
                                pdf.text(x, ry - 5, i.capitalize())
                                ry = ry + rh + 5
                                count = count+1
                    else:
                        print('got new value ', i)

                y = y + spacing + 20
                if y > (pdf.h - 20):
                    pdf.add_page()
                    y = 60


    pdf.output("damage-report5gDB.pdf")
    path = 'detectedImages/'
    for i in os.listdir(path):
        os.remove(path+i)
    return jsonify(fetched)


if __name__ == '__main__':
    app.run()
