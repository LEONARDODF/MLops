import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

def train_model():
    print("🚀 Iniciando o treinamento do modelo...")

    # 1. Dados Simples (Poderia ser um CSV, mas vamos criar aqui para facilitar)
    data = {
        'text': [
            'Ganhe dinheiro fácil agora', 'Promoção imperdível de hoje',
            'Oi, vamos almoçar hoje?', 'Reunião marcada para as 15h',
            'Clique aqui para seu prêmio', 'Segue o relatório em anexo',
            'Você ganhou um iPhone grátis', 'O código do projeto foi atualizado'
        ],
        'label': ['spam', 'spam', 'ham', 'ham', 'spam', 'ham', 'spam', 'ham']
    }
    df = pd.DataFrame(data)

    # 2. Divisão de Treino e Teste
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

    # 3. Criação do Pipeline (Vetorização + Modelo)
    # Isso facilita o MLOps porque o 'binário' já sabe converter texto em números
    model_pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('nb', MultinomialNB())
    ])

    # 4. Treinamento
    model_pipeline.fit(X_train, y_train)
    print("✅ Modelo treinado com sucesso!")

    # 5. Exportação do Artefato
    # No MLOps, salvar o modelo é como dar um 'build' no código
    os.makedirs('models', exist_ok=True)
    joblib.dump(model_pipeline, 'models/model.pkl')
    print("💾 Artefato salvo em: models/model.pkl")

if __name__ == "__main__":
    train_model()