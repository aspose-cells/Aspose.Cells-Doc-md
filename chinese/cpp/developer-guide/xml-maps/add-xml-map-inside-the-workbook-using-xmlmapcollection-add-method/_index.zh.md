---
title: 使用XmlMapCollection.Add方法在工作簿内添加XML映射，使用C++
linktitle: 使用XmlMapCollection.Add方法在工作簿中添加XML映射
type: docs
weight: 10
url: /zh/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: 使用C++的XmlMapCollection.Add方法在工作簿内添加XML映射。
---

## **可能的使用场景**

Aspose.Cells 提供了 [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) 方法，您可以使用该方法将 XML 映射导入工作簿。

## **使用XmlMapCollection.Add方法在工作簿中添加XML映射**

以下示例代码使用 [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) 方法向工作簿中添加 XML 映射，并将其保存为 [输出 Excel 文件](5115434.xlsx)。屏幕截图显示了已从 [sample.xml](5115433.xml) 中导入的 XML 映射。

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
