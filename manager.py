# manager.py
from models.contact import Contact
from models.lead import Lead
from utils.validations import is_valid_email


class ContactManager:
    """
    Clase para gestionar contactos, leads y registros.
    """

    def __init__(self):
        """
        Inicializa las listas de contactos y leads.
        """
        self.contacts = []  # Lista de instancias de Contact
        self.leads = []     # Lista de instancias de Lead

    def add_contact(self, contact: Contact):
        """
        Agrega un nuevo contacto a la lista si no existe ya.

        :param contact: Instancia de Contact a agregar.
        """

        self.contacts.append(contact)

    def add_lead(self, lead: Lead):
        """
        Agrega un nuevo lead a la lista si no existe ya.

        :param lead: Instancia de Lead a agregar.
        """

        self.leads.append(lead)

    def process_registrant(self, registrant: dict):
        """
        Procesa un registro según las reglas descritas.

        :param registrant: Diccionario con los datos del registrado (name, email, phone).
        """
        name = registrant.get("name")
        email = registrant.get("email")
        phone = registrant.get("phone")

        # Validar el formato del correo electrónico
        if email and not is_valid_email(email):
            print(f"Correo electrónico inválido: {email}")
            return
        if (email is None) & (phone is None) :
            print(f"Datos de contactos no validos")
            return

        # Buscar en contactos por email
        for contact in self.contacts:
            prove_contact_email = (contact.email == email) & ( email != None) 
            if prove_contact_email:
                print(f"El registrado ya existe en contactos por email: {contact}")
                return

        # Buscar en contactos por teléfono
        
        for contact in self.contacts:
            prove_contact_phone = (contact.phone == phone) & ( phone != None)
            if prove_contact_phone:
                print(f"El registrado ya existe en contactos por telefono: {contact}")
                return

        # Buscar en leads por email
        for lead in self.leads:
            prove_lead_email = (lead.email == email ) & ( email != None) 
            if prove_lead_email:
                print(f"El registrado coincide con un lead por email, convirtiéndolo en contacto: {lead}")
                self.leads.remove(lead)
                self.add_contact(Contact(name or lead.name, email, phone or lead.phone))
                return

        # Buscar en leads por teléfono
        for lead in self.leads:
            prove_lead_phone = (lead.phone == phone) & ( phone != None)
            if prove_lead_phone:
                print(f"El registrado coincide con un lead por telefono, convirtiéndolo en contacto: {lead}")
                self.leads.remove(lead)
                self.add_contact(Contact(name or lead.name, email or lead.email, phone))
                return

        # Si no hay coincidencias, agregar como nuevo contacto
        print(f"Agregando un nuevo contacto: {name}, {email}, {phone}")
        self.add_contact(Contact(name, email, phone))
