---  
title: Node.jsとC++を使用したワークブックのフォントの個別またはプライベートセットの指定方法  
linktitle: ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Aspose.Cells for Node.js via C++を使用して、ワークブックのレンダリング時に個別またはプライベートなフォントセットを指定する方法を学びます。  
---  

## **可能な使用シナリオ**  

通常、すべてのワークブックに対してフォントディレクトリまたはフォントのリストを指定しますが、場合によっては、個別またはプライベートなフォントセットを指定する必要があります。Aspose.Cells for Node.js via C++は、ワークブック用に個別またはプライベートなフォントセットを指定できる[**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs)クラスを提供します。  

## **ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する**  

以下のサンプルコードは、[**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs)クラスを使用して個別またはプライベートなフォントセットを持つ[サンプルExcelファイル](67338268.xlsx)をロードします。コード内で利用される[サンプルフォント](67338271.zip)と、それによって生成される[出力PDF](67338269.pdf)も参照してください。スクリーンショットでは、フォントが正常に見つかった場合の出力PDFの見た目です。  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

