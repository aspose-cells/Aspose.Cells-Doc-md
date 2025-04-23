---
title: Ottieni il range massimo in un foglio di lavoro con C++
linktitle: Ottieni Max Range In Un Foglio di Lavoro
type: docs
weight: 360
url: /it/cpp/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere il range massimo, il massimo intervallo di dati, il massimo intervallo di visualizzazione dei file Excel con la libreria Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.

Quando esportiamo un'area specificata in HTML e PDF, dobbiamo conoscere l'area massima.

Aspose.Cells for C++ contiene diversi modi per trovare il range massimo in un foglio di lavoro. 

{{% /alert %}} 

## **Ottenere l'intervallo massimo**
In Aspose.Cells, se gli oggetti [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) e [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) sono inizializzati, queste righe e colonne verranno conteggiate per l'area massima, anche se non ci sono dati nelle righe o colonne vuote.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Ottieni il massimo intervallo di dati**
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.
E le impostazioni su forme, tabelle e tabelle pivot verranno ignorate.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Ottieni l'intervallo massimo di visualizzazione**
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.
I seguenti codici mostrano come rendere l'intervallo di visualizzazione massimo in HTML:

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

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ecco il [file excel di origine](Book1.xlsx).
