import json
import random
import secrets



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
    
    
        #Prompt
    Genre = ("romance", "comedy", "horror", "thriller", "drama", "sci-fi", "dystopian", "historical romance", "action", "supernatural", "vampire", "werewolf", "alien", "children's", "young adult", "high school")
    mc = ("two brothers", "two sisters", "a divorced couple", "a man and his alien neighbor", "a CEO and his assistant", "a waitress and doctor", "a grandmother and her caretaker", "three cousins", "a couple", "a cheerleader and a amster chess player", "a mother and son", "mob boss and cop", "four friends", "a teacher and the principal", "a doctor and a hidden royal", "a librarian and a single father of two", "a bar owner and their alcohol delieverer", "a mailman and a single mother")
    action = ("run a cartel", "run a small family business", "encounter aliens", "help a lost angel", "search for the fountain of youth", "teach a group of hidden vampires", "explore time and space", "go to the olympics", "meet a ghost", "write a book", "befriend a bear", "befriend a pack of werewolves", "cause a war between two gangs", "fly around the world in search of treasure", "plan a trip to pluto", "fail a being buddy cops", "spy on a group of grandmothers", "break into a bank on accident", "invent a new color", "discover a new category of lizard", "invite Godzilla over for tea", "pretend ot be wizards", "switch places with each other")


    if event["currentIntent"]["name"] == "Prompt":
        result["dialogAction"]["message"]["content"] = ("Here is a prompt: A  " + random.choice(Genre) + " story about " + random.choice(mc) + " who " + random.choice(action) + " and " + random.choice(action) + ".")
        
        
        #Ending
    end = ("lives happily ever after", "runs into the woods, never to be seen again", "turns into a monster", "dies in a fiery rain of bullets", "finds love in a hopeless place", "finds out the relationships cannot be built from stressful situations", "wins the crown", "is reincarnated", "looses the love of their live, promising to never move on", "gets a puppy", "retires and becomes a mail man", "becomes a spy", "learns how to ride a horse", "goes back to college, finishes their degree, and finally becomes a doctor", "realizes their dream of becomeing a prima ballerina", "conquers their fears")

    if event["currentIntent"]["name"] == "Ending":
        result["dialogAction"]["message"]["content"] = ("In the end, the main character " + random.choice(end))
            
            
        #Sidekick
    relationship = ("best friend", "brother", "sister", "grandmother", "dog", "cat", "parrot", "neighbor", "cousin", "friend", "co-worker", "boss", "highschool nemesis", "neighborhood grocery store owner", "karate instructor", "pilot", "teacher" )
    characteristic = ("sings", "dances", "talks", "lies", "steals", "jokes", "runs away", "eats", "cooks", "pranks", "plans", "high fives", "sketches", "writes down everything", "remembers everything", "forgets everything", "gives horrible advice", "talks about themself", "takes control", "mishears information", "ignores the main character", "replies sarcastically")

    if event["currentIntent"]["name"] == "Sidekick":
        result["dialogAction"]["message"]["content"] = ("The main character's sidekick should be their " + random.choice(relationship) + " who always " + random.choice(characteristic) + " and " + random.choice(characteristic))
        
        #Setting
            #time of story
    time = ("modern", "1700s", "1800s", "1900s", "futuristic", "dystopian" )
    place = ("New York", "San Fransisco", "Miami", "Madrid", "Costa Rica", "Cuba", "Puerto Rico", "Sacramento", "Austin, Texas", "Paris", "London", "Rome", "Bangkok", "Singapore", "Hong Kong", "Dubai", "Istanbul", "Tokyo", "Barcelona", "Las Vegas", "Shanghai", "Seoul", "Mumbai", "Taipei")
            #time of year
    TofY = ("Christmas", "football season", "New Years", "spring", "winter", "fall", "summer", "July", "August", "June", "April", "December", "October", "November", "January", "Feburary", "March", "May", "September", "Fourth of July", "Halloween", "Thanksgiving", "the ides of March")
    people = ("a large group of fans", "a hoard of zombies", "no one around", "three different dance mobs", "two fighting gangs", "an evil scientist trying to take over the tri-state area", "some bad acting aliens observing the population", "a famous talking cat")

    if event["currentIntent"]["name"] == "Setting":
        result["dialogAction"]["message"]["content"] = ("It should be set in   " + random.choice(time) + " " + random.choice(place) + ", during " + random.choice(TofY) + ", with " + random.choice(people) + ".")
        
        
        #Character#
    FName = ("Sarah", "Matthew","Jimmy", "Jordan", "Sam", "Kimberly", "Joanna", "Marti", "Michele", "Hanna", "Michael", "Tristian", "Isiah", "Roxanne", "Bernard", "Brian", "Norman", "Matt", "Jake", "Ranelle", "Frankie", "Annie", "Roberta", "Rob", "Mona", "Jackson", "Timothy", "Jasmine", "Beatrice", "Barth", "Roger", "Chris", "Missy", "Vickie", "Walter", "Vanessa", "Rachel", "Nikki", "Steph", "Steven", "Yvann", "Ivan", "Alyssa", "Katie", "Catherine", "Rose", "Andi", "Andy", "Max", " Tony", "Toni", "Millie", "Zachary", "Angel", "Julian", "Bella", "Isabella", "Pat", "Friday", "Wednesday", "Lina", "Rain", "Pheobe", "Penny")
    LName = ("Diaz", "Smith", "Perez", "Johnson", "Williams", "Miller", "Jones", "Davis", "Garcia", "Brown", "Rodriguez", "Wilson", "Martinez", "Taylor", "Anderson", "Hernandez", "Moore", "Pagano", "Greene", "Innocent", "Martin", "Lopez", "Lee", "Harris", "Gonzalez", "Hall", "Lewis", "Robinson", "Walker", "Clark" "Young", "King", "Wright", "Scott", "Torres", "Nguyen", "Allen", "Flores", "Nelson", "Rivera", "Campbell", "Gomez", "Phillips", "Evans", "Turner", "Cruz", "Morris", "Murphy", "Morales", "Cook","Rogers", "Peterson", "Reed", "Bailey", "Howard","Ramos", "Chavez", "Wood", "Bennet", "Cox", "Mendoza", "Price", "Alvarez", "Gray", "Hughes")
    HairColor = ("red", "pink", "purple", "blonde", "blue", "brunette", "green", "gray", "white", "black", "rainbow colored", "blonde with pink stripes", "blonde with pink highlights", "black with blue stipes", "brown with high lights")
    Hairdesc = ("short", "shoulder length", "a bob", "curly", "wavy", "long", "straight", "with bangs", "pixie cut", "with highlights") 
    Likes = ("Basketball", "dogs", "cats", "the color pink", "the color teal", "inventing", "science", "art", "money", "food", "sleep", "dancing", "research", "jumping out of planes", "pranking people", "best friend", "brother", "family", "cooking", "baking", "drawing", "gossiping", "shopping", "acting", "pizza", "ice cream", "high-fives", "rollar coaters", "buddy cop movies")
    Dislikes = ("homework", "Bob", "plants", "bugs", "movies", "legos", "cake", "flash mobs", "people who can't sing", "whistling", "pickles", "fish", "golf", "hecklers", "reality television", "being the butt of the joke" "riding in the back of a car", "long road trips", "lines", "creepy dolls", "peanut butter", "waking up", "alarms", "the heat", "dressed up animals", "loud eating", "stale chips")
    
    if event["currentIntent"]["name"] == "Character":
        result["dialogAction"]["message"]["content"] = ("Your character name should be " + random.choice(FName) + " " + random.choice(LName) + " and they are " +  str(random.choice(range(15, 500))) + " They have " + random.choice(HairColor) + " hair and it is " + random.choice(Hairdesc) + ". They like " + random.choice(Likes) + ", " + random.choice(Likes) + ", and  " + random.choice(Likes) + ". They don't like " + random.choice(Dislikes) + " and " + random.choice(Dislikes))
        

    return result
