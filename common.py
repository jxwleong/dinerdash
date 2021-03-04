image_dict = {
    'menu_chalkboard.png' : 'Main Menu',
    'endless_shift.png' : 'Endless Shift',
    'restaurant_min.png' : 'Restaurant',
    'endless_shift_easy.png' : 'Easy',
    'lets_play.png' : 'Play'
}

def get_refined_image_name (image):
    return image_dict.get(image)


print(get_refined_image_name('lets_play.png'))