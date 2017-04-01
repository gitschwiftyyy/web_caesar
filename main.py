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
  <style>
    span {
      color:red;
    }
    </style>
"""

page_footer = """
</body>
</html>
"""
encrypt_form = """
      <form action='/' method='post'>
      <label>
      Rotate by <input type='text' name='caesar' value='%(caesar)s'/><label>{0}<br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'>%(encrypted_message)s</textarea><br>
      <input type='submit' value='Encrypt'/><br>
      </form>
      
      """
back = "<p><a href='/'><input type='submit' value='Back'/></a></p>"
class MainPage(webapp2.RequestHandler):
    def get(self, encrypted_message = "", caesar = "", error = ""):
      content = page_header + encrypt_form.format(error) % {'encrypted_message':encrypted_message, 'caesar':caesar} + page_footer
      self.response.write(content)
    
    def post(self, error = ""):
      caesar = self.request.get('caesar')
      message = self.request.get('message')
      if caesar.isdigit():
        caesar = int(caesar)
        encrypted_message = encrypt(message,caesar)
        encrypted_message = cgi.escape(encrypted_message, quote=True)
      else:
        encrypted_message = message
        error = "<strong><span>   *Invalid Cypher*</span></strong>"
      content = page_header + encrypt_form.format(error) % {'encrypted_message':encrypted_message, 'caesar':caesar} + page_footer
      self.response.write(content)
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
