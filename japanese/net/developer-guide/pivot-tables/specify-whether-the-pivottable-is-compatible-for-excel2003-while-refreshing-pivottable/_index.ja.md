---
title: PivotTableがExcel2003に互換性があるかどうかを指定する
type: docs
weight: 80
url: /ja/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cellsは、PivotTableを更新する際にExcel2003に互換性があるかどうかを指定するための[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティを提供します。trueの場合、文字列は255文字以下である必要があります。したがって、文字列が255文字よりも大きい場合、切り捨てられます。falseの場合、文字列には前述の制限がありません。デフォルト値はtrueです。

{{% /alert %}}

## **PivotTableを更新する際にExcel2003に互換性があるかどうかを指定する**

次のサンプルコードは、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティの使用方法を説明しています。元の文字列は383文字ですが、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティをtrueに設定してピボットテーブルを更新すると、ピボットテーブルのセルB5のデータが切り捨てられて255文字になります。ただし、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)プロパティをfalseに設定してピボットテーブルを再度更新すると、ピボットテーブルのセルB5のデータが切り捨てられず、383文字のままです。このプロパティの理解のためにコード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
