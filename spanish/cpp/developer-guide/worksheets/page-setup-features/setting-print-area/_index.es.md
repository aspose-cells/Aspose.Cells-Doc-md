---
title: Cómo establecer el área de impresión con C++
linktitle: Cómo definir el área de impresión
type: docs
weight: 200
url: /es/cpp/how-to-set-print-area/
description: Este artículo muestra código que explica cómo establecer el área de impresión usando la biblioteca Aspose.Cells con C++.
keywords: Limitar rango de impresión, configurar rango de impresión, limpiar rango de impresión, establecer y limpiar rango de impresión usando C++, Cómo establecer el área de impresión en C++, establecer y limpiar área de impresión en C++, Cómo limpiar área de impresión en C++, Cómo agregar área de impresión usando C++, Cómo eliminar área de impresión usando C++, Cómo establecer el área de impresión en Excel, Cómo limpiar área de impresión en Excel.
---

## **Escenarios de uso posibles**

Configurar un área de impresión en un documento, como una hoja de cálculo de Excel, ayuda a controlar qué contenido se incluye al imprimir. Aquí algunas razones para establecer un área de impresión:

1. Centrarse en datos específicos: Puedes imprimir solo las secciones más relevantes, evitando contenido innecesario.
1. Mejorar el diseño: Ayuda a organizar y ajustar el contenido de forma ordenada en las páginas imprimidas, evitando divisiones o saltos de página no deseados.
1. Ahorrar recursos: Limitando el área de impresión, puedes reducir el uso de papel y tinta.
1. Presentación profesional: Asegura que solo se imprima la versión pulida y finalizada de los datos, especialmente importante para informes o presentaciones.
1. Consistencia: Al imprimir el mismo documento varias veces, tener un área de impresión estable garantiza la consistencia en el resultado.

<br>
Establecer un área de impresión es especialmente útil en documentos grandes donde solo una parte necesita ser compartida o revisada en forma impresa.

## **Cómo establecer el área de impresión en Excel**

Para establecer un área de impresión en Excel, siga estos pasos:

1. Seleccionar las celdas: Haga clic y arrastre para seleccionar el rango de celdas que desea establecer como área de impresión.
1. Abrir la pestaña Diseño de página: Vaya a la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Establecer área de impresión: En el grupo "Configuración de página", haga clic en "Área de impresión". En el menú desplegable, seleccione "Establecer área de impresión".
<br>
<img src="3.png" width=60% />

1. Agregar a la área de impresión: Si desea agregar más celdas al área de impresión existente, seleccione las celdas adicionales, vaya a "Área de impresión" en la pestaña "Diseño de página" y elija "Agregar a área de impresión".

<br>
Esta acción definirá las celdas seleccionadas como el área de impresión. Cuando imprima la hoja de cálculo, solo esta área definida se imprimirá.

## **Cómo borrar el área de impresión en Excel**

Para borrar el área de impresión en Excel, siga estos pasos:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Borrar área de impresión: En el grupo "Configuración de página", haga clic en "Área de impresión". En el menú desplegable, seleccione "Borrar área de impresión".
<br>
<img src="4.png" width=60% />

<br>
Esta acción eliminará cualquier área de impresión configurada anteriormente, permitiendo que toda la hoja de cálculo se imprima.

## **Qué sucede después de limpiar el área de impresión**

Borrar el área de impresión en una aplicación de hojas de cálculo como Excel utilizando Aspose.Cells resultará en que toda la hoja de cálculo se incluya al imprimir el documento. Si se establece un área de impresión, solo el rango especificado de celdas se imprimirá. Al borrar el área de impresión, se asegura que no se defina un rango específico y que la impresión por defecto, que incluye toda la hoja, tenga efecto.

1. Comportamiento de impresión predeterminado: Se considerará toda la hoja de cálculo para la impresión. Esto significa que todas las celdas con datos o formato serán impresas.
1. Sin límites de área de impresión: Se eliminarán los límites de área de impresión previamente definidos. Si había filas y columnas específicas designadas para imprimir, ya no estarán restringidas a esos límites.
1. Impresión de contenido completo: Todo el contenido, incluidos encabezados, pies de página y cualquier otro dato dentro de la hoja de cálculo, se incluirá en el trabajo de impresión.

## **Cómo configurar el área de impresión usando Aspose.Cells**

Para establecer el área de impresión en una hoja de cálculo específica: Primero, cargue el [archivo de ejemplo](input.xlsx), y luego necesita modificar la propiedad [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) del objeto [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) para la hoja deseada. Configurar esta propiedad con una cadena de rango establecerá el área de impresión.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Set the print area - specify the range you want to print
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"A1:D10");

    // Save the workbook
    U16String outputFilePath(u"set_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo limpiar el área de impresión usando Aspose.Cells**

Para borrar el área de impresión en una hoja de cálculo específica: Primero, cargue el [archivo de ejemplo](input.xlsx), y luego necesita modificar la propiedad [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) del objeto [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) para la hoja deseada. Configurar esta propiedad con una cadena vacía borrará el área de impresión.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"");

    // Save the workbook
    U16String outputFilePath(u"clear_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area cleared and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

El resultado de la salida:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
