---
title: 印刷するものが何もない場合、出力 PDF で空白ページを回避する
type: docs
weight: 30
url: /ja/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **考えられる使用シナリオ**

Excel ファイルが空で、ユーザーが Aspose.Cells を使用して PDF に保存すると、出力 PDF に空白のページが表示されます。場合によっては、このデフォルトの動作が望ましくないことがあります。 Aspose.Cells は[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)この問題に対処するプロパティ。として設定する場合**間違い**、 それから[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)出力 PDF に印刷するものがない場合に発生します。

## **印刷するものが何もない場合、出力 PDF で空白ページを回避する**

次のサンプル コードでは、空のワークブックを作成し、それを PDF として保存します。[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)プロパティとして**間違い**.出力 PDF には印刷するものが何もないため、[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)下図のように発生します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **例外**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
