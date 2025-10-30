---
title: Golang経由でチャートシリーズの値フォーマットコードを設定
linktitle: 数値形式
type: docs
weight: 100
url: /ja/go-cpp/set-the-values-format-code-of-chart-series/
description: Aspose.Cells for C++でチャートシリーズの値フォーマットコードを設定する方法を学びます。適切なフォーマットコードを使ってデータを正確かつ専門的に表示できるようになります。
keywords: Aspose.Cells for C++、チャートシリーズ、値フォーマットコード、フォーマット、データの提示、正確さ、専門性。
---

## **可能な使用シナリオ**
チャートシリーズの値フォーマットコードは、[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) プロパティを使用して設定できます。このプロパティは、ワークシート内の範囲に基づくシリーズだけでなく、値の配列から作成されたシリーズにも役立ちます。

## **チャートシリーズの値の形式コードを設定する**
次のサンプルコードは、以前にシリーズがなかった空のチャートにシリーズを追加します。値の配列を使用してシリーズを追加します。一度シリーズを追加すると、[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) プロパティを使ってコード `$#,##0` で書式設定し、数字 `10000` を `$10,000` にします。スクリーンショットは、コードの効果を [サンプルExcelファイル](51740712.xlsx) および [出力Excelファイル](51740713.xlsx) に実行後に示しています。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
