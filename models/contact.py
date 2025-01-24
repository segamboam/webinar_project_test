class Contact:
    """
    Clase que representa un contacto en el proyecto.
    """

    def __init__(self, first_name: str, last_name: str, email: str, phone: str = None):
        """
        Inicializa un contacto con información básica.

        :param first_name: Nombre del contacto.
        :param last_name: Apellido del contacto.
        :param email: Correo electrónico del contacto.
        :param phone: Número de teléfono del contacto (opcional).
        """          
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        """
        Retorna una representación legible del contacto.

        :return: Cadena con el nombre completo y el correo electrónico.
        """
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone}"

    def to_dict(self) -> dict:
        """
        Convierte la información del contacto en un diccionario.

        :return: Diccionario con los datos del contacto.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone
        }


