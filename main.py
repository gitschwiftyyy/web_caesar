import webapp2
from caesar import encrypt
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
</head>
<body>
    <h1>Web Caesar</h1>
"""

page_footer = """
</body>
</html>
"""
encrypt_form = """
      <form action='/' method='post'>
      <label>
      Rotate by <input type='text' name='caesar' value='%(caesar)s'/><label><br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'>%(encrypted_message)s</textarea><br>
      <input type='submit' value='Encrypt'/><br>
      </form>
      
      """
back = "<p><a href='/'><input type='submit' value='Back'/></a></p>"
class MainPage(webapp2.RequestHandler):
    def get(self, encrypted_message = "", caesar = ""):
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'caesar':caesar} + page_footer
      self.response.write(content)
    
    def post(self):
      caesar = self.request.get('caesar')
      caesar = int(caesar)
      message = self.request.get('message')
      encrypted_message = encrypt(message,caesar)
      encrypted_message = cgi.escape(encrypted_message, quote=True)
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'caesar':caesar} + page_footer
      self.response.write(content)
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
