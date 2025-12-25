# Rule-Based Chatbot with Enhanced Semantic Intelligence
# CODSOFT Task 1
# Author: Gauri

# Semantic dictionary (concept → related words/phrases)
semantic_map = {
    "greeting": ["hello", "hi", "hey"],
    "status": ["how are you", "how r you", "how do you do"],
    "identity": ["who are you", "your name", "what are you"],
    "capability": ["what can you do", "your work", "your purpose"],
    "exit": ["bye", "goodbye", "exit", "quit"]
}

# Responses for each concept
responses = {
    "greeting": "Hello! How can I help you today?",
    "status": "I am doing well. Thanks for asking!",
    "identity": "I am a rule-based chatbot created for the CODSOFT internship.",
    "capability": "I can respond to user queries using semantic rule-based logic.",
    "exit": "Goodbye! Have a great day 😊",
    "unknown": "Sorry, I didn't fully understand that. Can you rephrase?"
}

# Store last detected concept (basic context memory)
last_concept = None


def detect_concept(user_input):
    """
    Detects the most relevant concept
    using keyword scoring instead of first match
    """
    user_input = user_input.lower()
    concept_scores = {}

    for concept, words in semantic_map.items():
        score = 0
        for word in words:
            if word in user_input:
                score += 1
        if score > 0:
            concept_scores[concept] = score

    # Return concept with highest score
    if concept_scores:
        return max(concept_scores, key=concept_scores.get)

    return "unknown"


def get_response(concept):
    """
    Generates response based on detected concept
    and simple context awareness
    """
    global last_concept

    # Context-based response example
    if concept == "status" and last_concept == "greeting":
        response = "I'm doing well 😊 How about you?"
    else:
        response = responses.get(concept, responses["unknown"])

    last_concept = concept
    return response
