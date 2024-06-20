---
title: ExcelからPDFへの変換のための画像の再サンプリング
type: docs
weight: 250
url: /ja/java/resample-images-for-excel-to-pdf-conversion/
description: この記事では、ExcelファイルをPDFに変換する際に画像サイズを削減する方法を示しています。
keywords: excelからpdf、excelからpdf変換中に画像を再サンプリング、excelからpdf変換中に画像を圧縮、excelからpdf変換中に画像サイズを縮小、画像再サンプリングでexcelからpdf変換、画像圧縮でexcelからpdf変換、excelからpdf変換で画像再サンプリング、excelからpdf変換で画像圧縮、Javaでexcelからpdf変換中に画像を再サンプリングする
---

{{% alert color="primary" %}}

大きなMicrosoft Excelファイルに多くの画像が含まれている場合、出力PDFファイルのサイズを縮小し、全体的な変換性能を向上させるために画像の圧縮が必要になることがあります。Aspose.Cells は、追加された画像を再サンプリングして出力PDFファイルのサイズを縮小し、パフォーマンスを向上させることをサポートしています。

{{% /alert %}}

## **ExcelからPDFへの変換のための画像の再サンプリング**

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

出力PDFのサイズを最小限に抑えるために[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int))オプションを使用すると、画像の品質に若干影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
