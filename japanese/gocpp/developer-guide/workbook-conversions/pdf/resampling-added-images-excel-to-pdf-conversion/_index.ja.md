---
title: 追加画像のリサンプリング  Golang経由でC++を使用したExcelからPDFへの変換
linktitle: 画像のリサンプリングの追加  ExcelからPDFへの変換
type: docs
weight: 150
url: /ja/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aspose.Cellsを使用してGolang経由でC++でPDFサイズを削減するために追加画像をリサンプルする方法を学ぶ。
---

{{% alert color="primary" %}}

大量の画像を含む大きなMicrosoft Excelファイルで作業する際に、追加された画像を圧縮して出力PDFファイルサイズを減らし、全体的な変換パフォーマンスを向上させる必要がある場合があります。 Aspose.Cellsは、追加された画像をリサンプリングして出力PDFファイルサイズを減らし、パフォーマンスを改善するためのサポートを提供しています。

{{% /alert %}}

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

出力PDFのサイズを最小限に抑えるために[**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/)オプションを使用すると、画像の品質に若干影響を与える可能性があります。

{{% /alert %}} 

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}

