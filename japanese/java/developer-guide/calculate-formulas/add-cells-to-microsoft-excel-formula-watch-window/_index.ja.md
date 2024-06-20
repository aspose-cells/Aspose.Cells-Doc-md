---
title: Microsoft Excelフォーミュラ監視ウィンドウにセルを追加する
type: docs
weight: 20
url: /ja/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft ExcelのWatch Windowはセルの値とその数式を便利に監視するための有用なツールです。Microsoft Excelを開き、*数式 > リスト* > *ウォッチ* *ウィンドウ*をクリックして*Watch Window*を開けることができます。そこでは、*Add Watch*ボタンをクリックしてインスペクション用のセルを追加することができます。同様に、Aspose.Cells APIを使用して*Watch Window*にセルを追加するために[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int))メソッドを使用することができます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

次のサンプルコードは、セルC1とE1の式を設定し、両者を*Watch Window*に追加し、その後ワークブックを[出力エクセルファイル](67338509.xlsx)として保存します。出力エクセルファイルを開き、*Watch Window*を表示すると、このスクリーンショットに表示されているように両方のセルが表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
