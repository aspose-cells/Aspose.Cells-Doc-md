---
title: Recognise Self Closing Tags with C++
linktitle: Recognise Self Closing Tags
type: docs
weight: 120
url: /cpp/recognise-self-closing-tags/
description: Learn how to handle self-closing tags in HTML using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

HTML can have a variety of tag formats for empty tags like `<td></td>` or `<td/>`. Aspose.Cells now supports both of these formats, whereas earlier it supported only `<td></td>`-like tags. This feature can be tested by converting the attached sample HTML file to an Excel file. The sample HTML file and the output Excel file can be downloaded from the following links for testing.

[sampleSelfClosingTags.html](sampleSelfClosingTags)

[outsampleSelfClosingTags.xlsx](73990156.xlsx)

## **Sample Code**

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

    // Set HTML load options and keep precision true
    HtmlLoadOptions loadOptions(LoadFormat::Html);

    // Load sample source file
    Workbook wb(srcDir + u"sampleSelfClosingTags.html", loadOptions);

    // Save the workbook
    wb.Save(outDir + u"outsampleSelfClosingTags.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
