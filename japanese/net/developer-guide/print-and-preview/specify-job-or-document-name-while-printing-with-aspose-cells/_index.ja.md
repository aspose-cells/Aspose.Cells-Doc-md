---
title: Aspose.Cells で印刷時にジョブまたはドキュメント名を指定する
type: docs
weight: 270
url: /ja/net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

WorkbookRender や SheetRender オブジェクトを使用してワークブックやワークシートを印刷する際にジョブまたはドキュメント名を指定することができます。Aspose.Cells は、指定したジョブ名を使用してワークブックやワークシートを印刷するための WorkbookRender.ToPrinter(printerName, jobName) および SheetRender.ToPrinter(printerName, jobName) メソッドを提供しています。

{{% /alert %}}

## Aspose.Cellsを使用して印刷時にジョブまたは文書名を指定する

サンプルコードは、元のExcelファイルをロードし、WorkbookRender.ToPrinter（printerName、jobName）およびSheetRender.ToPrinter（printerName、jobName）メソッドを使用してジョブまたは文書名を指定して印刷用に送信します。

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
