faq_responses = {
    "what is phishing": "Phishing is a type of cyber attack where attackers trick you into revealing sensitive information.",
    "how to report cybercrime": "You can report cybercrime at the NCRP India portal: https://cybercrime.gov.in/",
    "what is malware": "Malware is malicious software designed to harm your computer or steal data."
}

def get_response(user_input):
    user_input = user_input.lower()
    for key, value in faq_responses.items():
        if key in user_input:
            return value
    return "I'm not sure. You can also report at NCRP India / FBI IC3 / Europol."
