---
title: Guardar cada hoja de cálculo en un archivo PDF diferente con C++
linktitle: Guardar Cada Hoja de Cálculo en un Archivo PDF Diferente
type: docs
weight: 130
url: /es/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Aprende cómo guardar cada hoja de cálculo en un archivo Excel en un PDF separado usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells soporta convertir archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for C++ puede trabajar de manera independiente para convertir una hoja de cálculo a PDF y no necesitas usar Aspose.PDF para C++ para la conversión. La conversión no requiere que el software cree o utilice archivos temporales, ya que todo el proceso se puede hacer en memoria.

{{% /alert %}} 

## **Guardar cada hoja de cálculo en un archivo PDF diferente**
Si necesitas guardar cada hoja de cálculo en tu archivo Excel plantilla para generar diferentes archivos PDF, puedes lograrlo fácilmente. Puedes intentar establecer un índice de hoja a la opción [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) a la vez para renderizar a PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Si tu hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizar la hoja a formato PDF. Hacerlo asegurará que los valores dependientes de fórmulas sean recalculados y que se rendericen los valores correctos en el PDF.

{{% /alert %}}
