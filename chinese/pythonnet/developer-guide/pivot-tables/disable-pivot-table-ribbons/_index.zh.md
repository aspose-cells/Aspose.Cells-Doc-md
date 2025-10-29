---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/python-net/disable-pivot-table-ribbons/
description: 如何使用Aspose.Cells for Python via .NET禁用数据透视表功能区
keywords: 使用Aspose.Cells for Python Excel库禁用数据透视表功能区
---

{{% alert color="primary" %}}

基于数据透视表的报告很有用，但是如果目标用户不了解如何配置这些报告，则容易出错。在这种情况下，组织将希望限制用户无法更改基于数据透视表的报告。通常不建议每个用户使用常见的数据透视表功能，如添加附加筛选器，切片器，字段或更改报告中某些内容的顺序。另一方面，这些用户还应能够刷新报告并使用现有的筛选器或切片器。Aspose.Cells for Python via .NET为开发人员提供了限制用户在创建这些报告时更改这些报告的能力。为此，Excel提供了一个功能来禁用数据透视表功能区，Aspose.Cells for Python via .NET也提供了相同的功能，即开发人员可以禁用包含用于修改这些报告的控件的功能区。

{{% /alert %}}

## **如何使用Aspose.Cells for Python Excel库禁用数据透视表功能区**

以下代码通过访问工作表中的数据透视表，并将[**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/)设置为**false**来演示此功能。示例数据透视表文件可以从此[链接](pivot_table_test.xlsx)下载。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
{{< app/cells/assistant language="python-net" >}}
