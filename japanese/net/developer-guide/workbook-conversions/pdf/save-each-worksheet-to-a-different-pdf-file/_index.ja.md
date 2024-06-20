---
title: 異なるPDFファイルにそれぞれのワークシートを保存する
type: docs
weight: 130
url: /ja/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像、グラフなどを含むXLSファイルをPDFドキュメントに変換する機能をサポートしています。Aspose.Cells for .NETを使用してスプレッドシートをPDFに変換するためには、Aspose.PDF for .NETを使用する必要はありません。この変換では、一時ファイルを作成または使用するためのソフトウェアが必要ではなく、プロセス全体をメモリで行うことができます。

{{% /alert %}} 
## **異なるPDFファイルごとに各ワークシートを保存**
テンプレートExcelファイルの各ワークシートを保存して異なるPDFファイルを生成する必要がある場合は、これを簡単に実現できます。 1回に1シートインデックスを[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)オプションに設定して、PDFにレンダリングします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
