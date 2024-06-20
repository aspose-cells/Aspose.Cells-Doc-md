---
title: 生成されるページ数を制限  Excel を PDF に変換
type: docs
weight: 180
url: /ja/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する際に、生成されるページの数を制限する方法を学びます。
keywords: Pythonを使用してExcelをPDFに変換する際に生成されるページの数を制限し、生成されるページの数を制限してExcelをPDFに保存する方法を学びます。Pythonを使用してExcelをPDFに変換する際に生成されるページの数を制限し、PythonでExcelをPDFに変換する際に生成されるページの数を制限します。
---

{{% alert color="primary" %}}

時々、出力PDFファイルにページの範囲を印刷したい場合があります。Aspose.Cells for Python via .NETは、ExcelスプレッドシートをPDFファイル形式に変換する際に、生成されるページの数を制限する機能をサポートしています。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

スプレッドシートに式が含まれている場合、PDFにレンダリングする前に[Workbook.calculate_formula]（https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#）メソッドを呼び出すことが最善です。これにより、式に依存する値が再計算され、正しい値が出力ファイルにレンダリングされます。

{{% /alert %}}
