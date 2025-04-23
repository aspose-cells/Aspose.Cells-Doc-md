---  
title: BuiltInドキュメントプロパティを使用してExcelファイルのバージョンを指定する方法（Node.jsとC++を使用）  
linktitle: ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Node.jsとC++を使用して、組み込みドキュメントプロパティを使ったExcelファイルのバージョン指定方法を学びます。  
---  

## **可能な使用シナリオ**  

Excelファイルの**バージョン番号**を変更するには、ファイルを右クリックして[プロパティ] > [詳細]を選択し、**バージョン番号**フィールドを編集します。Aspose.Cells APIを使用してプログラム的に変更するには[**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)プロパティを使用してください。  

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**  

次のサンプルコードは、ワークブックを作成し、その組み込みドキュメントプロパティ（タイトル、著者、バージョン番号）を変更します。コードで生成された[出力Excelファイル](64716811.xlsx)と、[**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)プロパティによって修正されたバージョン番号のスクリーンショットを確認してください。  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

