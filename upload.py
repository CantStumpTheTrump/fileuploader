import web;from os import path
urls = (
  '/', 'post'
)
class post:
  def GET(self):
   return """<form method='post' enctype='multipart/form-data'><input id='filename' placeholder='filename' name='filename'/><br/><input type='file' name='file' id='file'/><input type='submit' value='upload' name='submit'/><br/></form><br/><a href='/static/'>See other uploaded images</a>"""
  def POST(self):
    filetosave = web.input()['file']
    filename = 'static/'+str(web.input()['filename'])+'.png'
    if(path.exists(filename)):
     return "File with that name already exists, pick another name."
    else:
      with open(filename, 'wb') as saved:
       saved.write(filetosave) 
       web.seeother(filename)
   

  if __name__ == "__main__": 
      app = web.application(urls, globals())
      app.run()        
