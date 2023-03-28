class Alumno:
    nombre = ""
    nota = ""

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def alumno_aprueba(self):
        if self.nota > 7:
            resultado = "APROBADO :-)"
        else:
            resultado = 'No aprobado :-('
        return resultado


estudiante1 = Alumno("David", 6)

print("Nombre Estudiante:", estudiante1.nombre)
print("Nota (> 7 aprueba):", estudiante1.nota)
print("Resultado:", estudiante1.alumno_aprueba())
