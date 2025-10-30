---
title: C++を使ってXMLマップのルート要素名を見つける方法
linktitle: XML Mapのルート要素名を検索する
type: docs
weight: 30
url: /ja/cpp/find-the-root-element-name-of-xml-map/
description: Aspose.Cells for C++を使ってXMLマップのルート要素名を見つける方法を学びます。
---

## **可能な使用シナリオ**

Microsoft ExcelでXMLマップの*ルート要素名*を[**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/)プロパティを使用して検索できます。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **サンプルコード**

次のサンプルコードは、[sample Excel file](55541789.xlsx)を読み込み、最初のXMLマップにアクセスし、その[**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/)プロパティを出力します。

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

## **コンソール出力**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
