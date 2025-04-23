---  
title: Node.js経由でC++を使って背景処理を行うODSファイルの操作  
linktitle: ODSファイルでの背景の処理  
type: docs  
weight: 150  
url: /ja/nodejs-cpp/working-with-background-in-ods-files/  
description: Aspose.Cells for Node.js via C++を使用してODSファイルの背景を管理する方法。  
---  

## **ODSファイルでの背景**  

ODSファイルにシートに背景を追加することができます。背景は塗りつぶしの背景やグラフィック背景のいずれかです。この背景はファイルが開かれている場合は見えませんが、PDFとして印刷されると、PDFに背景が表示されます。背景は印刷プレビューダイアログにも表示されます。  

Aspose.Cells for Node.js via C++は、背景情報を読み取り、ODSファイルに背景を追加する機能を提供します。  

## **ODSファイルの背景を読み込む**  

Aspose.Cells for Node.js via C++は、背景管理のための[**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)クラスを提供します。以下のコードサンプルは、[ソースODS](90112030.ods)ファイルを読み込み、背景情報を取得するための[**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)クラスの使用例です。コードによって生成されたコンソール出力も参考にしてください。  

### **サンプルコード**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **コンソール出力**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **ODSファイルに色付きの背景を追加する**  

Aspose.Cells for Node.js via C++は、背景管理のための[**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)クラスを提供します。以下のコードサンプルは、[**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--)プロパティを使用してODSファイルにカラー背景を追加する例です。コードによって生成された[出力ODS](90112031.ods)ファイルも参考にしてください。  

### **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **ODSファイルにグラフィックの背景を追加する**  

Aspose.Cells for Node.js via C++は、背景管理のための[**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)クラスを提供します。以下のコードサンプルは、[**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--)プロパティを使用してグラフィック背景をODSファイルに追加する例です。コードによって生成された[出力ODS](90112030.ods)ファイルも参考にしてください。  

### **サンプルコード**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

