---
title: 导入HTML时删除换行后多余空格（使用C++）
linktitle: 导入HTML时删除换行后多余空格
type: docs
weight: 20
url: /zh/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: 了解如何在导入HTML时删除换行后的多余空格（使用Aspose.Cells for C++）。
---

{{% alert color="primary" %}}

 请使用[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/)属性，并将其设置为**true**，以删除换行标签后的所有多余空格。默认情况下，此属性为**false**，在输出Excel文件时会保留多余空格。

{{% /alert %}}

## 将HTMLLoadOptions.DeleteRedundantSpaces属性设置为false和true的效果

以下截图显示了将此属性设置为**false**和**true**的效果。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

在导入HTML时删除换行后的多余空格

###编程示例

以下示例代码展示了[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/)属性的用法。请将其设置为**true**或**false**以获得上面截图中显示的输出。

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
