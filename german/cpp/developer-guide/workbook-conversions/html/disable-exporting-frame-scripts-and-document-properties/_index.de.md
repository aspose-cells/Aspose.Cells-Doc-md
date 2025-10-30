---
title: Deaktivieren Sie das Exportieren von Frame Skripten und Dokumenteigenschaften mit C++
type: docs
weight: 310
url: /de/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Deaktivieren Sie das Exportieren von Frame Skripten und Dokumenteigenschaften mit Aspose.Cells in C++.
---

{{% alert color="primary" %}}

Aspose.Cells exportiert Frame-Skripte und Dokumenteigenschaften beim Konvertieren eines Arbeitsblatts in HTML. Version 8.6.0 von Aspose.Cells for C++ führt eine Option ein, die es ermöglicht, das Exportieren von Frame-Skripten und Dokumenteigenschaften optional zu deaktivieren. Bitte verwenden Sie die Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties, um das Exportieren zu deaktivieren.

{{% /alert %}}

## **Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften**

Der folgende Beispielcode ermöglicht es Ihnen, den Export von Rahmen-Skripten und Dokumenteigenschaften zu deaktivieren. Nach der Konvertierung einer Arbeitsmappe in HTML enthält die Ausgabedatei keine Rahmen-Skripte und Dokumenteigenschaften.

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
{{< app/cells/assistant language="cpp" >}}
