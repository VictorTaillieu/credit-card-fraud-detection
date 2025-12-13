# Credit card fraud detection

🎯 **Problématique Business**

La banque subit 2M€ de pertes annuelles dues à la fraude. Les transactions frauduleuses représentent 0.17% du volume mais 15% des pertes. Objectif : détecter 95% des fraudes en < 50ms.

📊 **Dataset**

- **Source** : [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Volume** : 284,807 transactions sur 2 jours
- **Simulation** : Créer un stream avec Python + générateur de nouvelles fraudes
- **Features** : 30 variables (PCA transformées) + montant + temps

🏗️ **Architecture Technique**
```
Transaction Stream → Processing → ML Model → Decision → Alert
        ↓              ↓            ↓          ↓        ↓
    CSV + Faker      pandas      XGBoost    FastAPI   Plotly
    Simulation     numpy/scipy  scikit-learn Docker   Dashboard
```

📦 **Livrables Attendus**
1. **Simulateur de transactions** avec Faker pour stream temps réel
2. **Feature engineering** avec pandas et numpy
3. **Modèle ML** XGBoost avec gestion du déséquilibre (SMOTE)
4. **API REST** FastAPI avec prédictions temps réel
5. **Dashboard monitoring** avec plotly/dash

🎯 **Critères de Réussite**
- Precision > 90% (limiter les faux positifs)
- Latence < 50ms par prédiction via API
- Containerisation Docker complète

🛠️ **Stack**
- **ML** : Python, pandas, scikit-learn, XGBoost, imbalanced-learn
- **API** : FastAPI, uvicorn
- **Container** : Docker
- **Viz** : plotly, matplotlib
- **Dev** : Jupyter, VS Code
