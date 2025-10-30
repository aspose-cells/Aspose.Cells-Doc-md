---
title: ピボットテーブルセルの書式設定
type: docs
weight: 30
url: /ja/python-net/format-pivot-table-cells/
description: Aspose.Cells for Python via .NET を使用してピボットテーブルセルを書式設定する方法
keywords: ピボットテーブルセルの書式設定
---

{{% alert color="primary" %}}

時々、ピボットテーブルセルを書式設定したい場合があります。たとえば、ピボットテーブルセルに背景色を適用したい場合があります。 Aspose.Cells for Python via .NET では、この目的のために使用できる [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) および [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/) の2つのメソッドを提供しています。

[**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) は、ピボットテーブル全体にスタイルを適用し、[**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/) はピボットテーブルの個々のセルにスタイルを適用します。

{{% /alert %}}
次のサンプルコードは、２つのピボットテーブルを含む [サンプルExcelファイル](pivot_format.xlsx) を読み込み、全体のピボットテーブルの書式設定およびピボットテーブル内の個々のセルの書式設定の操作を実行します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormatPivotTableCells-1.py" >}}

## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/python-net/formatting-pivot-table/)
- [行と列のフォーマット](/cells/ja/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="python-net" >}}
