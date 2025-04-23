---  
title: Node.js経由でC++を使用してスマートアートのテキストを置換  
linktitle: スマートアート内のテキストの置換  
type: docs  
weight: 1200  
url: /ja/nodejs-cpp/replace-text-in-smart-art/  
description: Aspose.Cells for Node.js via C++を使ったスマートアートのテキスト置換方法を学びます。  
---  

## **可能な使用シナリオ**  

スマートアートはワークブックの主要なオブジェクトの一つです。スマートアートのテキストを更新する必要がしばしばあります。Aspose.Cells for Node.js via C++はこの機能を、[**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)プロパティを設定することで提供します。  

次のリンクからサンプルソースファイルをダウンロードできます:  

[SmartArt.xlsx](77496338.xlsx)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SmartArt.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(sourceFilePath);

const worksheets = wb.getWorksheets();
for (let i = 0; i < worksheets.getCount(); i++) 
{
const worksheet = worksheets.get(i);
const shapes = worksheet.getShapes();
for (let j = 0; j < shapes.getCount(); j++) 
{
const shape = shapes.get(j);
shape.setAlternativeText("ReplacedAlternativeText"); // This works fine just as the normal Shape objects do.
if (shape.isSmartArt()) 
{
const smartArtShapes = shape.getResultOfSmartArt().getGroupedShapes();
for (let k = 0; k < smartArtShapes.length; k++) 
{
const smartart = smartArtShapes[k];
smartart.setText("ReplacedText"); // This doesn't update the text in Workbook which I save to the another file.
}
}
}
}

const options = new AsposeCells.OoxmlSaveOptions();
options.setUpdateSmartArt(true);
const outputFilePath = path.join(dataDir, "outputSmartArt.xlsx");
wb.save(outputFilePath, options);
```  

