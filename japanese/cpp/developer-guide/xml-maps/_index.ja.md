---
title: XMLをExcelワークブックにインポート（C++対応）
linktitle: XMLマップ
type: docs
weight: 210
url: /ja/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Aspose.Cellsを使ってXMLデータファイルからMicrosoft Excelにデータをインポート
---

{{% alert color="primary" %}}

Aspose.Cellsは[**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)メソッドを使用してワークブック内にXMLマップをインポートすることができます。Microsoft ExcelでXMLマップをインポートする手順は次のとおりです：

- **開発者**タブを選択。
- XMLセクションで**インポート**をクリックし、必要な手順に従います。

インポートを完了するためにXMLデータを提供する必要があります。テストに使用できる[サンプルXMLデータ](5115037.txt)を以下に示します。

{{% /alert %}}

## **Microsoft Excelを使用してXML Mapをインポート**

以下のスクリーンショットは、Microsoft Excelを使用してXML Mapをインポートする方法を示しています。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cellsを使用してXML Mapをインポートする**

以下のサンプルコードは、[**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)メソッドの使い方を示しています。スクリーンショットのように[出力Excelファイル](5115036.xlsx)を生成します。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **上級トピック**
- [XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する](/cells/ja/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [ブック内のXMLマップにリンクされたXMLデータをエクスポート](/cells/ja/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XMLマップのルート要素名を検出する](/cells/ja/cpp/find-the-root-element-name-of-xml-map/)
- [セルをXMLマップ要素にリンクする](/cells/ja/cpp/link-cells-to-xml-map-elements/)
