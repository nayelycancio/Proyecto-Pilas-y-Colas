class PilaApoyos:
    def __init__(self):
        self.items = []

    def empilar(self, item):
        self.items.append(item)

    def desempilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar_pila(self):
        return self.items

    def __str__(self):
        return str(self.items) 