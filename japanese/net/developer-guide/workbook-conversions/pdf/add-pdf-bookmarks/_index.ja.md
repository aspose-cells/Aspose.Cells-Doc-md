---
title: PDFブックマークを追加する
type: docs
weight: 10
url: /ja/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

この記事では、スプレッドシートをPDFに変換する際にPDFブックマークを挿入する方法についての情報を提供します。

ダイナミックにブックマークを追加できるAspose.Cells。PDFブックマークは、長い文書の操作性を飛躍的に改善することができます。PDF文書にブックマークリンクを追加する際、ページにリンクするのに限定されることはありません。確かなビューを設定することができます。

{{% /alert %}}

次のサンプルコードでは、シンプルなワークブックを生成し、PDFブックマークとその場所の特定を指定し、PDFファイルを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式がある場合は、PDF形式でレンダリングする直前に[**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)を呼び出すことが最適です。これにより、数式に依存する値が更新され、正しくPDFにレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
