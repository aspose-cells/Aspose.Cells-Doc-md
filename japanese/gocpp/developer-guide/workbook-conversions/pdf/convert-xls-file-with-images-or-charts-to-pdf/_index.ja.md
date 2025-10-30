---
title: 画像やチャートを含むXLSファイルをPDFに変換する
linktitle: 画像やグラフが含まれる XLS ファイルを PDF ドキュメントに変換する
type: docs
weight: 50
url: /ja/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: 画像やチャートを含むXLSファイルをPDFドキュメントに変換するAspose.Cellsの使用例
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像やチャートを含むXLSファイルをPDFドキュメントに変換することをサポートしています。Aspose.Cells for C++は、スプレッドシートのPDFへの変換を独立して行うことができます。Aspose.PDF for C++は変換には必要ありません。このプロセスはメモリ内で行われ、テンポラリーや中間XMLファイルに依存しません。これにより、大きなExcelファイル、例えば画像、チャート、その他の描画オブジェクトを含むものも迅速かつ効率的に変換できます。

{{% /alert %}} 
## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、[Calculate(CalculationData data)]メソッドを呼び出してからPDFにレンダリングするのが最良です。これにより、数式に依存する値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
