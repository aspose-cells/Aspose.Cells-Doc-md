---
title: ContentTypePropertiesの操作（C++使用例）
linktitle: ContentTypePropertiesの操作
type: docs
weight: 150
url: /ja/cpp/working-with-contenttypeproperties/
description: Aspose.Cellsを使ってC++でExcelファイルにカスタムContentTypePropertiesを追加します。
---

Aspose.Cellsは、ExcelファイルにカスタムContentTypePropertiesを追加するための [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) メソッドを提供します。 [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) プロパティを **true** に設定することで、プロパティをオプションにすることも可能です。以下のコードスニペットは、オプションのカスタムContentTypePropertiesをExcelファイルに追加する例です。以下の画像は、サンプルコードで追加された両方のプロパティを示しています。

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

サンプルコードによって生成された出力ファイルが添付されています。

[出力ファイル](95584314.xlsx)

## **サンプルコード**

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
