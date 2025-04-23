---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/nodejs-cpp/disable-pivot-table-ribbons/
description: 如何使用 Aspose.Cells for Node.js via C++ 禁用数据透视表功能区
keywords: Aspose.Cells for Node.js Excel，Excel Node.js 库，使用 Aspose.Cells for Node.js via C++ 禁用数据透视表功能区
---

{{% alert color="primary" %}}

基于数据透视表的报告虽然有用，但如果目标用户没有详细的Excel知识来配置这些报告，就容易出错。在这种情况下，组织通常会限制用户更改数据透视表报告的能力。像添加额外过滤器、切片器、字段或更改报告中某些内容的顺序这些常见功能，不建议每个用户都使用。另一方面，这些用户仍然应能够刷新报告，使用现有的过滤器或切片器。Aspose.Cells for Node.js via C++ 为开发者提供了限制用户更改这些报告的能力。在创建这些报告时，Excel 提供了禁用数据透视表功能区的功能，而 Aspose.Cells for Node.js via C++ 也提供了同样的功能，即开发者可以禁用包含用于修改这些报告的控件的功能区。

{{% /alert %}}

## **如何使用 Aspose.Cells for Node.js via C++ 禁用数据透视表功能区**

以下代码通过访问工作表中的数据透视表，并将[**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-)设置为**false**来演示此功能。示例数据透视表文件可以从此[链接](pivot_table_test.xlsx)下载。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
