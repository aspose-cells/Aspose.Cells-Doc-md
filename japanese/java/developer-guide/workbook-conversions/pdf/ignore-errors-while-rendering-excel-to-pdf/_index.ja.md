---
title: Excel を PDF にレンダリングする際のエラーを無視する
type: docs
weight: 70
url: /ja/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **考えられる使用シナリオ**

Excel ファイルを PDF に変換するときに、エラーまたは例外が発生し、変換プロセスが終了することがあります。を使用して、変換プロセス中にそのようなエラーをすべて無視できます。[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)財産。このようにして、変換プロセスはエラーや例外をスローすることなくスムーズに完了しますが、データが失われる可能性があります。したがって、データの損失が重大でない場合にのみ、このプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視する**

次のコードは、[サンプル Excel ファイル](55541813.xlsx)しかし、サンプルの Excel ファイルには誤りがあり、実行中にエラーがスローされます。[PDFへの変換](55541814.pdf)17.11では使用していますが、使用しているため[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)プロパティ、それはエラーをスローしません。ただし、このスクリーンショットに示されているような丸い赤い矢印のような形状が 1 つ失われています。

![todo:画像_代替_文章](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
