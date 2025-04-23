---
title: C++でAspose.CellsにカスタムXMLパーツを使用する
linktitle: カスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/cpp/use-custom-xml-parts-in-aspose-cells/
description: Aspose.Cellsを使用してC++でプログラム的にExcelファイル内にカスタムXMLパーツを使用する方法を学びましょう。
---

## Aspose.Cells でカスタムXMLパーツを使用する

カスタムXMLパーツは、SharePointなどのさまざまなアプリケーションによってExcelファイル内に格納されるXMLデータです。このデータは、それを必要とするさまざまなアプリケーションによって消費されます。Microsoft Excelはこのデータを使用しないため、GUIから追加する仕組みはありません。このデータは、**.xlsx**の拡張子を**.zip**に変更して開くか、またはサードパーティのWindows圧縮ユーティリティ（WinRARやWinZipなど）を使用してZIPファイルとして開くことで閲覧可能です。このデータは**customXml**フォルダ内にあります。

Aspose.Cellsの [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) メソッドを使ってカスタムXMLパーツを追加可能。

以下のサンプルコードは、[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)メソッドを使用して「Book Catalog XML」を追加し、その名前を「BookStore」にする例です。このコードの結果を示す画像は以下の通りです。ご覧の通り、「Book Catalog XML」は、「BookStore」ノード内に追加されました。これはこのプロパティの名前です。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++によるカスタムXMLパーツの使用コード

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 関連記事

- [ドキュメント情報パネル内に表示されるカスタムプロパティの追加](/cells/ja/cpp/adding-custom-properties-visible-inside-document-information-panel/)
