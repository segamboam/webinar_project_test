# main.py
from models.contact import Contact
from models.lead import Lead
from manager import ContactManager

# Inicializar el gestor de contactos
manager = ContactManager()

# Datos iniciales: Contactos
initial_contacts = [
    Contact("Alice", "Brown", None, "1231112223"),
    Contact("Bob", "Crown", "bob@crowns.com", None),
    Contact("Carlos", "Drew", "carl@drewess.com", "3453334445"),
    Contact("Doug", "Emerty", None, "4564445556"),
    Contact("Egan", "Fair", "eg@fairness.com", "5675556667"),
]

# Datos iniciales: Leads
initial_leads = [
    Lead(None, "kevin@keith.com", None),
    Lead("Lucy", "lucy@liu.com", "3210001112"),
    Lead("Mary Middle", "mary@middle.com", "3331112223"),
    Lead(None, None, "4442223334"),
    Lead(None, "ole@olson.com", None),
]

# Agregar contactos iniciales al gestor
for contact in initial_contacts:
    manager.add_contact(contact)

# Agregar leads iniciales al gestor
for lead in initial_leads:
    manager.add_lead(lead)

# Datos de registros
registrants = [
    # Caso 1: Coincidencia con un contacto por correo electrónico
    {"name": "Carlos Drew", "email": "carl@drewess.com", "phone": None},
    # Caso 2: Coincidencia con un contacto por teléfono
    {"name": "Doug Emerty", "email": None, "phone": "4564445556"},
    # Caso 3: Coincidencia con un lead por correo electrónico
    {"name": "Kevin Keith", "email": "kevin@keith.com", "phone": None},
    # Caso 4: Coincidencia con un lead por teléfono
    {"name": "Anonymous", "email": None, "phone": "4442223334"},
    # Caso 5: Registro sin coincidencias (nuevo contacto)
    {"name": "John Doe", "email": "john@doe.com", "phone": "3214567890"},
    # Caso 6: Registro con correo inválido
    {"name": "Invalid Email", "email": "invalid-email@", "phone": "1231231234"},
    # Caso 7: Registro sin correo ni teléfono
    {"name": "No Data", "email": None, "phone": None},
    # Caso 8: Coincidencia parcial con un lead y contacto
    {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": "1234567890"},
]


# Procesar registros
print("Procesando registros...\n")
for registrant in registrants:
    manager.process_registrant(registrant)

# Ver resultados
print("\nContactos finales:")
for contact in manager.contacts:
    print(contact)

print("\nLeads finales:")
for lead in manager.leads:
    print(lead)
