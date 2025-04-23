---
title: Cómo dar formato a un número como fecha con C++
linktitle: Cómo formatear número como fecha
type: docs
weight: 10
url: /es/cpp/format-number-to-date/
description: Este artículo presentará cómo formatear un número a fecha usando la API Aspose.Cells for C++.
keywords: formatear número como fecha, configuraciones de número en la celda, formato número a fecha, configuraciones de fecha, formato de fecha.
---

## **Escenarios de uso posibles**
Formatear números como fechas en Excel (o cualquier software de hojas de cálculo) es importante por varias razones, especialmente cuando trabajas con datos que incluyen información de tiempo o programación. He aquí por qué es beneficioso formatear números a fechas:

1. **Interpretación adecuada de valores de fecha**: En Excel, las fechas se almacenan como números seriales (por ejemplo, 1 representa el 1 de enero de 1900 y 44210 representa el 6 de septiembre de 2021). Si estos números no están formateados como fechas, los usuarios pueden ver números sin sentido en lugar de fechas reconocibles. Formatearlos correctamente permite que Excel los muestre como fechas reales (por ejemplo, 06/09/2021 en lugar de 44210).
2. **Simplifica cálculos relacionados con el tiempo**: Excel puede realizar muchos cálculos usando fechas, como calcular la cantidad de días entre dos fechas, añadir o restar días, o determinar el día de la semana. Si los números no están formateados como fechas, Excel no podrá realizar estas operaciones eficazmente. Por ejemplo, si deseas saber cuántos días hay entre el 01/09/2023 y el 01/10/2023, Excel puede calcularlo fácilmente si los números están en formato de fecha.
3. **Asegura la consistencia**: Cuando todos los valores relacionados con fechas están formateados correctamente, se garantiza que todas las fechas aparezcan en un estilo uniforme y legible. Esta consistencia es importante en informes de negocios, programaciones de proyectos y bases de datos donde la coherencia de las fechas es crucial. Diferentes regiones usan diferentes formatos de fecha (por ejemplo, MM/DD/AAAA en EE. UU. vs. DD/MM/AAAA en otros países), por lo que el formato ayuda a interpretar las fechas correctamente.
4. **Mejora la legibilidad**: Las fechas presentadas en un formato estándar (por ejemplo, 01/01/2024) son más fáciles de leer que los números seriales sin formato como 45000. Formatear correctamente la fecha hace que tu hoja de cálculo sea más fácil de usar y evita confusiones. Esto es especialmente importante en escenarios como programación, cronogramas, planificación de eventos o datos históricos.
5. **Ayuda en ordenar y filtrar**: Cuando las fechas están formateadas correctamente, Excel las reconoce como fechas reales, lo que facilita ordenar o filtrar datos cronológicamente. Por ejemplo, puedes ordenar una lista de eventos por fecha o filtrar un rango de datos para mostrar solo registros entre dos fechas específicas. Sin el formato de fecha correcto, ordenar podría ocurrir según el número en bruto en lugar de las fechas en el calendario.
6. **Permite el uso de funciones de fecha**: Excel proporciona una variedad de potentes funciones de fecha, como: HOY(), DATEDIF(), WORKDAY(), AÑO(), MES(), DÍA(). Estas funciones requieren que las fechas estén formateadas correctamente para cálculos precisos.
7. **Apoya la visualización (gráficos/ líneas de tiempo)**: Las fechas formateadas correctamente pueden usarse para crear gráficos y diagramas donde el tiempo es un eje clave. Por ejemplo, en un gráfico de línea de tiempo, Excel necesita fechas en un formato reconocido para trazar eventos con precisión en el tiempo. Los números mal formateados o sin formato pueden resultar en gráficos que no tengan sentido o muestren información incorrecta.
8. **Previene interpretaciones erróneas**: Los números en bruto pueden ser malinterpretados fácilmente. Por ejemplo, 44210 puede leerse como un valor numérico general, pero cuando se formatea como fecha, está claro que representa el 6 de septiembre de 2021. Las fechas en formato correcto ayudan a evitar interpretaciones erróneas de los datos.
9. **Facilita la entrada de datos**: Cuando las celdas están formateadas como fechas, se pide a los usuarios que ingresen datos en un formato de fecha válido, lo que previene errores en la entrada de datos y garantiza que los valores de la fecha se capturen correctamente.
10. **Crítico para programar y hacer seguimiento**: En cualquier situación que implique programación, seguimiento o fechas límite (como gestión de proyectos, pronósticos financieros o informes con tiempos sensibles), formatear números como fechas es crucial para la precisión y comprensión. Permite una mejor planificación y ejecución.

## **Cómo formatear un número como fecha en Excel**
Para formatear un número como fecha en Excel, sigue estos pasos:

### **Usando la cinta (Pestaña Inicio)**
1. Selecciona las celdas que contienen los números que deseas formatear como fechas.
2. Vaya a la pestaña Inicio en la cinta de opciones.
3. En el grupo Número, haga clic en la flecha desplegable en el cuadro de Formato de número (que puede mostrar "General" o "Número" por defecto).
4. Elige Fecha Corta o Fecha Larga en el menú desplegable. Fecha Corta: Muestra la fecha en un formato conciso, por ejemplo, MM/DD/AAAA (formato de EE.UU.) o DD/MM/AAAA (formato internacional). Fecha Larga: Muestra la fecha en un formato más descriptivo, por ejemplo, lunes, 1 de enero de 2024.
<br>
<img src="1.png" width=60% />

### **Usando el cuadro de diálogo de Formato de celdas**
1. Selecciona las celdas que deseas formatear.
2. Haz clic derecho en las celdas seleccionadas y elige Formato de Celdas, o presiona Ctrl + 1 (Windows) o Cmd + 1 (Mac).
3. En el cuadro de diálogo Formato de Celdas, ve a la pestaña Número.
4. En la lista de la izquierda, selecciona Fecha.
5. Elige el formato de fecha deseado de la lista de la derecha (por ejemplo, MM/DD/AAAA, DD/MM/AAAA, o formatos personalizados).
<br>
<img src="2.png" width=60% />
6. Haz clic en OK para aplicar el formato de fecha.

## **Cómo formatear números como fecha en Aspose.Cells**

Para formatear números como fecha en la biblioteca Aspose.Cells for C++ para trabajar con archivos de Excel, puedes aplicar formateo de fecha a las celdas programáticamente. Aquí te mostramos cómo hacerlo usando C++ con Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
