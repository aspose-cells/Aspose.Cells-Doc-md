---
title: 工作表视图
type: docs
weight: 40
url: /zh/go-cpp/worksheet-views/
---

## **分页预览**

所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示工作表将要打印的内容。分页预览显示数据将会出现在每一页上，因此您可以调整打印区域和分页。使用Aspose.Cells开发人员可以启用普通视图或分页预览模式。

### **控制视图模式**

Aspose.Cells 提供代表Microsoft Excel文件的 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类。该类包含一个 [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) 集合，可访问每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类表示。该类提供了广泛的管理工作表的方法。要启用正常或分页预览模式，使用 [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) 方法。 [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) 返回布尔值，仅能存储 **真** 或 **假**。

#### **启用普通视图**

通过将 [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) 方法设置为 **假** ，将工作表设为正常视图。

#### **启用分页预览**

通过将 [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) 方法设置为 **真** ，即可将任何工作表设为分页预览。这样可以将工作表从正常视图切换到分页预览状态。

下面提供完整示例，演示如何使用 [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) 方法为Excel文件的第一张工作表启用分页预览模式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **缩放因子**

### **使用Microsoft Excel**

Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。

### **Aspose.Cells和缩放因子**

Aspose.Cells 也允许开发者设置工作表的缩放比例。该库提供 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类，代表一个Microsoft Excel文件。该类包含 [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) 集合，便于访问每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类表示。该类提供用于管理工作表的多种方法。要设置工作表的缩放比例，调用 [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) 方法。缩放比例通过赋值一个整数值来设置。

下面提供完整示例，演示如何使用 [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) 方法设置Excel文件第一张工作表的缩放比例。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **冻结窗格**

### **使用Microsoft Excel**

冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。

### **Aspose.Cells 和 冻结窗格**

Aspose.Cells 还允许开发者在运行时对工作表应用冻结窗格。提供了 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类，代表Excel文件。

工作表由 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类表示，提供多种管理方法。要配置冻结窗格，调用该类的 [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) 方法，该方法接受参数如下：

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见的列数

下面提供完整示例，演示如何使用 [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) 方法冻结Excel文件第一张工作表的行列（从C4开始，代表第4行和第3列，行和列索引从0开始）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **拆分窗格**

如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。

### **应用和移除拆分窗格**

#### **拆分窗格**

Aspose.Cells 提供 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类，代表Excel文件。该类提供各种管理Excel的方法。要实现拆分视图，使用 [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) 方法。要移除拆分窗格，使用 [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) 方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **移除窗格**

使用 [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) 方法移除拆分窗格。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
