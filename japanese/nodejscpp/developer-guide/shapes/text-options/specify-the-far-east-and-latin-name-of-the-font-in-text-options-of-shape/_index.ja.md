---  
title: Node.jsとC++を通じて形状のテキストオプションで東アジアとラテン文字のフォント名を指定する方法  
linktitle: テキストオプションのフォントの遠隔地およびラテン名を指定する  
type: docs  
weight: 1600  
url: /ja/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Aspose.Cells for Node.js via C++を使用して、Shapeのテキストオプションで東アジアとラテンフォント名を指定する方法を学びます。  
---  

## **可能な使用シナリオ**  

時には、東アジア言語のフォント（例：日本語、中国語、タイ語など）でテキストを表示したい場合があります。Aspose.Cells for Node.js via C++は、東アジア言語のフォント名を指定するための [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) プロパティを提供します。さらに、[**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--) プロパティを使用してラテンフォント名も指定できます。  

## **テキストオプションのフォントの遠隔地およびラテン名を指定する**  

次のサンプルコードは、テキストボックスを作成し、その中に日本語のテキストを追加します。次に、テキストのラテンフォント名と東アジアフォント名を指定し、ワークブックを[出力Excelファイル](67338274.xlsx)として保存します。以下のスクリーンショットは、Microsoft Excelで出力されたテキストボックスのラテンと東アジアフォント名を示しています。  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

