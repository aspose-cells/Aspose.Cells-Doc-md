---
title: ピボットテーブルセルの書式設定
type: docs
weight: 20
url: /ja/java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

時々、ピボットテーブルセルのフォーマットが必要です。たとえば、ピボットテーブルセルに背景色を適用したい場合。Aspose.Cellsは、この目的に使用できる2つのメソッド[**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-)と[**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-)を提供しています。

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-)はピボットテーブル全体にスタイルを適用し、[**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-)はピボットテーブルの単一セルにスタイルを適用します。

{{% /alert %}}

以下のサンプルコードは、ピボットテーブル全体をライトブルーの色でフォーマットし、次に2番目の表行を黄色でフォーマットします。

**コードを実行する前の入力ピボットテーブル**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**コードを実行した後の出力ピボットテーブル**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
{{< app/cells/assistant language="java" >}}
