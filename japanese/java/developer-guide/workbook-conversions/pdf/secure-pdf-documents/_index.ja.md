---
title: 安全な PDF ドキュメント
type: docs
weight: 260
url: /ja/java/secure-pdf-documents/
description: Excel ファイルからの変換中に PDF ファイルを保護します。この記事では、Aspose.Cells for Java API を使用して Excel から安全な PDF ファイルを生成する方法を示します。
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

場合によっては、開発者は暗号化された PDF ファイルを操作する必要があります。たとえば、ユーザーと所有者のパスワードを使用してドキュメントを保護し、誰もがドキュメントを開くことができないようにしたり、ドキュメントの内容を印刷または抽出できるように制限したりする必要があります。

この記事では、スプレッドシートを PDF に保存するときに PDF セキュリティ オプションを渡す方法について説明します。

{{% /alert %}} 

Aspose.Cells API は、[**Pdfセキュリティオプション**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)PDF ファイル形式のセキュリティを扱うためのクラス。以下のサンプル コードは、Aspose.Cells for Java API で保護された PDF ファイルを作成する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) PDF にレンダリングする直前。これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
