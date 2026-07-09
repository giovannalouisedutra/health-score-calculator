# 📊 Calculadora de Health Score de Clientes

Um projeto de exemplo para aprender GitHub na prática — com tema de **Customer Success**!

## O que este projeto faz

Calcula o health score (0-100) de uma carteira de clientes combinando três métricas:

| Métrica | Peso | Por quê |
|---------|------|---------|
| Adoção do produto | 50% | Melhor preditor de renovação |
| Engajamento com o CSM | 30% | Detecta churn silencioso |
| NPS | 20% | Sentimento do cliente |

O resultado classifica cada cliente como 🟢 Saudável, 🟡 Atenção ou 🔴 Risco de churn — com uma ação recomendada para o CSM.

## Como rodar localmente

```bash
python health_score.py
```

## Como rodar os testes

```bash
pip install pytest
pytest -v
```

## CI/CD com GitHub Actions ⚙️

Este repositório tem um workflow em `.github/workflows/ci.yml` que roda os testes **automaticamente** a cada push ou pull request. Vá na aba **Actions** do repositório para ver a mágica acontecer!

---

*Projeto criado para fins de aprendizado.*
