#Desarrolla un sistema de gestion de un cine en Phyton. 
#Crea un conjunto de clases para representar peliculas, espectadores y funciones de cine. 
#implementa relaciones entre estas clases para administrar la venta de entradas la programcion de funciones 
#y la disponivilidad de asientos. Detalla las propiedades esenciales y metodos de cada clase, 
#asegurando un diseño escalable para futuras actulaizaciones. 
#los objetos de la clase pelicula deben almacenar detalles como titulo, genero, duracion 
#y horarios de proyeccion implementa metodos para actualizar la programcion de peliuclas y gestionar los horaios de proyeccion. 
#la clase funcion debe permitir la reserva y venta de entradas para una pelicula especifica registrar la fecha 
#y hora de la funcion y manterner registro de los asientos disponibles imcluye metodos para reservar asienteps 
#calucular el precio total y gestioanr el estado de la reserva (pendiente, confirmada, cancelada). 
#ademas las funciones regulares de cine se requiere introducicr una funcion especial nocturl¿na con caracteristicas 
#diferentes modifica la clase funcion para manejar las funciones nocturnas de manera especial sin alterar el funcionamiento
#de las funciones regulares, las nocturnas tienen unprecio diferente horarios distintos y politica espical de reservas
#Usando herencia, polimorfismo, abstraccion y encapsulamiento y ademas composicon y agregacion donde corresponda mostrando 
#al menos un ejemplo de cada uno

from datetime import datetime

class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.horarios = []

    def agregar_horario(self, horario):
        self.horarios.append(horario)

    def actualizar_horario(self, horario_viejo, horario_nuevo):
        if horario_viejo in self.horarios:
            self.horarios.remove(horario_viejo)
            self.horarios.append(horario_nuevo)
            return True
        else:
            return False

class Funcion:
    def __init__(self, pelicula, fecha, hora, precio_base, asientos_disponibles):
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora
        self.precio_base = precio_base
        self.asientos_disponibles = asientos_disponibles
        self.reservas = {}

    def reservar_asiento(self, espectador, cantidad):
        if cantidad <= self.asientos_disponibles:
            self.reservas[espectador] = cantidad
            self.asientos_disponibles -= cantidad
            return True
        else:
            return False

    def calcular_precio_total(self, cantidad):
        return self.precio_base * cantidad

    def confirmar_reserva(self, espectador):
        if espectador in self.reservas:
            del self.reservas[espectador]
            return True
        else:
            return False

class FuncionNocturna(Funcion):
    def __init__(self, pelicula, fecha, hora, precio_base, asientos_disponibles):
        super().__init__(pelicula, fecha, hora, precio_base, asientos_disponibles)
        self.precio_base = precio_base * 1.2  # Precio base aumentado para funciones nocturnas

class Espectador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.funciones = []

    def agregar_funcion(self, funcion):
        self.funciones.append(funcion)

    def buscar_funcion(self, pelicula, fecha):
        for funcion in self.funciones:
            if funcion.pelicula == pelicula and funcion.fecha == fecha:
                return funcion
        return None

    def vender_entrada(self, pelicula, fecha, espectador, cantidad):
        funcion = self.buscar_funcion(pelicula, fecha)
        if funcion:
            if funcion.reservar_asiento(espectador, cantidad):
                precio_total = funcion.calcular_precio_total(cantidad)
                print(f"Se han vendido {cantidad} entradas para la película {pelicula.titulo} el {fecha} a {espectador.nombre} por un total de ${precio_total}.")
                return True
            else:
                print("Lo sentimos, no hay suficientes asientos disponibles.")
                return False
        else:
            print("Función no encontrada.")
            return False

# Ejemplo de uso
pelicula1 = Pelicula("Titanic", "Drama", 195)
pelicula1.agregar_horario("2024-03-01 19:00")
pelicula1.agregar_horario("2024-03-01 21:30")

funcion1 = Funcion(pelicula1, "2024-03-01", "19:00", 10, 100)

pelicula2 = Pelicula("El Señor de los Anillos", "Fantasía", 228)
pelicula2.agregar_horario("2024-03-02 18:00")
pelicula2.agregar_horario("2024-03-02 21:00")

funcion2 = FuncionNocturna(pelicula2, "2024-03-02", "21:00", 12, 80)

espectador1 = Espectador("Juan", 25)

cine = Cine("Cine XYZ")
cine.agregar_funcion(funcion1)
cine.agregar_funcion(funcion2)

cine.vender_entrada(pelicula1, "2024-03-01", espectador1, 2)
cine.vender_entrada(pelicula2, "2024-03-02", espectador1, 3)


# Este ejemplo utiliza herencia para diferenciar entre funciones regulares y nocturnas, 
# composición para conectar películas y funciones con el cine, 
# y agregación para manejar las reservas de asientos en cada función. 
# Además, se utilizan abstracción y encapsulamiento para definir las propiedades y métodos esenciales de cada clase.