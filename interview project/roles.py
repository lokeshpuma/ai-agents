INTERVIEW_ROLES = {
    "software_engineer":{
        "keywords": ["coding", "algorithms", "data structures", "system design"],
        "difficulty_levels": ["easy", "medium", "hard"]
    },
    "python_developer": {
        "keywords": ["python", "django", "flask", "data analysis"],
        "difficulty_levels": ["easy", "medium", "hard"]
    },
    "data_scientist": {
        "keywords": ["statistics", "machine learning", "data visualization", "python"],
        "difficulty_levels": ["medium", "hard"]
    },
    "devops_engineer": {
        "keywords": ["ci/cd", "docker", "kubernetes", "cloud services"],
        "difficulty_levels": ["medium", "hard"]
    },
    "product_manager": {
        "keywords": ["roadmap", "stakeholder management", "agile", "user stories"],
        "difficulty_levels": ["easy", "medium"] 
    },
    "cloud_architect": {
        "keywords": ["aws", "azure", "gcp", "infrastructure as code"],
        "difficulty_levels": ["hard"]
    },
    "ux_designer": {
        "keywords": ["user research", "wireframing", "prototyping", "usability testing"],
        "difficulty_levels": ["easy", "medium"]
    },
    "cybersecurity_specialist": {
        "keywords": ["network security", "encryption", "vulnerability assessment", "firewalls"],
        "difficulty_levels": ["medium", "hard"]
    }
}

def chose_role():
    print("\n welcome to the interview role selector \n")
    print("Available interview roles:")

    roles = list(INTERVIEW_ROLES.keys())

    for idx, role in enumerate(roles, start=1):
        print(f"{idx}. {role.replace('_', ' ').title()}")

    choice = int(input("\nSelect a role by entering the corresponding number: "))
    role = roles[choice - 1]

    print(f"\nYou have selected the role: {role.replace('_', ' ').title()}")
    return role, INTERVIEW_ROLES[role]