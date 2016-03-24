
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')
    
    def index(self):
        notes = self.models['Note'].all()
        return self.load_view('/notes/index.html', notes = notes)
    
    # def index_json(self):
    #     notes = self.models['Note'].all()
    #     return jsonify(quotes=quotes)

    def index_html(self):
        notes = self.models['Note'].all()
        return self.load_view('partials/notes.html', notes = notes)

    def create(self):
        new_note = {
            'title' : request.form['title']
        }
        self.models['Note'].create(new_note)
        notes = self.models['Note'].all()
        # return redirect ('/')
        return self.load_view('partials/notes.html', notes = notes)
    
    def update(self):
        description = {
            'description': request.form['description'],
            'id': request.form['id']
        }
        self.models['Note'].update(description)
        notes = self.models['Note'].all()
        # return redirect ('/')
        return self.load_view('partials/notes.html', notes = notes)

    def destroy(self, id):
        self.models['Note'].destroy(id)
        return redirect('/')