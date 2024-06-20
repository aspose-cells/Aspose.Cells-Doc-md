---
title: データラベルとしてのセル範囲を表示
type: docs
weight: 110
url: /ja/java/showing-cell-range-as-the-data-labels/
---

## Microsoft Excelでデータラベルとしてセル範囲を表示する

Microsoft Excel 2013では、データラベルのセル範囲を表示することができます。次の手順に従ってこのオプションを選択できます

- シリーズのデータラベルを選択し、右クリックしてポップアップメニューを開きます。
- **データラベルの書式設定...** をクリックすると、**ラベルのオプション** が表示されます。
- チェックボックス **ラベルが含む - セルの値** をオンまたはオフにします。

### **データラベルとしてセル範囲を表示するためのチェックボックス**

次のスクリーンショットは、このオプションを強調しています。

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## Aspose.Cellsを使用した、データラベルとしてセル範囲を表示する

Aspose.Cellsは、上記のスクリーンショットに示すように、**ラベルが含む - セルの値** チェックボックスをオンまたはオフにするための [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) メソッドを提供します。

## チャートにセル範囲としてデータラベルを表示するJavaコード

以下のサンプルコードは、チャートのシリーズのデータラベルにアクセスし、**ラベルが含む - セルの値** オプションをオンにするための [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) メソッドを設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
