
import spacy

def getAction(doc):
    for token in doc:
        if (token.tag_ == u'VB') :
            return token.text
    return ""

def getObject(doc):
    for token in doc:
        if (token.dep_ == u'dobj') :
            return token.text
    return ""
    
action_reserve_synonyms = set([u'book', u'reserve', u'make', u'have'])
object_room_synonyms = set([u'hotel', u'room', u'inn', u'motel', u'reservation'])


nlp = spacy.load('en_core_web_sm')


#while (True):
#   query = input("Hello. What can I do for you today? ")

def bookHotel(command) : 
   reply = "Hello. What can I do for you today? "

   #doc = nlp(u'I want to reserve a hotel room')
   doc = nlp(command);
            
#   for token in doc:
#       print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)

   action = getAction(doc);
   actionObject = getObject(doc);
#   print("Action is " + getAction(doc));
#   print("Object is " + getObject(doc));

   if ((action == '') or (actionObject == '')):
       reply = "I didn't get you. Can you please rephrase?"
   elif (action in action_reserve_synonyms): 
       if (actionObject in object_room_synonyms):
           reply = "Booking a room for you Sir!"
       else:
           reply = "We don't support " + action + " on " + actionObject
   else:
       reply = "We don't support doing " + action

   return reply
