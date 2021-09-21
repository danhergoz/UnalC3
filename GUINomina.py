from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import csv
import FunctionsNomina

def procesarDatos(sena_icbf, perfil, smmlv, sueldo, dotacion, profesiones):
    if sueldo == '':
        messagebox.showwarning('Sueldo', 'Por favor, ingrese un sueldo')
        return
    sueldo_temp = int(sueldo)
    smmlv_temp = int(smmlv)
    if sueldo_temp < smmlv_temp:
        entry_sueldo.config(bg = 'red')
    if perfil == '':
        messagebox.showwarning('Perfil', 'Ingrese un perfil')
        return
    elif sueldo == '':
        messagebox.showwarning('Sueldo', 'Ingrese un sueldo')
        return
    auxilio_transporte_temp = FunctionsNomina.calcularAuxilioTransporte(sueldo_temp, smmlv_temp)
    auxilio_transporte.set(str(auxilio_transporte_temp))
    pension_temp = FunctionsNomina.calcularPension(sueldo_temp)
    pension.set(str(pension_temp))
    salud_temp = FunctionsNomina.calcularSalud(sueldo_temp)
    salud.set(str(salud_temp))
    ciou08.set(profesiones[perfil]['Código CIOU-08'])
    clase_riesgo.set(profesiones[perfil]['Clase de Riesgo'])
    riesgo.set(profesiones[perfil]['Cotizacion'])
    arl_temp = FunctionsNomina.calcularArl(sueldo_temp)
    arl.set(str(arl_temp))
    caja_compensacion_temp = FunctionsNomina.calcularCajaCompensacion(int(sueldo))
    caja_compensacion.set(str(caja_compensacion_temp))
    sena_temp = 0
    icbf_temp = 0
    if sena_icbf == 'Si':
        sena_temp = FunctionsNomina.calcularSena(sueldo_temp)
        sena.set(str(sena_temp))
        icbf_temp = FunctionsNomina.calcularIcbf(sueldo_temp)
        icbf.set(str(icbf_temp))
    else:
        sena.set('0')
        icbf.set('0')
    total_1_temp = (sueldo_temp + auxilio_transporte_temp + pension_temp + salud_temp +
                    arl_temp + caja_compensacion_temp + sena_temp + icbf_temp)
    total_1.set(str(total_1_temp))
    cesantias_mensual_temp = int((sueldo_temp + auxilio_transporte_temp) / 12)
    cesantias_mensual.set(str(cesantias_mensual_temp))
    intereses_cesantias_mensual_temp = int(cesantias_mensual_temp * 0.12)
    intereses_cesantias_mensual.set(str(intereses_cesantias_mensual_temp))
    prima_mensual_temp = int(((sueldo_temp + auxilio_transporte_temp) / 2) / 6)
    prima_mensual.set(str(prima_mensual_temp))
    vacaciones_mensual_temp = int((sueldo_temp / 2) / 12)
    vacaciones_mensual.set(str(vacaciones_mensual_temp))
    dotacion_mensual_temp = 0
    if dotacion != '':
        dotacion_mensual_temp = int(dotacion)
    if dotacion_mensual_temp > smmlv_temp * 2:
        messagebox.showwarning('Dotación', 'La dotación no puede superar a 2 SMMLV')
    dotacion_mensual.set(str(dotacion_mensual_temp))
    total_2_temp = (total_1_temp + cesantias_mensual_temp + intereses_cesantias_mensual_temp +
                    prima_mensual_temp + vacaciones_mensual_temp + dotacion_mensual_temp)
    total_2.set(str(total_2_temp))
    valor_hora_temp = int(total_2_temp / 192)
    valor_hora.set(str(valor_hora_temp))
    valor_minuto_temp = int(valor_hora_temp / 60)
    valor_minuto.set(str(valor_minuto_temp))

root = Tk()
root.title('Reporte Nómina')
root.resizable(0,0)
root.iconbitmap('pig.ico')

frame1 = Frame(root)
frame1.grid(row = 0, column = 0, columnspan = 2)

frame2 = Frame(root)
frame2.grid(row = 1, column = 0)

frame3 = Frame(root)
frame3.grid(row = 1, column = 1, sticky = 'n')

auxilio_transporte = StringVar()
pension = StringVar()
salud = StringVar()
ciou08 = StringVar()
clase_riesgo = StringVar()
riesgo = StringVar()
arl = StringVar()
caja_compensacion = StringVar()
sena = StringVar()
icbf = StringVar()
total_1 = StringVar()
cesantias_mensual = StringVar()
intereses_cesantias_mensual = StringVar()
prima_mensual = StringVar()
vacaciones_mensual = StringVar()
dotacion_mensual = StringVar()
total_2 = StringVar()
valor_hora = StringVar()
valor_minuto = StringVar()
salario_minimo = StringVar()
salario_minimo.set('908526')

label_sena_icbf = Label(frame1, text = 'SENA/ICBF:')
label_sena_icbf.grid(row = 0, column = 0, padx = 3, pady =3)
combo_sena_icbf = Combobox(frame1)
combo_sena_icbf['values'] = ('Si', 'No')
combo_sena_icbf.current(1)
combo_sena_icbf.grid(row = 0, column = 1, padx = 3, pady =3)

label_cargo = Label(frame2, text = 'Cargo:')
label_cargo.grid(row = 0, column = 0, padx = 3, pady =3)
entry_cargo = Entry(frame2)
entry_cargo.grid(row = 0, column = 1, padx = 3, pady =3)

label_perfiles = Label(frame1, text = 'Perfil:')
label_perfiles.grid(row = 1, column = 0, padx = 3, pady =3)
combo_perfiles = Combobox(frame1)
combo_perfiles.grid(row = 1, column = 1, padx = 3, pady =3)

label_smmlv = Label(frame2, text = 'SMMLV:')
label_smmlv.grid(row = 2, column = 0, padx = 3, pady =3)
entry_smmlv = Entry(frame2, state = DISABLED, textvariable = salario_minimo)
entry_smmlv.grid(row = 2, column = 1, padx = 3, pady =3)

label_sueldo = Label(frame2, text = 'Sueldo base:')
label_sueldo.grid(row = 3, column = 0, padx = 3, pady =3)
entry_sueldo = Entry(frame2)
entry_sueldo.grid(row = 3, column = 1, padx = 3, pady =3)

label_auxilio_transporte = Label(frame2, text = 'Auxilio Transporte:')
label_auxilio_transporte.grid(row = 4, column = 0, padx = 3, pady =3)
entry_auxilio_transporte = Entry(frame2, textvariable = auxilio_transporte)
entry_auxilio_transporte.grid(row = 4, column = 1, padx = 3, pady =3)

label_seguridad_social = Label(frame2, text = 'SEGURIDAD SOCIAL')
label_seguridad_social.grid(row = 5, column = 0, columnspan = 2, padx = 3, pady =3)

label_pension = Label(frame2, text = 'Pensión:')
label_pension.grid(row = 6, column = 0, padx = 3, pady =3)
entry_pension = Entry(frame2, textvariable = pension)
entry_pension.grid(row = 6, column = 1, padx = 3, pady =3)

label_salud = Label(frame2, text = 'Salud:')
label_salud.grid(row = 7, column = 0, padx = 3, pady =3)
entry_salud = Entry(frame2, textvariable = salud)
entry_salud.grid(row = 7, column = 1, padx = 3, pady =3)

label_ciuo08 = Label(frame2, text = 'CIUO 08:')
label_ciuo08.grid(row = 8, column = 0, padx = 3, pady =3)
entry_ciuo08 = Entry(frame2, textvariable = ciou08)
entry_ciuo08.grid(row = 8, column = 1, padx = 3, pady =3)

label_clase_riesgo = Label(frame2, text = 'Clase de Riesgo:')
label_clase_riesgo.grid(row =9, column = 0, padx = 3, pady =3)
entry_clase_riesgo = Entry(frame2, textvariable = clase_riesgo)
entry_clase_riesgo.grid(row = 9, column = 1, padx = 3, pady =3)

label_riesgo = Label(frame2, text = 'Riesgo:')
label_riesgo.grid(row = 10, column = 0, padx = 3, pady =3)
entry_riesgo = Entry(frame2, textvariable = riesgo)
entry_riesgo.grid(row = 10, column = 1, padx = 3, pady =3)

label_arl = Label(frame2, text = 'ARL:')
label_arl.grid(row = 11, column = 0, padx = 3, pady =3)
entry_arl = Entry(frame2, textvariable = arl)
entry_arl.grid(row = 11, column = 1, padx = 3, pady =3)

label_parafiscales = Label(frame2, text = 'PARAFISCALES')
label_parafiscales.grid(row = 12, column = 0, columnspan = 2, padx = 3, pady =3)

label_caja_compensacion = Label(frame2, text = 'Caja de Compensación:')
label_caja_compensacion.grid(row = 13, column = 0, padx = 3, pady =3)
entry_caja_compensacion = Entry(frame2, textvariable = caja_compensacion)
entry_caja_compensacion.grid(row = 13, column = 1, padx = 3, pady =3)

label_sena = Label(frame2, text = 'SENA:')
label_sena.grid(row = 14, column = 0, padx = 3, pady =3)
entry_sena = Entry(frame2, textvariable = sena)
entry_sena.grid(row = 14, column = 1, padx = 3, pady =3)

label_icbf = Label(frame2, text = 'ICBF:')
label_icbf.grid(row = 15, column = 0, padx = 3, pady =3)
entry_icbf = Entry(frame2, textvariable = icbf)
entry_icbf.grid(row = 15, column = 1, padx = 3, pady =3)

label_total_1 = Label(frame2, text = 'Total 1:')
label_total_1.grid(row = 16, column = 0, padx = 3, pady =3)
entry_total_1 = Entry(frame2, textvariable = total_1)
entry_total_1.grid(row = 16, column = 1, padx = 3, pady =3)

label_prestaciones_sociales = Label(frame3, text = 'PRESTACIONES SOCIALES (Previsiones)')
label_prestaciones_sociales.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady =3)

label_cesantias_mensual = Label(frame3, text = 'Cesantías mensual:')
label_cesantias_mensual.grid(row = 1, column = 0, padx = 3, pady =3)
entry_cesantias_mensual = Entry(frame3, textvariable = cesantias_mensual)
entry_cesantias_mensual.grid(row = 1, column = 1, padx = 3, pady =3)

label_intereses_cesantias = Label(frame3, text = 'Intereses de Cesantías Mensual:')
label_intereses_cesantias.grid(row = 2, column = 0, padx = 3, pady =3)
entry_intereses_cesantias = Entry(frame3, textvariable = intereses_cesantias_mensual)
entry_intereses_cesantias.grid(row = 2, column = 1, padx = 3, pady =3)

label_prima_mensual = Label(frame3, text = 'Prima Mensual:')
label_prima_mensual.grid(row = 3, column = 0, padx = 3, pady =3)
entry_prima_mesual = Entry(frame3, textvariable = prima_mensual)
entry_prima_mesual.grid(row = 3, column = 1, padx = 3, pady =3)

label_otros_previsiones = Label(frame3, text = 'OTROS (Previsiones)')
label_otros_previsiones.grid(row = 4, column = 0, columnspan = 2, padx = 3, pady =3)

label_vacaciones_mensual = Label(frame3, text = 'Vacaciones Mensual:')
label_vacaciones_mensual.grid(row = 5, column = 0, padx = 3, pady =3)
entry_vacaciones_mensual = Entry(frame3, textvariable = vacaciones_mensual)
entry_vacaciones_mensual.grid(row = 5, column = 1, padx = 3, pady =3)

label_dotacion_mensual = Label(frame3, text = 'Dotación Mensual:')
label_dotacion_mensual.grid(row = 6, column = 0, padx = 3, pady =3)
entry_dotacion_mensual = Entry(frame3, textvariable = dotacion_mensual)
entry_dotacion_mensual.grid(row = 6, column = 1, padx = 3, pady =3)

label_total_2 = Label(frame3, text = 'Total 2:')
label_total_2.grid(row = 7, column = 0, padx = 3, pady =3)
entry_total_2 = Entry(frame3, textvariable = total_2)
entry_total_2.grid(row = 7, column = 1, padx = 3, pady =3)

label_valor_hora = Label(frame3, text = 'Valor Hora:')
label_valor_hora.grid (row = 8, column = 0, padx = 3, pady =3)
entry_valor_hora = Entry(frame3, textvariable = valor_hora)
entry_valor_hora.grid(row = 8, column = 1, padx = 3, pady =3)

label_valor_minuto = Label(frame3, text = 'Valor Minuto:')
label_valor_minuto.grid(row = 9, column = 0, padx = 3, pady =3)
entry_valor_minuto = Entry(frame3, textvariable = valor_minuto)
entry_valor_minuto.grid(row = 9, column = 1, padx = 3, pady =3)

labels = (label_smmlv, label_sena, label_icbf,label_sena_icbf, label_arl, label_total_2,
          label_total_1, label_valor_minuto, label_valor_hora, label_dotacion_mensual,
          label_vacaciones_mensual, label_cesantias_mensual, label_prima_mensual,
          label_cargo, label_ciuo08, label_pension, label_perfiles, label_sueldo,
          label_salud, label_riesgo, label_clase_riesgo, label_auxilio_transporte,
          label_caja_compensacion)

for item in labels:
    item.grid(sticky = 'w')

entries_combos = (combo_sena_icbf, combo_perfiles, entry_icbf, entry_sena, entry_sueldo,
                  entry_smmlv, entry_arl, entry_cargo, entry_salud, entry_ciuo08,
                  entry_valor_minuto, entry_valor_hora, entry_total_2, entry_total_1,
                  entry_dotacion_mensual, entry_vacaciones_mensual, entry_intereses_cesantias,
                  entry_caja_compensacion, entry_pension, entry_prima_mesual, entry_riesgo,
                  entry_clase_riesgo, entry_auxilio_transporte, entry_cesantias_mensual)

for item in entries_combos:
    item.grid(sticky = 'w')

only_combos = (combo_sena_icbf, combo_perfiles)

for item in only_combos:
    item.config(width = 50)

only_entries = (entry_icbf, entry_sena, entry_sueldo,
                  entry_smmlv, entry_arl, entry_cargo, entry_salud, entry_ciuo08,
                  entry_valor_minuto, entry_valor_hora, entry_total_2, entry_total_1,
                  entry_dotacion_mensual, entry_vacaciones_mensual, entry_intereses_cesantias,
                  entry_caja_compensacion, entry_pension, entry_prima_mesual, entry_riesgo,
                  entry_clase_riesgo, entry_auxilio_transporte, entry_cesantias_mensual)

for item in only_entries:
    item.config(width = 13)

professions_dict = {}
professions_list = []
new_line = ''

with open('Professions.csv', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        for item in line:
            new_line += item
        line_splited = new_line.split(';')
        new_line = ''
        data = {}
        data['Código CIOU-08'] = line_splited[1]
        data['Clase de Riesgo'] = line_splited[2]
        cotizacion = line_splited[3]
        cotizacion = cotizacion.replace('%', '')
        cotizacion2 = int(cotizacion)
        data['Cotizacion'] = cotizacion2 / 1000
        professions_dict[line_splited[0]] = data
        professions_list.append(line_splited[0])

professions_tuple = tuple(professions_list)
combo_perfiles['values'] = professions_tuple

boton_procesar = Button(root, text = 'Procesar', bg = 'black', fg = 'white',
                        command = lambda:procesarDatos(combo_sena_icbf.get(), combo_perfiles.get(),
                                                       entry_smmlv.get(), entry_sueldo.get(),
                                                       entry_dotacion_mensual.get(), professions_dict))
boton_procesar.grid(row = 2, column = 0, columnspan = 2, padx = 3, pady = 3)

root.mainloop()