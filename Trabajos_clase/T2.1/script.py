def calculoeficiencia (nombre, disponibilidad, replicas):

	if replicas == 1:
		disp_solucion = disponibilidad
	else:
		disponibilidad_anterior = calculoeficiencia(nombre, disponibilidad, replicas - 1)
		disp_solucion = disponibilidad_anterior + (1 - disponibilidad_anterior) * disponibilidad

	print ('Componente: ' + nombre)
	print ('\tReplicas: ' + str(replicas) )
	print ('\tDisponibilidad: ' + str(disp_solucion) )

	return disp_solucion

import csv

solucion = 1
lector = csv.reader(open('datos.csv','rb'))
for fila in lector:
	solucion *= calculoeficiencia(fila[0], float(fila[1]), float(fila[2]))
	print ('-----------------------------------------')

print ('Disponibilidad final del sistema: ' + str(solucion))