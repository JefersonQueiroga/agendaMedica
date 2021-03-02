from rolepermissions.roles import AbstractUserRole

class Medico(AbstractUserRole):
    available_permissions = {
        'cadastrar_paciente': True,
        'marcar_consulta': True,
    }

class Secretaria(AbstractUserRole):
    available_permissions = {
        'edit_patient': True,
    }