---
title: Cómo crear una barra de progreso
description: Aprende cómo crear una barra de progreso usando Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Barra de Progreso, crear una barra de progreso, agregar una barra de progreso, insertar una barra de progreso.
type: docs
weight: 73
url: /es/net/how-to-create-a-progress-bar/
---

## **Escenarios de uso posibles**
La razón principal para crear una barra de progreso en Excel es transformar números en bruto en una métrica visual comprensible al instante, facilitando la comprensión de datos complejos de un vistazo.

1. Claridad Visual Mejorada e Información Inmediata: Una tabla con números como "75%", "8/10" o "15000/20000" requiere esfuerzo cognitivo para interpretar. Una barra de progreso permite que cualquier persona, desde un gerente senior hasta un miembro del equipo, entienda el estado, rendimiento o nivel de finalización al instante sin leer y procesar los números.

2. Identificación Rápida de Estado y Tendencias: Nuestros cerebros están programados para procesar información visual como la longitud y el color más rápido que el texto. Puedes ver rápidamente: ¿Qué está en camino? (Barrasp largas y verdes), ¿Qué va retrasado? (Barras cortas y rojas) y ¿Qué casi está completo? (Barras casi llenas). Esto permite decisiones y priorización más rápidas.

3. Mejoras en Paneles e Informes: Las barras de progreso son fundamentales en paneles efectivos. Hacen que los informes sean más atractivos, profesionales y fáciles de presentar. Un panel con barras de progreso para indicadores clave de rendimiento (KPI) es mucho más efectivo que una hoja llena de números.

4. Motivación y Seguimiento del Rendimiento: Para equipos de ventas, rastreadores de proyectos o metas personales, ver una representación visual del progreso puede ser altamente motivador. Proporciona una sensación clara y satisfactoria de logro a medida que la barra se llena.

5. Comunicación Eficiente: En reuniones o presentaciones, una barra de progreso transmite el mensaje mucho más eficazmente que decir, "Estamos al 72.5% de nuestro objetivo trimestral." La visualización hace el trabajo, ahorra tiempo y previene malentendidos.


## **Cómo Crear una Barra de Progreso en Excel**

Crear una barra de progreso en Excel es una excelente manera de visualizar la finalización de tareas, el progreso de un proyecto o las tendencias de datos. Aquí tienes una guía sobre cómo crear una usando diferentes métodos, junto con algunos consejos para personalización.

### **Usando Formato Condicional (Barras de Datos)**
1. Prepara tus datos: Ten al menos una columna de valores que representen el progreso, idealmente como porcentajes (por ejemplo, 0.5 para 50%). Puedes calcular esto usando una fórmula como =Valor_Actual/Valor_Meta.
2. Selecciona celdas: Resalta las celdas que contienen tus valores porcentuales.
3. Aplica barras de datos: Ve a la pestaña Inicio > Formato condicional > Barras de datos. Elige rellenado con gradiente o relleno sólido.
4. Personaliza (Opcional): Para mayor control, ve a Formato condicional > Administrar reglas > Editar regla.
5. Establece los tipos Mínimo y Máximo a Número, con valores 0 y 1, respectivamente, para asegurar una correcta visualización del 0-100%.
6. Ajusta colores y estilos de borde aquí. Para mostrar tanto el número como la barra, edita la regla y asegúrate de que "Mostrar solo barra" no esté marcado.

### **Usando la función REPT (Barra basada en texto)**
1. Ingresa una fórmula: En una celda, usa una fórmula como =REPT("█", B2*10) & REPT("░", 10 - B2*10), donde B2 contiene el porcentaje de progreso. Este ejemplo crea una barra de 10 caracteres: cuadrados rellenos (█) para completar y cuadrados ligeros (░) para lo que falta.
2. Ajusta y da formato: Modifica el multiplicador (por ejemplo, *20 para una barra de 20 caracteres) según la longitud deseada. Usa una fuente monoespaciada como Courier New para un alineamiento correcto.

### **Usando un gráfico (Para paneles de control)**
1. Estructura los datos: Crea una tabla para calcular los valores:
|**Número**|**A**|**B**|
| :- | :- | :- |
|1|Progreso|Restante|
|2|=Valor_Actual/Valor_Meta|=1-A2|
<br>
2. Inserta gráfico: Selecciona los datos > pestaña Insertar > Gráficos > Gráfico de barras apiladas 2D.
3. Da formato al gráfico: Quita el título, la leyenda y las líneas de cuadrícula para un aspecto limpio. Haz clic derecho en la serie de datos "Restante" > Formato de serie de datos > Relleno > Sin relleno. Haz clic derecho en la serie "Progreso" > Formato de serie de datos > Ajusta la superposición de series a 100% y el ancho del espacio a 0%. Da formato al eje horizontal: establece los límites > mínimo a 0 y máximo a 1.

## **Cómo Crear una Barra de Progreso en Aspose.Cells**

### **Usar la función REPT (barra basada en texto) para crear una barra de progreso**
Por favor vea el siguiente código de muestra. Crea un nuevo libro y añade algunos datos de ejemplo. Luego agrega la función REPT (barra basada en texto) basada en los datos iniciales. Finalmente, guarda el libro en un archivo xlsx. La siguiente captura de pantalla muestra el formato condicional (Barras de Datos) creado por Aspose.Cells en el archivo Excel de salida.
<br>
<img src="formula.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-Formula.cs" >}}

### **Usar formato condicional (Barras de Datos) para crear una barra de progreso**
Por favor vea el siguiente código de muestra. Crea un nuevo libro y añade algunos datos de ejemplo. Luego añade formato condicional (Barras de Datos) basado en los datos iniciales y establece propiedades relevantes. Finalmente, guarda el libro en un archivo xlsx. La siguiente captura de pantalla muestra el formato condicional (Barras de Datos) creado por Aspose.Cells en el archivo Excel de salida.
<br>
<img src="databar.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-ConditionalFormats.cs" >}}


### **Usar gráfico de barras apiladas para crear una barra de progreso**
Por favor vea el siguiente código de muestra. Carga el [archivo Excel de muestra](sample.xlsx) que contiene algunos datos de ejemplo. Luego crea un gráfico de barras apiladas basado en los datos iniciales y configura propiedades relevantes. Finalmente, guarda el libro en formato XLSX de salida. La siguiente captura de pantalla muestra la barra de progreso creada por Aspose.Cells en el archivo Excel de salida.

<br>
<img src="barchart.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Use-BarStacked-Chart.cs" >}}
