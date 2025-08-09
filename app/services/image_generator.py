


from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_image_with_text(text: str, file_path: str):
    # Settings
    width, height = 1000, 600
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)
    font_size = 36
    margin = 50
    line_spacing = 10  # vertical spacing between lines

    # Create image
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Try loading a clean font
    try:
        font_path = "arial.ttf"  # Windows
        if not os.path.exists(font_path):
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Linux fallback

        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    # Calculate max characters per line based on font size
    max_chars_per_line = (width - 2 * margin) // font.getsize("A")[0]
    wrapped_text = textwrap.wrap(text, width=max_chars_per_line)

    # Calculate total text height
    total_text_height = sum(font.getsize(line)[1] + line_spacing for line in wrapped_text) - line_spacing

    # Vertical centering
    current_y = (height - total_text_height) // 2

    # Draw each line
    for line in wrapped_text:
        text_width, text_height = font.getsize(line)
        x = (width - text_width) // 2  # center horizontally
        draw.text((x, current_y), line, font=font, fill=text_color)
        current_y += text_height + line_spacing

    # Save
    img.save("D:\Generative.AI\Linkedin_Project_copy\Image_generae_saver\linkedin_post.png")
    print(f"Image saved to: {file_path}")
