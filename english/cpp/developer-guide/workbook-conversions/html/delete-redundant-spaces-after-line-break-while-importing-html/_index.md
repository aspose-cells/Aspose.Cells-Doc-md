---
title: Delete redundant spaces after line break while importing HTML with C++
linktitle: Delete redundant spaces after line break while importing HTML
type: docs
weight: 20
url: /cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Learn how to delete redundant spaces after line breaks while importing HTML using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Please use [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) property and set it **true** to delete all the redundant spaces coming after the line break tag. By default, this property is **false** and redundant spaces are preserved in the output Excel files.

{{% /alert %}}

## Effect of setting the HTMLLoadOptions.DeleteRedundantSpaces property to false and true

The following screenshot shows the effect of setting this property to **false** and **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Delete redundant spaces after line break while importing HTML

### Programming Sample

The following sample code shows the usage of the [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) property. Please set it **true** or **false** to get the output as shown in the above screenshot.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
