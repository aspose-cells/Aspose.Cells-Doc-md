---
title: 创建数据透视表和数据透视图
type: docs
weight: 10
url: /zh/java/create-pivot-tables-and-pivot-charts/
description: 在Aspose.Cells for Java API中创建透视表和透视图。
keywords: excel创建透视表java，excel创建透视图java，excel创建透视表和透视图java，创建excel透视表java，创建excel透视图java，创建excel透视表和透视图java，java创建excel透视表和透视图，如何创建excel透视表和透视图java
---

{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，您可能在工作表的列表中有数百个发票条目。数据透视表可以按客户、产品或日期对发票进行汇总。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更容易地理解数据，因为数据透视表会自动创建小计和合计。

Aspose.Cells支持[pivot tables](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table)和[pivot charts](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table)。

{{% /alert %}}

## **添加数据透视表和数据透视视图**

Aspose.Cells提供了一组特殊的类来创建数据透视表。 这些类用于创建和设置PivotTable对象，这些对象充当了数据透视表的基本组成部分:

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有PivotField对象的集合。
- PivotTable，工作表上的数据透视表报告。
- PivotTables，工作表上所有PivotTable对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装Aspose.Cells.Zip：
   1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java)。
   1. 在开发计算机上解压缩。
      所有[Aspose](http://www.aspose.com/)组件在安装后均以评估模式运行。评估模式没有时间限制，只会将水印注入生成的文档中。
1. 创建一个项目
   1. 您可以使用某些Java编辑器（例如Eclipse）创建项目，也可以使用NotePad创建一个简单的程序。
1. 添加类路径:
   使用Eclipse设置类路径:
   1. 从Aspose.Cells.zip中提取Aspose.Cells.jar和dom4j_1.6.1.jar。
   1. 在Eclipse中设置项目的类路径:
   1. 在Eclipse中选择项目，然后单击菜单项目-属性。
   1. 在弹出窗口的左侧选择“Java构建路径”，然后选择“库”选项卡，单击“添加JAR”或“添加外部JAR”以选择Aspose.Cells.jar和dom4j_1.6.1.jar，并将其添加到构建路径中。
   1. 编写应用程序以调用Aspose组件的API。
      或者您可以在Windows的DOS提示符下在运行时设置它。

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **创建数据透视表**

使用Aspose.Cells创建数据透视表:

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用模板文件，该文件已经填充了数据。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。
1. 使用PivotTable对象封装的任何透视表对象来管理表格。

以下是给出的代码示例。执行代码会生成一个新文件：pivotTable_test.xls。

**输入数据** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**输出透视表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **基于透视表创建透视图表**

使用Aspose.Cells创建透视图表：

1. 添加一个图表。
1. 将图表的PivotSource设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

以下是组件用来完成任务的代码。执行代码会生成一个新文件：pivotChart_test.xls。

**透视图表工作表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

本文介绍如何使用Aspose.Cells创建透视表和透视图表。希望可以帮助您在自己的场景中使用这些功能。

Aspose.Cells受益于多年的研究、设计和精心调整。

欢迎在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)提出您的问题、评论和建议。我们保证会及时回复。

{{% /alert %}}

## 相关文章

- [数据透视表中的自定义排序](/cells/zh/java/custom-sorting-in-pivot-table/)
- [格式化数据透视表](/cells/zh/java/formatting-pivot-table/)
- [刷新和计算包含计算项的数据透视表](/cells/zh/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [禁用数据透视表功能区](/cells/zh/java/disable-pivot-table-ribbons/)

