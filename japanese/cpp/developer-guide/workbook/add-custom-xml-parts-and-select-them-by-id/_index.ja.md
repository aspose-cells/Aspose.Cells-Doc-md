---
title: カスタムXMLパーツを追加し、IDで選択する（C++）
linktitle: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 70
url: /ja/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aspose.Cellsを使用してExcelファイルにカスタムXMLパーツを追加および選択する方法を学びます。
---

## **可能な使用シナリオ**

カスタムXMLパーツは、Microsoft Excelドキュメント内部に格納されたXMLデータであり、それらと連携するアプリケーションによって利用されます。現時点では、Microsoft ExcelのUIを使って直接追加する方法はありません。ただし、VSTOやAspose.Cellsを使用してプログラム的に追加できます。[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)メソッドを使用してAspose.Cells APIでカスタムXMLパーツを追加し、[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)プロパティでIDを設定できます。IDで選択したい場合は、[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)メソッドを使用します。

## **カスタムXMLパーツの追加およびIDでの選択**

以下のサンプルコードは、まず[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)メソッドを使って4つのカスタムXMLパーツを追加し、その後[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)プロパティを使ってIDを設定します。最後に、[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)メソッドを使用して追加したカスタムXMLパーツの1つを検索または選択します。コードのコンソール出力も参考にしてください。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
