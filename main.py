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
      <form action='/encrypt' method='post'>
      <label>
      Rotate by <input type='text' name='caesar'/><label><br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'></textarea><br>
      <input type='submit' value='Encrypt'/><br>
      </form>
      
      """
back = "<p><a href='/'><input type='submit' value='Back'/></a></p>"
class MainPage(webapp2.RequestHandler):
    def get(self):
      content = page_header + encrypt_form + page_footer
      self.response.write(content)
    def writeForm(self, caesar='', encrypted_message=''):
      self.response.out.write(content % {'caesar':caesar,'encrypted_message':encrypted_message})
    

class EncryptedMessage(webapp2.RequestHandler):
    def post(self):
      caesar = self.request.get('caesar')
      message = self.request.get('message')
      encrypted_message = encrypt(message,caesar)
      encrypted_message = cgi.escape(encrypted_message, quote=True)
      content = page_header + encrypted_message + back + page_footer
      self.response.write(content)
    
app = webapp2.WSGIApplication([
    ('/', MainPage),('/encrypt',EncryptedMessage)
], debug=True)
