# ======================================
# 🧠 CAREER GUIDANCE CHATBOT USING PYDATALOG (ENHANCED VERSION)
# ======================================

from pyDatalog import pyDatalog
import time

pyDatalog.clear()

# Create logic terms
pyDatalog.create_terms('Career, Field, Skill, Interest, Education, suggest_career, has_interest, has_skill, has_education')

# -------------------------------
# ✅ Define Careers
# -------------------------------
careers = [
    'Software Engineer', 'Data Scientist', 'AI Engineer', 'Web Developer', 'Cybersecurity Analyst',
    'Mechanical Engineer', 'Civil Engineer', 'Electrical Engineer', 'Doctor', 'Nurse', 'Teacher', 'Professor',
    'Digital Marketer', 'Graphic Designer', 'Product Manager', 'Game Developer', 'Business Analyst',
    'Financial Analyst', 'Lawyer', 'Psychologist', 'Journalist', 'Architect', 'UI/UX Designer',
    'Cloud Engineer', 'DevOps Engineer', 'Mobile App Developer', 'Blockchain Developer', 'Network Engineer',
    'Content Writer', 'Video Editor', 'Photographer', 'Animator', 'Biotechnologist', 'Pharmacist',
    'Dentist', 'Veterinarian', 'Entrepreneur', 'HR Manager', 'Data Engineer', 'Machine Learning Researcher',
    'Robotics Engineer', 'Environmental Scientist', 'Civil Planner', 'Interior Designer'
]

for c in careers:
    +Career(c)

# -------------------------------
# ✅ Interest-based rules
# -------------------------------
interests = [
    ('coding', ['Software Engineer', 'Web Developer', 'Game Developer', 'AI Engineer', 'Data Scientist', 'Cloud Engineer', 'DevOps Engineer']),
    ('ai', ['AI Engineer', 'Machine Learning Researcher']),
    ('data', ['Data Scientist', 'Business Analyst', 'Data Engineer']),
    ('security', ['Cybersecurity Analyst', 'Network Engineer']),
    ('machines', ['Mechanical Engineer', 'Robotics Engineer']),
    ('construction', ['Civil Engineer', 'Civil Planner']),
    ('electricity', ['Electrical Engineer']),
    ('healthcare', ['Doctor', 'Nurse', 'Pharmacist', 'Dentist', 'Biotechnologist', 'Veterinarian']),
    ('teaching', ['Teacher', 'Professor']),
    ('research', ['Professor', 'Machine Learning Researcher', 'Environmental Scientist']),
    ('marketing', ['Digital Marketer', 'Product Manager']),
    ('design', ['Graphic Designer', 'UI/UX Designer', 'Interior Designer']),
    ('management', ['Product Manager', 'HR Manager']),
    ('business', ['Business Analyst', 'Entrepreneur', 'Financial Analyst']),
    ('finance', ['Financial Analyst']),
    ('law', ['Lawyer']),
    ('mind', ['Psychologist']),
    ('writing', ['Journalist', 'Content Writer']),
    ('photography', ['Photographer']),
    ('animation', ['Animator']),
    ('architecture', ['Architect', 'Interior Designer']),
    ('environment', ['Environmental Scientist']),
    ('technology', ['Software Engineer', 'AI Engineer', 'Data Scientist', 'Cloud Engineer']),
]

for interest, jobs in interests:
    for job in jobs:
        +has_interest(interest, job)

# -------------------------------
# ✅ Skill-based rules
# -------------------------------
skills = [
    ('python', ['Data Scientist', 'AI Engineer', 'Software Engineer', 'Data Engineer', 'Machine Learning Researcher']),
    ('java', ['Software Engineer', 'Mobile App Developer']),
    ('html', ['Web Developer']),
    ('css', ['Web Developer']),
    ('javascript', ['Web Developer', 'UI/UX Designer']),
    ('unity', ['Game Developer']),
    ('c++', ['Game Developer', 'Robotics Engineer']),
    ('networking', ['Cybersecurity Analyst', 'Network Engineer']),
    ('cloud computing', ['Cloud Engineer', 'DevOps Engineer']),
    ('docker', ['DevOps Engineer']),
    ('kubernetes', ['DevOps Engineer']),
    ('android', ['Mobile App Developer']),
    ('blockchain', ['Blockchain Developer']),
    ('smart contracts', ['Blockchain Developer']),
    ('mechanics', ['Mechanical Engineer']),
    ('autocad', ['Civil Engineer', 'Architect']),
    ('electrical circuits', ['Electrical Engineer']),
    ('biology', ['Doctor', 'Biotechnologist']),
    ('nursing', ['Nurse']),
    ('pharmacology', ['Pharmacist']),
    ('dentistry', ['Dentist']),
    ('animal care', ['Veterinarian']),
    ('communication', ['Teacher', 'Journalist', 'Content Writer']),
    ('public speaking', ['Professor', 'HR Manager']),
    ('marketing', ['Digital Marketer', 'Product Manager']),
    ('seo', ['Digital Marketer']),
    ('graphic design', ['Graphic Designer']),
    ('ui design', ['UI/UX Designer']),
    ('animation', ['Animator']),
    ('video editing', ['Video Editor']),
    ('photography', ['Photographer']),
    ('project management', ['Product Manager', 'Entrepreneur']),
    ('data analysis', ['Business Analyst', 'Data Scientist']),
    ('excel', ['Financial Analyst']),
    ('law knowledge', ['Lawyer']),
    ('psychology', ['Psychologist']),
    ('creativity', ['Architect', 'Interior Designer']),
    ('leadership', ['HR Manager', 'Entrepreneur']),
    ('robotics', ['Robotics Engineer']),
    ('machine learning', ['AI Engineer', 'Machine Learning Researcher']),
    ('environmental analysis', ['Environmental Scientist']),
]

for skill, jobs in skills:
    for job in jobs:
        +has_skill(skill, job)

# -------------------------------
# ✅ Education-based rules
# -------------------------------
educations = [
    ('engineering', ['Software Engineer', 'Mechanical Engineer', 'Electrical Engineer', 'Civil Engineer', 'AI Engineer', 'Cloud Engineer', 'DevOps Engineer', 'Robotics Engineer']),
    ('computer science', ['Web Developer', 'Data Scientist', 'AI Engineer', 'Game Developer', 'Cybersecurity Analyst', 'Mobile App Developer', 'Blockchain Developer', 'Data Engineer']),
    ('medical', ['Doctor', 'Nurse', 'Pharmacist', 'Dentist', 'Veterinarian']),
    ('education', ['Teacher', 'Professor']),
    ('business', ['Business Analyst', 'Product Manager', 'Entrepreneur', 'HR Manager']),
    ('commerce', ['Financial Analyst']),
    ('arts', ['Graphic Designer', 'UI/UX Designer', 'Animator', 'Interior Designer', 'Photographer', 'Content Writer']),
    ('law', ['Lawyer']),
    ('psychology', ['Psychologist']),
    ('mass communication', ['Journalist']),
    ('architecture', ['Architect', 'Interior Designer']),
    ('marketing', ['Digital Marketer']),
    ('environmental science', ['Environmental Scientist']),
    ('biotechnology', ['Biotechnologist']),
]

for edu, jobs in educations:
    for job in jobs:
        +has_education(edu, job)

# -------------------------------
# ✅ Rule: Suggest career if all match
# -------------------------------
suggest_career(Interest, Skill, Education, Career) <= (
    has_interest(Interest, Career) &
    has_skill(Skill, Career) &
    has_education(Education, Career)
)

# -------------------------------
# 🎨 Helper Functions
# -------------------------------
def print_slow(text, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_career_description(career):
    """Return a brief description of the career"""
    descriptions = {
        'Software Engineer': 'Design and develop software applications and systems.',
        'Data Scientist': 'Analyze complex data to help companies make better decisions.',
        'AI Engineer': 'Build intelligent systems and machine learning models.',
        'Web Developer': 'Create and maintain websites and web applications.',
        'Doctor': 'Diagnose and treat patients to improve health outcomes.',
        'Teacher': 'Educate and inspire students in various subjects.',
        'Digital Marketer': 'Promote products and services using digital channels.',
        'Graphic Designer': 'Create visual content for brands and communication.',
        'Business Analyst': 'Bridge the gap between IT and business using data analytics.',
        'Lawyer': 'Represent clients and provide legal advice.',
        'Architect': 'Design buildings and oversee construction projects.',
    }
    return descriptions.get(career, 'Exciting career opportunity in this field!')

def validate_input(user_input, input_type, valid_options):
    """Validate user input and check if it's meaningful"""
    user_input = user_input.lower().strip()
    
    # Check for empty or meaningless inputs
    invalid_responses = ['none', 'no', 'nothing', 'idk', "i don't know", 'na', 'n/a', 
                         'nil', 'null', '', 'not sure', 'dont know', "don't know"]
    
    if user_input in invalid_responses:
        return False, None
    
    # Check if input exists in valid options
    if user_input not in valid_options:
        return None, user_input  # Input doesn't exist but is not invalid
    
    return True, user_input

def get_valid_input(prompt, input_type, valid_options, examples):
    """Get valid input from user with retry logic"""
    while True:
        user_input = input(prompt).lower().strip()
        
        is_valid, cleaned_input = validate_input(user_input, input_type, valid_options)
        
        if is_valid is False:
            print_slow(f"\n⚠️  Oops! You can't say '{user_input}' here.", 0.02)
            print_slow(f"🤔 Everyone has some {input_type}! Think about what you enjoy or are good at.", 0.02)
            print(f"\n💡 Here are some examples of {input_type}:")
            print(f"   {examples}")
            print()
            continue
        
        if is_valid is None:
            print_slow(f"\n❓ Hmm, I don't recognize '{cleaned_input}' in my database.", 0.02)
            print_slow(f"Let me show you what I know about {input_type}...", 0.02)
            print(f"\n📚 Available {input_type}:")
            print(f"   {examples}")
            
            retry = input(f"\n🔄 Would you like to try again with a valid option? (yes/no): ").lower().strip()
            if retry in ['yes', 'y', 'yeah', 'sure']:
                continue
            else:
                print_slow("\n💭 No problem! Let me suggest based on what might work...", 0.02)
                return cleaned_input  # Return anyway, will handle no results later
        
        return cleaned_input

# -------------------------------
# 🤖 Chatbot Interaction
# -------------------------------
def main():
    print("\n" + "="*60)
    print_slow("🎯 Welcome to Your Career Guidance Assistant!", 0.02)
    print("="*60)
    print_slow("\nI'm here to help you discover the perfect career path!", 0.02)
    print_slow("Let me get to know you better...\n", 0.02)
    
    # Get user's name for personalization
    name = input("👤 First, what's your name? ").strip()
    if name:
        print_slow(f"\nNice to meet you, {name}! Let's explore your career options.\n", 0.02)
    else:
        name = "there"
        print_slow("\nGreat! Let's get started.\n", 0.02)
    
    # Extract all valid options from the data structures
    valid_interests = [interest for interest, _ in interests]
    valid_skills = [skill for skill, _ in skills]
    valid_educations = [edu for edu, _ in educations]
    
    # Show available options and get interest
    print("📋 Here are some areas to consider:")
    interest_examples = "coding, ai, healthcare, design, business, law, teaching, research, writing"
    print(f"   {interest_examples}")
    interest = get_valid_input(
        "\n💡 What is your main area of interest? ",
        "interests",
        valid_interests,
        interest_examples
    )
    
    print(f"\n✨ {interest.capitalize()} - that's a great field!")
    
    # Get skill with validation
    print("\n📋 Skills you might have:")
    skill_examples = "python, communication, mechanics, graphic design, law knowledge, leadership, creativity"
    print(f"   {skill_examples}")
    skill = get_valid_input(
        "\n🎯 What is your strongest skill? ",
        "skills",
        valid_skills,
        skill_examples
    )
    
    print(f"\n👍 Excellent! {skill.capitalize()} is a valuable skill.")
    
    # Get education with validation
    print("\n📋 Educational backgrounds:")
    education_examples = "computer science, engineering, business, medical, arts, law, psychology, commerce"
    print(f"   {education_examples}")
    education = get_valid_input(
        "\n🎓 What is your field of study? ",
        "educational backgrounds",
        valid_educations,
        education_examples
    )
    
    print(f"\n🎓 Great choice with {education}!")
    print_slow("\n🔍 Analyzing your profile...", 0.05)
    time.sleep(1)
    
    # Query using PyDatalog
    result = pyDatalog.ask(f"suggest_career('{interest}', '{skill}', '{education}', Career)")
    
    if result:
        careers_found = set()
        for r in result.answers:
            careers_found.add(str(r[0]))
        
        print(f"\n{'='*60}")
        print_slow(f"🎉 Fantastic news, {name}! I found {len(careers_found)} career path(s) that match your profile:", 0.02)
        print(f"{'='*60}\n")
        
        for idx, career in enumerate(sorted(careers_found), 1):
            print(f"  {idx}. 🌟 {career}")
            description = get_career_description(career)
            print(f"     → {description}\n")
        
        print("="*60)
        print_slow("\n💭 These careers align perfectly with your:", 0.02)
        print(f"   • Interest in {interest}")
        print(f"   • Skills in {skill}")
        print(f"   • Education in {education}")
        
    else:
        print(f"\n{'='*60}")
        print_slow(f"🤔 Hmm, I couldn't find an exact match for that combination.", 0.02)
        print("="*60)
        print_slow("\n💡 This might be because:", 0.02)
        print(f"   • Your {interest}, {skill}, and {education} don't overlap in our database")
        print("   • You might need to use more general or related terms")
        print("\n💭 Don't worry! Here are some successful combinations:")
        print("   ✓ ai + python + computer science → AI Engineer")
        print("   ✓ design + graphic design + arts → Graphic Designer")
        print("   ✓ healthcare + biology + medical → Doctor")
        print("   ✓ business + data analysis + commerce → Financial Analyst")
        print("   ✓ technology + cloud computing + engineering → Cloud Engineer")
    
    # Ask if user wants to try again
    print("\n" + "="*60)
    retry = input("\n🔄 Would you like to try different inputs? (yes/no): ").lower().strip()
    if retry in ['yes', 'y', 'yeah', 'sure']:
        print("\n" + "="*60 + "\n")
        main()
    else:
        print_slow(f"\n✨ Thank you for using Career Guidance Assistant, {name}!", 0.02)
        print_slow("🚀 Best of luck on your career journey!\n", 0.02)

# -------------------------------
# 🚀 Run the chatbot
# -------------------------------
if __name__ == "__main__":
    main()