---
title: 用 C++ 使用内置文档属性指定Excel文件的语言
linktitle: 指定Excel文件的语言
type: docs
weight: 30
url: /zh/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: 学习如何使用 Aspose.Cells for C++ 编程改变Excel文件的语言。
---

## **可能的使用场景**

你可以通过右键点击文件，选择 属性 > 详细信息，并编辑“语言”字段，来更改Excel文件的语言。请使用 [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) 属性通过 Aspose.Cells API 以编程方式更改。

## **使用内置文档属性指定Excel文件的语言**

以下示例代码创建一个工作簿，并更改其名为“Language”的内置文档属性。请查看由此代码生成的[输出Excel文件](64716891.xlsx)，以及显示通过 [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) 属性修改的“语言”字段的截图。

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
