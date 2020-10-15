import tensorflow as tf

import utils



image_url = "https://static01.nyt.com/images/2020/05/04/sports/04nosports1/merlin_171778071_00664c6e-ecdb-4792-997c-8b190fadca23-articleLarge.jpg?quality=75&auto=webp&disable=upscale"
image_extension = image_url[-4:]
image_path = tf.keras.utils.get_file('image'+image_extension,
                                     origin=image_url)

result, attention_plot = utils.evaluate(image_path)
print ('Prediction Caption:', ' '.join(result))
