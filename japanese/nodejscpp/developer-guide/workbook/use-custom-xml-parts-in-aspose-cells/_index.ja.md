---
title: Node.js経由でC++を使用し、Aspose.CellsでカスタムXMLパーツを使用
linktitle: Aspose.Cells でカスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aspose.Cells for Node.js via C++を使ってカスタムXMLパーツの使用方法を学習し、外部XMLデータをExcelファイルにシームレスに統合します。
--- 

## Aspose.Cells でカスタムXMLパーツを使用する

カスタムXMLパーツは、SharePointなどの異なるアプリケーションによってExcelファイルに保存されるXMLデータです。このデータはそれを必要とするさまざまなアプリケーションによって使用されます。Microsoft Excelはこのデータを利用しないためGUIから追加できません。このデータは、**.xlsx** の拡張子を **.zip** に変更し、その後 **WinZip** で開くことで閲覧可能です。また、WinRARやWinZipなどのサードパーティのWindows圧縮ユーティリティを使ってZIPファイルを開くこともできます。データは**customXml**フォルダ内に存在します。

Aspose.Cellsの [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) メソッドを使ってカスタムXMLパーツを追加可能。

次のサンプルコードは、[**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) メソッドを使用し、**Book Store** という名前の **Book Catalog XML** を追加する例を示しています。以下の画像は、このコードの結果を示しています。ご覧の通り、Book Catalog XMLは、このプロパティの名前であるBookStoreノード内に追加されています。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Node.jsを使用したカスタムXMLパーツの使用コード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
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
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## 関連記事

- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
