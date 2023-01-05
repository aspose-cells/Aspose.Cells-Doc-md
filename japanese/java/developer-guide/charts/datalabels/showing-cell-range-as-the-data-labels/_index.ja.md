---
title: Cell 範囲をデータ ラベルとして表示
type: docs
weight: 110
url: /ja/java/showing-cell-range-as-the-data-labels/
---
## MS Excel でセル範囲をデータ ラベルとして表示する

Microsoft Excel 2013 では、データ ラベルの Cell 範囲を表示できます。このオプションを選択するには、次の手順に従います

- シリーズのデータ ラベルを選択し、右クリックしてポップアップ メニューを開きます。
- クリック**データ ラベルの書式設定...**そしてそれは表示されます**ラベル オプション**.
- チェックボックスをオンまたはオフにする**ラベルの内容 - Cells からの値**.

### **Cell 範囲をデータ ラベルとして表示するためのチェックボックス**

次のスクリーンショットは、参考のためにこのオプションを強調しています。

![todo:画像_代替_文章](showing-cell-range-as-the-data-labels_1.png)

## セル範囲を Aspose.Cells のデータ ラベルとして表示する

Aspose.Cells は[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)チェックボックスをオンまたはオフにするメソッド**ラベルの内容 - Cells からの値**上のスクリーンショットに示すように。

## Java セル範囲をデータ ラベルとして表示するコード

以下のサンプル コードは、チャート シリーズのデータ ラベルにアクセスし、設定します。[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)チェックするメソッドを true にする**ラベルの内容 - Cells からの値**オプション。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
