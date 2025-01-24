class Lead:
    """
    Clase que representa un lead (prospecto) en el proyecto.
    Un lead es alguien que intentó contactarnos, pero no tenemos suficiente información para verificar su autenticidad.
    
    Atributos:
        name (str): Nombre del lead (puede ser None).
        email (str): Correo electrónico del lead (puede ser None).
        phone (str): Número de teléfono del lead (puede ser None).
    """

    def __init__(self, name: str = None, email: str = None, phone: str = None):
        """
        Inicializa un lead con información básica.
        

        :param name: Nombre del lead (opcional).
        :param email: Correo electrónico del lead (opcional).
        :param phone: Número de teléfono del lead (opcional).
        """
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        """
        Retorna una representación legible del lead.

        :return: Cadena con el nombre (si existe) y el correo electrónico (si existe).
        """
        return f"{self.name or 'Desconocido'} - {self.email or 'Sin correo'}"

    def to_dict(self) -> dict:
        """
        Convierte la información del lead en un diccionario.

        :return: Diccionario con los datos del lead.
        """
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
