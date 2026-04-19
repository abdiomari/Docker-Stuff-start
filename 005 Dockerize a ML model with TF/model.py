import tensorflow as tf 
import numpy as np

# using a pre-trained mobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet')
print(f"Model input shape: {model.input_shape}")
dummy_image = np.random.random((1,224,224,3)).astype(np.float32)
predictions = model.predict(dummy_image)
print(f"Top predicted class index: {np.argmax(predictions[0])}")