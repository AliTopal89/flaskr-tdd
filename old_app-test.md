took some notes on testing too. TODO-should be on a readme
<!-- class FlaskrTestCase(unittest.TestCase):

    # The code in the setUp() method creates a new test client and initializes a new database. 
    # To close the file, keep the db_fd around so that we can use the os.close() function
    def setUp(self):
        """Set up a blank temp database before each test."""
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    # To delete after the test, we close the file and remove it from filesystem in the tearDown() method.
    def tearDown(self):
        """Destroy blank temp database after each test."""
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def login(self, username, password):
        """Login helper function."""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Logout helper function."""
        return self.app.get('/logout', follow_redirects=True) -->


<!-- # assert functions

    # test adding messages - eg - b'no stories here so far'
    def test_empty_db(self):
        """Ensure database is blank."""
        rv = self.app.get('/')
        assert b'No entries yet. Add some!' in rv.data

    def test_login_logout(self):
        """Test login and logout using helper functions."""
        rv = self.login(
            app.app.config['USERNAME'],
            app.app.config['PASSWORD']
        )
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        rv = self.login(
            app.app.config['USERNAME'] + 'x',
            app.app.config['PASSWORD']
        )
        assert b'Invalid username' in rv.data
        rv = self.login(
            app.app.config['USERNAME'],
            app.app.config['PASSWORD'] + 'x'
        )
        assert b'Invalid password' in rv.data

    def test_messages(self):
        """Ensure that a user can post messages."""
        self.login(
            app.app.config['USERNAME'],
            app.app.config['PASSWORD']
        )
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'&lt;Hello&gt;' in rv.data
        assert b'<strong>HTML</strong> allowed here' in rv.data

# Manually test this out by running the server and adding two new entries.
# Click on one of them. It should be removed from the DOM as well as the database
# localhost:5000/delete/1 
    def test_delete_message(self):
        """Ensure the messages are being deleted."""
        rv = self.app.get('/delete/1')
        data = json.loads((rv.data).decode('utf-8'))
        self.assertEqual(data['status'], 1)
 -->