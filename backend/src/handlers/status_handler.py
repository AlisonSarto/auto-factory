# src/handlers/status_handler.py
# No futuro, você vai importar seus Services aqui para tomar decisões
# ex: from src.services.agua_service import AguaService

def processar_mensagem_status(topico: str, payload: str):
    # Aqui você converte o JSON e chama os Services adequados
    print(f"📥 [Handler processou] Tópico: {topico} | Mensagem: {payload}")
    
    # Exemplo futuro:
    # if "balanca" in topico and "concluido" in payload:
    #     AguaService().ligar_agua()