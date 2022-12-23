---
title: 追加画像のリサンプリング - Excel から PDF への変換
type: docs
weight: 150
url: /ja/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

大量の画像を含む大きな Microsoft Excel ファイルを操作している場合、出力される PDF ファイル サイズを縮小し、全体的な変換パフォーマンスを向上させるために、追加された画像を圧縮する必要がある場合があります。 Aspose.Cells は、追加された画像のリサンプリングをサポートして、出力 PDF ファイルのサイズを縮小し、パフォーマンスをいくらか改善します。

{{% /alert %}}

Aspose.Cells API を使用してタスクを実行する方法を説明する次のサンプル コードを参照してください。この例では、ファイル内の画像を圧縮しながら、Microsoft Excel ファイルを PDF ファイルに変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

を使用して[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)オプションは、出力 PDF のサイズを最小化しますが、画質に少し影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、正しい値が PDF に表示されるようになります。

{{% /alert %}}
