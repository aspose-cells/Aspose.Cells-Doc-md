---
title: C++でXMLマップにリンクされたXMLデータをエクスポート
linktitle: ワークブックにリンクされたXML Map内のXMLデータをエクスポート
type: docs
weight: 20
url: /ja/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Aspose.Cells for C++を使用して、ワークブック内のXMLマップにリンクされたXMLデータをエクスポートする方法を学びます。
---

## **ブック内のXMLマップにリンクされたXMLデータをエクスポート**

ワークブック内のXMLマップにリンクされたXMLデータをエクスポートするには、[**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/)メソッドを使用してください。以下のサンプルコードは、ワークブックからすべてのXMLマップのXMLデータを一つずつエクスポートします。このコードで使用される[サンプルExcelファイル](5115497.xlsx)と[最初のXMLマップのエクスポート済みXMLデータ](5472487.xml)を確認してください。

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
