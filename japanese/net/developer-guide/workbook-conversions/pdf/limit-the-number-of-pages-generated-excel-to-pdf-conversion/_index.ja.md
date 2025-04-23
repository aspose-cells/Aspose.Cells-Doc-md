---
title: 生成されるページ数を制限  Excel を PDF に変換
type: docs
weight: 180
url: /ja/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

時には、特定のページ範囲を出力PDFファイルに印刷したいことがあります。Aspose.Cellsには、ExcelスプレッドシートをPDFファイル形式に変換する際に生成されるページ数を制限する機能があります。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値が出力ファイルに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
