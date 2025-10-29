---
title: 用 C++ 指定Excel文件的文档版本，通过内置文档属性
linktitle: 指定文档版本
type: docs
weight: 20
url: /zh/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: 学习如何使用 Aspose.Cells for C++ 通过内置文档属性指定Excel文件的版本。
---

## **可能的使用场景**

你可以通过右键点击文件，然后选择 属性 > 详细信息并编辑“版本号”字段，来更改Excel文件的**版本号**。请使用 [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) 属性通过 Aspose.Cells API 以编程方式更改。

## **使用内置文档属性指定Excel文件的文档版本**

以下示例代码创建一个工作簿并更改其内置文档属性，包括标题、作者和版本号。请查看由此代码生成的[输出Excel文件](64716811.xlsx)和截图，显示通过 [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) 属性修改的版本号。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **示例代码**

```cpp
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

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
