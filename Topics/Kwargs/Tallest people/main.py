def tallest_people(**peoples):
    all_heights = peoples.values()
    max_height = max(all_heights)
    tallest = sorted([name for name, height in peoples.items() if height == max_height])
    for name in tallest:
        print(name, ':', max_height)


# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
