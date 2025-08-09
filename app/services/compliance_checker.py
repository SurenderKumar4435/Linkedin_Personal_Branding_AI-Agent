





import re
from typing import Tuple, List

def check_post_compliance(post: str) -> Tuple[bool, List[str]]:
    # Extendable list of inappropriate words
    bad_words = [
        "hate", "violence", "offensive", "racist", "sexist", "abuse", "terror",
        "bully", "kill", "harm", "nsfw", "discriminate", "slur"
    ]

    # Regex pattern to match whole bad words, case-insensitive
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in bad_words) + r')\b'
    matches = re.findall(pattern, post.lower())

    # Return False (not compliant) if any bad words found
    return len(matches) == 0, matches

# Example usage
post = "We should not promote hate or violence in the workplace."
is_compliant, found = check_post_compliance(post)

if is_compliant:
    print("✅ Post is clean and compliant.")
else:
    print(f"❌ Post is non-compliant. Found banned words: {found}")
