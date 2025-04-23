---
title: Ohal Report Canvas 组件
type: docs
weight: 30
url: /zh/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[报告PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**在报告画布组件中使用Aspose.Cells**

Robert Chilvers, 2008年3月17日

{{% /alert %}}

## **产品背景**

报告画布组件允许用户基于预加载的数据集创建可视化报告。用户可以向画布添加不同的组件，包括图片、文本框、图表和表格，然后指定数据以及如何进行聚合。用户可以重新排列和调整对象以适应其页面。用户可以指定颜色调色板并保存模板以供将来使用。Aspose.Cells被用于将画布上的所有对象以正确的数据导出到Excel中。该组件是使用Visual Studio 2008中的VB.Net编写的。

## **需求场景**

我们选择Aspose.Cells是因为它几乎完全具备Microsoft Excel导出能力。对我们来说，最重要的是能够导出图表和表格，特别是在Microsoft Excel 2007中 - 这些在其他第三方组件中缺失。

## **解决方案实施**

报告画布上的每个对象都有一个函数，该函数接收Aspose.Cells工作表的实例，并将自己添加到工作表中。当用户请求导出时，工作簿和工作表被初始化，并且报告画布上的每个对象都调用了此函数。

## **优势**

Aspose.Cells使我们能够完全独立于Excel构建Excel工作簿，然后以用户选定的格式保存工作簿。这节省了大量使用Excel互操作和实现保存到不同版本Excel的不同例程的调试时间。

## **未来实施**

我们很可能会使用Aspose.Cells来加载和保存所有的Excel文件。这将包括加载数据模板和导出结果。

## **结论**

{{% alert color="primary" %}}

到目前为止，我们在使用Aspose.Cells组件时没有遇到任何问题，该组件应该能为我们节省短期和长期的开发时间。支持和销售查询都得到了迅速和有益的回复。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
