---
title: Expanderar text från högra till vänster vid export av Excel fil till HTML med C++
linktitle: Expandera text från höger till vänster vid export av Excel fil till HTML
type: docs
weight: 60
url: /sv/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Lär dig hur du expanderar text från höger till vänster vid export av Excel filer till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells for C++ stöder nu att expandera text från höger till vänster vid export av Excel-filer till HTML. Denna funktion har implementerats sedan version v8.9.0.0. Om din ursprungliga Excel-fil innehåller text som expanderar från höger till vänster, kommer Aspose.Cells att exportera den korrekt till HTML.

{{% /alert %}} 

## **Expandera text från höger till vänster vid export av Excel-fil till HTML**

Följande exempel konverterar [exempel Excel-fil](5115502.xlsx) till HTML. Denna skärmbild visar hur Excel-filen ser ut i Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Denna skärmbild visar [utdata HTML som genererades med den äldre versionen](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Denna skärmbild visar [utdata HTML som genererades med den nyare versionen](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Som du kan se i skärmbilderna expanderar den nyare versionen den högra inriktade texten till vänster korrekt, precis som Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
