---
title: 管理 OLE 对象
type: docs
weight: 30
url: /zh/java/managing-ole-objects/
---
## **介绍**

OLE（Object Linking and Embedding）是Microsoft的一种复合文档技术框架。简而言之，复合文档类似于显示桌面，可以包含各种视觉和信息对象：文本、日历、动画、声音、动态视频、3D、不断更新的新闻、控件等。每个桌面对象都是一个独立的程序实体，可以与用户交互，也可以与桌面上的其他对象进行通信。

许多不同的程序都支持 OLE（对象链接和嵌入），用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将 Microsoft 的 Word 文档插入到 Microsoft 的 Excel 中。要查看您可以插入的内容类型，请单击**目的**在**插入**菜单。只有安装在计算机上并支持 OLE 对象的程序才会出现在**对象类型**盒子。

## **将 OLE 对象插入工作表**

Aspose.Cells 支持在工作表中添加、提取和操作 OLE 对象。因此，Aspose.Cells 具有[**OleObject集合**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)类，用于将新的 OLE 对象添加到集合列表中。另一个班级，[**对象**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)代表一个 OLE 对象。它有一些重要的成员：

- [**图像数据**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)指定字节数组类型的图像（图标）数据。将显示图像以显示工作表中的 OLE 对象。
- [**对象数据**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)以字节数组的形式指定对象数据。当您双击 OLE 对象图标时，该数据将显示在其相关程序中。

以下示例显示如何将 OLE 对象添加到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **提取工作簿中的 OLE 对象**

以下示例显示如何在工作簿中提取 OLE 对象。该示例从现有的 XLS 文件中获取不同的 OLE 对象，并根据 OLE 对象的文件格式类型保存不同的文件（DOC、XLS、PPT、PDF 等）。

这是模板 XLS 文件的屏幕截图，它在第一个工作表中嵌入了不同的 OLE 对象。

**模板文件包含四个 OLE 对象** 

![待办事项：图像_替代_文本](managing-ole-objects_1.png)

运行代码后，我们可以根据各自的 OLE Objects 格式类型保存不同的文件。以下是一些已创建文件的屏幕截图。

**提取的 XLS 文件** 

![待办事项：图像_替代_文本](managing-ole-objects_2.png)

**提取的PPT文件** 

![待办事项：图像_替代_文本](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **提取嵌入式 MOL 文件**

Aspose.Cells 支持提取不常见类型的对象，如 MOL（包含有关原子和键的信息的分子数据文件）。下面的代码片段演示了如何提取嵌入的 MOL 文件并将其保存到磁盘[示例 excel 文件](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **推进主题**
- [访问和修改链接 Ole 对象的显示标签](/cells/zh/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [使用 Aspose.Cells 通过 Microsoft Excel 自动刷新 OLE 对象](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取 OLE 对象](/cells/zh/java/extract-ole-objects-from-workbook/)
- [获取或设置嵌入式 OLE 对象的类标识符](/cells/zh/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
