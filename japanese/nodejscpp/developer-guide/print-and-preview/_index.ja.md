---  
title: Node.jsを使ったワークブックのプレビュー（C++経由）  
linktitle: ワークブックのプレビュー 
type: docs  
weight: 70  
url: /ja/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cellsは、Microsoft Excelをインストールせずとも、Node.js経由のC++を使ってExcelファイルの印刷とプレビューをサポートしています。  
---  

## **印刷プレビュー**  

数百ページのExcelファイルをPDFや画像に変換する必要がある場合があります。これらのファイルを処理すると、多大な時間とリソースを消費します。そんな時、ワークブックとワークシートの印刷プレビュー機能が役立ちます。変換前に総ページ数を確認し、変換の可否を判断できます。この記事では、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスを使って総ページ数を調べる方法に焦点を当てます。  

Aspose.Cellsには印刷プレビュー機能があり、そのために[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスを提供します。全ワークブックの印刷プレビューを作成するには、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)クラスのインスタンスを作成し、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)オブジェクトを引数に渡します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)クラスには、このプレビューのページ数を返す[**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--)メソッドがあります。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)クラスと同様に、[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスは特定のワークシートの印刷プレビューを生成するために使われます。ワークシートのプレビューを作成するには、[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスのインスタンスを作成し、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)オブジェクトを渡します。[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスも、生成されたプレビューのページ数を返す[**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--)メソッドを提供します。  

次のコードスニペットは、[サンプルエクセルファイル](94896177.xlsx)を使った[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)クラスの両方の使用例を示しています。  

### **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

上記のコードを実行した結果生成された出力は次のとおりです。  

### **コンソール出力**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **高度なトピック**  
- [スプレッドシートのレンダリング用フォントの設定](/cells/ja/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [ワークシートをイメージに変換 - データ周りの空白を削除](/cells/ja/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [ImageOrPrintオプションを使用してワークシートを画像に変換](/cells/ja/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [ワークシートのセルの範囲をイメージにエクスポート](/cells/ja/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [ImageOrPrintOptionsを使用してワークシートから画像を抽出](/cells/ja/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [ワークシートのサムネイルを生成](/cells/ja/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [印刷するものがない場合、空白ページを出力](/cells/ja/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [ページ設定および印刷オプション](/cells/ja/nodejs-cpp/page-setup-and-printing-options/)  
- [ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする](/cells/ja/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [ワークシートをグラフィックコンテキストにレンダリング](/cells/ja/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する](/cells/ja/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

