import tornado.web


accountDatabase = {
    "alice": {
        "realname": "Alice Smith",
        "dateOfBirth": "Jan 1",
        "email": "alice@example.com"
    }, "bob": {
        "realname": "Bob Jones",
        "dateOfBirth": "Dec 31",
        "email": "bob@bob.xyz"
    }, "carol": {
        "realname": "Carol Ling",
        "dateOfBirth": "Jul 17",
        "email": "carol@example.com"
    }, "dave": {
        "realname": "Dave N. Port",
        "dateOfBirth": "Mar 14",
        "email": "dave@dave.dave"
    }

}

class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        uname = p.split("/")[2]
        PlaceholderText = "Username:"
        self.write(f'Username: {uname} \n')
        self.write(f'Real Name: {accountDatabase[uname]["realname"]} \n')
        self.write(f'Date of Birth: {accountDatabase[uname]["dateOfBirth"]} \n')
        self.write(f'Email: {accountDatabase[uname]["email"]} \n')