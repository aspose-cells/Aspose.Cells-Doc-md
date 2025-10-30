---
title: Riutilizzo di oggetti stile con C++
linktitle: Riutilizzo degli oggetti stile
description: In Aspose.Cells for C++, creando e usando oggetti stile riutilizzabili, puoi semplificare la gestione degli stili e migliorare l efficienza del codice. La nostra guida ti aiuterà a sfruttare i vantaggi degli oggetti stile riutilizzabili e a implementarli nella tua applicazione.
keywords: Aspose.Cells for C++, Riutilizzo di oggetti stile, Gestione degli stili, Efficienza del codice, Stili riutilizzabili, Sviluppo applicazioni, Riferimento API, Codice di esempio, Download, Supporto.
type: docs
weight: 3000
url: /it/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Il riutilizzo degli oggetti stile può risparmiare memoria e rendere un programma più veloce.

{{% /alert %}}

Per applicare una formattazione a un'ampia gamma di celle in un foglio di lavoro:

1. Creare un oggetto stile.
1. Specificare gli attributi.
1. Applicare lo stile alle celle nell'intervallo.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Poiché l'approccio [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) utilizza molto meno memoria ed è efficiente, la vecchia proprietà Cell.Style che consumava molta memoria inutile, è stata rimossa con il rilascio di Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
