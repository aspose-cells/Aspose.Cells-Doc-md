---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

基于数据透视表的报告很有用，但是如果目标用户没有详细的Excel知识来配置这些报告，则容易出错。在这些情况下，组织将希望限制用户无法更改基于数据透视表的报告。一般不建议每个用户进行更改数据透视表报告的常见数据透视表功能，比如添加额外的筛选器，切片器，字段，或更改报告中某些内容的顺序。另一方面，这些用户还应该能够刷新报告并使用现有的筛选器或切片器。Aspose.Cells已为开发人员提供了这种在创建这些报告时限制用户更改这些报告的能力。为此，Excel提供了禁用数据透视表功能区的功能，Aspose.Cells也提供了这个功能，即开发人员可以禁用包含控制这些报告修改的功能区。

{{% /alert %}}

## **使用PivotTable.EnableWizard禁用数据透视表功能区**

以下代码通过访问表中的数据透视表并将[**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard)设置为**false**来演示此功能。可以从此[链接](pivot_table_test.xlsx)下载示例数据透视表文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
