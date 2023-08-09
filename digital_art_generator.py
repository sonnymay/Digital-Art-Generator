from PIL import Image, ImageDraw
import random

def random_color():
    """Generate a random color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_art(filename="generated_art.png", width=800, height=600):
    """Generate a random piece of digital art."""
    
    # Create a blank white canvas
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Draw random lines
    for _ in range(random.randint(20, 100)):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=random_color(), width=random.randint(1, 5))
    
    # Draw random circles
    for _ in range(random.randint(10, 50)):
        upper_left = (random.randint(0, width), random.randint(0, height))
        lower_right = (random.randint(upper_left[0], width), random.randint(upper_left[1], height))
        draw.ellipse([upper_left, lower_right], outline=random_color(), width=random.randint(1, 5))
    
    # Draw random rectangles
    for _ in range(random.randint(10, 50)):
        upper_left = (random.randint(0, width), random.randint(0, height))
        lower_right = (random.randint(upper_left[0], width), random.randint(upper_left[1], height))
        draw.rectangle([upper_left, lower_right], outline=random_color(), width=random.randint(1, 5))

    # Save the generated image
    image.save(filename)

if __name__ == "__main__":
    generate_art()
