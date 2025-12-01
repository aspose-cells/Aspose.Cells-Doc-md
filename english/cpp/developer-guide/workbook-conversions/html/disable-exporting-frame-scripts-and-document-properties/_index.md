---
title: Disable Exporting Frame Scripts and Document Properties with C++
type: docs
weight: 310
url: /cpp/disable-exporting-frame-scripts-and-document-properties/
description: Disable exporting frame scripts and document properties using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells exports frame scripts and document properties while converting a workbook into HTML. The 8.6.0 version of Aspose.Cells for C++ introduces an option which allows you to optionally disable exporting frame scripts and document properties. Please use the HtmlSaveOptions.ExportFrameScriptsAndProperties property to disable the export.

{{% /alert %}}

## **Disable exporting frame scripts and document properties**

The following sample code allows you to disable exporting frame scripts and document properties. Once you convert a workbook into HTML, the output file will not contain any frame scripts and document properties.

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
