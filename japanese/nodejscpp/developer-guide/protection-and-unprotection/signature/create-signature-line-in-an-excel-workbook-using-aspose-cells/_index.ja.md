---  
title: Aspose.Cells for Node.js via C++を使用してExcelワークブックに署名線を作成  
linktitle: Aspose.Cellsを使用してExcelブック内に署名行を作成する  
type: docs  
weight: 150  
url: /ja/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: この記事は、Node.jsコードを使用してAspose.Cells for Node.js via C++でExcelワークブックに署名線を作成する方法を説明します。  
keywords: Node.jsを用いてC++経由でExcelワークブックに署名線を作成する方法、署名線を作成する方法、署名線を追加する方法、Excelファイルに署名線を追加する方法。  
---  

## **紹介**  

Microsoft ExcelはExcelブック内に**署名行**を追加する機能を提供しています。**挿入**タブをクリックし、**テキスト**グループから**署名行**を選択して、署名行を追加できます。  

## **Excelファイルの署名行を作成する方法**  

Aspose.Cells for Node.js via C++はこの機能も提供しており、この目的のために[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)プロパティを公開しています。この記事では、このプロパティを使用してAspose.Cellsで署名線を追加する方法について説明します。  

以下のサンプルコードは、[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)プロパティを使用して署名線を追加し、ワークブックを保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

