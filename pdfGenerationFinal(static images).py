from fpdf import FPDF
from datetime import datetime
import glob
import random
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 12, '5G Tech Locobot Reporting', 1, 1, 'C')
        self.image("glogo2.png", 10, 8, 0, 15 )
        pdf.ln(7)

pdf = PDF() # Instance of custom class
pdf.add_page()
print('pdf.h',pdf.h)
page_y = round(pdf.get_y())
print('page_y here', page_y)
page_h = pdf.h
# if (pdf.get_y()+10)
pdf.image("./servicecentercar.jpg",7, 50, w=190, h=40 , type="jpg")
pdf.ln(15)

date = datetime.today().now()
pdf.set_font('Arial', '', 12)
m,pw, ch= 10, 210 - 20, 50      # m= Margin, pw = Page width: Width of A4 is 210mm - 2*m , ch =Cell height

#Giving title
pdf.set_font('Times', 'UB', 12)
pdf.cell(w=0, h=-0.5, txt="Damage Report", ln=1, align='C')

#Printing Today's date & Client Name
pdf.set_font('Arial', '', 14)
pdf.cell(w=150, h=120, txt="Date Of Issue: ", ln=0)
pdf.cell(w=30, h=120, txt=str(date.strftime("%d %b %Y")), ln=1)
pdf.cell(w=100, h=10, txt="Billed To: ", ln=0)

#printing Multiline User Details & Address
addtxt = """  Max Smith
              5Th Avenue, Boulevard 4
              City : Austin
              state : Texas
              Zipcode : 102010"""
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=9, txt=addtxt, align="R")
pdf.ln(30)

#printing Small info on auto pdf creation
pdf.set_font('Arial', '', 12 )

text = """* This report is generated with locobot wx200 
 * In inspection it has detected below damages, 
 * please find the damage image and details below """

pdf.multi_cell(w=0, h=9, txt=text, border=1)
pdf.ln(70)

#Taking captured images from current folder and displaying in pdf
captured_Image = []
captured_Image.extend(glob.glob(pathname='*.jpg'  ))

pdf.ln(50)
pdf.set_font('Times','B',12.0)                                         #Font
pdf.set_fill_color(200, 220, 255)                                      # Background color
pdf.cell(0, 6, "Detected damage Report: -", 0, 1, 'L', 1)              # Title
pdf.ln(4)                                                              #Line break
# pdf.image("crash-report.jpg", x=10, y=None, w=190, h=45, type='jpg')   #Image
pdf.ln(10)

#Creating Table...

pdf.set_font('Arial', 'B', 10)
# table_Data = [
#             ['Damaged part', 'Car Model', 'Owner', 'Quantity','Cost'],
#             ['Headlights', 'Honda City', 'Max Smith', '2', '$24.99'],
#             ['Bumper front', 'Honda City', 'Max Smith', '1','$38.86'],
#             ['Bumper Back', 'Honda City', 'Max Smith', '1','$26.99'],
#             ['Front Wheel', 'Honda City', 'Max Smith', '1' ,'$157.76']
#             ]
# for row in table_Data:
#     for item in row:
#         pdf.cell(38, 10 ,txt=item, border=1, align='C')
#     pdf.ln(10)

pdf.ln(20)
pdf.set_font('Times','B',12.0)                                         #Font
pdf.set_fill_color(200, 220, 255)                                      # Background color
pdf.cell(0, 6, "Detected damage Images: -", 1, 1, 'L', 1)              #title
pdf.ln(15)



carpath = './car-1.jpg'
damagepath1 = './dmg1.jpg'
rimpath1 = './3rim3.jpg'

images = [{'car': carpath,
          'damage': {'damage1': damagepath1, 'damage3': damagepath1,'damage2': damagepath1},
          'rim': {'rim1': rimpath1, 'rim2': rimpath1, 'rim3': rimpath1},
          },
          {'car': carpath,
           'damage': {'damage4': damagepath1, 'damage5': damagepath1, 'damage6': damagepath1},
           'rim': {'rim4': rimpath1, 'rim5': rimpath1, 'rim6': rimpath1},
           },
          {'car': carpath,
           'damage': {'damage7': damagepath1, 'damage8': damagepath1, 'damage9': damagepath1},
           'rim': {'rim7': rimpath1, 'rim8': rimpath1, 'rim9': rimpath1},
           },
            {'car': carpath,
           'damage': {'damage10': damagepath1, 'damage11': damagepath1, 'damage12': damagepath1},
           'rim': {'rim10': rimpath1, 'rim11': rimpath1, 'rim12': rimpath1},
           },
            {'car': carpath,
           'damage': {'damage13': damagepath1, 'damage14': damagepath1, 'damage15': damagepath1},
           'rim': {'rim13': rimpath1, 'rim14': rimpath1, 'rim15': rimpath1},
           },
            {'car': carpath,
           'damage': {'damage16': damagepath1, 'damage17': damagepath1, 'damage18': damagepath1},
           'rim': {'rim16': rimpath1, 'rim17': rimpath1, 'rim18': rimpath1},
           }

          ]
print('coordinate before y',pdf.get_y())
x = 20
spacing = 60
y = pdf.get_y() + spacing/3
w = 50
h = 60
new_y = 0
new_x = 0

for ind,k in enumerate(images):
    if ind >=0:
        # y = new_y + 30
        x = 20
        print('y before')
        for i, v in k.items():
            pdf.set_font('Times', 'UB', 12.0)
            if i == 'car':
                print('y in car', y)
                print(('pdf.h now', pdf.h))
                pdf.image(v, x=x-10, y=y, w=w+10, h=h)
                pdf.text(x, y - 5, i.capitalize())

            elif i == 'damage':
                if isinstance(v, dict):
                    dh = h / len(v.values())
                    print('dh here', dh)
                    dy = y
                    x = x + spacing
                    for subkey, subvalue in v.items():
                        print(subkey + ': ' + subvalue)
                        pdf.image(subvalue, x=x, y=dy, w=w, h=dh-5)
                        pdf.text(x, dy - 5, subkey.capitalize())
                        dy = dy + dh + 5
            else:
                if isinstance(v, dict):
                    rh = h / len(v.values())
                    print('rh here', rh)
                    ry = y
                    x = x + spacing
                    for subkey, subvalue in v.items():
                        pdf.image(subvalue, x=x, y=ry, w=w, h=rh-5)
                        pdf.text(x, ry - 5, subkey.capitalize())
                        ry = ry + rh + 5
                        new_y = ry
                        new_x = x
                        print(new_y)
                        # if y + h > pdf.h:
                        #     pdf.add_page()  # Add a new page
        y = y + spacing + 30
        if y> (pdf.h - 20):
            pdf.add_page()
            y = 40
            #     y = 100
pdf.output(f'pdfGenFnlreport-{str(date.strftime("%d %b %Y"))}.pdf')