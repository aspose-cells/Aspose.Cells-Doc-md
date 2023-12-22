---
title: 安全な PDF ドキュメント
type: docs
weight: 120
url: /ja/python-net/secure-pdf-documents/
description: スプレッドシートを Aspose.Cells for Python via .NET API で PDF に保存するときに、PDF セキュリティ オプションを渡す方法について説明します。
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

場合によっては、開発者は暗号化された PDF ファイルを操作する必要があります。例えば：

- 所有者パスワードとユーザーパスワードを使用してドキュメントを保護し、誰でも開くことができないようにします。
- ドキュメントを開いた後、ドキュメントに対する制限またはアクセス許可を設定します。たとえば、ドキュメントのコンテンツを印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートを PDF に保存するときに PDF セキュリティ オプションを渡す方法について説明します。

{{% /alert %}}

 Aspose.Cells for Python via .NET が提供します[**PDFセキュリティオプション**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)セキュリティ関連の作業に使用します。 PDF に保存するときに、所有者パスワードとユーザー パスワードを設定できます。暗号化された PDF ドキュメントを開いて表示するには、所有者パスワードまたはユーザー パスワードが必要です。

- ユーザー パスワードには null または空の文字列を指定できます。この場合、PDF ドキュメントを開くときにユーザーにパスワードは要求されません。
- 正しい所有者パスワードを使用して PDF ドキュメントを開くと、ドキュメントへのフル アクセス (アクセス制限が指定されていない) が許可されます。
- 正しいユーザー パスワードを使用して PDF 文書を開くと (またはユーザー パスワードを持たない文書を開くと)、指定されたアクセス許可に従って制限付きアクセスが許可されます。

以下のサンプル コードでは、Aspose.Cells for Python via .NET を使用して PDF を保護する方法を説明します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされるようになります。

{{% /alert %}}
