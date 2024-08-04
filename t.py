import logging

# Configuração do logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def divide(a, b):
    try:
        result = a / b
        logger.info(f"Divisão bem-sucedida: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Tentativa de divisão por zero")
        return None


# Testando a função
divide(10, 2)
divide(10, 0)
