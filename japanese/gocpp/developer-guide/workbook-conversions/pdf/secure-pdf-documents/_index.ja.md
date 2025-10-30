---
title: Golang経由でC++を使用してPDFドキュメントをセキュリティ保護
linktitle: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/go-cpp/secure-pdf-documents/
description: Aspose.Cellsを使用してGolang経由でC++で所有者およびユーザーパスワードを設定してPDFドキュメントを保護する方法を学ぶ。
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cellsはセキュリティを扱うための[**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/)を提供します。PDFに保存する際に所有者パスワードとユーザーパスワードを設定できます。暗号化されたPDFドキュメントを開くには、所有者またはユーザーパスワードが必要です。

- ユーザーパスワードはnullまたは空の文字列にすることができます。この場合、ユーザーがPDFドキュメントを開く際にパスワードが要求されません。
- 正しい所有者パスワードを使ってPDFドキュメントを開くと、アクセス制限なしでドキュメントに完全にアクセスできます。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.CellsでPDFをセキュアにする方法を説明しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、これをPDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)を呼び出すのが最良です。これにより、数式に依存した値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
