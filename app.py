from flask import Flask, request
from flask import render_template

app = Flask(__name__)



my_contacts = [
    {
        "name": "Ran",
        "age": 44,
        "phone": "0500000000",
        "email": "coco@coco.coco",
        "favorite": True,
    },
    {
        "name": "Itzik",
        "age": 21,
        "phone": "0511111111",
        "email": "koko@koko.koko",
        "favorite": False
    },
]

@app.route('/Hello')
def favorite():
    favorite_contacts = [contact for contact in my_contacts if contact['favorite']]
    if favorite_contacts:
        return render_template('single_contact.html', my_contacts=favorite_contacts)
    else:
        return 'No Contact Found'



# @app.route('/')
# def contacts():
#         return render_template('contact_list.html', contacts = my_contacts)
    


# @app.route("/")
# def contacts_list():
#         return render_template('contact_list.html', contacts = my_contacts)

    # final_html_str = ""
    # for contact in my_contacts:
    #     final_html_str += f"{contact['name']} <br> {contact['age']} <br> {contact['phone']} <br> {contact['email']}"
    # return final_html_str


@app.route("/contacts/<int:index>")
def single_contact(index):
    return f"<h2>The user is: {my_contacts[index]['name']} <br> Age: {my_contacts[index]['age']} <br> Phone: {my_contacts[index]['phone']} <br> Email: {my_contacts[index]['email']}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
