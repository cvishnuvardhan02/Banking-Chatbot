import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "I'm sorry, but I am not sure what you are asking. Can you please rephrase your question?...",
                "I'm sorry, but I am not sure what you are asking. Can you please rephrase your question?",
                "What does that mean?"][
        random.randrange(4)]
    return response
import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!\n \n Hey there! Are you curious about this website? \n im an Open AI-powered chatbot here to answer any questions you might have.\n Hello! I am an AI bot here to assist you. \n this website is designed to provide information and answer question on a wide range of topics. \n Feel free to ask me anythig! \n You can ask me any questions. e.g: \n 1.How can i reset my password? \n  2.What are the payment options available?\n  3. Can you provide information on the return policy?" , Im an AI assistant representing the company. How can I assist you today?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('To reset your password, you cn follow these steps: \n  \n 1. Go to the Settings/Security section. \n 2. Look for the rest password link and click on it. \n 3. A recover page should appear where you can enter your new password. \n 4. Enter your new password and confirm it.\n 5. save the changes. \n ifyou encounter any issues with the reset password process, please let us know.', ['how', 'can', 'i', 'reset', 'my', 'password'], required_words=['reset', 'password'])
    response('The payment terms and conditions are as follows: \n \n Optional paid services or upgrades may be available on the Website. \n \n When utilizing an optional paid service or upgrade, you agree to pay Tars the monthly or annual subscription fees indicated.\n \n Payments will be charged on a pre-pay basis on the day you begin utilizing the service or upgrade.\n \n The fees are not refundable.\n \n Unless you notify Tars before the end of the applicable subscription period that you want to cancel a service or upgrade, your subscription will automatically renew.\n \n You authorize us to collect the then-applicable annual or monthly subscription fee (as well as any taxes) using any credit card or other payment mechanism we have on record for you \n \n Subscriptions can be canceled at any time.\n \n Please let me know if you have any other questions.', ['what', 'are', 'the', 'payment', 'options', 'available?'], required_words=['payment', 'options'])
    response('We provide a chatbot for banking FAQs that can answer a wide variety of questions related to banking and finances. However, we do not have information about specific bank branches', ['bank', 'branches'], required_words=['branches'])
    response('To create an account, please follow these steps: \n \n Visit our website and click on the "Sign Up" or "Create Account" button.\n \n Fill out the required information, such as your name, email address, and password. \n \n Review and accept our terms and conditions, if applicable.\n \n Click on the "Create Account" or "Sign Up" button to complete the process.\n \n You may need to verify your email address by clicking on a confirmation link sent to your email.\n \n If you have any further questions or need assistance, please let us know.', ['how', 'can', 'i', 'create', 'a', 'account'], required_words=['create', 'account'])
    response('I am not sure, can you rephrase the question.', ['can', 'you', 'provide', 'information', 'on', 'the', 'return', 'policy'], required_words=['information', 'return', 'policy'])
    
        # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))