---
title: Excel から PDF への変換のための画像のリサンプル
type: docs
weight: 250
url: /ja/java/resample-images-for-excel-to-pdf-conversion/
description: この記事では、Excel ファイルを PDF に変換する際の画像サイズの縮小について説明します
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

大量の画像を含む大きな Microsoft Excel ファイルを操作している場合、追加された画像を圧縮して、出力 PDF ファイルのサイズを縮小し、全体的な変換パフォーマンスを向上させる必要がある場合があります。 Aspose.Cells は、追加された画像の再サンプリングをサポートして、出力 PDF ファイルのサイズを縮小し、パフォーマンスを向上させます。

{{% /alert %}}

## **Excel から PDF への変換のための画像のリサンプル**

Aspose.Cells API を使用してタスクを実行する方法を説明する次のサンプル コードを参照してください。この例では、ファイル内の画像を圧縮しながら、Microsoft Excel ファイルを PDF ファイルに変換します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

を使用して[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) オプションは、出力 PDF のサイズを最小化しますが、画質に少し影響する場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
