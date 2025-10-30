---
title: 追加されたイメージを再サンプリング  ExcelからPDFへの変換
type: docs
weight: 150
url: /ja/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する際の追加イメージの再サンプリング方法
keywords: PythonでExcelをPDFに変換する際の追加イメージの再サンプリング
---

{{% alert color="primary" %}}

多くのイメージが追加された大きなMicrosoft Excelファイルで作業する際は、追加されたイメージを圧縮して出力PDFファイルのサイズを減らし、全体的な変換パフォーマンスを向上させる必要があるかもしれません。Aspose.Cells for Python via .NETは追加されたイメージを再サンプリングして、出力PDFファイルのサイズを減らし、パフォーマンスを幾分向上させることができます。

{{% /alert %}}

Aspose.Cells for Python via .NET APIを使用してタスクを実行する方法を説明する以下のサンプルコードを参照してください。この例では、ファイル内の画像を圧縮しながら、Microsoft ExcelファイルをPDFファイルに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)オプションを使用すると、出力PDFのサイズを最小限に抑えることができますが、画質にわずかな影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
