---
title: ピボットテーブルセルの書式設定
type: docs
weight: 30
url: /ja/nodejs-cpp/format-pivot-table-cells/
description: Aspose.Cells for Node.js via C++ を使用したピボットテーブルのセルの書式設定方法。
keywords: ピボットテーブルセルの書式設定
---

{{% alert color="primary" %}}

時には、ピボットテーブルのセルの書式設定を行いたい場合があります。例えば、ピボットテーブルのセルに背景色を適用したい場合です。Aspose.Cells for Node.js via C++ は、この目的に [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) と [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) の2つのメソッドを提供します。

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) は、ピボットテーブル全体にスタイルを適用し、[**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) はピボットテーブルの個々のセルにスタイルを適用します。

{{% /alert %}}
次のサンプルコードは、２つのピボットテーブルを含む [サンプルExcelファイル](pivot_format.xlsx) を読み込み、全体のピボットテーブルの書式設定およびピボットテーブル内の個々のセルの書式設定の操作を実行します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/nodejs-cpp/formatting-pivot-table/)
- [行と列のフォーマット](/cells/ja/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
