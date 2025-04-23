---
title: 管理OLE对象
type: docs
weight: 50
url: /zh/python-net/managing-ole-objects/
---

## **介绍**

OLE (对象链接和嵌入) 是微软的复合文档技术框架。简而言之，复合文档类似于一个显示桌面，可以包含各种视觉和信息对象: 文本、日历、动画、声音、动态视频、3D、不断更新的新闻、控件等。每个桌面对象都是一个独立的程序实体，可以与用户交互，并与桌面上的其他对象进行通信。

OLE (对象链接和嵌入) 受到许多不同程序的支持，并用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将Microsoft Word文档插入Microsoft Excel。要查看可以插入的内容的类型，请单击**插入**菜单上的**对象**。只有安装在计算机上并支持OLE对象的程序才会出现在**对象类型**框中。

### **将OLE对象插入工作表**

Aspose.Cells for Python via .NET 支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells for Python via .NET 具有 [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection) 类，用于向集合列表添加新的OLE对象。另一类 [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject)，代表OLE对象。它有一些重要成员：

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data)属性指定图像（图标）数据为字节数组类型。将显示该图像以显示工作表中的OLE对象。
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data)属性指定对象数据的字节数组形式。当您双击OLE对象图标时，将在其关联的程序中显示此数据。

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **从工作簿中提取OLE对象**

以下示例显示了如何从工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并根据OLE对象的文件格式类型保存不同的文件(DOC、XLS、PPT、PDF等)。

运行代码后，我们可以根据各自OLE对象的格式类型保存不同的文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **提取嵌入的MOL文件**

Aspose.Cells for Python via .NET 支持提取不常见类型的对象，如 MOL（分子数据文件，包含有关原子和键的信息）。以下代码片段演示如何使用此[示例Excel文件](94896196.xlsx) 提取嵌入的 MOL 文件并保存到磁盘。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **高级主题**
- [访问和修改链接的OLE对象的显示标签](/cells/zh/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [自动刷新OLE对象](/cells/zh/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取OLE对象](/cells/zh/python-net/extract-ole-objects-from-workbook/)
- [获取或设置嵌入的OLE对象的类标识符](/cells/zh/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [将WAV文件插入为一个OLE对象。](/cells/zh/python-net/inserting-a-wav-file-as-an-ole-object/)

