import numpy as np
import tensorflow as tf

def create_acoustic_model(input_shape=(128, 128, 1), num_classes=5):
    """
    Crea una rete neurale leggera (CNN) ottimizzata per l'esecuzione 
    su dispositivi mobili (Edge AI) tramite TensorFlow Lite.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=input_shape),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(num_classes, activation='softmax') # Classi di guasto
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    print("Inizializzazione struttura modello AI acustica per IAmecc...")
    model = create_acoustic_model()
    model.summary()