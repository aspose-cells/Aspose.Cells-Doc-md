---
title: 创建数据透视表和数据透视图
type: docs
weight: 10
url: /zh/java/create-pivot-tables-and-pivot-charts/
description: 使用 Aspose.Cells for Java API 创建数据透视表和数据透视图。
keywords: excel创建数据透视表java, excel创建数据透视图java, excel创建数据透视表和数据透视图java, 创建excel数据透视表java, 创建excel数据透视图java, 创建excel数据透视表和数据透视图java, java创建excel数据透视表和数据透视图, 如何创建excel数据透视表和数据透视图java
---

{{% alert color="primary" %}}

数据透视表是记录的互动摘要。例如，您可能有数百个工作表中列表中的发票条目。数据透视表可以按客户、产品或日期总计发票。使用Microsoft Excel，可以通过将按钮拖到新位置，快速重新排列数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells支持 [数据透视表](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) 和 [数据透视图](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table)。

{{% /alert %}}

## **添加数据透视表和数据透视图**

Aspose.Cells 提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置 PivotTable 对象，作为数据透视表对象的基本构建快：

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 一个工作表上的数据透视表。
- 数据透视表是工作表上所有数据透视表对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装Aspose.Cells.Zip：
   1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. 在开发计算机上解压缩。
      所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。
1. 创建一个项目
   1. 您可以使用Java编辑器（例如Eclipse）创建项目，或者使用NotePad创建一个简单的程序。
1. 添加类路径：
   在Eclipse中设置类路径：
   1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
   1. 在 Eclipse 的项目中设置类路径：
   1. 在Eclipse中选择您的项目，然后点击菜单Project-Properties。
   1. 在弹出窗口的左侧选择“Java Build Path”，然后选择“Libraries”选项卡，单击“Add JARs”或“Add External JARs”以选择Aspose.Cells.jar和dom4j_1.6.1.jar，并将它们添加到构建路径中。
   1. 编写调用Aspose组件API的应用程序。
      或者您可以在Windows的dos提示符下在运行时设置它。

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **创建数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用已填充数据的模板文件。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。
1. 使用PivotTable对象中封装的任何数据透视表对象来管理表。

下面给出了一段代码示例。执行该代码将生成一个新文件：pivotTable_test.xls。

**输入数据** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**输出的数据透视表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **基于数据透视表创建数据透视图**

使用Aspose.Cells创建一个数据透视图:

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

以下是组件用于完成任务的代码。执行代码会生成一个新文件：pivotChart_test.xls。

**数据透视图表工作表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells创建数据透视表和数据透视图表。希望能帮助您在自己的场景中使用这些功能。

Aspose.Cells 从多年的研究、设计和精心调整中受益。

我们欢迎您在[Aspose.Cells 论坛](https://forum.aspose.com/c/cells/9)上提出问题、评论和建议。我们保证会及时回复。

{{% /alert %}}

## 相关文章

- [数据透视表中的自定义排序](/cells/zh/java/custom-sorting-in-pivot-table/)
- [格式化数据透视表](/cells/zh/java/formatting-pivot-table/)
- [刷新和计算包含计算项的数据透视表](/cells/zh/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [禁用数据透视表功能区](/cells/zh/java/disable-pivot-table-ribbons/)

