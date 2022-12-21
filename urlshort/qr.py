# import modules
import qrcode
from PIL import Image

def create_qr(url, code, QRcolor, Backcolor, logo_file=None):
    
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # adding URL or text to QRcode
    QRcode.add_data(url)
    
    # generating QR code
    QRcode.make()

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color=Backcolor).convert('RGB')
    
    if logo_file != None:

        logo = Image.open(logo_file)
        # taking base width
        basewidth = 100
        
        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    else: 
        logo = Image.new(mode="RGB", size=(0, 0))
    
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    
    # save the QR code generated
    save_name = code + ".png"
    QRimg.save('urlshort/static/user_files/qr/' + save_name)
    return save_name