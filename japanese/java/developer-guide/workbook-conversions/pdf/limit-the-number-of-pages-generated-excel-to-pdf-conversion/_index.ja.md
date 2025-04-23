---
title: 生成されるページ数を制限  Excel を PDF に変換
type: docs
weight: 60
url: /ja/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

時々、範囲内のページを出力PDFファイルに印刷したいことがあります。Aspose.Cellsには、ExcelスプレッドシートをPDFに変換する際に生成されるページ数を制限する機能があります。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれる場合、「[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)」をPDF形式にレンダリングする直前に呼び出すことが最善です。これにより、数式に依存する値が再計算され、正しい値が出力ファイルにレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
