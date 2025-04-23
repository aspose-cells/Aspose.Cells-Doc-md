---
title: Inaktivera export av Frame Scripts och Dokumentegenskaper med C++
type: docs
weight: 310
url: /sv/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Inaktivera export av frame scripts och dokumentegenskaper med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells exporterar frame scripts och dokumentegenskaper när en arbetsbok konverteras till HTML. Version 8.6.0 av Aspose.Cells for C++ introducerar ett alternativ som tillåter att du valfritt inaktiverar export av frame scripts och dokumentegenskaper. Använd egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties för att inaktivera exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
