---
title: ピボットテーブルセルの書式設定
type: docs
weight: 20
url: /ja/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

時々、ピボットテーブルセルのフォーマットが必要です。たとえば、ピボットテーブルセルに背景色を適用したい場合。Aspose.Cellsは、この目的に使用できる2つのメソッド[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style))と[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style))を提供しています。

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style))はピボットテーブル全体にスタイルを適用し、[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style))はピボットテーブルの単一セルにスタイルを適用します。

{{% /alert %}}

以下のサンプルコードは、ピボットテーブル全体をライトブルーの色でフォーマットし、次に2番目の表行を黄色でフォーマットします。

**コードを実行する前の入力ピボットテーブル**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**コードを実行した後の出力ピボットテーブル**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
