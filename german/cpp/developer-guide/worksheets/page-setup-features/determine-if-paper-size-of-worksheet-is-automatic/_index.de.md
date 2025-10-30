---
title: Bestimmen, ob die Papiergröße eines Arbeitsblatts automatisch ist, mit C++
linktitle: Feststellen, ob das Papierformat des Arbeitsblatts automatisch ist
type: docs
weight: 90
url: /de/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Dieser Artikel erklärt, wie man die C++ API oder den Beispielcode verwendet, um programmgesteuert zu bestimmen, ob die Papiergröße eines Arbeitsblatts automatisch ist.
keywords: Bestimmung, ob die Papiergröße des Arbeitsblatts automatisch ist, C++
---

## **Mögliche Verwendungsszenarien**

Meist ist die Papiergröße des Arbeitsblatts automatisch. Wenn sie automatisch ist, wird sie oft auf *Brief* eingestellt. Manchmal legt der Benutzer die Papiergröße des Arbeitsblatts entsprechend seinen Anforderungen fest. In diesem Fall ist die Papiergröße nicht automatisch. Sie können feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist oder nicht, indem Sie die [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/)-Eigenschaft der **Worksheet**-Klasse verwenden.

## **Feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist**

Der folgende Beispielscode lädt die folgenden beiden Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

und feststellen, ob die Papiergröße ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie überprüfen, ob die Papiergröße automatisch ist oder nicht, über das Page Setup Fenster, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit den angegebenen Beispieldateien ausgeführt wird.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
