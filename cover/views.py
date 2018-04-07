from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image, ImageFont, ImageDraw
from .forms import CoverForm
from .utils import COLOR_CODES

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data  # 이미지를 생성할 데이터는 여기 있음
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form,
    })


def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_index = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_im = Image.open(animal_path)


    color = COLOR_CODES[int(color_index)]  # request를 통해 받은 모든값은 문자이므로 int 변환 필요

    canvas_im = Image.new('RGB', (500, 700), (255, 255, 255, 100))
    animal_im = animal_im.resize((400, 400))
    canvas_im.paste(animal_im, (50, 40))  # left_top wlwjd

    # 위 데이터를 받아서, 이미지를 여기서 그리는것

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    draw = ImageDraw.Draw(canvas_im)

    draw.rectangle((10, 0, 480, 10), fill=color)
    draw.rectangle((10, 400, 480, 530), fill=color)

    fnt = ImageFont.truetype(ttf_path, 70)
    draw.text((45, 430), title, font=fnt, fill=(255, 255, 255, 255))  # 글짜 색상

    fnt = ImageFont.truetype(ttf_path, 20)
    draw.text((160, 14), top_text, font=fnt, fill=(0, 0, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 25)
    draw.text((380, 665), author, font=fnt, fill=(0, 0, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 30)
    if guide_text_placement == 'bottom_right':
        position = (250, 535)
    elif guide_text_placement == 'bottom_left':
        position = (10, 535)
    elif guide_text_placement == 'top_right':
        position = (265, 368)
    else:
        position = (10, 368)
    draw.text(position, guide_text, font=fnt, fill=(0, 0, 0, 255))

    response = HttpResponse(content_type='image/png')  # file-like
    canvas_im.save(response, format='PNG')
    return response