---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

基于数据透视表的报告很有用，但如果目标用户不具备详细的 Excel 知识来配置这些报告，则容易出错。在这些情况下，组织将希望限制用户更改基于数据透视表的报告。大多数情况下，不建议每个用户使用常见的数据透视表功能，例如添加额外的过滤器、切片器、字段或更改报告中某些内容的顺序。另一方面，这些用户也应该能够刷新报告并使用现有的过滤器或切片器。 Aspose.Cells 已向开发人员提供此功能，以限制用户在创建这些报告时更改这些报告。为此，Excel 提供了禁用数据透视表功能区的功能，Aspose.Cells 也提供了同样的功能，即开发人员可以禁用包含修改这些报表的控件的功能区。

{{% /alert %}}

## **使用 PivotTable.EnableWizard 禁用数据透视表功能区**

以下代码通过从工作表访问数据透视表然后设置来演示此功能[**启用向导**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard)至**错误的**.可以从这里下载示例数据透视表文件[关联](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
