---
title: 生成されるページ数を制限する - Excel から PDF への変換
type: docs
weight: 180
url: /ja/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Excel のレンダリング中に生成されるページ数を Aspose.Cells for Python via .NET API で PDF に制限する方法について説明します。
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

場合によっては、ある範囲のページを出力 PDF ファイルに印刷したいことがあります。 Aspose.Cells for Python via .NET には、Excel スプレッドシートを PDF ファイル形式に変換するときに生成されるページ数に制限を設定する機能があります。

{{% /alert %}}

##  **生成されるページ数の制限**

次の例は、Microsoft Excel ファイル内のページ範囲 (3 と 4) を PDF にレンダリングする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)これにより、式に依存する値が再計算され、正しい値が出力ファイルにレンダリングされます。

{{% /alert %}}
