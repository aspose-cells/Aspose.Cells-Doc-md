---
title: Copia e sposta fogli di lavoro all’interno e tra i workbook con C++
linktitle: Copia e sposta fogli di lavoro
type: docs
weight: 80
url: /it/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Impara come copiare e spostare fogli di lavoro all’interno e tra i workbook Excel utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario avere più fogli di lavoro con formattazione e inserimento dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare un workbook con fogli che contengono gli stessi intestazioni di colonna, intestazioni di riga e formule. Esiste un modo per farlo: creando un foglio e poi copiandolo più volte.

Aspose.Cells supporta la copia o lo spostamento dei fogli di lavoro all'interno o tra i workbook. I fogli di lavoro, compresi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Copia e Sposta Fogli di Lavoro**

### **Copiare un foglio di lavoro all'interno di un libro di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi:

1. Crea due workbook con alcuni dati in Microsoft Excel. Per questo esempio, abbiamo creato due nuovi workbook in Excel e inserito alcuni dati nei fogli:
   - FirstWorkbook.xlsx (3 fogli di lavoro)
   - SecondWorkbook.xlsx (1 foglio di lavoro)

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. Installa sul computer di sviluppo

1. Crea un progetto:
   1. Crea un nuovo progetto C++ nel tuo IDE preferito

1. Aggiungi riferimenti:
   1. Aggiungi la libreria Aspose.Cells for C++ al tuo progetto

1. Copia il foglio di lavoro all'interno di un workbook
   Il primo esempio copia il primo foglio di lavoro (Copia) all'interno di FirstWorkbook.xlsx.

Quando si esegue il codice, il foglio di lavoro chiamato Copia viene copiato all'interno di FirstWorkbook.xlsx con il nome Ultimo foglio.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Spostamento di un foglio di lavoro all'interno di un workbook**

Il codice sottostante mostra come spostare un foglio di lavoro da una posizione all'interno di un workbook a un'altra. Eseguendo il codice sposta il foglio di lavoro chiamato Spostare dall'indice 1 all'indice 2 in FirstWorkbook.xlsx.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Copia un Foglio di Lavoro tra i Workbooks**

Eseguendo il codice, viene copiato il foglio di lavoro chiamato Copy in SecondWorkbook.xlsx con il nome Sheet2.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Spostare un foglio di lavoro tra i Workbooks**

Eseguendo il codice sposta il foglio di lavoro chiamato Spostare da FirstWorkbook.xlsx a SecondWorkbook.xlsx con il nome Foglio3.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
