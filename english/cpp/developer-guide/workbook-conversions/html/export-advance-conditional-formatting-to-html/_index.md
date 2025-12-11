---
title: Export DataBar, ColorScale, and IconSet Conditional Formatting while Converting Excel to HTML with C++
linktitle: Export Conditional Formatting to HTML
type: docs
weight: 30
url: /cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Learn how to export DataBar, ColorScale, and IconSet conditional formatting while converting Excel files to HTML using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

You can export DataBar, ColorScale, and IconSet Conditional Formatting while converting your Excel file into HTML. This feature is partially supported by Microsoft Excel but Aspose.Cells for C++ supports it fully.

{{% /alert %}} 

## **Export DataBar, ColorScale, and IconSet Conditional Formatting while Converting Excel to HTML**
The following screenshot shows the [sample Excel file](5115558.xlsx) with DataBar, ColorScale, and IconSet Conditional Formatting. You can download the [sample Excel file](5115558.xlsx) from the given link.

![todo:image_alt_text](conversion_1.png)

The following screenshot shows the Aspose.Cells output HTML file showing DataBar, ColorScale, and IconSet Conditional Formatting. As you can see, it looks exactly like the [sample Excel file](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Sample Code**
The following sample code converts the sample Excel file into HTML, which is just a normal [Excel to HTML conversion](/cells/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample Excel file into a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
