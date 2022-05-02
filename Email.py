import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders



def send_mail(subject, send_to, send_from=None, text_message='', html_message='', attachments=[], image_path=None):
    """
    Send email to recipients

    Parameters
    ----------
    subject
    send_from
    send_to
    text_message
    html_message
    attachments : list of dicts
        mandatory keys:
            'data' - filename w. path,
            'filename' - name of attached file


    Returns
    -------

    """

    COMMASPACE = ', '
        # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = subject
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    # author = formataddr((str(Header(u'Jan Frydendall', 'utf-8')), send_from))
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    text = text_message
    html = """\
    <html>
    <head></head>
    <body>
    %s
    </body>
    </html>
    """ % html_message.replace('\n', '<br>')
    body = MIMEMultipart('alternative')
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    body.attach(part1)
    body.attach(part2)
    msg.attach(body)

    if image_path is not None:
        # This example assumes the image is in the current directory
        fp = open(image_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)


    if attachments:
        for attachment in attachments:
            if attachment['filename'].find('doc') > 0:
                attach_file = MIMEBase('application', 'msword')
            elif attachment['filename'].find('pdf') > 0:
                attach_file = MIMEBase('application', 'pdf')
            elif attachment['filename'].find('xls') > 0:
                attach_file = MIMEBase('application', 'ms-excel')
            else:
                attach_file = MIMEBase('application', 'octet-stream')
            with open(attachment['data'], 'rb') as file:
                attach_file.set_payload(file.read())
            encoders.encode_base64(attach_file)
            attach_file.add_header('Content-Disposition', 'attachment', filename=attachment['filename'])
            msg.attach(attach_file)

    # smtp_server = Mailserver URL !musst du noch definieren

    smtp = smtplib.SMTP(smtp_server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
