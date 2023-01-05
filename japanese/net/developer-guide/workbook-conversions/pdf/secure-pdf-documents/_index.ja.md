---
title: 安全な PDF ドキュメント
type: docs
weight: 120
url: /ja/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

場合によっては、開発者は暗号化された PDF ファイルを操作する必要があります。たとえば、ユーザーと所有者のパスワードを使用してドキュメントを保護し、誰もがドキュメントを開くことができないようにしたり、ドキュメントの内容を印刷または抽出できるように制限したりする必要があります。

この記事では、スプレッドシートを PDF に保存するときに PDF セキュリティ オプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cells は[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity)セキュリティを扱うための名前空間。以下のサンプル コードは、PDF を Aspose.Cells で保護する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
