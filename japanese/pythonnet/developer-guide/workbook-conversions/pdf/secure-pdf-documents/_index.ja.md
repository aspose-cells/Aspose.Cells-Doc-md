---
title: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/python-net/secure-pdf-documents/
description: Aspose.Cells for Python via .NET APIを使用して、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について学んでください。
keywords: PythonでPDFにセキュリティオプションを書き込み、PDFドキュメントを暗号化する 
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cells for Python via .NETは[**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)を提供します。セキュリティでの作業に役立ちます。PDFに保存する際にオーナーパスワードとユーザーパスワードを設定できます。暗号化されたPDF文書を表示するためには、オーナーパスワードまたはユーザーパスワードが必要になります。

- ユーザーパスワードはnullまたは空の文字列にすることができます。この場合、ユーザーがPDFドキュメントを開く際にパスワードが要求されません。
- 正しい所有者パスワードでPDFドキュメントを開くと、ドキュメントへのフルアクセス（指定されたアクセス制限なし）が可能です。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードでは、Aspose.Cells for Python via .NETを使用してPDFをセキュリティで保護する方法が説明されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
