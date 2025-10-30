---
title: Golangを使用してC++経由でMicrosoft Excelの式ウォッチウィンドウにセルを追加する
linktitle: 数式の監視ウィンドウにセルを追加
description: Excelの数式監視ウィンドウにセルを追加するためにAspose.Cells for C++を使う方法を学びます。Excelファイルをロードまたは作成し、セルを操作し、数式を設定し、変更したファイルを保存します。
keywords: Aspose.Cells、Excel、数式監視ウィンドウ、セルの追加、C++
type: docs
weight: 60
url: /ja/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft Excelの監視ウィンドウは、セルの値や数式をウィンドウで便利に監視できるツールです。Microsoft Excelで*数式 > 監視ウィンドウ*をクリックして*監視ウィンドウ*を開くことができます。このウィンドウには*監視の追加*ボタンがあり、監視するセルを追加できます。同様に、Aspose.Cells APIの[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/)メソッドを使用してセルを*監視ウィンドウ*に追加できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

次のサンプルコードは、セルC1とE1の数式を設定し、それらを監視ウィンドウに追加します。その後、ワークブックを[出力Excelファイル](67338481.xlsx)として保存します。出力Excelファイルを開き、*監視ウィンドウ*を見ると、両方のセルがこのスクリーンショットのように表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
