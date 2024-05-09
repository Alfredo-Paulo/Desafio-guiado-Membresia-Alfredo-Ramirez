from abc import ABC , abstractmethod


membresia={
    1:"basica",
    2:"familiar",
    3:"sin Conexion",
    4:"pro"
}


class Membresia(ABC): #clase abstracta
    def __init__(self,correo_suscriptor,numero_tarjeta) -> None:
        self.__correo_suscriptor=correo_suscriptor
        self.__numero_tarjeta= numero_tarjeta
    
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self):
        pass
    
    
    def _crear_nueva_membresia(self, nueva_membresia):
        if nueva_membresia== 1:
            print("bienvenido a la suscripcion basica")
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia== 2:
            print("bienvenido a la suscripcion FAMILIAR")
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia==3:
            print("bienvenido a la suscripcion SIN-CONEXION")
            return Sin_Conexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia ==4:
            print("bienvenido a la suscripcion PRO")
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            print("no se reconoce membresia")
            
class Gratis(Membresia):
    print("Bienvenido a la suscripcion GRATIS")
    costo=0
    dispositivos=1
    def __init__(self, correo_suscriptor, numero_tarjeta) -> None:
        super().__init__(correo_suscriptor, numero_tarjeta)
        print("--Su suscripcion es Gratuita---")
    
    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1,2,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self 

class Basica(Membresia):
    costo=3000
    dispositivos=2
    
    def __init__(self,correo_suscriptor,numero_tarjeta):
        super().__init__(correo_suscriptor,numero_tarjeta)  
        if isinstance(self,Familiar) or isinstance(self,Sin_Conexion):
            self.__dias_gratis=7
        elif isinstance(self, Pro):
            self.__dias_gratis=15
            
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor,self.numero_tarjeta)

    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [2,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self


class Familiar(Basica):
    costo=5000
    dispositivos=5
    
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self   
    
    def control_parental(self):
        pass
    


class Sin_Conexion(Basica):
    costo=3500
    dispositivos=2

    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,2,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self   
        
    def contenido_maximo(self):
        pass



class Pro(Familiar,Sin_Conexion):
    costo=7000
    dispositivos=6
    
    
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,2,3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self  

g=Gratis("correo@correo.cl",12345678910)

print(type(g))
print("costo de la suscricion", g.costo)
print("Dispositivos permitidos",g.dispositivos)

b=g.cambiar_suscripcion(1)
print("costo de la suscricion", b.costo)
print("Dispositivos permitidos",b.dispositivos)

f = b.cambiar_suscripcion(2)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

f = f.cambiar_suscripcion(1)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

f = f.cambiar_suscripcion(4)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

#Vamos a cancelar la suscripción del usuario "f" en en este momento es "Pro"... Por consecuencia, nos debería dejar en el gratis

f = f.cancelar_suscripcion()
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

#Vamos a dar una número de membremsia que no existe...

f = f.cambiar_suscripcion(5)