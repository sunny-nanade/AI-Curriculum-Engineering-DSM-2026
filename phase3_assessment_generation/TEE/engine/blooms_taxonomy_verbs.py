"""
Bloom's Taxonomy Levels and Action Verbs
Revised Bloom's Taxonomy has 6 levels (from lower to higher order thinking)
"""

BLOOMS_TAXONOMY = {
    "L1_Remember": {
        "level": 1,
        "name": "Remember",
        "description": "Recall facts and basic concepts",
        "verbs": [
            "define", "describe", "identify", "label", "list", "match", 
            "name", "outline", "recall", "recognize", "reproduce", "select",
            "state", "mention", "quote", "repeat", "arrange", "enumerate"
        ]
    },
    "L2_Understand": {
        "level": 2,
        "name": "Understand",
        "description": "Explain ideas or concepts",
        "verbs": [
            "classify", "compare", "contrast", "demonstrate", "explain", 
            "extend", "illustrate", "infer", "interpret", "outline", 
            "relate", "rephrase", "show", "summarize", "translate",
            "paraphrase", "discuss", "distinguish", "estimate", "give examples"
        ]
    },
    "L3_Apply": {
        "level": 3,
        "name": "Apply",
        "description": "Use information in new situations",
        "verbs": [
            "apply", "build", "choose", "construct", "develop", "execute",
            "experiment", "identify", "implement", "interview", "make use of",
            "model", "organize", "plan", "select", "solve", "utilize",
            "calculate", "compute", "demonstrate", "modify", "operate"
        ]
    },
    "L4_Analyze": {
        "level": 4,
        "name": "Analyze",
        "description": "Draw connections among ideas",
        "verbs": [
            "analyze", "attribute", "break down", "categorize", "compare",
            "contrast", "deconstruct", "differentiate", "discriminate",
            "distinguish", "examine", "experiment", "focus", "infer",
            "inspect", "integrate", "outline", "organize", "relate",
            "separate", "structure", "investigate", "diagnose"
        ]
    },
    "L5_Evaluate": {
        "level": 5,
        "name": "Evaluate",
        "description": "Justify a stand or decision",
        "verbs": [
            "appraise", "argue", "assess", "choose", "conclude", "critique",
            "defend", "estimate", "evaluate", "judge", "justify", "predict",
            "prioritize", "prove", "rank", "rate", "recommend", "select",
            "support", "test", "validate", "verify", "weigh"
        ]
    },
    "L6_Create": {
        "level": 6,
        "name": "Create",
        "description": "Produce new or original work",
        "verbs": [
            "assemble", "build", "compose", "construct", "create", "design",
            "develop", "devise", "formulate", "generate", "hypothesize",
            "invent", "make", "originate", "plan", "prepare", "produce",
            "propose", "synthesize", "write", "integrate", "modify"
        ]
    }
}

def get_bloom_level_from_verb(verb):
    """
    Return Bloom's level based on action verb
    """
    verb = verb.lower().strip()
    for level_key, level_data in BLOOMS_TAXONOMY.items():
        if verb in level_data["verbs"]:
            return {
                "level_key": level_key,
                "level_number": level_data["level"],
                "level_name": level_data["name"]
            }
    return None

def display_blooms_taxonomy():
    """
    Display Bloom's Taxonomy levels and verbs
    """
    print("=" * 80)
    print("BLOOM'S TAXONOMY - REVISED VERSION")
    print("=" * 80)
    print()
    
    for level_key, level_data in BLOOMS_TAXONOMY.items():
        print(f"Level {level_data['level']}: {level_data['name'].upper()}")
        print(f"Description: {level_data['description']}")
        print(f"Action Verbs: {', '.join(level_data['verbs'][:15])}")
        print(f"             ... and {len(level_data['verbs']) - 15} more")
        print()

if __name__ == "__main__":
    display_blooms_taxonomy()
    
    # Test examples
    print("\n" + "=" * 80)
    print("EXAMPLE VERB MATCHING")
    print("=" * 80)
    test_verbs = ["define", "explain", "apply", "analyze", "evaluate", "design"]
    for verb in test_verbs:
        result = get_bloom_level_from_verb(verb)
        if result:
            print(f"Verb: '{verb}' -> {result['level_name']} (Level {result['level_number']})")
        else:
            print(f"Verb: '{verb}' -> Not found in standard list")
