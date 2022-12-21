---
title: Cells を Microsoft に追加 Excel 数式ウォッチ ウィンドウ
type: docs
weight: 20
url: /ja/java/add-cells-to-microsoft-excel-formula-watch-window/
---
## **考えられる使用シナリオ**

Microsoft Excel ウォッチ ウィンドウは、セルの値とその数式をウィンドウで簡単に監視できる便利なツールです。開くことができます*ウォッチウィンドウ*Microsoft Excel を使用して*数式 > ウォッチ* *窓*.それは*ウォッチを追加*検査用のセルを追加するために使用できるボタン。同様に、使用できます[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) セルを追加するメソッド*ウォッチウィンドウ*Aspose.Cells API を使用します。

## **Cells を Microsoft に追加 Excel 数式ウォッチ ウィンドウ**

次のサンプル コードは、セル C1 と E1 の数式を設定し、両方を追加します。*ウォッチウィンドウ*.次に、ワークブックを次のように保存します[出力エクセルファイル](67338509.xlsx).出力された Excel ファイルを開いて表示すると、*ウォッチウィンドウ*、このスクリーンショットに示すように、両方のセルが表示されます。

![todo:画像_代替_文章](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
