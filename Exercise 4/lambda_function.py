import json
import random
import markovify


def lambda_handler(event, context):

    # TODO implement
    result = {
        "dialogAction":
        {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText"
            }
        }
    }
    import secrets
    title = ["Pride and Prejudice", "I Know Why the Caged Bird Sings", "Grapes of Wrath", "Perks of Being a Wallflower", "To Kill a Mockingbird", "Alice's Adventure in Wonderland", "Of Mice and Men", "The Little Princess", "Sense and Sensibility", "The Lord of the Rings", "The Book Thief", "The Fault in Our Stars", "A Wrinkle in Time", "The Road", "Tangerine", "Charlotte's Web", "The Sun Also Rises", "Call of the Wild", "The Importance of Being Earnest", "Life of Pi", "The Notebook", "The Hate U Give", "Hatchet", "Animal Farm", "Bridge to Terabithia", "Holes", "Wonder", "The Kite Runner", "Fried Green Tomatoes at the Whistle Stop Cafe", "Emma", "My Sister's Keeper", "The Giver", "Marley and Me", "Frankenstein", "Carrie", "The Shining", "Dracula", "Coraline", "The Picture of Dorian Gray", "The Tell-Tale Heart", "Peter Pan", "The House of Usher", "Brave New World", "Fahrenheit 451", "The Handmaiden's Tale", "Game of Thrones", "Into the Wild", "The Diary of Anne Frank", "The Green Mile"]
    if event["currentIntent"]["name"] == "Books":
        result["dialogAction"]["message"]["content"] = (secrets.choice(title))
    show = ["Attack on Titan", "Naruto", "Naruto: Shippuden", "Boruto: Naruto Next Generations", "Death Note", "Sword of the Stranger", "Natsume's Book of Friends", "Full Metal Alchemist: Brotherhood", "One Punch Man", "My Hero Academia", "Cowboy Bebop", "Magi Series", "Erased", "Yuri on Ice", "Sword Art Online", "Haikyu", "Bleach", "One Piece", "Tokyo Ghoul", "Black Torch", "Jujitsu Kaisen", "Your Lie in April", "Akudama Drive", "High Rise Invasion", "Pokemon: Indigo Leauge", "Pokemon: Adventures in the Orange Islands", "Pokemon: The Johto Journeys", "Pokemon: Johto League Champions", "Pokemon: Master Quest"]
    if event["currentIntent"]["name"] == "Animes":
        result["dialogAction"]["message"]["content"] = (secrets.choice(show))
    games = ["Mass Effect", "God of War", "Heavenly Sword", "Horizon Zero Dawn", "Last of Us", "Spider Man","Death Stranding"]
    if event["currentIntent"]["name"] == "Video Games":
        result["dialogAction"]["message"]["content"] = (secrets.choice(games))
    
    elif event["currentIntent"]["name"] == "RandomNumber":
        upper = event["currentIntent"]["slots"]["upper"]
        lower = event["currentIntent"]["slots"]["lower"]
        # Do the intent 1
        randomNum = str(random.randint(lower, upper))
        result["dialogAction"]["message"]["content"] = "Your random number is " + randomNum
        if event["sessionAttributes"]:
            result["dialogAction"]["message"]["content"] += ". The last random number was " + \
                event["sessionAttributes"]["lastNumber"]
        result["sessionAttributes"] = {
            "lastNumber": randomNum,
            "lower": event["currentIntent"]["slots"]["lower"],
            "upper": event["currentIntent"]["slots"]["upper"]}
    elif event["currentIntent"]["name"] == "AskAusten":
        with open("./austen-pride-and-prejudice.txt") as f:
            text = f.read()
            # Build the model.
            text_model = markovify.Text(text)
            sentences = []
            # Print five randomly-generated sentences
            for i in range(5):
                # Print three randomly-generated sentences of no more than 280 characters
                sentences.append(text_model.make_sentence())
            result["dialogAction"]["message"]["content"] = ". ".join(sentences)
    elif event["currentIntent"]["name"] == "AddNumbers":
        # Handle intent 2
        result["dialogAction"]["message"]["content"] = upper+lower
    return result
