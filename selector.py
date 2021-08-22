from random import randint, choice


def select_image():
    with open('count.txt', 'r') as count:  # Getting the total number of images that is available.
        total_images = int(count.read())
    line_number = randint(1, total_images)  # Choosing a random file

    # Opening that line
    with open('files.txt', 'r') as  file:
        count = 0;
        selected_line = ''
        for line in file:
            count += 1
            if count == line_number:
                selected_line = line
                break
            pass
    return (selected_line)


def select_unrelated_image( suitable_images,chosen_tag):

    # All images which have the chosen tag. We will later choose 2 random images from these.
    choices=[]
    for line in suitable_images:
        if (((',' + chosen_tag) not in line) or ((chosen_tag + ',') not in line) or (
                (',' + chosen_tag + ',') not in line)):
            choices.append(line)
        pass

    unrelated_line = choice(choices)  # Selecting a random image
    return (unrelated_line)


def select_tag(selected_line):
    selected_list = selected_line.split(",")
    tags = selected_list[1:]
    tags.pop()
    chosen_tag = choice(tags)
    return (chosen_tag)


def select_four_images(selected_line, chosen_tag):
    with open("files.txt", 'r') as file:
        suitable_images = []  # All images which have the chosen tag. We will later choose 2 random images from these.
        unsuitable_images=[]
        for line in file:
            if selected_line != line:
                if ((((',' + chosen_tag) in line) or (chosen_tag + ',') in line) or ((',' + chosen_tag + ',') in line)):
                    suitable_images.append(line)
                    pass
                else:
                    unsuitable_images.append(line)
    first_line = choice(suitable_images)
    # Selecting a random image

    suitable_images.remove(first_line)

    second_line = choice(suitable_images)  # Selecting a random image

    suitable_images.remove(second_line)
    image1 = first_line.split(",")[0]
    image2 = second_line.split(",")[0]
    image3 = selected_line.split(",")[0]
    image4 = select_unrelated_image(unsuitable_images, chosen_tag).split(",")[0]
    # correct option

    return ((image1, image2, image3, image4))


def selector_session():
    image = select_image()

    tag = select_tag(image)
    return (select_four_images(image, tag))
