iris = {}


def add_iris(id_n, species, petal_length, petal_width, **additional_features):
    iris[id_n] = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width, **additional_features}
    # iris[id_n].update(additional_features)

# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
# print(iris)
