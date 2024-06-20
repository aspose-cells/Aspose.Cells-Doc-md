---
title: 画像やグラフが含まれる XLS ファイルを PDF ドキュメントに変換する
type: docs
weight: 50
url: /ja/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Aspose.Cells for Python via .NET APIを使用して、Pythonで画像やグラフを含むXLSファイルをPDFに変換する方法について学びます。
keywords: Pythonで画像やグラフを含むXLSファイルをPDFに変換、Pythonを使用したxlsからpdfへの変換、Python XLSファイルの画像をPDFに、グラフを含むxlsファイルのpython pdfへの変換
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETは、画像やグラフを含むXLSファイルをPDFドキュメントに変換することをサポートしています。Aspose.Cells for Python via .NET APIは、スプレッドシートをPDFに変換するためにAspose.PDF for .NETを必要としません。プロセスは中間XMLファイルに依存せず、メモリ上で行うことができます。これにより、大きなExcelファイル（たとえば、画像やグラフ、その他の描画オブジェクトを含むもの）も迅速かつ効率的に変換できます。

{{% /alert %}} 
## **サンプルコード**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) メソッドを呼び出すことが最適です。これにより、数式に依存する値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
