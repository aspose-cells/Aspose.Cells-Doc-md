---
title: 使用C++处理ContentTypeProperties
linktitle: 使用ContentTypeProperties
type: docs
weight: 150
url: /zh/cpp/working-with-contenttypeproperties/
description: 使用Aspose.Cells在Excel文件中添加自定义ContentTypeProperties。
---

Aspose.Cells提供[**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)方法添加自定义ContentTypeProperties到Excel文件中。你还可以通过设置[**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/)属性为**true**，使其成为可选。以下代码展示了如何添加可选的自定义ContentTypeProperties。图片显示了两个已添加的属性。

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

由示例代码生成的输出文件附在下方以供参考。

[输出文件](95584314.xlsx)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Add content type properties
    int index = workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(false);

    // Get current date and time
    time_t now = time(nullptr);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S", localtime(&now));
    U16String dateTime(buffer);

    // Add another content type property with current date and time
    index = workbook.GetContentTypeProperties().Add(u"MK32", dateTime, u"DateTime");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(true);

    // Save the workbook
    workbook.Save(outDir + u"WorkingWithContentTypeProperties_out.xlsx");

    std::cout << "Content type properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
