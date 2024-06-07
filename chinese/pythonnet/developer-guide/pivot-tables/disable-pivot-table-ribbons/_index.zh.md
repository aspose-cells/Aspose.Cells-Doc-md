---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/python-net/disable-pivot-table-ribbons/
description: 如何通过Aspose.Cells for Python通过.NET禁用数据透视表选项卡
keywords: 使用Aspose.Cells for Python Excel库禁用数据透视表选项卡
---

{{% alert color="primary" %}}

基于数据透视表的报告非常有用，但如果目标用户不具备详细的Excel知识来配置这些报告，则容易出现错误。在这些情况下，组织将希望限制用户无法更改基于数据透视表的报告。通常不建议每个用户更改报告的常见数据透视表功能，比如添加额外的筛选器、切片器、字段或更改报告中某些内容的顺序。另一方面，这些用户也应该能够刷新报告并使用现有的筛选器或切片器。Aspose.Cells for Python通过.NET已经为开发人员提供了限制用户在创建这些报告时更改这些报告的能力。为此，Excel提供了一个禁用数据透视表选项卡的功能，Aspose.Cells for Python通过.NET也提供了相同的功能，即开发人员可以禁用包含控件以修改这些报告的工具栏。

{{% /alert %}}

## **使用Aspose.Cells for Python Excel库禁用数据透视表选项卡**

以下代码通过访问表中的数据透视表并将[**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/)设置为**false**来演示此功能。可以从此[链接](pivot_table_test.xlsx)下载示例数据透视表文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
