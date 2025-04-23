---
title: ExcelをPDFにレンダリングする際にスライサーを描画する
type: docs
weight: 60
url: /ja/java/draw-slicer-while-rendering-excel-to-pdf/
---

## **ExcelをPDFにレンダリングする際にスライサーを描画する**
スライサーが適用されたExcelファイルがあり、そのスライサー設定を含むPDFファイルにExcelファイルをエクスポートしたい場合、Aspose.Cellsはこれをデフォルトでサポートしています。Excelファイルをスライサー付きでPDFにエクスポートするだけで、生成されたPDFにはスライサーが適用されます。

次のサンプルコードは、既存のスライサーが含まれる[sample Excel file](SampleSlicerChart.xlsx)をロードします。次に、ワークブックを[output PDF file](SampleSlicerChart.pdf)として保存します。以下のスクリーンショットは、元のExcelファイルと生成されたPDFファイルを比較しています。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-ExportSlicerToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
