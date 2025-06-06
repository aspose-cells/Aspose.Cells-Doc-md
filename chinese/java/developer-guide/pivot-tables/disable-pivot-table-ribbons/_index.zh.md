---
title: 禁用数据透视表功能区
type: docs
weight: 40
url: /zh/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

基于数据透视表的报告很有用，但如果目标用户不具备详细的Excel知识来配置这些报告，则可能会出现错误。在这些情况下，组织将希望限制用户能够更改基于数据透视表的报告。通常不建议每个用户更改报告的常见数据透视表功能，如添加额外的筛选器、切片器、字段，或更改报告中某些内容的顺序。另一方面，这些用户还应该能够刷新报告，并使用现有的筛选器或切片器。Aspose.Cells已为开发人员提供了在创建这些报告时限制用户更改这些报告的能力。为此，Excel提供了一项禁用数据透视表功能区的功能，Aspose.Cells也提供了相同的功能，即开发人员可以禁用包含用于修改这些报告的控件的功能区。

{{% /alert %}}

## **使用PivotTable.setEnableWizard禁用数据透视表功能区**

以下代码通过访问工作表中的数据透视表，然后调用[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard)来将此标志设置为**false**，演示了此功能。示例数据透视表文件可以从此[链接](71630876.xlsx)下载。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
{{< app/cells/assistant language="java" >}}
