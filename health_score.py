"""
Calculadora de Health Score de Clientes
=======================================
Um exemplo simples e temático (Customer Success!) para você
praticar GitHub: commits, branches, pull requests e Actions.

O health score combina 3 métricas em uma nota de 0 a 100:
- Adoção do produto (% de licenças ativamente usadas)
- Engajamento (interações com o CSM nos últimos 90 dias)
- NPS do cliente (-100 a +100)
"""


def calcular_adocao(licencas_usadas: int, licencas_totais: int) -> float:
    """Retorna a taxa de adoção como percentual (0-100)."""
    if licencas_totais <= 0:
        return 0.0
    taxa = (licencas_usadas / licencas_totais) * 100
    return min(taxa, 100.0)


def pontuar_engajamento(interacoes_90_dias: int) -> float:
    """Converte número de interações em nota 0-100.

    0 interações  -> 0 pontos (churn silencioso!)
    6+ interações -> 100 pontos
    """
    if interacoes_90_dias <= 0:
        return 0.0
    return min(interacoes_90_dias / 6 * 100, 100.0)


def normalizar_nps(nps: int) -> float:
    """Converte NPS (-100 a +100) para escala 0-100."""
    nps = max(-100, min(100, nps))
    return (nps + 100) / 2

def pontuar_tickets(tickets_abertos: int) -> float:
       """Converte tickets de suporte abertos em nota 0-100.

       0 tickets  -> 100 pontos (sem fricção)
       10+ tickets -> 0 pontos (muita fricção!)
       """
       if tickets_abertos <= 0:
           return 100.0
       if tickets_abertos >= 10:
           return 0.0
       return 100.0 - (tickets_abertos * 10)


def calcular_health_score(
    licencas_usadas: int,
    licencas_totais: int,
    interacoes_90_dias: int,
    nps: int,
) -> dict:
    """Calcula o health score ponderado do cliente.

    Pesos: adoção 50%, engajamento 30%, NPS 20%.
    (Adoção pesa mais porque é o melhor preditor de renovação!)
    """
    adocao = calcular_adocao(licencas_usadas, licencas_totais)
    engajamento = pontuar_engajamento(interacoes_90_dias)
    nps_norm = normalizar_nps(nps)

    score = adocao * 0.4 + engajamento * 0.4 + nps_norm * 0.2

    if score >= 75:
        status = "🟢 Saudável"
        acao = "Explorar oportunidades de expansão"
    elif score >= 50:
        status = "🟡 Atenção"
        acao = "Agendar business review e plano de adoção"
    else:
        status = "🔴 Risco de churn"
        acao = "Escalar internamente e montar plano de recuperação"

    return {
        "score": round(score, 1),
        "status": status,
        "acao_recomendada": acao,
        "detalhes": {
            "adocao": round(adocao, 1),
            "engajamento": round(engajamento, 1),
            "nps_normalizado": round(nps_norm, 1),
        },
    }


if __name__ == "__main__":
    # Exemplo: carteira fictícia de clientes
    carteira = [
        {"nome": "TechCorp", "usadas": 180, "totais": 200, "interacoes": 8, "nps": 60},
        {"nome": "DataSystems", "usadas": 90, "totais": 200, "interacoes": 3, "nps": 10},
        {"nome": "CloudInc", "usadas": 30, "totais": 150, "interacoes": 0, "nps": -20},
    ]

    print("=" * 60)
    print("RELATÓRIO DE HEALTH SCORE DA CARTEIRA")
    print("=" * 60)

    for cliente in carteira:
        resultado = calcular_health_score(
            cliente["usadas"], cliente["totais"], cliente["interacoes"], cliente["nps"]
        )
        print(f"\nCliente: {cliente['nome']}")
        print(f"  Score: {resultado['score']} — {resultado['status']}")
        print(f"  Ação:  {resultado['acao_recomendada']}")
