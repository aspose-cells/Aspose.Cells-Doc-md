---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben mit C++
linktitle: Arbeitsblätter kopieren und verschieben
type: docs
weight: 80
url: /de/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Lernen Sie, wie Sie Arbeitsblätter innerhalb und zwischen Excel Arbeitsmappen mit Aspose.Cells for C++ kopieren und verschieben.
---

{{% alert color="primary" %}}

Manchmal benötigen Sie mehrere Arbeitsblätter mit gemeinsamer Formatierung und Dateneingabe. Zum Beispiel, wenn Sie vierteljährliche Budgets verwalten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die die gleichen Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Methode, dies zu tun: indem Sie ein Blatt erstellen und es dann mehrfach kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Genauigkeit kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die ersten Schritte sind für alle Beispiele gleich:

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir in Microsoft Excel zwei neue Arbeitsmappen erstellt und Daten in die Arbeitsblätter eingetragen:
   - FirstWorkbook.xlsx (3 Arbeitsblätter)
   - SecondWorkbook.xlsx (1 Arbeitsblatt)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Laden Sie Aspose.Cells for C++ herunter](https://downloads.aspose.com/cells/cpp)
   1. Installieren Sie es auf Ihrem Entwicklungscomputer

1. Ein Projekt erstellen:
   1. Erstellen Sie ein neues C++-Projekt in Ihrer bevorzugten IDE

1. Fügen Sie Verweise hinzu:
   1. Fügen Sie die Aspose.Cells for C++-Bibliothek zu Ihrem Projekt hinzu

1. Kopieren Sie das Tabellenblatt innerhalb einer Arbeitsmappe.
   Das erste Beispiel kopiert das erste Tabellenblatt (Kopie) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Kopie innerhalb von FirstWorkbook.xlsx mit dem Namen Last Sheet kopiert.

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

### **Verschieben eines Arbeitsblatts innerhalb eines Arbeitsmappes**

Der untenstehende Code zeigt, wie man ein Arbeitsblatt von einer Position in einer Arbeitsmappe an eine andere verschiebt. Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben vom Index 1 auf den Index 2 in FirstWorkbook.xlsx.

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

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes kopiert das Arbeitsblatt mit dem Namen Copy nach SecondWorkbook.xlsx mit dem Namen Sheet2.

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

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben von FirstWorkbook.xlsx nach SecondWorkbook.xlsx mit dem Namen Blatt3.

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
{{< app/cells/assistant language="cpp" >}}
