---
title: Kontrollera om VBA projektet är skyddat och låst för visning med C++
linktitle: Kontrollera om VBA projektet är skyddat och låst för visning
type: docs
weight: 30
url: /sv/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Lär dig hur du kontrollerar om VBA projekt är skyddat och låst för visning i Excel filer med Aspose.Cells for C++.
---

## Kontrollera om VBA-projekt är skyddat och låst för visning i C++

Aspose.Cells låter dig kontrollera om VBA (Visual Basic for Applications) projektet för en Excel-fil är skyddat och låst för visning. För detta tillhandahåller API:n egenskapen [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). Om det är låst för visning, returnerar egenskapen [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) **true**.

## **Exempelkod**

Följande exempel på kod läser in [exempel-Excelfilen](43352065.xlsm) och kontrollerar om VBA (Visual Basic for Applications)-projektet i Excel-filen är skyddat och låst för visning. Se även dess Konsolutmatning för referens.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

Detta är konsolresultatet av ovanstående exempelkod när den exekveras med den medföljande [exempelvisningsfilen för Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
