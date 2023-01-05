---
title: 印刷するものが何もない場合、出力 PDF で空白ページを回避する
type: docs
weight: 30
url: /ja/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **考えられる使用シナリオ**

Excel ファイルが空で、ユーザーが Aspose.Cells を使用してそれを PDF に保存すると、出力 PDF で空白のページがレンダリングされます。このデフォルトの動作が望ましくない場合があります。 Aspose.Cells は[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)この問題に対処するプロパティ。として設定する場合**間違い**、 それから[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)出力PDFに印刷するものがない場合は常に発生します。

## **印刷するものが何もない場合、出力 PDF で空白ページを回避する**

次のサンプル コードでは、空のワークブックを作成し、設定後に出力 PDF として保存します。[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)プロパティとして**間違い**.出力 PDF には何も出力されないため、[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)下図のように発生します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **例外**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
