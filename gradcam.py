import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.models import Model


def generate_gradcam(model, img_array, predicted_class):
    """
    Generate Grad-CAM heatmap
    """

    last_conv_layer = None

    # Find last convolutional layer
    for layer in reversed(model.layers):
        if "conv" in layer.name.lower():
            last_conv_layer = layer.name
            break

    if last_conv_layer is None:
        raise ValueError("No convolutional layer found.")

    grad_model = Model(
        inputs=model.inputs,
        outputs=[
            model.get_layer(last_conv_layer).output,
            model.output
        ]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        loss = predictions[:, predicted_class]

    grads = tape.gradient(loss, conv_outputs)

    pooled_grads = tf.reduce_mean(
        grads,
        axis=(0, 1, 2)
    )

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(
        pooled_grads * conv_outputs,
        axis=-1
    )

    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap) + 1e-8

    return heatmap


def overlay_heatmap(original_image, heatmap):
    """
    Overlay heatmap on image
    """

    image_np = np.array(original_image)

    heatmap = cv2.resize(
        heatmap,
        (image_np.shape[1], image_np.shape[0])
    )

    heatmap = np.uint8(255 * heatmap)

    heatmap_colored = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        image_np,
        0.6,
        heatmap_colored,
        0.4,
        0
    )

    return overlay