---
title: 追加された画像の再サンプル - Excel から PDF への変換
type: docs
weight: 150
url: /ja/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET API を使用して Excel を PDF に変換するときに追加された画像を再サンプリングする方法を学びます。
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

多数の画像を含む大きな Microsoft Excel ファイルを操作する場合、出力 PDF ファイルのサイズを減らし、全体的な変換パフォーマンスを向上させるために、追加された画像を圧縮する必要がある場合があります。 Aspose.Cells for Python via .NET は、追加されたイメージのリサンプリングをサポートし、出力 PDF ファイル サイズを削減し、パフォーマンスを若干向上させます。

{{% /alert %}}

Aspose.Cells for Python via .NET API を使用してタスクを実行する方法を説明する次のサンプル コードを参照してください。この例では、ファイル内の画像を圧縮しながら、Microsoft Excel ファイルを PDF ファイルに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

を使用して、[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)オプションは出力 PDF のサイズを最小化しますが、画質に少し影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}
