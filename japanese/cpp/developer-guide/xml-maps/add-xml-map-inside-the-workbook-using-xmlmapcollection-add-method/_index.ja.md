---
title: C++を使用してXmlMapCollection.Addメソッド内にXMLマップをワークブック内に追加
linktitle: XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する
type: docs
weight: 10
url: /ja/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: C++を使用してXmlMapCollection.Addメソッド内にXMLマップをワークブック内に追加
---

## **可能な使用シナリオ**

Aspose.CellsはXMLマップをブック内にインポートするために使用できる[**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/)メソッドを提供します。

## **XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する**

以下のサンプルコードは、[output excel file](5115434.xlsx)として保存される[サンプル.xml](5115433.xml)からインポートされたXMLマップをブック内に追加する[**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/)メソッドを使用しています。

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
