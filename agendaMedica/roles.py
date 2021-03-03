from rolepermissions.roles import AbstractUserRole

class Medico(AbstractUserRole):
    available_permissions = {
        'cadastrar_paciente': True,
        'marcar_consulta': True,
        'deletar_paciente': False,
    }

class Secretaria(AbstractUserRole):
    available_permissions = {
        'edit_patient': True,
        'deletar_paciente': True,
    }

class Enfermeira(AbstractUserRole):
    available_permissions = {
        'edit_patient': True,
        'deletar_paciente': True,
    }