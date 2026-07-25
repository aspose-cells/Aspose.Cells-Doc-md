---
title: GolangとC++を使用したピボットテーブルオプションの設定  空のセルを表示するために
linktitle: ピボットテーブルオプションの設定  空白セルに表示する内容を設定する
type: docs
weight: 40
url: /ja/go-cpp/setting-pivot-table-option-for-empty-cells-show/
description: GolangとC++を使用したピボットテーブルの"空のセルを表示"オプションの設定方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してさまざまなピボットテーブルオプションを設定できます。そのようなオプションの1つは"空白のセルに表示する内容"です。このオプションを設定することで、ピボットテーブル内のすべての空白セルが指定された文字列として表示されます。

{{% /alert %}}

## **Microsoft Excelでのピボットテーブルオプションの設定**

Microsoft Excelでこのオプションを見つけて設定するには:

1. ピボットテーブルを選択し、右クリックします。
1. **ピボットテーブルオプション**を選択します。
1. **レイアウトと書式**タブを選択します。
1. **空白のセルに表示する内容**オプションを選択し、文字列を指定します。

## **Aspose.Cellsを使用したピボットテーブルオプションの設定**

Aspose.Cellsは、「空白セルに表示する内容」ピボットテーブルオプションを設定するための[**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/go-cpp/pivottable/getdisplaynullstring/)および[**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/)プロパティを提供します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingPivotTableOptionForEmptyCellsShow.go" >}}
## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/cpp/formatting-pivot-table/)
