#!/usr/bin/python
import time

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

def writePdf(data, filename):
  doc = SimpleDocTemplate(filename, pagesize=letter)
  # container for the 'Flowable' objects
  elements = []
     
  styles = getSampleStyleSheet()     
  styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
  styleH = styles['Heading1']
  logo_ipbeja = "aux/images/ipbejaLogo.JPG"
  screenshot = "aux/images/screenshot.png"

  logo_ipbeja = Image(logo_ipbeja, hAlign='LEFT')
  logo_ipbeja.drawHeight = 1.25*inch*logo_ipbeja.drawHeight / logo_ipbeja.drawWidth
  logo_ipbeja.drawWidth = 1.25*inch
  screenshot = Image(screenshot, hAlign='CENTER')
  screenshot.drawHeight = 5*inch*screenshot.drawHeight / screenshot.drawWidth
  screenshot.drawWidth = 5*inch
 

  #logos = [ [logo_ipbeja, 0], [logo_estig,0]]


  elements.append(logo_ipbeja)
  elements.append(Spacer(1, 12))

  elements.append(screenshot)

  ptext = """<para align=CENTER>  <font size=14> Projeto de Linguagens de Programacao Dinamicas
  </font>    </para>"""

  elements.append(Spacer(1, 12))

  elements.append(Paragraph(ptext, styleH))
  elements.append(Spacer(1, 12))
  ptext = """<para align=CENTER>  <font size=14> Goncalo Pereira N 19020
  </font>    </para>"""

  elements.append(Paragraph(ptext, styleH))
  elements.append(Spacer(1, 12))
  ptext = """<para align=CENTER>  <font size=14> Beja 2019
  </font>    </para>"""

  elements.append(Paragraph(ptext, styleH))
  elements.append(Spacer(1, 12))
  elements.append(Spacer(1, 12))






  t=Table(data,style=([
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ]
    ))
  t._argW[0]=1.5*inch
     
  elements.append(t)

    # write the document to disk
  doc.build(elements)

def main():
  data= [['A', 'B', 'C', 'P0', 'D'],
           ['00', '01', '02', '[I,P]', '04'],
           ['10', '11', '12', '[P,I]', '14'],
           ['20', '21', '22', '23', '24'],
           ['30', '31', '32', '33', '34']]

  writePdf(data, 'teste.pdf')

if __name__=='__main__':
    main()