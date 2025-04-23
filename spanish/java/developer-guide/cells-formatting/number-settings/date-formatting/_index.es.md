---
title: Cómo formatear número como fecha
type: docs
weight: 10
url: /es/java/format-number-to-date/
description: Este artículo presentará cómo formatear número a fecha usando la API Aspose.Cells for Java.
keywords: formatear número como fecha, configuraciones de número en la celda, formato número a fecha, configuraciones de fecha, formato de fecha.
---

## **Escenarios de uso posibles**
Formatear números como fechas en Excel (o cualquier software de hojas de cálculo) es importante por varias razones, especialmente cuando trabajas con datos que incluyen información de tiempo o programación. He aquí por qué es beneficioso formatear números a fechas:

1. Interpretación adecuada de los valores de fecha: en Excel, las fechas se almacenan como números seriales (por ejemplo, 1 representa el 1 de enero de 1900 y 44210 representa el 6 de septiembre de 2021). Si estos números no están formateados como fechas, los usuarios podrían ver números sin sentido en lugar de fechas reconocibles. Formatearlos correctamente permite que Excel los muestre como fechas reales (por ejemplo, 06/09/2021 en lugar de 44210).
1. Simplifica cálculos relacionados con el tiempo: Excel puede realizar muchos cálculos usando fechas, como calcular el número de días entre dos fechas, sumar o restar días o determinar el día de la semana. Si los números no están formateados como fechas, Excel no podrá realizar estas operaciones eficazmente. Por ejemplo, si deseas conocer el número de días entre 01/09/2023 y 01/10/2023, Excel puede calcularlo fácilmente si los números están en formato de fecha.
1. Asegura consistencia: cuando todos los valores relacionados con fechas están formateados correctamente, se asegura que todas las fechas aparezcan en un estilo uniforme y legible. Esta consistencia es importante en informes comerciales, cronogramas de proyectos y bases de datos donde la consistencia de fechas es crucial.
Diferentes regiones usan diferentes formatos de fecha (por ejemplo, MM/DD/AAAA en EE. UU. vs. DD/MM/AAAA en muchos otros países), por lo que formatear ayuda a garantizar que las fechas se interpreten correctamente.
1. Mejora la legibilidad: las fechas presentadas en un formato estándar (por ejemplo, 01/01/2024) son más fáciles de leer que números seriales sin formato como 45000. El formateo correcto de fechas hace que tu hoja de cálculo sea más amigable para el usuario y evita confusiones. Esto es especialmente importante en escenarios como programación, cronogramas, planificación de eventos o datos históricos.
1. Ayuda en ordenar y filtrar: cuando las fechas están formateadas correctamente, Excel las reconoce como fechas reales, lo que facilita ordenar o filtrar datos cronológicamente. Por ejemplo, puedes ordenar una lista de eventos por fecha o filtrar un rango de datos para mostrar solo registros entre dos fechas específicas. Sin un formato de fecha adecuado, la ordenación puede basarse en el número sin significado en lugar de fechas de calendario reales.
1. Permite el uso de funciones de fecha: Excel proporciona una variedad de funciones de fecha poderosas, como: HOY(), DATEDIF(), WORKDAY(), YEAR(), MONTH(), DAY(). Estas funciones requieren que las fechas estén formateadas correctamente para cálculos precisos.
1. Soporta visualización (gráficos/líneas de tiempo): Las fechas formateadas correctamente pueden usarse para crear gráficos y diagramas donde el tiempo es un eje principal. Por ejemplo, en un gráfico de línea de tiempo, Excel necesita fechas en un formato reconocido para trazar eventos con precisión a lo largo del tiempo. Los números mal formateados o sin formato podrían resultar en gráficos que no tengan sentido o que reflejen información incorrecta.
1. Previene interpretaciones erróneas: los números sin formato pueden ser fácilmente malinterpretados. Por ejemplo, 44210 podría leerse como un valor numérico general, pero cuando está formateado como fecha, está claro que representa el 6 de septiembre de 2021. Las fechas correctamente formateadas ayudan a evitar interpretaciones erróneas de los datos.
1. Facilita la entrada de datos: Cuando las celdas están formateadas como fechas, se solicita a los usuarios que ingresen datos en un formato de fecha válido, lo que evita errores en la entrada de datos y asegura que los valores de fecha se capturen correctamente.
1. Fundamental para Programar y Rastrear: En cualquier situación que implique programación, seguimiento o plazos (como gestión de proyectos, pronósticos financieros o informes sensibles al tiempo), formatear números como fechas es crucial para la precisión y la comprensión. Permite una mejor planificación y ejecución.


## **Cómo formatear un número como fecha en Excel**
Para formatear un número como fecha en Excel, sigue estos pasos:

### **Usando la cinta (Pestaña Inicio)**
1. Selecciona las celdas que contienen los números que deseas formatear como fechas.
1. Ve a la pestaña Inicio en la cinta.
1. En el grupo Número, haz clic en la flecha desplegable en el cuadro Formato de número (que puede mostrar "General" o "Número" por defecto).
1. Elige Fecha corta o Fecha larga del menú desplegable. Fecha corta: Muestra la fecha en un formato conciso, p.ej., MM/DD/AAAA (formato EE. UU.) o DD/MM/AAAA (formato internacional). Fecha larga: Muestra la fecha en un formato más descriptivo, p.ej., lunes, 1 de enero de 2024.
<br>
<img src="1.png" width=60% />

### **Usando el cuadro de diálogo de Formato de celdas**
1. Selecciona las celdas que deseas formatear.
1. Haz clic derecho en las celdas seleccionadas y elige Formato de celdas, o presiona Ctrl + 1 (Windows) o Cmd + 1 (Mac).
1. En el cuadro de diálogo Formato de celdas, ve a la pestaña Número.
1. Desde la lista de la izquierda, selecciona Fecha.
1. Elige el formato de fecha deseado de la lista de la derecha (p.ej., MM/DD/AAAA, DD/MM/AAAA, o formatos personalizados).
<br>
<img src="2.png" width=60% />
1. Haz clic en OK para aplicar el formato de fecha.

## **Cómo formatear números como fecha en Aspose.Cells**

Para formatear números como fecha en la biblioteca Aspose.Cells for Java para trabajar con archivos de Excel, puedes aplicar formateo de fecha a las celdas programáticamente. Aquí te mostramos cómo hacerlo usando Java con Aspose.Cells:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Cells-Formatting-FormatNumberToDate.java" >}}
{{< app/cells/assistant language="java" >}}
