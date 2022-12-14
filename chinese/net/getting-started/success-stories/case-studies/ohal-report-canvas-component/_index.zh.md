---
title: Ohal 报表画布组件
type: docs
weight: 30
url: /zh/net/ohal-report-canvas-component/
---
{{% alert color="primary" %}}

[报告PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**在 Report Canvas 组件中使用 Aspose.Cells**

罗伯特·奇尔弗斯，2008 年 3 月 17 日

{{% /alert %}}

## **产品背景**

Report Canvas 组件允许用户基于预加载的数据集创建可视化报告。用户可以在他们的画布上添加不同的组件，包括图片、文本框、图表和表格，然后他们指定数据及其聚合方式。然后用户可以重新排列对象并调整其大小以适合他们的页面。用户可以指定调色板并保存模板以备将来使用。 Aspose.Cells 用于将画布上的所有对象导出到具有正确数据的 Excel。该组件是在 Visual Studio 2008 中使用 VB.Net 编写的。

## **需求场景**

我们选择 Aspose.Cells 是因为它具有几乎完整的 Microsoft Excel 导出功能。对我们来说最重要的是导出图表和表格的能力，尤其是在 Microsoft Excel 2007 中——这些在其他第 3 方组件中是缺乏的。

## **解决方案实施**

报表画布上的每个对象都有一个函数，该函数传递 Aspose.Cells 工作表的实例并将其自身添加到工作表。当用户请求导出时，工作簿和工作表被初始化，报表画布上的每个对象都调用此函数。

## **好处**

Aspose.Cells 允许我们完全独立于 Excel 构建 Excel 工作簿，然后以用户选择的格式保存工作簿。这节省了使用 Excel 互操作和实施不同例程以保存到不同版本的 Excel 时调试交互的时间。

## **未来实施**

我们很可能会使用 Aspose.Cells 来进行所有 Excel 文件的加载和保存。这将包括加载数据模板和导出结果。

## **结论**

{{% alert color="primary" %}}

到目前为止，我们在使用 Aspose.Cells 组件时没有遇到任何问题，该组件应该可以为我们节省短期和长期的开发时间。支持和销售查询已得到迅速而有益的回答。

{{% /alert %}}
