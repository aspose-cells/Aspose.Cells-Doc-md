---
title: 管理OLE对象
type: docs
weight: 30
url: /zh/java/managing-ole-objects/
---

## **介绍**

OLE（对象链接与嵌入）是微软的一个复合文档技术框架。简单地说，一个复合文档类似于一个显示桌面，可以包含各种视觉和信息对象：文本、日历、动画、声音、运动视频、3D、持续更新的新闻、控件等。每个桌面对象都是一个可以与用户交互并与桌面上的其他对象通信的独立程序实体。

OLE（对象链接与嵌入）受许多不同的程序支持，用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将Microsoft Word文档插入到Microsoft Excel中。要查看您可以插入的内容类型，请单击**插入**菜单上的**对象**。只有已安装在计算机上并支持OLE对象的程序才会出现在**对象类型**框中。

## **将 OLE 对象插入工作表**

Aspose.Cells 支持在工作表中添加、提取和操作 OLE 对象。因此，Aspose.Cells 有 [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection) 类，用于向集合列表中添加新的 OLE 对象。另一个类，[**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)，表示一个 OLE 对象，它具有一些重要的成员：

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) 指定 byte 数组类型的图像（图标）数据。在工作表中显示图像以显示 OLE 对象。
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) 指定以字节数组形式的对象数据。在双击 OLE 对象图标时，该数据将显示在相关程序中。

以下示例显示了如何向工作表中添加一个 OLE 对象。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **在工作簿中提取OLE对象**

以下示例显示了如何在工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并基于OLE对象的文件格式类型保存不同的文件（DOC、XLS、PPT、PDF等）。

这是模板 XLS 文件的屏幕截图，其中在第一个工作表中嵌入了不同的 OLE 对象。

**模板文件包含四个 OLE 对象** 

![todo:image_alt_text](managing-ole-objects_1.png)

运行代码后，我们可以根据各自的 OLE 对象格式类型保存不同的文件。以下是部分创建的文件的屏幕截图。

**提取的 XLS 文件** 

![todo:image_alt_text](managing-ole-objects_2.png)

**提取的 PPT 文件** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **提取嵌入的MOL文件**

Aspose.Cells 支持提取像 MOL（包含关于原子和键的分子数据文件）这样的不常见类型的对象。以下代码段演示了如何提取嵌入的 MOL 文件并将其保存到磁盘，使用的是这个 [示例 excel 文件](EmbeddedMolSample.xlsx)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **高级主题**
- [访问和修改关联OLE对象的显示标签](/cells/zh/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [使用Aspose.Cells通过Microsoft Excel自动刷新OLE对象](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取OLE对象](/cells/zh/java/extract-ole-objects-from-workbook/)
- [获取或设置嵌入式OLE对象的类标识符](/cells/zh/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
