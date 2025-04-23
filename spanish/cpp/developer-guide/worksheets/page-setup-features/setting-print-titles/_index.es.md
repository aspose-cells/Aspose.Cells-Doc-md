---
title: Cómo establecer títulos de impresión con C++
linktitle: Cómo establecer títulos de impresión
type: docs
weight: 200
url: /es/cpp/how-to-set-print-titles/
description: Este artículo te muestra un código que explica cómo establecer títulos de impresión usando la biblioteca Aspose.Cells con C++.
keywords: Imprimir filas y columnas repetidamente, C++ Cómo Configurar Títulos de Impresión, Establecer y Borrar Títulos de Impresión usando C++, Cómo borrar títulos de impresión en C++, Cómo agregar títulos de impresión usando C++, cómo eliminar títulos de impresión usando C++, Cómo establecer títulos de impresión en Excel, Cómo borrar títulos de impresión en Excel.
---

## **Escenarios de uso posibles**

Configurar títulos de impresión en Excel asegura que filas o columnas específicas se repitan en cada página impresa, lo cual es especialmente útil para hojas de cálculo grandes que abarcan varias páginas. Aquí tienes algunas razones para establecer títulos de impresión:

1. Mejor legibilidad: Los títulos de impresión ayudan a los lectores a entender los datos manteniendo los encabezados visibles en todas las páginas, facilitando la interpretación de la información sin tener que volver a la primera página.

1. Presentación profesional: Mostrar consistentemente encabezados o etiquetas en cada página crea una apariencia más pulida y profesional en los documentos impresos.

1. Mejor navegación: Para documentos con datos extensos, repetir los encabezados en cada página permite una navegación y referencia más rápida, reduciendo la necesidad de volver a pasar entre páginas.

1. Reducción de errores: Cuando los encabezados están presentes en cada página, se minimizan las oportunidades de malentendidos o errores de entrada de datos, ya que los usuarios pueden ver fácilmente el contexto de los datos.

1. Consistencia: Asegurar que información importante, como encabezados de columnas o etiquetas de filas, siempre sea visible mantiene la consistencia y claridad en todo el documento.

## **Cómo establecer títulos de impresión en Excel**

Para establecer títulos de impresión en Excel, sigue estos pasos:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".
1. Configurar filas para repetir: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". En la sección "Títulos de impresión", especifica las filas a repetir en la parte superior haciendo clic en el cuadro junto a "Filas para repetir en la parte superior" y seleccionando la(s) fila(s) que deseas repetir.
1. Configurar columnas para repetir (si es necesario): De manera similar, puedes especificar las columnas para repetir en la izquierda haciendo clic en el cuadro junto a "Columnas para repetir en la izquierda" y seleccionando la(s) columna(s) que deseas repetir.
<br>
<img src="3.png" width=60% />

1. Confirmar y imprimir: Haz clic en "Aceptar" para aplicar la configuración. Cuando imprimas la hoja, las filas o columnas especificadas aparecerán en cada página impresa.

## **Cómo borrar títulos de impresión en Excel**

Para borrar títulos de impresión en Excel, necesitas eliminar las filas o columnas que están configuradas para repetirse en cada página impresa. Aquí te decimos cómo hacerlo:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".
1. Borrar títulos de impresión: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". Borra el contenido de los cuadros "Filas para repetir en la parte superior" y "Columnas para repetir en la izquierda" eliminando cualquier contenido dentro de ellos.
<br>
<img src="4.png" width=60% />

1. Confirmar y cerrar: Haz clic en "Aceptar" para aplicar los cambios.

## **Cómo establecer títulos de impresión usando Aspose.Cells**

Para establecer títulos de impresión en una hoja de cálculo específica: Primero, carga el [archivo de muestra](input.xlsx), y luego debes modificar las propiedades [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) y [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) del objeto [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) para la hoja deseada. Configurar estas propiedades con una cadena de rango establecerá los títulos de impresión.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo borrar títulos de impresión usando Aspose.Cells**

Para borrar los títulos de impresión en una hoja de cálculo específica: Primero, carga el [archivo de muestra](input.xlsx), y luego debes modificar las propiedades [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) y [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) del objeto [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) para la hoja deseada. Configurar estas propiedades con una cadena vacía borrará los títulos de impresión.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

El resultado de la salida:
<br>
<img src="2.png" width=60% />
