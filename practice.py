# @app.route("/")
# def hello_tal():
#    return "<h1>Hello, Tal!</h1>"


# @app.route("/list")
# def contact_list():
#    return f"{my_contacts}"


# @app.route("/Contact<int:usernumber>")
# def show_contact(usernumber):
#    return f"user is {usernumber}"


# @app.route("/Full")
# def hello_fullsite():
#     return """
#     <html>
#         <head>
#             <title>Hello Tal Page</title>
#         </head>
#         <body>
#             <h1>Hello, Tal!</h1>
#             <p>Welcome to my website.</p>
#             <button onclick="location.href='/Add'">Go To Add</button>
#             <button onclick="location.href='/Contact'">Go To Contact</button>
#             <input>
#             <div>
#                 <h2>About Me</h2>
#                 <p>This is a brief introduction about myself.</p>
#             </div>
#             <footer>
#                 <p>Contact me at <a href="mailto:tal@example.com">tal@example.com</a></p>
#             </footer>
#         </body>
#     </html>
#     """

# @app.route("/Main")
# def hello():
#     return '''
#     <form action="/shown" method="POST">
#         <label for="showContact">Add a contact:</label>
#         <input type="text" id="showContact" name="showContact">
#         <button type="submit">Enter</button>
#     </form>
#     '''


# @app.route("/shown", methods=['POST'])
# def shown():
#     show_contact = request.form.get('showContact')
#     return f"<h2>{show_contact}</h2>"
