---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，您在工作表的列表中可能有数百个发票条目。数据透视表可以按客户、产品或日期汇总发票。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更轻松地理解数据，因为数据透视表会自动创建小计和总计。

 Aspose.Cells 支持[数据透视表](/cells/zh/net/create-pivot-tables-and-pivot-charts/)和[数据透视表](/cells/zh/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **添加数据透视表和图表**

Aspose.Cells 提供了一组用于创建数据透视表的特殊类。这些类用于创建和设置数据透视表对象，这些对象充当数据透视表对象的基本构建块：

- PivotField，数据透视表报表中的一个字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 数据透视表，工作表上的数据透视表。
- 数据透视表，工作表上所有数据透视表对象的集合。

### **准备使用 Aspose.Cells**

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. 在您的开发计算机上安装它。
全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。要以其全部功能使用该组件，您需要拥有有效的许可证。
1. 创建一个项目：
 1. 启动 Visual Studio.Net。
 1. 创建一个新的控制台应用程序。
1. 添加参考资料：
将对 Aspose.Cells 组件的引用添加到您的项目中，例如 ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **添加数据透视表**

使用 Aspose.Cells 创建数据透视表：

1. 使用 Cell 对象的 PutValue/setValue 方法将一些数据添加到工作表单元格。您还可以使用已填充数据的模板文件。数据将用作数据透视表的数据源。
1. 通过调用 PivotTables 集合的 add 方法（封装在 Worksheet 对象中）向工作表添加数据透视表。
1. 通过传递其索引从 PivotTables 集合访问新的 PivotTable 对象。 # 使用任何封装在数据透视表对象中的数据透视表对象来管理表格。

下面给出了代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **添加数据透视图**

要使用 Aspose.Cells 创建数据透视图：

1. 添加图表。
1. 将图表的 PivotSource 设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

