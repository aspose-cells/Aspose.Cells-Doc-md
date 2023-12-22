---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/python-net/disable-pivot-table-ribbons/
description: 如何使用 Aspose.Cells for Python via .NET 禁用数据透视表功能区。
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

基于数据透视表的报告很有用，但如果目标用户不具备详细的 Excel 知识来配置这些报告，则容易出错。在这些情况下，组织将希望限制用户更改基于数据透视表的报告。大多数情况下，不建议每个用户使用常见的数据透视表功能，例如添加额外的过滤器、切片器、字段或更改报表中某些内容的顺序。另一方面，这些用户还应该能够刷新报告并使用现有的过滤器或切片器。 Aspose.Cells for Python via .NET 为开发人员提供了此功能，用于限制用户在创建这些报告时更改这些报告。为此，Excel 提供了禁用数据透视表功能区的功能，Aspose.Cells for Python via .NET 提供了相同的功能，即开发人员可以禁用包含修改这些报表的控件的功能区。

{{% /alert %}}

##  **使用 PivotTable.EnableWizard 禁用数据透视表功能区**

以下代码通过从工作表访问数据透视表然后设置来演示此功能[**启用向导**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/)为*假**。可以从此下载示例数据透视表文件[关联](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
