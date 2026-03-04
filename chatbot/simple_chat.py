"""
Simple fallback chatbot for wildlife conservation
Works without NLTK or ML models
"""

import random

# Wildlife knowledge base
WILDLIFE_DATA = {
    'lion': {
        'name': 'African Lion',
        'scientific': 'Panthera leo',
        'status': 'Vulnerable',
        'habitat': 'Grasslands and savannas of Africa',
        'threats': 'Habitat loss, human-wildlife conflict, poaching',
        'population': 'Approximately 20,000 remaining in the wild',
        'facts': [
            'Lions are the only cats that live in groups called prides.',
            'A lion\'s roar can be heard from up to 5 miles away.',
            'Female lions do most of the hunting for the pride.'
        ]
    },
    'tiger': {
        'name': 'Bengal Tiger',
        'scientific': 'Panthera tigris',
        'status': 'Endangered',
        'habitat': 'Tropical forests, mangroves, and grasslands of India and Bangladesh',
        'threats': 'Poaching, habitat destruction, human conflict',
        'population': 'Approximately 2,500 remaining in the wild',
        'facts': [
            'Tigers are the largest cat species in the world.',
            'Each tiger has a unique stripe pattern, like human fingerprints.',
            'Tigers are excellent swimmers and enjoy bathing in water.'
        ]
    },
    'elephant': {
        'name': 'African Elephant',
        'scientific': 'Loxodonta africana',
        'status': 'Endangered',
        'habitat': 'Savannas, forests, and deserts of Africa',
        'threats': 'Poaching for ivory, habitat loss, human conflict',
        'population': 'Approximately 415,000 remaining',
        'facts': [
            'Elephants are the largest land animals on Earth.',
            'They have excellent memory and can recognize other elephants after years apart.',
            'Elephants communicate using infrasound, which humans cannot hear.'
        ]
    },
    'rhino': {
        'name': 'Rhinoceros',
        'scientific': 'Rhinocerotidae',
        'status': 'Critically Endangered',
        'habitat': 'Grasslands and savannas of Africa and Asia',
        'threats': 'Poaching for horns, habitat loss',
        'population': 'Approximately 27,000 remaining (all species combined)',
        'facts': [
            'Rhino horns are made of keratin, the same material as human hair and nails.',
            'Despite their size, rhinos can run up to 30-40 mph.',
            'White rhinos are actually gray - the name comes from the Afrikaans word "wijd" meaning wide.'
        ]
    },
    'panda': {
        'name': 'Giant Panda',
        'scientific': 'Ailuropoda melanoleuca',
        'status': 'Vulnerable',
        'habitat': 'Bamboo forests of central China',
        'threats': 'Habitat loss, low birth rate',
        'population': 'Approximately 1,800 in the wild',
        'facts': [
            'Pandas spend 12-16 hours a day eating bamboo.',
            'Despite being classified as carnivores, 99% of their diet is bamboo.',
            'Newborn pandas are about the size of a stick of butter!'
        ]
    },
    'gorilla': {
        'name': 'Mountain Gorilla',
        'scientific': 'Gorilla beringei',
        'status': 'Endangered',
        'habitat': 'Mountain forests of Central Africa',
        'threats': 'Habitat loss, poaching, disease',
        'population': 'Approximately 1,000 remaining',
        'facts': [
            'Gorillas share 98.3% of their DNA with humans.',
            'They are highly intelligent and can learn sign language.',
            'Gorillas live in family groups led by a dominant silverback male.'
        ]
    },
    'leopard': {
        'name': 'Snow Leopard',
        'scientific': 'Panthera uncia',
        'status': 'Vulnerable',
        'habitat': 'Mountain ranges of Central and South Asia',
        'threats': 'Poaching, habitat loss, climate change',
        'population': 'Approximately 4,000-6,500 remaining',
        'facts': [
            'Snow leopards can jump up to 50 feet in a single leap.',
            'Their thick fur and tail help them survive in temperatures as low as -40°F.',
            'They are solitary animals and rarely seen in the wild.'
        ]
    },
    'bear': {
        'name': 'Polar Bear',
        'scientific': 'Ursus maritimus',
        'status': 'Vulnerable',
        'habitat': 'Arctic ice and coastal areas',
        'threats': 'Climate change, habitat loss, pollution',
        'population': 'Approximately 22,000-31,000 remaining',
        'facts': [
            'Polar bears are the largest land carnivores.',
            'They can swim for days at a time covering hundreds of miles.',
            'Their fur is actually transparent, not white - it appears white due to light reflection.'
        ]
    }
}

# Response patterns
GREETINGS = [
    "Hello! I'm here to help you learn about endangered wildlife. What would you like to know?",
    "Hi there! Ask me about any endangered species!",
    "Welcome! I can tell you about lions, tigers, elephants, rhinos, pandas, gorillas, leopards, and polar bears. What interests you?"
]

FAREWELLS = [
    "Goodbye! Remember to help protect our wildlife! 🌿",
    "Take care! Every action counts in conservation!",
    "See you later! Stay wild! 🦁"
]

UNKNOWN_RESPONSES = [
    "I'm not sure about that. Try asking about lions, tigers, elephants, rhinos, pandas, gorillas, leopards, or polar bears!",
    "I specialize in endangered species. Ask me about specific animals like tigers, elephants, or rhinos!",
    "Could you ask about a specific animal? I know about lions, tigers, elephants, pandas, and more!"
]

def simple_get_response(message):
    """
    Simple pattern-matching chatbot for wildlife information
    """
    message = message.lower().strip()
    
    # Greetings
    if any(word in message for word in ['hello', 'hi', 'hey', 'greetings']):
        return random.choice(GREETINGS)
    
    # Farewells
    if any(word in message for word in ['bye', 'goodbye', 'see you', 'farewell']):
        return random.choice(FAREWELLS)
    
    # Help
    if 'help' in message or 'what can you do' in message:
        return "I can provide information about endangered species including their conservation status, habitat, threats, and interesting facts. Try asking about lions, tigers, elephants, rhinos, pandas, gorillas, leopards, or polar bears!"
    
    # Check for animal mentions
    for animal_key, animal_data in WILDLIFE_DATA.items():
        if animal_key in message or animal_data['name'].lower() in message:
            
            # Status query
            if any(word in message for word in ['status', 'endangered', 'conservation', 'threat']):
                return f"🔴 {animal_data['name']} ({animal_data['scientific']}) is classified as {animal_data['status']}. Main threats include: {animal_data['threats']}. Population: {animal_data['population']}."
            
            # Habitat query
            elif any(word in message for word in ['habitat', 'live', 'where', 'location']):
                return f"🌍 {animal_data['name']} lives in {animal_data['habitat']}."
            
            # Population query
            elif any(word in message for word in ['population', 'how many', 'number', 'count']):
                return f"📊 {animal_data['name']}: {animal_data['population']}. Status: {animal_data['status']}."
            
            # Facts query
            elif any(word in message for word in ['fact', 'interesting', 'tell me', 'about']):
                fact = random.choice(animal_data['facts'])
                return f"🦁 {animal_data['name']} fact: {fact}"
            
            # General info
            else:
                return f"🦁 **{animal_data['name']}** ({animal_data['scientific']})\n\n" \
                       f"📍 Status: {animal_data['status']}\n" \
                       f"🌍 Habitat: {animal_data['habitat']}\n" \
                       f"⚠️ Threats: {animal_data['threats']}\n" \
                       f"📊 Population: {animal_data['population']}\n\n" \
                       f"💡 Fun fact: {random.choice(animal_data['facts'])}"
    
    # Conservation query
    if any(word in message for word in ['conservation', 'protect', 'save', 'help']):
        return "🌿 You can help wildlife conservation by:\n" \
               "• Supporting conservation organizations\n" \
               "• Reducing your carbon footprint\n" \
               "• Avoiding products made from endangered species\n" \
               "• Spreading awareness about wildlife protection\n" \
               "• Supporting sustainable practices"
    
    # List animals
    if 'list' in message or 'which animals' in message:
        animals = ', '.join([data['name'] for data in WILDLIFE_DATA.values()])
        return f"I can tell you about these endangered species: {animals}. What would you like to know?"
    
    # Default response
    return random.choice(UNKNOWN_RESPONSES)

if __name__ == "__main__":
    print("Simple Wildlife Chatbot")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot:", random.choice(FAREWELLS))
            break
        
        response = simple_get_response(user_input)
        print("Bot:", response)
        print()
