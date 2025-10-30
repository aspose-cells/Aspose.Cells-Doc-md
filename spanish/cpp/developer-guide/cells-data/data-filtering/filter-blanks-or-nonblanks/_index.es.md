---
title: Cómo filtrar vacíos o no vacíos con C++
linktitle: Cómo filtrar celdas en blanco o no en blanco
type: docs
weight: 85
url: /es/cpp/how-to-filter-blanks-and-non-blanks/
description: Aprende cómo filtrar en blanco y no en blanco usando la API Aspose.Cells for C++.
keywords: Filtrar celdas en blanco, filtrar celdas no en blanco, filtrar celdas en blanco en la hoja de cálculo, filtrar celdas no en blanco en la hoja de cálculo, filtrar celdas en blanco en Excel, filtrar celdas no en blanco en Excel, filtrar celdas en blanco y no en blanco en Excel
---

## **Escenarios de uso posibles**
Filtrar datos en Excel es una herramienta valiosa que mejora el análisis, la exploración y la presentación de datos al permitir a los usuarios centrarse en subconjuntos específicos de datos según sus criterios, lo que hace que el proceso general de manipulación e interpretación de datos sea más eficiente y efectivo.

## **Cómo filtrar celdas en blanco o no en blanco en Excel**
En Excel, puedes filtrar fácilmente celdas en blanco o no en blanco utilizando las opciones de filtrado. Así es como puedes hacerlo:

### **Cómo filtrar celdas en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar en blanco. Desmarca todas las opciones excepto "En blanco" y haz clic en Aceptar. Esto mostrará solo las celdas en blanco en esa columna.
<br>
<image src="2.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="3.png" width="70%" />

### **Cómo filtrar celdas no en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas no en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas no en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar no en blanco. Desmarca todas las opciones excepto "No en blanco" o "Personalizado" y establece las condiciones correspondientes. Haz clic en Aceptar. Esto mostrará solo las celdas que no están en blanco en esa columna.
<br>
<image src="4.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="5.png" width="70%" />

## **Cómo filtrar celdas en blanco usando Aspose.Cells**
Si una columna contiene texto de modo que algunas celdas estén en blanco y se requiere filtrar solo aquellas filas donde hay celdas en blanco, las funciones [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) y [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) pueden usarse como se demuestra a continuación. 

Consulta el siguiente código de muestra que carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. El código de muestra utiliza tres métodos para filtrar en blanco. Luego guarda el libro como [archivo de Excel de salida](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Cómo filtrar celdas no en blanco usando Aspose.Cells**

Por favor, vea el siguiente código de ejemplo que carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. Después de cargar el archivo, llame a la función [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) para filtrar datos no en blanco y, finalmente, guarde el libro de trabajo como [archivo Excel de salida](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


{{< app/cells/assistant language="cpp" >}}
