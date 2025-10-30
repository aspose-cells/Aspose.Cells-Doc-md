---
title: ExcelをPDFにレンダリングする際にスライサーを描画する
type: docs
weight: 60
url: /ja/nodejs-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **ExcelをPDFにレンダリングする際にスライサーを描画する**
既存のExcelファイルにスライサーが適用されている場合、その設定を維持してExcelをPDFにエクスポートしたい場合、Aspose.Cells for Node.js via C++はデフォルトでこれをサポートします。スライサーを適用したExcelファイルをPDFにエクスポートすると、スライサーの設定も反映されます。

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](94044165.xlsx)を読み込みます。その後、ワークブックを[output PDFファイル](94044166.pdf)として保存します。次のスクリーンショットは、元のExcelファイルと生成されたPDFファイルを比較しています。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **サンプルコード**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-ExportSlicerToPDF-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
