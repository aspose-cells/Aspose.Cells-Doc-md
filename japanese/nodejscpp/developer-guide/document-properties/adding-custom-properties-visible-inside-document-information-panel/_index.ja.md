---
title: Node.jsを通じてC++でドキュメント情報パネル内に表示可能なカスタムプロパティを追加します。
linktitle: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.Cells for Node.js via C++ を使って、ワークブックオブジェクトにカスタムプロパティを追加する方法を学びます。これらのプロパティはドキュメント情報パネルで閲覧できます。
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

Aspose.Cells for Node.js via C++は、ドキュメント情報パネル内に表示されるカスタムプロパティをワークブック内に追加するために使用できます。Microsoft Excelでは、ファイル > 情報 > プロパティ > ドキュメントパネルの表示メニューからドキュメント情報パネルを開くことができます。

[**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-)メソッドを使用して、ドキュメント情報パネルに表示されるカスタムプロパティを追加してください。

次のサンプルコードは、2つのカスタムプロパティを追加します。最初のプロパティにはタイプがなく、2つ目のプロパティにはDateTimeタイプがあります。このコードで生成されたExcelファイルを開くと、これらの2つのプロパティがドキュメント情報パネル内に表示されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
