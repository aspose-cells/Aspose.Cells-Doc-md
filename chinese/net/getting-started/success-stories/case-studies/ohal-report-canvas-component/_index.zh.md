---
title: Ohal 报告Canvas组件
type: docs
weight: 30
url: /zh/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[报告PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Report Canvas组件中使用Aspose.Cells**

Robert Chilvers，2008年3月17日

{{% /alert %}}

## **产品背景**

Report Canvas组件允许用户基于预加载的数据集创建可视化报告。用户可以向画布添加不同的组件，包括图片、文本框、图表和表格，然后指定数据及其聚合方式。用户可以重新排列和调整对象大小以适应其页面。用户可以指定调色板并保存模板以供将来使用。Aspose.Cells用于将画布上的所有对象正确导出到Excel中。该组件使用VB.Net在Visual Studio 2008中编写。

## **需求情景**

我们选择Aspose.Cells，是因为它几乎具备完整的Microsoft Excel导出功能。对我们而言，最重要的是能够导出图表和表格，尤其是在Microsoft Excel 2007中 - 这是其他第三方组件所缺少的。

## **解决方案实施**

报表画布上的每个对象都有一个函数，该函数接收Aspose.Cells工作表实例，并将自身添加到工作表中。当用户请求导出时，工作簿和工作表将被初始化，并调用报表画布上的每个对象的此函数。

## **优势**

Aspose.Cells使我们能够完全独立于Excel构建Excel工作簿，然后将工作簿保存为用户选择的格式。这在使用Excel互操作和实现保存到不同版本Excel的不同程序时，节省了大量调试时间。

## **未来实施**

我们很可能会在所有加载和保存Excel文件时使用Aspose.Cells。这将包括加载数据模板和导出结果。

## **结论**

{{% alert color="primary" %}}

到目前为止，我们在使用Aspose.Cells组件时没有遇到任何问题，该组件应该为我们节省短期和长期的开发时间。支持和销售查询被迅速和有用地回答。

{{% /alert %}}
