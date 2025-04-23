---
title: セキュアなPDFドキュメント
type: docs
weight: 260
url: /ja/java/secure-pdf-documents/
description: Excelファイルからの変換時にセキュアなPDFファイルを作成します。この記事では、Aspose.Cells for Java APIを使用してExcelからセキュアなPDFファイルを生成する方法を示します。
keywords: セキュアPDFドキュメントjava、セキュアPDFドキュメント、ExcelからセキュアPDF、ExcelからセキュアPDF java、Excelからパスワード保護されたPDFに変換、Excelからパスワード保護されたPDFに変換java、Excelからパスワード保護されたPDFに変換、Excelからパスワード保護されたPDFに変換java、Excelからパスワード保護されたPDFに変換java、Excelからパスワード保護されたPDF
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cells はセキュリティを扱うための [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) を提供します。 PDFに保存する際に所有者パスワードとユーザーパスワードを設定することができます。 オーナーパスワードまたはユーザーパスワードは、ビューで暗号化されたPDFドキュメントを開くために必要です。

- ユーザーパスワードはnullまたは空の文字列にすることができます。この場合、ユーザーがPDFドキュメントを開く際にパスワードが要求されません。
- 正しい所有者パスワードでPDFドキュメントを開くと、ドキュメントへのフルアクセス（指定されたアクセス制限なし）が可能です。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.Cells for Java APIを使用してセキュアなPDFファイルを作成する方法を説明しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
