def calcularAuxilioTransporte(sueldo, smmlv):
    if sueldo <= smmlv * 2:
        return 106454
    else:
        return 0
def calcularPension(sueldo):
    return int(sueldo * 0.12)

def calcularSalud(sueldo):
    return int(sueldo * 0.085)

def calcularArl(sueldo):
    return int(sueldo * 0.01044)

def calcularCajaCompensacion(sueldo):
    return int(sueldo * 0.04)

def calcularSena(sueldo):
    return int(sueldo * 0.02)

def calcularIcbf(sueldo):
    return int(sueldo * 0.03)