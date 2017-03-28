import webapp2
from caesar import encrypt

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

class MainPage(webapp2.RequestHandler):
    def get(self):
      encrypt_form = """
      <form action='/encrypt' method='post'>
      <label>
      Rotate by <input type='text' name='caesar'/><label><br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'></textarea><br>
      <input type='submit' value='Encrypt'/>
      </form>
      
      """
      content = page_header + encrypt_form + page_footer
      self.response.write(content)

class EncryptedMessage(webapp2.RequestHandler):
  def post(self):
    caesar = self.request.get('caesar')
    message = self.request.get('message')
    encrypted_message = encrypt(message,caesar)
    content = page_header + encrypted_message + page_footer
    self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/encrypt',EncryptedMessage)
], debug=True)
