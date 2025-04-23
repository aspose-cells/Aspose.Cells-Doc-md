---
title: 用C++将单元格链接至XML映射元素
linktitle: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/cpp/link-cells-to-xml-map-elements/
description: 学习如何使用Aspose.Cells与C++将单元格链接至XML映射元素。
---

## **可能的使用场景**

您可以使用 Aspose.Cells 将单元格链接到 XML 地图元素。请使用此目的的 [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) 方法。

## **将单元格链接到 XML 地图元素**

以下示例代码加载了包含 XML 地图的 [源 Excel 文件](5115471.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在 [输出 Excel 文件](5115467.xlsx) 中。

如果您打开 [输出 Excel 文件](5115467.xlsx) 并单击“开发人员 > 源”按钮，您将看到单元格已链接到 XML 地图元素，并且它们也将被 Microsoft Excel 标记，如下图所示。

```cpp
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

    // Load sample workbook
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the Xml Map inside it
    XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Map FIELD1 and FIELD2 to cell A1 and B2
    ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
    ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");

    // Map FIELD4 and FIELD5 to cell C3 and D4
    ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
    ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");

    // Map FIELD7 and FIELD8 to cell E5 and F6
    ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
    ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
