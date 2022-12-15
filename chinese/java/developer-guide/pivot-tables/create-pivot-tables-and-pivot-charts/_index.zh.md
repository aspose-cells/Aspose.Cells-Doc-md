---
title: 创建数据透视表和数据透视图
type: docs
weight: 10
url: /zh/java/create-pivot-tables-and-pivot-charts/
description: 使用 Aspose.Cells for Java API 创建数据透视表和数据透视图。
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，您在工作表的列表中可能有数百个发票条目。数据透视表可以按客户、产品或日期汇总发票。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更轻松地理解数据，因为数据透视表会自动创建小计和总计。

 Aspose.Cells 支持[数据透视表](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table)和[数据透视表](/cells/zh/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **添加数据透视表和图表**

Aspose.Cells 提供了一组用于创建数据透视表的特殊类。这些类用于创建和设置数据透视表对象，这些对象充当数据透视表对象的基本构建块：

- PivotField，数据透视表报表中的一个字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 数据透视表，工作表上的数据透视表。
- 数据透视表，工作表上所有数据透视表对象的集合。

### **准备使用 Aspose.Cells**

1. 下载并安装Aspose.Cells.Zip：
   1. [下载 Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 在您的开发计算机上解压它。
全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。
1. 创建项目
 1. 您可以使用某些 Java 编辑器（例如 Eclipse）创建一个项目，或者使用记事本创建一个简单的程序。
1. 添加类路径：
使用 Eclipse 设置类路径：
1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
 1、在Eclipse中设置项目的类路径：
1. 在 Eclipse 中选择您的项目，然后单击菜单 Project-Properties。
 1、在弹出的窗口左侧选择“Java Build Path”，然后选择“Libraries”选项卡，点击“Add JARs”或“Add External JARs”选择Aspose.Cells.jar和dom4j_1.6.1.jar并添加进入构建路径。
 1.编写应用调用Aspose的组件API。
或者您可以在运行时在 Windows 的 dos 提示符下设置它。

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **创建数据透视表**

使用 Aspose.Cells 创建数据透视表：

1. 使用 Cell 对象的 PutValue/setValue 方法将一些数据添加到工作表单元格。您还可以使用已填充数据的模板文件。数据将用作数据透视表的数据源。
1. 通过调用 PivotTables 集合的 add 方法（封装在 Worksheet 对象中）向工作表添加数据透视表。
1. 通过传递其索引从 PivotTables 集合访问新的 PivotTable 对象。
1. 使用任何封装在数据透视表对象中的数据透视表对象来管理表格。

下面给出了代码示例。执行代码会生成一个新文件：pivotTable_test.xls。

**输入数据** 

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_1.png)

**输出数据透视表**

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **基于数据透视表创建数据透视图**

要使用 Aspose.Cells 创建数据透视图：

1. 添加图表。
1. 将图表的 PivotSource 设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

下面是组件用来完成任务的代码。执行代码会生成一个新文件：pivotChart_test.xls。

**枢轴图表表**

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells 创建数据透视表和数据透视图。希望它能帮助您在自己的场景中使用这些功能。

Aspose.Cells 得益于多年的研究、设计和精心调整。

我们欢迎您的查询、意见和建议[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).我们保证及时回复。

{{% /alert %}}

## 相关文章

- [数据透视表中的自定义排序](/cells/zh/java/custom-sorting-in-pivot-table/)
- [格式化数据透视表](/cells/zh/java/formatting-pivot-table/)
- [刷新并计算具有计算项的数据透视表](/cells/zh/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [禁用数据透视表功能区](/cells/zh/java/disable-pivot-table-ribbons/)

