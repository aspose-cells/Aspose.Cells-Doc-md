---
title: 在Aspose.Cells中使用C++的自定义XML部分
linktitle: 使用自定义XML部分
type: docs
weight: 390
url: /zh/cpp/use-custom-xml-parts-in-aspose-cells/
description: 学习如何使用Aspose.Cells在Excel文件中以编程方式使用自定义XML部分。
---

## 在Aspose.Cells中使用自定义XML部件

自定义XML部分是由不同应用程序（如SharePoint）存储在Excel文件内的XML数据。这些数据由需要的应用程序使用。Microsoft Excel不使用这些数据，因此没有GUI来添加它。你可以通过将**.xlsx**的扩展名改为**.zip**，然后用**WinZip**打开，查看此数据。你也可以用第三方Windows压缩工具（如WinRAR或WinZip）打开ZIP文件。数据在**customXml**文件夹内。

你可以通过调用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)方法，使用Aspose.Cells添加自定义XML部分。

以下示例代码使用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)方法添加了名为**Book Store**的**Book Catalog XML**，其效果如下图所示。你可以看到，Book Catalog XML被加入至BookStore节点中，这是此属性的名称。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 使用C++的自定义XML部分的代码示例

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 相关文章

- [在文档信息面板中添加可见的自定义属性](/cells/zh/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
