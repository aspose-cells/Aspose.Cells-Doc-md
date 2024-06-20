---
title: Microsoft Excelフォーミュラ監視ウィンドウにセルを追加する
description: Aspose.Cellsライブラリを使用して、Excelの式ウォッチウィンドウにセルを追加する方法。既存のExcelファイルをロードするか新しいファイルを作成して、その中のセルを操作して式を設定できます。最後に、変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、式ウォッチウィンドウ、セル、追加
type: docs
weight: 60
url: /ja/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft Excelの式ウォッチウィンドウは、セルの値と式を便利にウォッチするための便利なツールです。*Formulas > Watch* *Window*をクリックしてMicrosoft Excelで**ウォッチウィンドウ**を開きます。そこには**ウォッチを追加**するボタンがあり、それを使用してセルを検査することができます。同様に、Aspose.Cells APIを使用して*Watch Window*にセルを追加するために、[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index)メソッドを使用できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

次のサンプルコードは、セルC1とE1の数式を設定し、両方をWatchウィンドウに追加します。その後、ブックを[出力Excelファイル](67338481.xlsx) として保存します。出力Excelファイルを開き、*Watch Window*を表示すると、このスクリーンショットに示すように両方のセルが表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
