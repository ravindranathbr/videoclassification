import tensorflow as tf


# CUSTOM CONSTANTS

STATIC_DIRECTORY_NAME = '/var/www/python/django/aiadmin_static/'
graph_file_name = STATIC_DIRECTORY_NAME + 'models/' + 'output_graph.pb'
images_dir_name = STATIC_DIRECTORY_NAME + 'images_aiadmin/'
video_dir_name = STATIC_DIRECTORY_NAME + 'videos_aiadmin/'

def predict_on_image(image, labels):

    # Unpersists graph from file
    with tf.gfile.FastGFile(graph_file_name, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image, 'rb').read()

        try:
            predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
            prediction = predictions[0]
        except:
            print("Error making prediction.")
            sys.exit()

        # Return the label of the top classification.
        prediction = prediction.tolist()
        max_value = max(prediction)
        max_index = prediction.index(max_value)
        predicted_label = labels[max_index]
        
        return prediction

