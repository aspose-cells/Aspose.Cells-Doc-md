---
title: 画像のリサンプリングの追加  ExcelからPDFへの変換
type: docs
weight: 150
url: /ja/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

大量の画像を含む大きなMicrosoft Excelファイルで作業する際に、追加された画像を圧縮して出力PDFファイルサイズを減らし、全体的な変換パフォーマンスを向上させる必要がある場合があります。 Aspose.Cellsは、追加された画像をリサンプリングして出力PDFファイルサイズを減らし、パフォーマンスを改善するためのサポートを提供しています。

{{% /alert %}}

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)オプションを使用すると、出力PDFのサイズを最小限に抑えることができますが、画質にわずかな影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
