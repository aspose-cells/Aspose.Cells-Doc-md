---
title: 使用 C++ 和 Golang 创建数据透视表和数据透视图
linktitle: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/go-cpp/create-pivot-tables-and-pivot-charts/
description: 学习如何使用 C++ 和 Golang 与 Aspose.Cells 在 Excel 文件中创建数据透视表和数据透视图
---

{{% alert color="primary" %}}

数据透视表是一个交互式的记录汇总。例如，你的工作表中可能有数百条发票条目。数据透视表可以按客户、产品或日期汇总发票。使用微软Excel，可以通过拖动按钮快速重新整理数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells支持[数据透视表](/cells/zh/cpp/create-pivot-tables-and-pivot-charts/)和[数据透视图](/cells/zh/cpp/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **添加数据透视表和数据透视图**

Aspose.Cells 提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置 PivotTable 对象，作为数据透视表对象的基本构建快：

- **PivotField**，数据透视表中的字段。
- **PivotFields**，所有PivotField对象的集合。
- **PivotTable**，工作表上的数据透视表报告。
- **PivotTables**，工作表上所有数据透视表对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/)
   1. 在您的开发计算机上安装它。
      所有[Aspose](http://www.aspose.com/)组件安装后都为评估模式，评估模式没有时间限制，只会在生成的文档中加入水印。若要充分使用组件功能，你需要拥有有效的许可证。
1. 创建一个项目：
   1. 启动你的C++集成开发环境（如Visual Studio）。
   1. 创建新的控制台应用程序。
1. 添加引用：
   将Aspose.Cells组件添加为你的项目引用，例如，`...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`。

### **添加数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用`Cell`对象的`PutValue`方法向工作表单元格中添加一些数据。你也可以使用已填充数据的模板文件。数据将用作数据透视表的数据源。
1. 通过调用`PivotTables`集合的`Add`方法（封装在`Worksheet`对象中）向工作表添加数据透视表。
1. 通过传递索引从`PivotTables`集合中访问新的`PivotTable`对象。使用任何封装在`PivotTable`对象中的数据透视表对象来管理表格。

下面是代码示例。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **添加数据透视图**

使用Aspose.Cells创建数据透视图：

1. 添加图表。
1. 设置图表的`PivotSource`，指向工作表中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
