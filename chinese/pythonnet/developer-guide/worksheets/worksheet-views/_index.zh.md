---
title: 工作表视图
type: docs
weight: 40
url: /zh/python-net/worksheet-views/
description: 本文将描述如何使用Aspose.Cells for Python via .NET API与Excel工作簿和工作表的分页预览进行交互。使用分隔窗格、冻结窗格和缩放系数。 
keywords: Python Excel库，Python如何设置分页预览，Python如何启用普通视图，Python如何设置缩放系数，Python如何冻结窗格，Python如何拆分窗格，Python如何移除窗格。
---

## **分页预览**

所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示工作表将要打印的内容。分页预览显示每页上将显示哪些数据，因此您可以调整打印区域和分页符。使用Aspose.Cells for Python via .NET，开发者可以启用普通视图或分页预览模式。

### **控制视图模式**

Aspose.Cells for Python via .NET提供了一个[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类，表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班提供了各种属性和方法，用于管理工作表。为了启用普通或页面分页预览模式，使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班的 [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 属性。[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 是一个布尔属性，只能存储 **true** 或 **false** 值。

#### **启用普通视图**

通过将 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班的 [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 属性设置为 **false**，将工作表设置为普通视图。

#### **启用分页预览**

通过将 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班的 [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 属性设置为 **true**，将任何工作表设为页面分页预览。这样做将工作表从普通视图切换到页面分页预览。

下面给出一个完整的示例，演示了如何使用 [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 属性为Excel文件的第一个工作表启用页面分页预览模式。

通过创建 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 班的实例打开book1.xls文件。通过将 [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) 属性设置为 **true**，将视图切换为页面分页预览第一个工作表。修改后的文件被保存为output.xls。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **缩放因子**

### **使用Microsoft Excel**

Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。

### **Aspose.Cells和缩放因子**

Aspose.Cells允许开发人员设置工作表的缩放因子。
Aspose.Cells提供了一个代表Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 班。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 班包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许访问Excel文件中的每个工作表。

一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班提供了各种属性和方法，用于管理工作表。为了设置工作表的缩放因子，使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 班的 [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) 属性。通过将数字（整数）值分配给 [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) 属性，设置缩放因子。

下面提供了一个完整的示例，演示了如何使用 [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) 属性设置Excel文件的第一个工作表的缩放因子。

通过创建一个[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的实例来打开book1.xls文件。将第一个工作表的缩放比例设置为75，并将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **冻结窗格**

### **使用Microsoft Excel**

冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。

### **Aspose.Cells 和 冻结窗格**

Aspose.Cells允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells提供一个代表Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了各种属性和方法来管理工作表。要配置冻结窗格，请调用Worksheet类的[**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int)方法。[**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int)方法接受以下参数:

- **row**，冻结将从该单元格开始的行索引。
- **column**，冻结将从该单元格开始的列索引。
- **frozen_rows**，顶部窗格中可见行数。
- **frozen_columns**，左侧窗格中可见列数。

通过在实例化时调用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的构造函数来打开book1.xls文件，并在第一个工作表中冻结了一些行和列。修改后的文件保存为output.xls。

下面给出了一个完整示例，展示如何使用[**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)方法来冻结第一个工作表（从C4开始，由第4行和第3列表示，其中行和列从0索引开始）的行和列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **拆分窗格**

如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。

### **应用和移除拆分窗格**

#### **拆分窗格**

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类提供了一系列用于管理Excel文件的属性和方法。要实现分割视图，请使用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类的[**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split)。要移除分割窗格，请使用[**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split)方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

运行以上代码后，生成的文件将具有分割视图。

#### **移除窗格**

使用 [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split) 方法来删除分割窗格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **高级主题**
- [隐藏工作表中零值的显示](/cells/zh/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/python-net/set-worksheet-tab-color/)
- [显示和隐藏网格线以及行列标题](/cells/zh/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [显示和隐藏行、列和滚动条](/cells/zh/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [显示和隐藏工作表和标签](/cells/zh/python-net/show-and-hide-worksheets-and-tabs/)
- [在工作表中显示公式而非数值](/cells/zh/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/python-net/use-error-checking-options/)

