---  
title: 画像をNode.js経由でC++で操作  
linktitle: 画像  
type: docs  
weight: 300  
url: /ja/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。  
{{% /alert %}}  

## ワークブックをTIFF形式に変換  

Excelファイルは複数のシートと複数ページを含むことができます。[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)を使えば、Excelを多ページのTIFFに変換可能です。さらに、[ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--)、[ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--)、解像度([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)、[ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)) を制御できます。  

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **ワークシートをイメージに変換**  

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。  

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) クラスは、画像として描画するワークシートを表します。オーバーロードされた [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-) メソッドにより、異なる属性またはオプションを持つワークシートの画像ファイルへの変換が可能です。それは Buffer オブジェクトを返し、画像ファイルをディスクに保存したりストリームに流したりできます。BMP、PNG、GIF、JPG、JPEG、TIFF、EMF など、多くの画像フォーマットをサポート。  

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。  
{{% /alert %}}  

## **ワークシートをSVGに変換**  

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。  

バージョン7.1.0以降、Aspose.Cells for Node.js via C++はワークシートをSVG画像に変換できるようになりました。以下のコードスニペットは、Excelファイル内のワークシートをSVG画像に変換する例を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **高度なトピック**  
- [Excelのチャートを画像に変換](/cells/ja/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [SVG形式でチャートを画像に変換](/cells/ja/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
