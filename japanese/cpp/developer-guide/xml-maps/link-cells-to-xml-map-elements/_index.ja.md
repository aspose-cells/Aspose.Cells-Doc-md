---
title: C++を使ってセルとXMLマップの要素をリンクする方法
linktitle: セルをXML Map要素にリンク
type: docs
weight: 50
url: /ja/cpp/link-cells-to-xml-map-elements/
description: Aspose.Cellsを使って、セルとXMLマップの要素をリンクする方法を学びます。
---

## **可能な使用シナリオ**

Aspose.Cellsを使用して、セルをXMLマップの要素にリンクできます。この目的には[**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/)メソッドを使用してください。

## **Xml Map要素にセルをリンク**

次のサンプルコードは、XML Mapを含む[source excel file](5115471.xlsx)を読み込み、セルA1、B2、C3、D4、E5、F6をそれぞれXML Map要素FIELD1、FIELD2、FIELD4、FIELD5、FIELD7、FIELD8にリンクし、[output excel file](5115467.xlsx)としてブックを保存します。

[output excel file](5115467.xlsx)を開いて、開発者 > ソース ボタンをクリックすると、セルがXMLマップの要素にリンクされ、Microsoft Excelによって強調表示されます。

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
