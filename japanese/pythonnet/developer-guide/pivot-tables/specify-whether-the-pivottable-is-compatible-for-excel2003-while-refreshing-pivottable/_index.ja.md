---
title: PivotTableがExcel2003に互換性があるかどうかを指定する
type: docs
weight: 80
url: /ja/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: この記事は、Aspose.Cells for Python via .NETを使用してPivotTableを更新する際にExcel2003用にPivotTableが互換性があるかどうかを指定する方法を示しています。
keywords: PythonのAspose.Cells for Excel、Excel Pythonライブラリを使用して、PivotTableを更新する際にExcel2003用にPivotTableが互換性があるかどうかを指定する方法。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、PivotTableを更新する際にExcel2003用にPivotTableが互換性があるかどうかを指定するための [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) プロパティを提供し、これを使用します。trueの場合、文字列は255文字以下でなければならず、文字列が255文字を超える場合は切り捨てられます。**false**の場合、文字列に前述の制限はありません。デフォルト値は**true**です。

{{% /alert %}}

## **ピボットテーブルを更新する際にExcel2003との互換性があるかどうかを指定する方法**

次のサンプルコードは、[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)プロパティの使用方法を説明しています。元の文字列は383文字ですが、[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)プロパティをtrueに設定してピボットテーブルを更新すると、ピボットテーブルのセルB5のデータが切り捨てられて255文字になります。ただし、[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)プロパティをfalseに設定してピボットテーブルを再度更新すると、ピボットテーブルのセルB5のデータが切り捨てられず、383文字のままです。このプロパティの理解のためにコード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
