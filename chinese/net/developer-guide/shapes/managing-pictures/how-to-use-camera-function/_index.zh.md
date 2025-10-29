---
title: 如何添加摄像头到范围
type: docs
weight: 10
url: /zh/net/how-to-add-camera-for-range/
description: 本文将介绍如何为内容范围Aspose.Cells for .NET API添加摄像头。
keywords: 如何使用摄像头功能，如何为范围内容添加摄像头，如何使用摄像头工具，Excel中的摄像头功能，如何在Aspose.Cells for .NET中使用摄像头功能
---

## **可能的使用场景**
Excel中的摄像头工具是一个隐藏但强大的功能，它可以让你创建任何单元格范围的实时链接快照。以下是原因及使用场景。

摄像头工具的作用：
1. 拍摄所选范围单元格的“图片”。
2. 这张“图片”是实时链接——如果源单元格发生变化，图片会自动更新。
3. 你可以在工作表上的任何位置移动或调整图片大小，甚至可以移动到另一个工作表。


## **如何在Excel中使用摄像头功能**
以下是使用Excel中摄像头工具的逐步指南——一种创建单元格范围实时动态图像的强大方法。

### 启用摄像头工具

摄像头工具默认是隐藏的。以下是添加方法：

1. 点击Excel左上角快速访问工具栏的向下箭头。
2. 选择“更多命令...”。
3. 在对话框中：从“选择命令来源”下拉菜单中选择“功能区之外的命令”。向下滚动并选择“相机”。点击“添加 >>”以将其添加到工具栏。
4. 点击“确定”。现在你会在工具栏中看到一个小相机图标。

### 使用相机工具
1. 选择你要捕获的单元格区域（例如 A1:C5）。
2. 点击快速访问工具栏上的相机图标。
3. 你的光标将变成十字线。
4. 在工作表上点击你想放置图片的任何位置。所选范围的实时图片会被插入。

### 动态链接
该图片与原始单元格链接。如果源区域中的值或格式发生变化，图片会自动更新。


## **如何在 Aspose.Cells for .NET 中为区域添加相机**
Aspose.Cells 支持显示单元格或区域内容为图片形状。你可以将图片链接到包含你想显示数据的单元格或区域。由于该单元格或区域与图形对象是关联的，你对单元格或区域中数据所做的更改会自动显示在图形对象中。 

以下是使用 [示例文件](camera.xlsx)在 Aspose.Cells for .NET 中使用相机功能的基本示例：

1. 使用 [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook) 类加载示例文件。
1. 通过调用 [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) 方法（封装在 [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 集合的 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 对象中）在工作表中添加图片。 
1. 使用 [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) 属性指定单元格区域（封装在 [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) 对象中）。
1. 更新工作表中所选形状的值。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **输出结果**
下图显示由 Aspose.Cells for .NET 在输出 Excel 文件中创建的区域 (A1:E12) 的相机截图。
<br>
添加数据前：
<br>
<img src="1.png" width=70% />
<br>
添加数据后：
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
