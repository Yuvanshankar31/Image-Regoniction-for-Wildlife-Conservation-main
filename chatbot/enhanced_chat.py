"""
Enhanced Wildlife Conservation Chatbot
Improved efficiency with comprehensive knowledge base and better pattern matching
"""

import random
import re

# Comprehensive Wildlife Knowledge Base
WILDLIFE_DATABASE = {
    'lion': {
        'name': 'African Lion',
        'scientific': 'Panthera leo',
        'status': 'Vulnerable',
        'habitat': 'Grasslands, savannas, and open woodlands of sub-Saharan Africa',
        'threats': 'Habitat loss, human-wildlife conflict, poaching, trophy hunting',
        'population': 'Approximately 20,000 remaining in the wild (declined by 43% over past 21 years)',
        'diet': 'Carnivore - hunts zebras, wildebeest, buffalo, and other large mammals',
        'lifespan': '10-14 years in wild, up to 20 years in captivity',
        'weight': '190 kg (males), 130 kg (females)',
        'conservation': 'Protected in national parks, anti-poaching efforts, community conservation programs',
        'facts': [
            'Lions are the only cats that live in groups called prides, typically 15 members.',
            'A lion\'s roar can be heard from up to 8 kilometers (5 miles) away.',
            'Female lions do 85-90% of the hunting for the pride.',
            'Male lions sleep up to 20 hours a day.',
            'Lions can run up to 80 km/h (50 mph) in short bursts.'
        ]
    },
    'tiger': {
        'name': 'Bengal Tiger',
        'scientific': 'Panthera tigris tigris',
        'status': 'Endangered',
        'habitat': 'Tropical forests, mangroves, grasslands of India, Bangladesh, Nepal, and Bhutan',
        'threats': 'Poaching for body parts, habitat destruction, human conflict, prey depletion',
        'population': 'Approximately 2,500-3,000 in the wild (India has 70% of world\'s tigers)',
        'diet': 'Carnivore - hunts deer, wild boar, buffalo, and occasionally elephants',
        'lifespan': '8-10 years in wild, up to 20 years in captivity',
        'weight': '220 kg (males), 140 kg (females)',
        'conservation': 'Project Tiger, anti-poaching patrols, habitat corridors, breeding programs',
        'facts': [
            'Tigers are the largest cat species in the world.',
            'Each tiger has a unique stripe pattern, like human fingerprints.',
            'Tigers are excellent swimmers and can swim up to 6 km.',
            'A tiger\'s roar can be heard up to 3 km away.',
            'Tigers can eat up to 40 kg of meat in one sitting.'
        ]
    },
    'elephant': {
        'name': 'African Elephant',
        'scientific': 'Loxodonta africana',
        'status': 'Endangered',
        'habitat': 'Savannas, forests, deserts, and marshes across 37 African countries',
        'threats': 'Poaching for ivory, habitat loss, human-elephant conflict, climate change',
        'population': 'Approximately 415,000 (declined by 30% over 7 years)',
        'diet': 'Herbivore - eats grass, leaves, bark, fruits (300 kg per day)',
        'lifespan': '60-70 years in wild',
        'weight': '6,000 kg (males), 3,000 kg (females)',
        'conservation': 'Ivory trade ban, anti-poaching units, wildlife corridors, community programs',
        'facts': [
            'Elephants are the largest land animals on Earth.',
            'They have excellent memory and can recognize other elephants after decades.',
            'Elephants communicate using infrasound (below human hearing range).',
            'They can detect water sources up to 20 km away.',
            'Elephants mourn their dead and have burial rituals.'
        ]
    },
    'rhino': {
        'name': 'Rhinoceros',
        'scientific': 'Rhinocerotidae (5 species)',
        'status': 'Critically Endangered',
        'habitat': 'Grasslands, savannas, tropical forests of Africa and Asia',
        'threats': 'Poaching for horns (traditional medicine), habitat loss, political instability',
        'population': 'Approximately 27,000 total (White: 18,000, Black: 5,600, Indian: 3,700, Javan: 74, Sumatran: 80)',
        'diet': 'Herbivore - grass, leaves, shoots, fruits',
        'lifespan': '35-50 years',
        'weight': '800-3,600 kg depending on species',
        'conservation': 'Armed guards, dehorning programs, breeding sanctuaries, translocation',
        'facts': [
            'Rhino horns are made of keratin, same as human hair and nails.',
            'Despite their size, rhinos can run 30-40 mph (50-65 km/h).',
            'White rhinos are actually gray - name comes from Afrikaans "wijd" (wide).',
            'Rhinos have poor eyesight but excellent hearing and smell.',
            'A rhino horn can grow 3 inches per year.'
        ]
    },
    'panda': {
        'name': 'Giant Panda',
        'scientific': 'Ailuropoda melanoleuca',
        'status': 'Vulnerable',
        'habitat': 'Bamboo forests of central China (Sichuan, Shaanxi, Gansu provinces)',
        'threats': 'Habitat fragmentation, low birth rate, climate change affecting bamboo',
        'population': 'Approximately 1,864 in wild, 600 in captivity (increasing)',
        'diet': 'Herbivore - 99% bamboo (12-38 kg per day), occasionally small animals',
        'lifespan': '15-20 years in wild, 30 years in captivity',
        'weight': '100-115 kg (males), 70-100 kg (females)',
        'conservation': 'Breeding programs, habitat corridors, 67 panda reserves in China',
        'facts': [
            'Pandas spend 12-16 hours a day eating bamboo.',
            'Newborn pandas are about the size of a stick of butter (100g)!',
            'Pandas have a "pseudo-thumb" - an enlarged wrist bone for gripping bamboo.',
            'They can poop up to 40 times a day.',
            'Pandas are excellent tree climbers despite their size.'
        ]
    },
    'gorilla': {
        'name': 'Mountain Gorilla',
        'scientific': 'Gorilla beringei beringei',
        'status': 'Endangered',
        'habitat': 'Mountain forests of Central Africa (Rwanda, Uganda, DR Congo)',
        'threats': 'Habitat loss, poaching, disease (especially from humans), civil unrest',
        'population': 'Approximately 1,063 (increased from 680 in 2008)',
        'diet': 'Herbivore - leaves, shoots, stems, bamboo, fruits, insects',
        'lifespan': '35-40 years in wild, 50+ in captivity',
        'weight': '195 kg (males), 100 kg (females)',
        'conservation': 'Gorilla tourism, veterinary care, anti-poaching patrols, habitat protection',
        'facts': [
            'Gorillas share 98.3% of their DNA with humans.',
            'They can learn sign language and use tools.',
            'Silverback males can lift 10 times their body weight.',
            'Gorillas live in family groups led by a dominant silverback.',
            'They build new nests every night for sleeping.'
        ]
    },
    'leopard': {
        'name': 'Snow Leopard',
        'scientific': 'Panthera uncia',
        'status': 'Vulnerable',
        'habitat': 'Mountain ranges of Central and South Asia (12 countries, 3,000-5,500m altitude)',
        'threats': 'Poaching, habitat loss, climate change, human-wildlife conflict, prey decline',
        'population': 'Approximately 4,000-6,500 in wild',
        'diet': 'Carnivore - blue sheep, ibex, marmots, hares, birds',
        'lifespan': '15-18 years in wild, 21 years in captivity',
        'weight': '30-55 kg',
        'conservation': 'Community-based conservation, livestock insurance, protected areas',
        'facts': [
            'Snow leopards can jump up to 15 meters (50 feet) in a single leap.',
            'Their thick fur and tail help survive temperatures as low as -40°C.',
            'They are solitary and extremely elusive - rarely seen in wild.',
            'Their large paws act like natural snowshoes.',
            'They cannot roar but make a unique "chuffing" sound.'
        ]
    },
    'bear': {
        'name': 'Polar Bear',
        'scientific': 'Ursus maritimus',
        'status': 'Vulnerable',
        'habitat': 'Arctic ice, coastal areas of Arctic Ocean (5 countries: US, Canada, Russia, Greenland, Norway)',
        'threats': 'Climate change (sea ice loss), pollution, oil development, hunting',
        'population': 'Approximately 22,000-31,000 (declining)',
        'diet': 'Carnivore - primarily ringed and bearded seals, also fish, birds, eggs',
        'lifespan': '25-30 years in wild',
        'weight': '450-680 kg (males), 150-250 kg (females)',
        'conservation': 'International agreements, hunting quotas, protected areas, climate action',
        'facts': [
            'Polar bears are the largest land carnivores.',
            'They can swim continuously for days, covering hundreds of miles.',
            'Their fur is transparent, not white - appears white due to light reflection.',
            'They have black skin underneath to absorb heat.',
            'Polar bears can smell seals up to 1 km away through 1m of ice.'
        ]
    },
    'cheetah': {
        'name': 'Cheetah',
        'scientific': 'Acinonyx jubatus',
        'status': 'Vulnerable',
        'habitat': 'Grasslands and savannas of Africa and Iran',
        'threats': 'Habitat loss, human-wildlife conflict, illegal pet trade, low genetic diversity',
        'population': 'Approximately 7,000 in wild',
        'diet': 'Carnivore - gazelles, impalas, hares, birds',
        'lifespan': '8-12 years in wild, 17 years in captivity',
        'weight': '40-65 kg',
        'conservation': 'Breeding programs, livestock guarding dogs, protected corridors',
        'facts': [
            'Cheetahs are the fastest land animals, reaching 120 km/h (75 mph).',
            'They can accelerate from 0 to 100 km/h in just 3 seconds.',
            'Unlike other big cats, cheetahs cannot roar but purr like house cats.',
            'They have distinctive "tear marks" from eyes to mouth.',
            'Cheetahs hunt during the day to avoid larger predators.'
        ]
    },
    'orangutan': {
        'name': 'Orangutan',
        'scientific': 'Pongo (3 species)',
        'status': 'Critically Endangered',
        'habitat': 'Rainforests of Borneo and Sumatra',
        'threats': 'Deforestation (palm oil), illegal pet trade, hunting, forest fires',
        'population': 'Approximately 104,700 Bornean, 13,800 Sumatran, 800 Tapanuli',
        'diet': 'Omnivore - fruits (especially durian), leaves, bark, insects, eggs',
        'lifespan': '35-45 years in wild, 60 years in captivity',
        'weight': '50-90 kg (males), 30-50 kg (females)',
        'conservation': 'Reforestation, sustainable palm oil, rescue centers, protected areas',
        'facts': [
            'Orangutans share 97% of DNA with humans.',
            'They are the largest tree-dwelling animals.',
            'Orangutans use tools and have been observed making umbrellas from leaves.',
            'They have the longest childhood of any animal except humans (7-8 years).',
            'Males develop large cheek pads called "flanges" when mature.'
        ]
    }
}

# Conservation topics
CONSERVATION_INFO = {
    'help': """🌿 **How You Can Help Wildlife Conservation:**

1. **Support Conservation Organizations**
   - Donate to WWF, Wildlife Conservation Society, local wildlife trusts
   - Adopt an animal symbolically

2. **Reduce Your Environmental Impact**
   - Lower carbon footprint (climate change affects habitats)
   - Use sustainable products (FSC-certified wood, sustainable palm oil)
   - Reduce plastic use (ocean pollution)

3. **Make Ethical Choices**
   - Don't buy products from endangered species (ivory, fur, exotic pets)
   - Choose eco-tourism that supports conservation
   - Eat sustainably (avoid overfished species)

4. **Spread Awareness**
   - Educate others about endangered species
   - Share conservation news on social media
   - Participate in citizen science projects

5. **Support Policy Changes**
   - Vote for leaders who prioritize environment
   - Sign petitions for wildlife protection
   - Support stronger anti-poaching laws

6. **Volunteer**
   - Join local conservation groups
   - Participate in habitat restoration
   - Help with wildlife surveys

**Every action counts! 🦁🌍**""",
    
    'threats': """⚠️ **Major Threats to Wildlife:**

1. **Habitat Loss** (Biggest threat)
   - Deforestation for agriculture
   - Urban development
   - Mining and resource extraction

2. **Poaching & Illegal Wildlife Trade**
   - Ivory, rhino horn, tiger parts
   - Exotic pet trade
   - $20 billion illegal industry

3. **Climate Change**
   - Habitat shifts
   - Food source changes
   - Extreme weather events

4. **Human-Wildlife Conflict**
   - Competition for resources
   - Livestock predation
   - Crop raiding

5. **Pollution**
   - Plastic in oceans
   - Chemical contamination
   - Air and water pollution

6. **Disease**
   - Spread from domestic animals
   - Reduced genetic diversity
   - Pandemic impacts

**We must act now to protect our planet's biodiversity! 🌍**""",
    
    'success': """✅ **Conservation Success Stories:**

1. **Giant Panda** - Downgraded from Endangered to Vulnerable
   - Population increased from 1,000 to 1,864
   - 67 panda reserves established

2. **Mountain Gorilla** - Population growing
   - Increased from 680 (2008) to 1,063 (2021)
   - Gorilla tourism funding conservation

3. **Southern White Rhino** - Saved from near extinction
   - Recovered from <100 (1900s) to 18,000 today
   - Intensive protection worked

4. **Humpback Whale** - Removed from endangered list
   - Population recovered from 5,000 to 135,000
   - Whaling ban was crucial

5. **Bald Eagle** - Recovered in USA
   - From 417 pairs (1963) to 71,400 pairs (2021)
   - DDT ban and protection laws

**Conservation works when we commit to it! 🎉**"""
}

# Greeting patterns
GREETING_PATTERNS = [
    r'\b(hi|hello|hey|greetings|good\s+(morning|afternoon|evening))\b',
    r'^(yo|sup|howdy)',
]

# Farewell patterns
FAREWELL_PATTERNS = [
    r'\b(bye|goodbye|see\s+you|farewell|later|cya)\b',
]

def enhanced_get_response(message):
    """
    Enhanced chatbot with better pattern matching and comprehensive responses
    """
    message_lower = message.lower().strip()
    
    # Remove punctuation for better matching
    clean_message = re.sub(r'[^\w\s]', '', message_lower)
    
    # Greetings
    if any(re.search(pattern, message_lower) for pattern in GREETING_PATTERNS):
        greetings = [
            "Hello! 🦁 I'm your wildlife conservation assistant. I can tell you about endangered species, conservation efforts, and how you can help. What would you like to know?",
            "Hi there! 🌿 Ask me about lions, tigers, elephants, rhinos, pandas, gorillas, leopards, bears, cheetahs, or orangutans!",
            "Welcome! 🐯 I'm here to help you learn about endangered wildlife and conservation. What interests you?"
        ]
        return random.choice(greetings)
    
    # Farewells
    if any(re.search(pattern, message_lower) for pattern in FAREWELL_PATTERNS):
        farewells = [
            "Goodbye! Remember, every action counts in wildlife conservation! 🌍🦁",
            "Take care! Stay wild and help protect our planet's amazing creatures! 🌿",
            "See you later! Don't forget to spread awareness about endangered species! 🐯✨"
        ]
        return random.choice(farewells)
    
    # Help/capabilities
    if any(word in clean_message for word in ['help', 'what can you do', 'capabilities', 'features']):
        return """🤖 **I can help you with:**

📚 **Animal Information** - Detailed facts about 10 endangered species
🔴 **Conservation Status** - Current endangerment levels
🌍 **Habitat & Range** - Where animals live
📊 **Population Data** - Current numbers and trends
⚠️ **Threats** - What endangers these species
💡 **Fun Facts** - Interesting trivia
🛡️ **Conservation Efforts** - How we're helping
🌿 **How to Help** - Actions you can take

**Available Animals:**
Lions, Tigers, Elephants, Rhinos, Pandas, Gorillas, Snow Leopards, Polar Bears, Cheetahs, Orangutans

**Try asking:**
- "Tell me about tigers"
- "Are rhinos endangered?"
- "How can I help?"
- "Conservation success stories"
- "What threatens wildlife?"

What would you like to know? 🦁"""
    
    # Conservation help
    if any(phrase in clean_message for phrase in ['how can i help', 'what can i do', 'help conservation', 'protect wildlife', 'save animals']):
        return CONSERVATION_INFO['help']
    
    # Threats
    if any(phrase in clean_message for phrase in ['threat', 'danger', 'why endangered', 'what threatens', 'problems facing']):
        return CONSERVATION_INFO['threats']
    
    # Success stories
    if any(phrase in clean_message for phrase in ['success', 'good news', 'positive', 'recovery', 'saved']):
        return CONSERVATION_INFO['success']
    
    # List animals
    if any(phrase in clean_message for phrase in ['list', 'which animals', 'what animals', 'all animals', 'available species']):
        animals = ', '.join([data['name'] for data in WILDLIFE_DATABASE.values()])
        return f"🦁 **I have detailed information about these endangered species:**\n\n{animals}\n\nWhat would you like to learn about?"
    
    # Check for animal mentions with enhanced matching
    detected_animal = None
    for animal_key, animal_data in WILDLIFE_DATABASE.items():
        # Check for animal name or scientific name
        if (animal_key in clean_message or 
            animal_data['name'].lower() in message_lower or
            animal_data['scientific'].lower() in message_lower):
            detected_animal = (animal_key, animal_data)
            break
    
    if detected_animal:
        animal_key, animal_data = detected_animal
        
        # Specific queries
        if any(word in clean_message for word in ['status', 'endangered', 'conservation status', 'how endangered']):
            return f"""🔴 **{animal_data['name']} Conservation Status**

**Status:** {animal_data['status']}
**Scientific Name:** {animal_data['scientific']}

**Population:** {animal_data['population']}

**Main Threats:**
{animal_data['threats']}

**Conservation Efforts:**
{animal_data['conservation']}

The situation is serious but there's hope with continued conservation efforts! 🌿"""
        
        elif any(word in clean_message for word in ['habitat', 'live', 'where', 'location', 'range', 'found']):
            return f"""🌍 **{animal_data['name']} Habitat**

**Location:** {animal_data['habitat']}

**Diet:** {animal_data['diet']}

**Lifespan:** {animal_data['lifespan']}

**Weight:** {animal_data['weight']}

These magnificent creatures need our help to preserve their natural habitats! 🌿"""
        
        elif any(word in clean_message for word in ['population', 'how many', 'number', 'count', 'left']):
            return f"""📊 **{animal_data['name']} Population**

**Current Population:** {animal_data['population']}

**Status:** {animal_data['status']}

**Trend:** The population is under threat from {animal_data['threats'].lower()}

**Conservation:** {animal_data['conservation']}

Every individual matters! Support conservation efforts to help these animals thrive. 🦁"""
        
        elif any(word in clean_message for word in ['fact', 'interesting', 'cool', 'amazing', 'fun']):
            facts_list = '\n'.join([f"• {fact}" for fact in animal_data['facts']])
            return f"""💡 **Amazing {animal_data['name']} Facts:**

{facts_list}

Aren't they incredible? Let's work together to protect them! 🌟"""
        
        elif any(word in clean_message for word in ['diet', 'eat', 'food', 'prey']):
            return f"""🍽️ **{animal_data['name']} Diet**

{animal_data['diet']}

**Lifespan:** {animal_data['lifespan']}

Their diet and habitat are closely connected to their survival! 🌿"""
        
        elif any(word in clean_message for word in ['weight', 'size', 'how big', 'how heavy']):
            return f"""📏 **{animal_data['name']} Size**

**Weight:** {animal_data['weight']}

**Lifespan:** {animal_data['lifespan']}

**Habitat:** {animal_data['habitat']}

These magnificent creatures are truly impressive! 🦁"""
        
        # General comprehensive info
        else:
            fact = random.choice(animal_data['facts'])
            return f"""🦁 **{animal_data['name']}** ({animal_data['scientific']})

📍 **Status:** {animal_data['status']}
🌍 **Habitat:** {animal_data['habitat']}
📊 **Population:** {animal_data['population']}
⚠️ **Threats:** {animal_data['threats']}
🍽️ **Diet:** {animal_data['diet']}
⏱️ **Lifespan:** {animal_data['lifespan']}
⚖️ **Weight:** {animal_data['weight']}

🛡️ **Conservation Efforts:**
{animal_data['conservation']}

💡 **Fun Fact:** {fact}

Want to know more? Ask about their habitat, population, or how you can help! 🌿"""
    
    # General conservation questions
    if any(word in clean_message for word in ['conservation', 'protect', 'save']):
        return CONSERVATION_INFO['help']
    
    # Endangered species general
    if 'endangered' in clean_message or 'extinction' in clean_message:
        return """🔴 **Endangered Species Information**

An endangered species is at risk of extinction. Categories include:

• **Critically Endangered** - Extremely high risk (e.g., Rhinos, Orangutans)
• **Endangered** - High risk (e.g., Tigers, Elephants, Gorillas)
• **Vulnerable** - Moderate risk (e.g., Lions, Pandas, Polar Bears, Cheetahs, Snow Leopards)

**Main causes of endangerment:**
- Habitat loss
- Poaching
- Climate change
- Human-wildlife conflict
- Pollution

Ask me about specific animals to learn more! 🦁"""
    
    # Thank you
    if any(word in clean_message for word in ['thank', 'thanks', 'appreciate']):
        return "You're welcome! 🌿 Feel free to ask me anything else about wildlife conservation! Together we can make a difference! 🦁"
    
    # Default - suggest topics
    return """I'd love to help you learn about wildlife! 🦁

**Try asking me:**
• "Tell me about tigers" - Get detailed species info
• "Are rhinos endangered?" - Conservation status
• "Where do elephants live?" - Habitat information
• "How many pandas are left?" - Population data
• "Fun facts about lions" - Interesting trivia
• "How can I help?" - Conservation actions
• "List all animals" - See available species
• "Conservation success stories" - Positive news

What would you like to know? 🌿"""

if __name__ == "__main__":
    print("🦁 Enhanced Wildlife Conservation Chatbot")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot:", enhanced_get_response("goodbye"))
            break
        
        response = enhanced_get_response(user_input)
        print("\nBot:", response)
        print()
