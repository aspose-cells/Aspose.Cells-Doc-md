---
title: Node.jsとC++を使ったドキュメントプロパティの管理
linktitle: ドキュメントプロパティ
type: docs
weight: 80
url: /ja/nodejs-cpp/managing-document-properties/
description: Aspose.Cells for Node.js via C++ APIを使ってドキュメントプロパティを管理する方法を学びます。
keywords: Node.js経由でC++を使用してドキュメントのプロパティを管理する方法、Node.jsを通じてドキュメントのプロパティを取得または設定する方法、Node.js経由でC++を使用してドキュメントのプロパティの追加または削除を行う方法、Node.jsを通じてC++でドキュメントのプロパティを挿入または削除する方法、Aspose.Cells for Node.js via C++ APIを使用してドキュメントのプロパティにアクセスする方法。
---


## **紹介**

Microsoft Excelはスプレッドシートファイルにプロパティを追加できる機能を提供します。これらのドキュメントプロパティは有用な情報を提供し、以下のように2つのカテゴリに分かれています。

- システム定義（組み込み）プロパティ: 組み込みプロパティには文書のタイトル、作成者名、文書の統計などの一般的な情報が含まれています。
- ユーザー定義（カスタム）プロパティ: ユーザーが名前-値のペアの形式で定義したカスタムプロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタムプロパティについて知っておくべき最も重要な点は、組み込みプロパティはアクセスおよび変更が可能ですが、作成または削除はできないということです。一方、カスタムプロパティは作成および管理が可能です。

{{% /alert %}}

## **Microsoft Excelを使用してドキュメントプロパティを管理する方法**

Microsoft Excelでは、ExcelファイルのドキュメントプロパティをWYSIWYG方式で管理できます。Excel 2016で**プロパティ**ダイアログを開く手順については、下記をお尋ねください。

1. **ファイル**メニューから**情報**を選択します。

|**情報メニューを選択**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **プロパティ**の見出しをクリックし、「詳細プロパティ」を選択します。

|**詳細プロパティの選択をクリック**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. ファイルのドキュメントプロパティを管理します。

|**プロパティダイアログ**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
プロパティダイアログでは、一般、概要、統計、内容、カスタムのような異なるタブがあります。各タブはファイルに関連する異なる種類の情報を設定するのに役立ちます。カスタムタブはカスタムプロパティを管理するために使用されます。

## **Aspose.Cellsを使用してドキュメントプロパティを操作する方法**

開発者はAspose.CellsのAPIを使用してドキュメントプロパティを動的に管理できます。この機能により、ファイルが受信された時点、処理された時点、タイムスタンプなどの有用な情報をファイルと一緒に保存できます。

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++はAPIおよびバージョン番号の情報を出力ドキュメントに直接記述します。例えば、ドキュメントをPDFにレンダリングするとき、Aspose.Cells for Node.js via C++は**Application**フィールドに'Aspose.Cells'を、**PDF Producer**フィールドに例えば'Aspose.Cells v17.9'を設定します。

この情報を出力ドキュメントから変更または削除するよう关于Aspose.Cells for Node.js via C++に指示できないことに注意してください。

{{% /alert %}}

### **ドキュメントプロパティにアクセスする方法**

Aspose.Cells APIは、組み込みとカスタムの両方のタイプのドキュメントプロパティをサポートします。Aspose.Cellsの[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスはExcelファイルを表し、そのようにファイルと同様に、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは複数のワークシートを含むことができ、各ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表され、ワークシートのコレクションは[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)クラスによって表されます。

下記の説明のとおり、[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)を使用してファイルのドキュメントプロパティにアクセスします。

- 組み込みドキュメントプロパティにアクセスするには、[**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--)を使用します。
- カスタムドキュメントのプロパティにアクセスするには[**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--)を使用します。

[**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--)と[**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--)はどちらも[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/)のインスタンスを返します。このコレクションは[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)オブジェクトを含み、各オブジェクトは単一の組み込みまたはカスタムドキュメントプロパティを表します。

どのようにプロパティにアクセスするかはアプリケーションの要件次第です。すなわち、例の通り[**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/)のインデックスまたは名前を使用します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)クラスは、ドキュメントプロパティの名前、値、型を取得できます。

- プロパティ名を取得するには[**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--)を使用します。
- プロパティの値を取得するには、[**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--)を使用します。[**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--)は値をObjectとして返します。
- プロパティの型を取得するには、[**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--)を使用します。これは[**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/)列挙値のいずれかを返します。プロパティの型を取得した後、適切な型の値を取得するために**DocumentProperty.ToXXX**メソッドのいずれかを使用してください。これらのメソッドは下表に記載されています。

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)クラスはまた、他のデータ型の値を返すメソッドセットも提供します。

{{% /alert %}}

|**メンバー名**|**説明**|**ToXXXメソッド**|
| :- | :- | :- |
|Boolean|プロパティのデータ型はブールです|ToBool|
|Date|プロパティのデータ型は日時です。Microsoft Excelでは日付部分のみが保存され、時刻は保存されません。|ToDateTime|
|Float|プロパティのデータ型はダブルです|ToDouble|
|Number|プロパティのデータ型はInt32です|ToInt|
|String|プロパティのデータ型はstring|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **カスタムドキュメントプロパティの追加または削除方法**

このトピックの冒頭で既に説明した通り、ビルトインプロパティはシステム定義されたものであり、開発者は追加または削除することはできませんが、ユーザー定義のカスタムプロパティを追加または削除することは可能です。

### **カスタムプロパティの追加方法**

Aspose.Cells APIは、[**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-)メソッドを公開し、[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/)クラスにカスタムプロパティを追加できるようにしています。[**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-)メソッドは、Excelファイルにプロパティを追加し、新しいドキュメントプロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)オブジェクトとして返します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **「コンテンツにリンク」カスタムプロパティの構成方法**

指定された範囲の内容にリンクされたカスタムプロパティを作成するには、[**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-)メソッドを呼び出し、プロパティ名とソースを渡します。プロパティがコンテンツにリンクされているかどうかは、[**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--)プロパティを使用して確認できます。さらに、[**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)クラスの[**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--)プロパティを使用してソース範囲を取得可能です。

この例では、シンプルなテンプレートのMicrosoft Excelファイルを使用します。 ワークブックには、**MyRange**と表記された名前付き範囲があり、セルの値を参照しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **カスタムプロパティを削除する方法**

Aspose.Cellsを使用してカスタムプロパティを削除するには、[**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-)メソッドを呼び出し、削除するドキュメントプロパティの名前を渡します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **高度なトピック**
- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する](/cells/ja/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する](/cells/ja/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する](/cells/ja/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="nodejs-cpp" >}}
