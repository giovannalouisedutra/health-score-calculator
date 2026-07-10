"""
Testes automatizados da calculadora de health score.

É ESTE arquivo que o GitHub Actions vai rodar automaticamente
a cada mudança no código. Se algum teste falhar, o Actions
mostra um X vermelho — se tudo passar, um check verde. ✅
"""

from health_score import (
    calcular_adocao,
    calcular_health_score,
    normalizar_nps,
    pontuar_engajamento,
    pontuar_tickets,
)


def test_adocao_total():
    assert calcular_adocao(100, 100) == 100.0


def test_adocao_metade():
    assert calcular_adocao(50, 100) == 50.0


def test_adocao_sem_licencas():
    # Não pode dividir por zero!
    assert calcular_adocao(10, 0) == 0.0


def test_engajamento_zero_e_churn_silencioso():
    assert pontuar_engajamento(0) == 0.0


def test_engajamento_maximo():
    assert pontuar_engajamento(10) == 100.0


def test_nps_neutro():
    assert normalizar_nps(0) == 50.0


def test_nps_maximo():
    assert normalizar_nps(100) == 100.0


def test_cliente_saudavel():
    resultado = calcular_health_score(180, 200, 8, 60)
    assert resultado["score"] >= 75
    assert "Saudável" in resultado["status"]


def test_cliente_em_risco():
    resultado = calcular_health_score(30, 150, 0, -20)
    assert resultado["score"] < 50
    assert "Risco" in resultado["status"]

def test_tickets_zero_e_nota_maxima():
       assert pontuar_tickets(0) == 100.0


   def test_tickets_moderados():
       assert pontuar_tickets(5) == 50.0


   def test_muitos_tickets_e_nota_zero():
       assert pontuar_tickets(15) == 0.0
