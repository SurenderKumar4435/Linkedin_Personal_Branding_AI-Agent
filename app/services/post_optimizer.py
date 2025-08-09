





import re

def optimize_post(post: str, hashtags=None, max_length=1300) -> str:
    """
    Cleans up LinkedIn post formatting and appends relevant hashtags.
    
    Args:
        post (str): The LinkedIn post content.
        hashtags (list, optional): List of hashtags to append. Defaults to standard tags.
        max_length (int): LinkedIn's character limit. Default: 1300.

    Returns:
        str: Optimized post.
    """
    if hashtags is None:
        hashtags = ["#AI", "#LinkedInBranding", "#CareerGrowth"]

    # Normalize newlines and spacing
    optimized = re.sub(r'\n\s*', '\n\n', post.strip())

    # Filter out duplicate hashtags (case-insensitive)
    existing_hashtags = {tag.lower() for tag in re.findall(r'#\w+', optimized)}
    new_hashtags = [tag for tag in hashtags if tag.lower() not in existing_hashtags]

    # Append hashtags
    if new_hashtags:
        optimized += "\n\n" + " ".join(new_hashtags)

    # Trim if post exceeds LinkedIn limit
    if len(optimized) > max_length:
        optimized = optimized[:max_length - 3].rstrip() + "..."

    return optimized
