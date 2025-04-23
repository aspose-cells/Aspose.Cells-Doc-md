---
title: Bestämma om pappersstorleken för arket är automatisk med C++
linktitle: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 90
url: /sv/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Denna artikel förklarar hur man använder C++ API eller bibliotek för att avgöra om pappersstorleken för arket är automatisk programmatiskt.
keywords: avgör om pappersstorlse på arbetsbladet är automatiskt c++
---

## **Möjliga användningsscenario**

De flesta gånger är papperstorleken på arbetsbladet automatisk. När den är automatisk är den ofta inställd som *Letter*. Ibland ställer användaren in papperstorleken på arbetsbladet enligt deras krav. I detta fall är inte papperstorleken automatisk. Du kan kontrollera om arbetsbladets papperstorlek är automatisk eller inte med hjälp av [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/)-egenskapen i **Worksheet**-klassen.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och kontrollerar om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via sidsetup- fönstret som visas i denna skärmdump.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

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

## **Konsoloutput**

Här är konsolutdata från ovanstående provkod när den körs med de angivna provexelfilerna.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
