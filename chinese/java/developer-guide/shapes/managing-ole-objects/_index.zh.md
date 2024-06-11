---
title: 管理OLE对象
type: docs
weight: 30
url: /zh/java/managing-ole-objects/
---

## **介绍**

OLE (对象链接和嵌入) 是微软的复合文档技术框架。简而言之，复合文档类似于一个显示桌面，可以包含各种视觉和信息对象: 文本、日历、动画、声音、动态视频、3D、不断更新的新闻、控件等。每个桌面对象都是一个独立的程序实体，可以与用户交互，并与桌面上的其他对象进行通信。

OLE (对象链接和嵌入) 受到许多不同程序的支持，并用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将Microsoft Word文档插入Microsoft Excel。要查看可以插入的内容的类型，请单击**插入**菜单上的**对象**。只有安装在计算机上并支持OLE对象的程序才会出现在**对象类型**框中。

## **向工作表中插入OLE对象**

Aspose.Cells支持在工作表中添加、提取和操纵OLE对象。因此，Aspose.Cells有[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)类，用于将新的OLE对象添加到集合列表中。另一个类，[**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)，表示一个OLE对象。它有一些重要的成员:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) 指定字节数组类型的图像(图标)数据。图像将被显示，以显示工作表中的OLE对象。
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) 指定以字节数组的形式的对象数据。当您双击OLE对象图标时，这些数据将显示在其相关程序中。

以下示例显示了如何将OLE对象添加到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **从工作簿中提取OLE对象**

以下示例显示了如何从工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并根据OLE对象的文件格式类型保存不同的文件(DOC、XLS、PPT、PDF等)。

这是模板XLS文件的屏幕截图，其中嵌入了不同的OLE对象。

**模板文件包含四个OLE对象** 

![todo:image_alt_text](managing-ole-objects_1.png)

运行代码后，我们可以根据它们各自的OLE对象格式类型保存不同的文件。以下是一些创建文件的屏幕截图。

**提取的XLS文件** 

![todo:image_alt_text](managing-ole-objects_2.png)

**提取的PPT文件** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **提取嵌入的MOL文件**

Aspose.Cells支持提取不常见类型的对象，例如MOL（包含有关原子和键的分子数据文件）。以下代码片段演示了提取嵌入的MOL文件并将其保存到磁盘中，使用的是这个[sample excel file](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **高级主题**
- [访问和修改链接的OLE对象的显示标签](/cells/zh/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取OLE对象](/cells/zh/java/extract-ole-objects-from-workbook/)
- [获取或设置嵌入的OLE对象的类标识符](/cells/zh/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
