from datetime import datetime  # Importa la fecha y hora actuales
from typing import List  # Importa la funcionalidad de listas con tipado

# Clase base Pedido
class Pedido:
    def __init__(self, id_pedido: int, detalles: str):
        # Encapsulación: atributos protegidos
        self._id_pedido = id_pedido  
        self._detalles = detalles  
        self._estado = "Pendiente"  

    # Método para "crear" un pedido (simula la creación)
    def crear_pedido(self):
        print(f"Pedido creado: {self._id_pedido} - {self._detalles}")
        return self

    # Getter: obtiene el estado del pedido
    def get_estado(self):
        return self._estado

    # Setter: actualiza el estado del pedido
    def set_estado(self, estado: str):
        self._estado = estado


# Subclase PedidoExpress (hereda de Pedido)
class PedidoExpress(Pedido):
    def __init__(self, id_pedido: int, detalles: str, tiempo_entrega: int):
        # Llama al constructor de la clase base
        super().__init__(id_pedido, detalles)
        self._tiempo_entrega = tiempo_entrega  # Tiempo estimado de entrega (en minutos)

    # Método específico para mostrar la entrega del pedido express
    def mostrar_entrega(self):
        print(f"Pedido Express: Tiempo de entrega {self._tiempo_entrega} minutos")


# Subclase PedidoNormal (hereda de Pedido)
class PedidoNormal(Pedido):
    def __init__(self, id_pedido: int, detalles: str, tipo_envio: str):
        # Llama al constructor de la clase base
        super().__init__(id_pedido, detalles)
        self._tipo_envio = tipo_envio  # Tipo de envío (por ejemplo: domicilio o recoger en tienda)

    # Método específico para mostrar el tipo de envío
    def mostrar_envio(self):
        print(f"Pedido Normal: Tipo de envío {self._tipo_envio}")


# Clase Comprobante
class Comprobante:
    def __init__(self, id_comprobante: int, detalles: str):
        self._id_comprobante = id_comprobante  # ID único del comprobante
        self._fecha = datetime.now()  # Fecha y hora actuales
        self._detalles = detalles  # Información del comprobante

    # Método para generar y mostrar un comprobante
    def generar_comprobante(self):
        print(f"Comprobante #{self._id_comprobante}: {self._detalles} - Fecha: {self._fecha}")
        return self


# Clase Cliente
class Cliente:
    def __init__(self, nombre: str, id_cliente: int):
        self._nombre = nombre  # Nombre del cliente
        self._id_cliente = id_cliente  # ID único del cliente

    # Método para realizar un pedido a través del sistema
    def realizar_pedido(self, sistema, pedido: Pedido):
        print(f"{self._nombre} realiza un pedido...")  # Mensaje informativo
        sistema.procesar_pedido(pedido)  # Procesa el pedido en el sistema


# Clase Cocina (actúa como auxiliar)
class Cocina:
    @staticmethod  # Método estático, no necesita instanciar la clase
    def preparar_alimento(pedido: Pedido):
        print(f"Preparando alimento para el pedido #{pedido._id_pedido}")  # Mensaje informativo
        pedido.set_estado("Preparado")  # Actualiza el estado del pedido


# Clase Sistema (gestiona pedidos y validaciones)
class Sistema:
    def __init__(self):
        self._pedidos: List[Pedido] = []  # Lista para almacenar pedidos

    # Método para validar los datos del pedido
    def validar_datos(self, pedido: Pedido) -> bool:
        if not pedido._detalles or not pedido._id_pedido:
            print("Error: Datos del pedido inválidos")  # Mensaje de error
            return False
        return True  # Datos válidos

    # Método para procesar el pedido
    def procesar_pedido(self, pedido: Pedido):
        try:
            if not self.validar_datos(pedido):  # Valida los datos
                raise ValueError("Pedido inválido")  # Lanza una excepción si hay error
            self._pedidos.append(pedido)  # Agrega el pedido a la lista
            # Genera un comprobante
            comprobante = Comprobante(len(self._pedidos), f"Pedido #{pedido._id_pedido} registrado")
            comprobante.generar_comprobante()
            # Envía el pedido a la cocina
            Cocina.preparar_alimento(pedido)
            print(f"Pedido #{pedido._id_pedido} procesado correctamente.\n")  # Mensaje de éxito
        except ValueError as e:  # Captura el error
            print(f"Error al procesar el pedido: {e}")  # Manejo de errores


# Programa principal
if __name__ == "__main__":
    sistema = Sistema()  # Instancia de la clase Sistema

    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", 1)

    # Crear un pedido normal
    pedido_normal = PedidoNormal(101, "Hamburguesa y papas fritas", "Domicilio")
    cliente1.realizar_pedido(sistema, pedido_normal)  # Cliente realiza el pedido

    # Crear un pedido express
    pedido_express = PedidoExpress(102, "Pizza familiar", 30)
    cliente1.realizar_pedido(sistema, pedido_express)  # Cliente realiza el pedido

    # Ver el estado final de los pedidos
    print(f"Estado del Pedido 101: {pedido_normal.get_estado()}")  # Ver estado del primer pedido
    print(f"Estado del Pedido 102: {pedido_express.get_estado()}")  # Ver estado del segundo pedido
