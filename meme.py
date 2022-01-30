from PIL import Image, ImageDraw, ImageFont

def gen_meme(input_file, output_file, meme_type, m_text, f_name):
    try:
        image = Image.open('memes/' + input_file)
    except:
        return print('File not found or unreadable!')

    width, height = image.size
    output_file = 'memes/exported/' + output_file

    meme_font = ''
    font_name = 'arial.ttf'
    font_size = int((width / height) * 60)
    text = ' '.join(m_text)

    if meme_type == 3:
        font_name = 'impact.ttf'

    if f_name is not None:
        font_name = f_name

    meme_font = ImageFont.truetype('fonts/' + font_name, font_size)

    if meme_type == 1:
        type_one(width, height, image, text, meme_font, font_size, output_file)
    elif meme_type == 2:
        type_two(width, height, image, text, meme_font, font_size, output_file)
    elif meme_type == 3:
        type_three(width, height, image, text, meme_font, output_file)
    else:
        print('[Error]: No such meme type.')

    print('Successfully exported meme!')

def type_one(width, height, image, text, meme_font, font_size, output_file):
    padding = int(height / 10)
    textPadding = font_size + 2
    new_height = height + textPadding + padding
    
    result = Image.new(image.mode, (width, new_height), (255, 255, 255))
    result.paste(image, (0, textPadding + padding))

    meme_text = ImageDraw.Draw(result)
    text_width, text_height = get_text_dim(text, meme_font)
    meme_text.text((20, ((padding + textPadding) / 2) - (text_height / 2) - 3), text, font=meme_font, fill=(0, 0, 0))

    result.save(output_file)

def type_two(width, height, image, text, meme_font, font_size, output_file):
    padding = int(height / 10)
    textPadding = font_size + 2
    new_height = height + textPadding + padding
    
    result = Image.new(image.mode, (width, new_height), (255, 255, 255))
    result.paste(image, (0, 0))

    meme_text = ImageDraw.Draw(result)
    text_width, text_height = get_text_dim(text, meme_font)
    meme_text.text((20, (height + (padding + textPadding) / 2) - (text_height / 2) - 3), text, font=meme_font, fill=(0, 0, 0))

    result.save(output_file)

def type_three(width, height, image, text, meme_font, output_file):
    top_text = text
    bottom_text = ''

    if ',' in text:
        dtext = text.split(',')
        top_text = dtext[0]
        bottom_text = dtext[1]

    meme_text = ImageDraw.Draw(image)

    text_width, text_height = get_text_dim(top_text, meme_font)
    center = (width / 2) - (text_width / 2)
    meme_text.text((center, 0), top_text, font=meme_font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

    if bottom_text != '':
        text_width, text_height = get_text_dim(bottom_text, meme_font)
        center = (width / 2) - (text_width / 2)
        meme_text.text((center, height - text_height - 30), bottom_text, font=meme_font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

    image.save(output_file)

def get_text_dim(text_string, font):
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    return (text_width, text_height)
