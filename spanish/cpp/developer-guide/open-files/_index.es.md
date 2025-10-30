---
title: Cargar y gestionar archivos de Excel, OpenOffice, Json, Csv y Html con C++
linktitle: Abrir archivos
type: docs
weight: 20
url: /es/cpp/loading-saving-and-managing/
description: Con Aspose.Cells for C++, es sencillo crear, abrir y administrar archivos de Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Imagen, Mht y XPS.
---

{{% alert color="primary" %}}

Con Aspose.Cells for C++, es sencillo crear, abrir y gestionar archivos de Excel, por ejemplo, para recuperar datos o usar una plantilla de diseño para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Creando un libro de trabajo nuevo**
El siguiente ejemplo crea un nuevo libro de trabajo desde cero.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Abrir y guardar un archivo**
Con Aspose.Cells for C++, es sencillo abrir, guardar y administrar archivos de Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas Avanzados**
- [Diferentes formas de abrir archivos](/cells/es/cpp/different-ways-to-open-files/)
- [Filtrar nombres definidos al cargar un libro de trabajo](/cells/es/cpp/filter-defined-names-while-loading-workbook/)
- [Filtrar objetos al cargar un libro de trabajo o una hoja de cálculo](/cells/es/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrar el tipo de datos al cargar el libro de trabajo desde un archivo de plantilla](/cells/es/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtener Advertencias al Cargar Archivo de Excel](/cells/es/cpp/get-warnings-while-loading-excel-file/)
- [Cargar archivo de Excel fuente sin gráficos](/cells/es/cpp/load-source-excel-file-without-charts/)
- [Cargar hojas de cálculo específicas en un libro de trabajo](/cells/es/cpp/load-specific-worksheets-in-a-workbook/)
- [Cargar Libro de Trabajo con Tamaño de Papel de Impresión Especificado](/cells/es/cpp/load-workbook-with-specified-printer-paper-size/)
- [Abrir archivos de diferentes versiones de Microsoft Excel](/cells/es/cpp/opening-different-microsoft-excel-versions-files/)
- [Abriendo Archivos con Diferentes Formatos](/cells/es/cpp/opening-files-with-different-formats/)
- [Optimizando el Uso de Memoria al Trabajar con Archivos Grandes con Grandes Conjuntos de Datos](/cells/es/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leer Planilla de Números Desarrollada por Apple Inc. Usando Aspose.Cells](/cells/es/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Detener la Conversión o Carga Usando InterruptMonitor Cuando Tarda Demasiado](/cells/es/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Usar la API LightCells](/cells/es/cpp/using-lightcells-api/)
- [Convertir CSV a JSON](/cells/es/cpp/convert-csv-to-json/)
- [Convertir Excel a JSON](/cells/es/cpp/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/cpp/convert-json-to-csv/)
- [Convertir JSON a Excel](/cells/es/cpp/convert-json-to-excel/)
- [Convertir Excel a Html](/cells/es/cpp/convert-excel-to-html/)
{{< app/cells/assistant language="cpp" >}}
