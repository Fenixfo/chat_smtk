import openai
from openai import OpenAI
clientes = [
    {
        "id": 1,
        "nombre": "ACME Corp",
        "estado_cuenta": "Activo",
        "monto_facturado": 12500,
        "nivel_madurez": "Intermedio",
        "última_reunión": "2024-12-10"
    },
    {
        "id": 2,
        "nombre": "BetaTech",
        "estado_cuenta": "Pendiente de renovación",
        "monto_facturado": 5300,
        "nivel_madurez": "Inicial",
        "última_reunión": "2025-01-20"
    }
]
empresa='SMTK'
prompt = f"""Actúa como un asistente de Customer Success.
El cliente es {clientes[0]['nombre']}, con estado de cuenta {clientes[0]['estado_cuenta']} y nivel de madurez {clientes[0]['nivel_madurez']}.
¿Qué debería preparar para la próxima reunión?"""
client = OpenAI(api_key="llave privada")
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
response = get_completion(prompt)
print(response)
