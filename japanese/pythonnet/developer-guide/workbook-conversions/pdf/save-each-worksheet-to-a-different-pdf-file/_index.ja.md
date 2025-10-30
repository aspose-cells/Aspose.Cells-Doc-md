---
title: 異なるPDFファイルにそれぞれのワークシートを保存する
type: docs
weight: 130
url: /ja/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Aspose.Cells for Python via .NET APIを使用して、各ワークシートを異なるPDFファイルに保存する方法
keywords: Pythonで各ワークシートを異なるPDFファイルに保存する方法
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETは、（画像、グラフなどを含む）XLSファイルをPDFドキュメントに変換することができます。Aspose.Cells for Python via .NETは、スプレッドシートをPDFに変換するためにAspose.PDF for .NETを使用する必要はありません。変換には一時ファイルを作成するためのソフトウェアを作成または使用する必要はありません。全体のプロセスはメモリ上で行うことができます。

{{% /alert %}} 
## **異なるPDFファイルごとに各ワークシートを保存**
テンプレートExcelファイルの各ワークシートを保存して異なるPDFファイルを生成する必要がある場合は、これを簡単に実現できます。 1回に1シートインデックスを[**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)オプションに設定して、PDFにレンダリングします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
