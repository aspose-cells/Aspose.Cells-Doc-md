---
title: GolangとC++を使用してピボットテーブルの更新時にExcel2003互換かどうかを指定する
linktitle: ピボットテーブルでExcel2003との互換性を指定
type: docs
weight: 80
url: /ja/go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Aspose.Cells for C++を使用してピボットテーブルを更新する際にExcel2003用の互換性を指定する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、PivotTableを更新する際にExcel2003に互換性があるかどうかを指定するための[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/)プロパティを提供します。trueの場合、文字列は255文字以下である必要があります。したがって、文字列が255文字よりも大きい場合、切り捨てられます。falseの場合、文字列には前述の制限がありません。デフォルト値はtrueです。

{{% /alert %}}

## **PivotTableを更新する際にExcel2003に互換性があるかどうかを指定する**

次のサンプルコードは、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/)プロパティの使用方法を説明しています。元の文字列は383文字ですが、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/)プロパティをtrueに設定してピボットテーブルを更新すると、ピボットテーブルのセルB5のデータが切り捨てられて255文字になります。ただし、[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/)プロパティをfalseに設定してピボットテーブルを再度更新すると、ピボットテーブルのセルB5のデータが切り捨てられず、383文字のままです。このプロパティの理解のためにコード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}
