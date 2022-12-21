---
title: Aspose.Cells で印刷中にジョブまたはドキュメント名を指定する
type: docs
weight: 270
url: /ja/net/specify-job-or-document-name-while-printing-with-aspose-cells/
---
{{% alert color="primary" %}}

WorkbookRender または SheetRender オブジェクトを使用してワークブックまたはワークシートを印刷するときに、ジョブまたはドキュメント名を指定できます。 Aspose.Cells は、ワークブックまたはワークシートの印刷中にジョブ名を指定するために使用できる WorkbookRender.ToPrinter(printerName, jobName) および SheetRender.ToPrinter(printerName, jobName) メソッドを提供します

{{% /alert %}}

## Aspose.Cells で印刷中にジョブまたはドキュメント名を指定する

サンプル コードは、ソース Excel ファイルを読み込み、WorkbookRender.ToPrinter(printerName, jobName) および SheetRender.ToPrinter(printerName, jobName) メソッドを使用してジョブまたはドキュメント名を指定することにより、プリンターに送信します。

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
