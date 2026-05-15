from canal import CanalNoticias
from suscriptores import SuscriptorEmail, SuscriptorSMS

canal = CanalNoticias("Claro")
suscriptor1 = SuscriptorEmail("Pacho")
suscriptor2 = SuscriptorSMS("beto")

canal.suscribir(suscriptor1)
canal.suscribir(suscriptor2)

canal.publicar("Hola, pasate a claro con tu mismo número")

print(suscriptor1.mensajes)
print(suscriptor2.mensajes)
