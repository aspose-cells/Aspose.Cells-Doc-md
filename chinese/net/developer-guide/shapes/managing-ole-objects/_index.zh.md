---
title: 管理OLE对象
type: docs
weight: 50
url: /zh/net/managing-ole-objects/
---

## **介绍**

OLE（对象链接与嵌入）是微软的一个复合文档技术框架。简单地说，一个复合文档类似于一个显示桌面，可以包含各种视觉和信息对象：文本、日历、动画、声音、运动视频、3D、持续更新的新闻、控件等。每个桌面对象都是一个可以与用户交互并与桌面上的其他对象通信的独立程序实体。

OLE（对象链接与嵌入）受许多不同的程序支持，用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将Microsoft Word文档插入到Microsoft Excel中。要查看您可以插入的内容类型，请单击**插入**菜单上的**对象**。只有已安装在计算机上并支持OLE对象的程序才会出现在**对象类型**框中。

### **将OLE对象插入工作表**

Aspose.Cells支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells具有[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)类，用于向集合列表添加新的OLE对象。另一个类[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)代表一个OLE对象。它有一些重要成员：

- [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)属性指定字节数组类型的图像(图标)数据。图像将显示在工作表中以显示OLE对象。
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)属性指定字节数组形式的对象数据。当您双击OLE对象图标时，将在其相关程序中显示此数据。

以下示例显示如何将OLE对象插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **在工作簿中提取OLE对象**

以下示例显示了如何在工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并基于OLE对象的文件格式类型保存不同的文件（DOC、XLS、PPT、PDF等）。

运行代码后，我们可以根据各自的OLE对象格式类型保存不同的文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **提取嵌入的MOL文件**

Aspose.Cells支持提取不常见类型的对象，如MOL（包含有关原子和键的信息的分子数据文件）。以下代码片段演示了提取嵌入的MOL文件并将其保存到磁盘中的方法，使用了这个[示例Excel文件](94896196.xlsx)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **高级主题**
- [访问和修改关联OLE对象的显示标签](/cells/zh/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [使用Aspose.Cells通过Microsoft Excel自动刷新OLE对象](/cells/zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取OLE对象](/cells/zh/net/extract-ole-objects-from-workbook/)
- [获取或设置嵌入式OLE对象的类标识符](/cells/zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [将WAV文件作为OLE对象插入](/cells/zh/net/inserting-a-wav-file-as-an-ole-object/)

