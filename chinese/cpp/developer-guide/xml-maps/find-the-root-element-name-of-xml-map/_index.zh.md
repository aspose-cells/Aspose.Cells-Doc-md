---
title: 用C++查找XML映射的根元素名称
linktitle: 查找 XML 地图的根元素名称
type: docs
weight: 30
url: /zh/cpp/find-the-root-element-name-of-xml-map/
description: 学习如何使用Aspose.Cells for C++查找XML映射的根元素名称。
---

## **可能的使用场景**

您可以使用 Aspose.Cells 的 [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) 属性来查找 *XML 地图的根元素名称* 。以下屏幕截图显示了 Microsoft Excel 中 XML 地图的根元素名称。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **示例代码**

以下示例代码加载了 [示例 Excel 文件](55541789.xlsx) 并访问了第一个 XML 地图，并打印了它的 [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) 属性。请参见下面给出的示例代码的控制台输出。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **控制台输出**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
