---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker med C++
linktitle: Kopiera och flytta arbetsblad
type: docs
weight: 80
url: /sv/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Lär dig hur du kopierar och flyttar arbetsblad inom och mellan Excel arbetsböcker med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver du flera arbetsblad med gemensam formatering och datainmatning. Till exempel, om du arbetar med kvartalsbudgeten, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det flera gånger.

Aspose.Cells stöder att kopiera eller flytta arbetsblad inom eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta noggrannhet.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

### **Kopiera ett arbetsblad inom en arbetsbok**

De initiala stegen är desamma för alla exempel:

1. Skapa två arbetsböcker med viss data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in viss data i arbetsbladen:
   - FirstWorkbook.xlsx (3 arbetsblad)
   - SecondWorkbook.xlsx (1 arbetsblad)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. Installera den på din utvecklingsdator

1. Skapa ett projekt:
   1. Skapa ett nytt C++-projekt i din föredragna IDE

1. Lägg till referenser:
   1. Lägg till Aspose.Cells for C++-biblioteket i ditt projekt

1. Kopiera kalkylbladet inom en arbetsbok
   Det första exemplet kopierar det första kalkylbladet (Kopiera) inom FirstWorkbook.xlsx.

När koden körs kopieras kalkylbladet med namnet Kopiera inom FirstWorkbook.xlsx med namnet Sista blad.

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

### **Flytta ett blad inom en arbetsbok**

Koden nedan visar hur man flyttar ett blad från en position i en arbetsbok till en annan. Utförande av koden flyttar bladet som kallas Flytta från index 1 till index 2 i FirstWorkbook.xlsx.

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

### **Kopiera ett kalkylblad mellan arbetsböcker**

När koden körs kopierar den arbetsbladet som heter Copy till SecondWorkbook.xlsx med namnet Sheet2.

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

### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas bladet med namnet Flytta från FirstWorkbook.xlsx till SecondWorkbook.xlsx med namnet Sheet3.

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
