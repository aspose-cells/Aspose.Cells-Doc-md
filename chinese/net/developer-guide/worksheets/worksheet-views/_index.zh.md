---
title: 工作表视图
type: docs
weight: 40
url: /zh/net/worksheet-views/
description: 本文将介绍如何使用C#和.NET API与Excel工作簿和工作表的分页预览交互。操作分栏窗格、冻结窗格和缩放倍数等。 
---

## **分页预览**

所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。页面分页预览是一种编辑视图，显示工作表的打印效果。页面分页预览显示数据将会显示在每一页，以便调整打印区域和页面分页。使用Aspose.Cells开发人员可以启用普通视图或页面分页预览模式。

### **控制视图模式**

Aspose.Cells提供了一个代表Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 班。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 班包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班提供了各种属性和方法，用于管理工作表。为了启用普通或页面分页预览模式，使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班的 [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 属性。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 是一个布尔属性，只能存储 **true** 或 **false** 值。

#### **启用普通视图**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班的 [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 属性设置为 **false**，将工作表设置为普通视图。

#### **启用分页预览**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班的 [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 属性设置为 **true**，将任何工作表设为页面分页预览。这样做将工作表从普通视图切换到页面分页预览。

下面给出一个完整的示例，演示了如何使用 [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 属性为Excel文件的第一个工作表启用页面分页预览模式。

通过创建 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 班的实例打开book1.xls文件。通过将 [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) 属性设置为 **true**，将视图切换为页面分页预览第一个工作表。修改后的文件被保存为output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **缩放因子**

### **使用Microsoft Excel**

Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。

### **Aspose.Cells和缩放因子**

Aspose.Cells允许开发人员设置工作表的缩放因子。
Aspose.Cells提供了一个代表Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 班。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 班包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班提供了各种属性和方法，用于管理工作表。为了设置工作表的缩放因子，使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 班的 [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) 属性。通过将数字（整数）值分配给 [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) 属性，设置缩放因子。

下面提供了一个完整的示例，演示了如何使用 [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) 属性设置Excel文件的第一个工作表的缩放因子。

通过创建一个[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的实例来打开book1.xls文件。将第一个工作表的缩放比例设置为75，并将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **冻结窗格**

### **使用Microsoft Excel**

冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。

### **Aspose.Cells 和 冻结窗格**

Aspose.Cells允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells提供一个代表Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了各种属性和方法来管理工作表。要配置冻结窗格，请调用Worksheet类的[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法。[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法接受以下参数:

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见的列数

通过在实例化时调用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的构造函数来打开book1.xls文件，并在第一个工作表中冻结了一些行和列。修改后的文件保存为output.xls。

下面给出了一个完整示例，展示如何使用[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法来冻结第一个工作表（从C4开始，由第4行和第3列表示，其中行和列从0索引开始）的行和列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **拆分窗格**

如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。

### **应用和移除拆分窗格**

#### **拆分窗格**

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了一系列用于管理Excel文件的属性和方法。要实现分割视图，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split)。要移除分割窗格，请使用[**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

运行以上代码后，生成的文件将具有分割视图。

#### **移除窗格**

使用 [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit) 方法来删除分割窗格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **高级主题**
- [隐藏工作表中零值的显示](/cells/zh/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/net/set-worksheet-tab-color/)
- [显示和隐藏网格线以及行列标题](/cells/zh/net/show-and-hide-gridlines-and-row-column-headers/)
- [显示和隐藏行、列和滚动条](/cells/zh/net/show-and-hide-rows-columns-and-scroll-bars/)
- [显示和隐藏工作表和标签](/cells/zh/net/show-and-hide-worksheets-and-tabs/)
- [在工作表中显示公式而非数值](/cells/zh/net/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/net/use-error-checking-options/)

{{< app/cells/assistant language="csharp" >}}
