---
title: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cells はセキュリティを扱うための [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) を提供します。 PDFに保存する際に所有者パスワードとユーザーパスワードを設定することができます。 オーナーパスワードまたはユーザーパスワードは、ビューで暗号化されたPDFドキュメントを開くために必要です。

- ユーザーパスワードはnullまたは空の文字列にすることができます。この場合、ユーザーがPDFドキュメントを開く際にパスワードが要求されません。
- 正しい所有者パスワードでPDFドキュメントを開くと、ドキュメントへのフルアクセス（指定されたアクセス制限なし）が可能です。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.CellsでPDFをセキュアにする方法を説明しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
