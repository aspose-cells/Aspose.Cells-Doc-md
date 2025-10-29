---
title: 使用C++导出与XML映射关联的XML数据
linktitle: 导出工作簿中与 XML 地图关联的 XML 数据
type: docs
weight: 20
url: /zh/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: 学习如何使用Aspose.Cells for C++在工作簿内导出与XML映射相关联的XML数据。
---

## **导出链接到工作簿中的 XML 映射的 XML 数据**

请使用[**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/)方法导出工作簿内与XML映射相关联的XML数据。以下示例代码逐个导出所有XML映射的XML数据。请查看此代码中使用的【示例Excel文件】(5115497.xlsx) 和【第一个XML映射导出的XML数据】(5472487.xml)。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get XML maps from the workbook
    auto xmlMaps = workbook.GetWorksheets().GetXmlMaps();

    // Export all XML data from all XML Maps from the Workbook
    for (int i = 0; i < xmlMaps.GetCount(); i++)
    {
        // Access the XML Map
        XmlMap map = xmlMaps.Get(i);

        // Exports its XML Data to file
        workbook.ExportXml(map.GetName(), outDir + map.GetName() + u".xml");
    }

    std::cout << "XML data exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
