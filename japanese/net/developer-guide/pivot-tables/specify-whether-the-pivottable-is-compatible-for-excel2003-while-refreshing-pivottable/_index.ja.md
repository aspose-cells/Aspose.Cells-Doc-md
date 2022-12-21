---
title: ピボットテーブルの更新中に、ピボットテーブルが Excel2003 と互換性があるかどうかを指定します
type: docs
weight: 80
url: /ja/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

Aspose.Cells は[**PivotTable.IsExcel2003互換**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)ピボットテーブルを更新するときに、ピボットテーブルが Excel2003 と互換性があるかどうかを指定するために使用できるプロパティ。 true の場合、文字列は 255 文字以下である必要があるため、文字列が 255 文字を超える場合は切り捨てられます。もしも**間違い**、文字列には前述の制限はありません。デフォルト値は**真実**.

{{% /alert %}}

## **ピボットテーブルの更新中に、ピボットテーブルが Excel2003 と互換性があるかどうかを指定します**

次のサンプル コードは、[**PivotTable.IsExcel2003互換**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)財産。元の文字列の長さは 383 文字です。でもいつ[**PivotTable.IsExcel2003互換**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティが設定されています**真実**ピボット テーブルを更新すると、ピボット テーブルのセル B5 のデータが切り捨てられ、255 文字になります。ただし、[**PivotTable.IsExcel2003互換**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティが設定されています**間違い**ピボット テーブルを再度更新すると、ピボット テーブルのセル B5 のデータは切り捨てられず、383 文字のままです。このプロパティをよりよく理解するために、コード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
