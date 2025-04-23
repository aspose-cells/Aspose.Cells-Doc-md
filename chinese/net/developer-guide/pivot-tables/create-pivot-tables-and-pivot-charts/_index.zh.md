---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

数据透视表是记录的互动摘要。例如，您可能有数百个工作表中列表中的发票条目。数据透视表可以按客户、产品或日期总计发票。使用Microsoft Excel，可以通过将按钮拖到新位置，快速重新排列数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells 支持[数据透视表](/cells/zh/net/create-pivot-tables-and-pivot-charts/)和[数据透视图](/cells/zh/net/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **添加数据透视表和数据透视图**

Aspose.Cells 提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置 PivotTable 对象，作为数据透视表对象的基本构建快：

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 一个工作表上的数据透视表。
- 数据透视表是工作表上所有数据透视表对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells](https://downloads.aspose.com/cells/net)。
   1. 在您的开发计算机上安装它。
      所有[Aspose](http://www.aspose.com/)组件在安装后均处于评估模式。 评估模式没有时间限制，只会在生成的文档中添加水印。若要充分发挥组件的功能，您需要有有效的许可证。
1. 创建一个项目：
   1. 启动 Visual Studio.Net。
   1. 创建新的控制台应用程序。
1. 添加引用：
   将Aspose.Cells组件的引用添加到项目中，例如...\ Program Files\ Aspose\ Aspose.Cells\ Bin\ Net1.0\ Aspose.Cells.dll

### **添加数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用已填充数据的模板文件。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传入索引从PivotTables集合中访问新的 PivotTable 对象。# 使用 PivotTable 对象中封装的任何数据透视表对象来管理表。

下面是代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **添加数据透视图**

使用Aspose.Cells创建数据透视图：

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
