---
title: フォーマット ピボット テーブル Cells
type: docs
weight: 20
url: /ja/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

ピボット テーブルのセルの書式を設定したい場合があります。たとえば、ピボット テーブルのセルに背景色を適用するとします。 Aspose.Cells は 2 つの方法を提供します[**ピボットテーブル.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ） と[**ピボットテーブル.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)）、この目的に使用できます。

[**ピボットテーブル.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) スタイルをピボット テーブル全体に適用し、[**ピボットテーブル.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) は、スタイルをピボット テーブルの 1 つのセルに適用します。

{{% /alert %}}

次のサンプル コードでは、ピボット テーブル全体を水色でフォーマットしてから、テーブルの 2 行目を黄色でフォーマットします。

**コードを実行する前の入力ピボット テーブル**

![todo:画像_代替_文章](format-pivot-table-cells_1.png)

**コード実行後の出力ピボット テーブル**

![todo:画像_代替_文章](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
