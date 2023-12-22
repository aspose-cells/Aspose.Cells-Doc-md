---
title: ピボットテーブルを更新するときにピボットテーブルが Excel2003 と互換性があるかどうかを指定します
type: docs
weight: 80
url: /ja/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: この記事では、Aspose.Cells for Python via .NET を使用してピボットテーブルを更新するときに、ピボットテーブルが Excel2003 と互換性があるかどうかを指定する方法を示します。
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、[**PivotTable.is_excel_2003_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)このプロパティを使用して、ピボットテーブルを更新するときにピボットテーブルが Excel2003 と互換性があるかどうかを指定できます。 true の場合、文字列は 255 文字以下である必要があるため、文字列が 255 文字を超える場合は切り捨てられます。 *false** の場合、文字列には前述の制限はありません。デフォルト値は *true** です。

{{% /alert %}}

##  **ピボットテーブルを更新するときにピボットテーブルが Excel2003 と互換性があるかどうかを指定します**

次のサンプルコードは、[**PivotTable.is_excel_2003_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)財産。元の文字列の長さは 383 文字です。でもいつ[**PivotTable.is_excel_2003_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)プロパティが設定されています**真実**ピボット テーブルが更新されると、ピボット テーブルのセル B5 のデータが切り捨てられ、長さは 255 文字になります。ただし、そのとき[**PivotTable.is_excel_2003_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)プロパティが設定されています**間違い**ピボット テーブルが再度更新されると、ピボット テーブルのセル B5 のデータは切り捨てられず、383 文字の長さのままになります。このプロパティをより深く理解するには、コード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
