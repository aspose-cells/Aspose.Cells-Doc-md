---
title: 安全な PDF ドキュメント
type: docs
weight: 120
url: /ja/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

場合によっては、開発者は暗号化された PDF ファイルを操作する必要があります。例えば：

- 所有者パスワードとユーザーパスワードを使用してドキュメントを保護し、誰でも開くことができないようにします。
- ドキュメントを開いた後、ドキュメントに対する制限またはアクセス許可を設定します。たとえば、ドキュメントのコンテンツを印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートを PDF に保存するときに PDF セキュリティ オプションを渡す方法について説明します。

{{% /alert %}}

 Aspose.Cellsが提供します[**PDFセキュリティオプション**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)セキュリティ関連の作業に使用します。 PDF に保存するときに、所有者パスワードとユーザー パスワードを設定できます。暗号化された PDF ドキュメントを開いて表示するには、所有者パスワードまたはユーザー パスワードが必要です。

- ユーザー パスワードには null または空の文字列を指定できます。この場合、PDF ドキュメントを開くときにユーザーにパスワードは要求されません。
- 正しい所有者パスワードを使用して PDF ドキュメントを開くと、ドキュメントへのフル アクセス (アクセス制限が指定されていない) が許可されます。
- 正しいユーザー パスワードを使用して PDF 文書を開くと (またはユーザー パスワードを持たない文書を開くと)、指定されたアクセス許可に従って制限付きアクセスが許可されます。

以下のサンプル コードでは、Aspose.Cells を使用して PDF を保護する方法を説明します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされるようになります。

{{% /alert %}}
