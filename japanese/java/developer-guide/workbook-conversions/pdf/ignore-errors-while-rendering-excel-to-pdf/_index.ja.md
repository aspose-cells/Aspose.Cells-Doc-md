---
title: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 70
url: /ja/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **可能な使用シナリオ**

Excel ファイルを PDF に変換する際、エラーや例外が発生し、変換プロセスが中断されることがあります。このようなエラーをすべて無視して変換プロセスを完了させたい場合は、[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) プロパティを使用できます。このようにすることで、エラーや例外はスローされませんが、データの欠落が発生する可能性があります。したがって、データの損失が重要でない場合にのみ、このプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視**

以下のコードは、[サンプル Excel ファイル](55541813.xlsx) を読み込みますが、サンプル Excel ファイルにエラーがあります。17.11 では [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) プロパティを使用していますが、エラーはスローされません。ただし、このスクリーンショットに表示されているように、1 つの丸みを帯びた赤い矢印のような形状が失われています。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
