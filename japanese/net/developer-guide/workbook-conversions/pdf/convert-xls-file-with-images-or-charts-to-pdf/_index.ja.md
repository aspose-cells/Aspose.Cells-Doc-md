---
title: 画像またはチャートを含む XLS ファイルを PDF に変換します
type: docs
weight: 50
url: /ja/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells は、画像とチャートを含む XLS ファイルの PDF ドキュメントへの変換をサポートします。 Aspose.Cells for .NET は独立してスプレッドシートを PDF に変換できます: Aspose.PDF for .NET は変換に必要ありません。プロセスは一時または中間の XML ファイルに依存しないため、プロセスはメモリ内で実行できます。これは、画像、チャート、その他の描画オブジェクトを含む大きな Excel ファイルをすばやく効率的に変換できることを意味します。

{{% /alert %}} 
## **サンプルコード**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、[Workbook.計算式](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)メソッドを PDF にレンダリングする直前に実行します。これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
