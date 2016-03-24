
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()
    
    def all(self):
        query = "SELECT * FROM notes"
        return self.db.query_db(query)
    def create(self, note):
        query = "INSERT INTO notes (title, created_at, updated_at) VALUES (%s, NOW(), NOW())"
        data = [note['title']]
        return self.db.query_db(query, data)

    def update(self, description):
    	print description
    	query = "UPDATE notes SET description = %s, updated_at = NOW() WHERE id= %s"
    	data = [description['description'], description['id']]
    	return self.db.query_db(query, data)

    def destroy(self, id):
    	query = "DELETE FROM notes WHERE id = %s"
    	data = [id]
    	return self.db.query_db(query, data)