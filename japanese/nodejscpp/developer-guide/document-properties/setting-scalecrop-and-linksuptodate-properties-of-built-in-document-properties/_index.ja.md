---
title: Node.jsを通じてC++で組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定
linktitle: ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する
type: docs
weight: 320
url: /ja/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for Node.js via C++を使用して、組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定方法を学習します。
---

## **可能な使用シナリオ**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--)と[BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--)は、OpenXmlフォーマット内で定義された2つの拡張された組み込みドキュメントプロパティです。これらのプロパティの目的は次の通りです。

## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**TRUE**に設定すると、ドキュメントサムネイルを表示に合わせてスケーリングします。この要素を**FALSE**に設定すると、ドキュメントサムネイルを表示に合わせてクロップします。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新であるかどうかを示します。この要素を**TRUE**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**FALSE**に設定すると、ハイパーリンクが更新されていないことを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する**
以下のサンプルコードは、ワークブックの[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--)と[BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--)拡張組み込みドキュメントプロパティを設定します。このコードで生成された[出力Excelファイル](5115500.xlsx)を確認し、拡張子を.zipに変更して中身を抽出し、app.xmlを上記のスクリーンショットのように表示してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
