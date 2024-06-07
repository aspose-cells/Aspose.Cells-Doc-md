---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，您可能在工作表的列表中有数百个发票条目。数据透视表可以按客户、产品或日期对发票进行汇总。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更容易地理解数据，因为数据透视表会自动创建小计和合计。

Aspose.Cells支持[数据透视表](/cells/zh/net/create-pivot-tables-and-pivot-charts/)和[数据透视图](/cells/zh/net/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **添加数据透视表和数据透视视图**

Aspose.Cells提供了一组特殊的类来创建数据透视表。 这些类用于创建和设置PivotTable对象，这些对象充当了数据透视表的基本组成部分:

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有PivotField对象的集合。
- PivotTable，工作表上的数据透视表报告。
- PivotTables，工作表上所有PivotTable对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装Aspose.Cells:
   1. [下载Aspose.Cells](https://downloads.aspose.com/cells/net)。
   1. 在开发计算机上安装它。
      安装[Aspose](http://www.aspose.com/)组件后，会以评估模式运行。 评估模式没有时间限制，只会向生成的文档中注入水印。 要充分利用组件，您需要拥有有效的许可证。
1. 创建一个项目:
   1. 启动 Visual Studio.Net。
   1. 创建一个新的控制台应用程序。
1. 添加引用:
   将Aspose.Cells组件的引用添加到您的项目中，例如...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **添加数据透视表**

使用Aspose.Cells创建数据透视表:

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用模板文件，该文件已经填充了数据。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。# 使用数据透视表对象封装的任何数据透视表对象来管理数据表。

以下是代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **添加数据透视图**

使用Aspose.Cells创建数据透视图:

1. 添加一个图表。
1. 将图表的PivotSource设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

