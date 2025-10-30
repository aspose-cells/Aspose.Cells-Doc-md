---  
title: Node.jsとC++を用いたリンク済みシェイプの値の更新  
linktitle: リンクされた形状の値をリフレッシュ  
type: docs  
weight: 3200  
url: /ja/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Aspose.Cells for Node.js via C++を使用してExcel内のリンクされたシェイプの値を更新する方法を学びます。  
---  

{{% alert color="primary" %}}  

Excelファイル内にリンクされたシェイプがあり、そのシェイプは特定のセルにリンクしています。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされたシェイプの値も変更されます。これはXLSやXLSX形式で保存する場合、Aspose.Cells for Node.js via C++でも問題なく動作します。ただし、PDFやHTML形式で保存したい場合は、[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)メソッドを呼び出してリンクされたシェイプの値を更新する必要があります。  

{{% /alert %}}  

## 例  

以下のスクリーンショットは、サンプルコードで使用されているソースExcelファイルを示しています。このファイルには、セルA1からE4にリンクされた画像があります。Aspose.Cellsを使ってセルB4の値を変更し、その後[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)メソッドを呼び出して画像の値を更新し、PDF形式で保存します。  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

指定されたリンク済みExcelファイル（[ソースExcelファイル](95584291.xlsx)）と出力PDF（[出力PDF](95584292.pdf)）はリンクからダウンロード可能です。  

### リンクされたシェイプの値を更新するNode.jsコード  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
