import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

@st.cache_resource
def carrega_modelo():
    loaded_model = tf.keras.models.load_model('modelo_vidente.h5')

    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    return loaded_model, vectorizer

def predict_next_words(model, vectorizer, text_sequence, num_words=3):
    """Prevê as próximas palavras mais prováveis em uma sequência de texto.

    Args:
        model: O modelo Keras treinado para prever a próxima palavra.
        vectorizer: O objeto vectorizer usado para transformar o texto em sequências numéricas.
        text_sequence: A sequência de texto para a qual prever as próximas palavras.
        num_words (opcional): O número de palavras a serem previstas (padrão: 3).

    Returns:
        Uma lista das próximas palavras mais prováveis.
    """
    token_list = vectorizer([text_sequence])[0].numpy()
    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
    predicted_probs = model.predict(token_list, verbose=0)[0]

    # Encontra os índices das 3 maiores probabilidades
    top_indices = np.argpartition(predicted_probs, -num_words)[-num_words:]

    # Ordena os índices em ordem decrescente de probabilidade
    top_indices = top_indices[np.argsort(-predicted_probs[top_indices])]

    # Mapeia os índices para as palavras correspondentes
    predicted_words = [vectorizer.get_vocabulary()[index] for index in top_indices]

    return predicted_words


#loaded_model = tf.keras.models.load_model('modelo_vidente.h5')
    #st.success("Modelo carregado com sucesso!")

max_vocab_size = 20000
max_sequence_len = 50





# Tokenizar o texto
#vectorizer = TextVectorization(max_tokens=max_vocab_size, output_sequence_length=max_sequence_len, output_mode='int')

# Adaptar a camada ao corpus
#vectorizer.adapt(corpus)

loaded_model, vectorizer = carrega_modelo()

# Interface Streamlit
st.title("🔮 Previsão de Próximas Palavras")

input_text = st.text_input("Digite uma sequência de texto:")

if st.button("Prever"):
    if input_text:
        try:
            predicted_words = predict_next_words(loaded_model, vectorizer, input_text) #predict_next_words(loaded_model, vectorizer, input_text)
            
            st.info("Palavras mais prováveis:")
            for word in predicted_words:
                st.success(word)  # Cada palavra em uma caixa de sucesso
        except Exception as e:
            st.error(f"Erro na previsão: {e}")
    else:
        st.warning("Por favor, insira algum texto.")
