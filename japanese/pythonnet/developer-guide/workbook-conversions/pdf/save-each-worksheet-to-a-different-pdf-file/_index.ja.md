---
title: 各ワークシートを別の PDF ファイルに保存
type: docs
weight: 130
url: /ja/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Aspose.Cells for Python via .NET API を使用して、各ワークシートを別の PDF ファイルに保存する方法を学びます。
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET は、XLS ファイル (画像、グラフなどが含まれる) から PDF ドキュメントへの変換をサポートしています。 Aspose.Cells for Python via .NET は独立して機能してスプレッドシートを PDF に変換できます。変換に Aspose.PDF for .NET を使用する必要はありません。変換はプロセス全体がメモリ内で実行できるため、ソフトウェアで一時ファイルを作成したり使用したりする必要はありません。

{{% /alert %}} 
##  **各ワークシートを別の PDF ファイルに保存**
各ワークシートをテンプレート Excel ファイルに保存して、異なる PDF ファイルを生成する必要がある場合は、これを簡単に実行できます。 1 つのシートのインデックスを次のように設定してみるとよいでしょう。**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**オプションを一度に PDF にレンダリングします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}
