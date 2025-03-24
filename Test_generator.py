from PIL import Image, ImageDraw, ImageFont
import os

def wrap_text(text, draw, font, max_width):
    """
    Wraps the text into lines so that each line does not exceed max_width.
    """
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def create_ocr_test_image(name, font_path):
    """
    Creates a test image with formatted and centered text for OCR testing,
    and saves it using the given name.
    
    Args:
    - name (str): The base name for the output image file (without extension).
    - font_path (str): Path to the .ttf font file to use for the text.
    
    Returns:
    - None
    """
    # The text to use (now with more line breaks for readability)
    test_text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Nam eget nunc nec sapien tempor efficitur. 
        Quisque gravida quam eu lorem auctor, sit amet interdum nunc scelerisque. Curabitur in erat quam. Aliquam erat volutpat. 
        Nunc id metus sit amet nisi tincidunt elementum vel ac odio. Integer vehicula sollicitudin sapien ac fringilla. 
        Vivamus tempor nisi quis odio iaculis, ut malesuada lorem viverra. Nam at nulla ac metus euismod interdum non non dui. 
        Suspendisse euismod arcu sed urna elementum, ac accumsan nulla consequat. Fusce malesuada purus sit amet sapien convallis, 
        id rhoncus velit feugiat. Integer ornare quam felis, nec consectetur nulla iaculis a. Curabitur sollicitudin urna et quam lobortis, 
        et bibendum odio consequat. Sed eget metus ac nunc auctor fringilla id a sapien. Ut feugiat varius nisi, sit amet iaculis erat iaculis nec. 
        Integer sit amet lectus at nisl condimentum facilisis. Nullam pellentesque, urna et tempor vehicula, sapien nunc luctus libero, 
        a gravida nulla erat vitae arcu.

        Cras quis augue vel lorem vestibulum vulputate. Vestibulum vehicula purus quis nunc malesuada, at ultricies dui placerat. 
        Donec hendrerit elit nisi, eget lacinia libero malesuada nec. Sed volutpat sollicitudin nulla, eget ullamcorper lectus bibendum nec. 
        Nulla facilisi. Integer laoreet lectus erat, et euismod orci lobortis vel. Sed vestibulum tortor non turpis gravida lacinia. 
        Nam tincidunt risus id turpis efficitur, nec tincidunt justo auctor. Aliquam dictum, nisi ut facilisis suscipit, velit lectus fringilla elit, 
        sit amet tincidunt nulla libero vitae purus. Phasellus euismod tempus ipsum, eget suscipit ipsum euismod ac. 
        Donec laoreet massa ac urna volutpat, at mollis velit rhoncus. Sed ultricies mauris lorem, eget placerat enim eleifend a. 
        Nulla vel enim eget odio tristique dapibus. Sed efficitur nisi magna, at lacinia nisi hendrerit a. Pellentesque nec tempor metus. 
        Duis bibendum bibendum augue ac aliquet.

        Etiam quis purus nec leo hendrerit vehicula. Sed gravida vehicula purus, eu pretium dui feugiat sit amet. Nam tempor ut nulla non aliquam. 
        Phasellus convallis nulla ut eros dignissim, nec congue lectus luctus. Morbi fringilla neque quis ante cursus, non tincidunt urna tincidunt. 
        Curabitur tincidunt, nisl nec placerat tincidunt, metus turpis dapibus erat, non euismod mi eros in justo. Aenean sit amet ultricies ante. 
        In tempor diam purus, nec sollicitudin dolor gravida id. Mauris sed ultricies neque, sed suscipit sem. Proin fermentum, risus nec faucibus fermentum, 
        nulla nisi iaculis erat, ac malesuada tortor risus in magna. Integer gravida lobortis orci ut bibendum. Quisque id lacus nisi. 
        Etiam feugiat ligula ligula, vitae hendrerit nunc rhoncus non. Integer fermentum, risus ut placerat tristique, purus justo varius ipsum, 
        a scelerisque sapien ipsum sit amet dui.
    """
    
    # Set up image and font parameters
    font_size = 20
    image_width = 800
    image_height = 1000
    margin = 20
    max_text_width = image_width - 2 * margin

    # Create a new white image and drawing context
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Process the text by paragraphs (split on blank lines) and wrap each paragraph
    paragraphs = [p.strip() for p in test_text.strip().split("\n\n")]
    lines = []
    for paragraph in paragraphs:
        wrapped = wrap_text(paragraph, draw, font, max_text_width)
        lines.extend(wrapped)
        lines.append("")  # add an empty line between paragraphs
    if lines and lines[-1] == "":
        lines.pop()  # remove trailing empty line

    # Calculate total text block height and determine starting y for vertical centering
    line_height = font_size + 5
    total_text_height = len(lines) * line_height
    y_start = (image_height - total_text_height) // 2

    # Draw each line centered horizontally
    for line in lines:
        if line.strip() == "":
            # For empty lines, just move the y coordinate
            y_start += line_height
            continue
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        x = (image_width - line_width) // 2
        draw.text((x, y_start), line, font=font, fill="black")
        y_start += line_height

    # Build the output file path based on the given name
    output_image_path = os.path.join(os.getcwd(), f"test_cases\\{name}.png")
    print(output_image_path)
    image.save(output_image_path)
    image.show()
    print(f"Test image created and saved to {output_image_path}")

# Example usage:
create_ocr_test_image("Roboto", r"fonts\Roboto.ttf")
