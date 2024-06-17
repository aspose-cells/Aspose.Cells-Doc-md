---
title: 从工作簿中提取OLE对象
type: docs
weight: 110
url: /zh/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

有时，你确实需要从工作簿中提取OLE对象。Aspose.Cells支持提取和保存这些Ole对象。

本文介绍了如何在Visual Studio.Net中创建一个控制台应用程序，并用几行简单的代码从工作簿中提取不同的OLE对象。

{{% /alert %}}

## **从工作簿中提取OLE对象**

### **创建模板工作簿**

1. 在Microsoft Excel中创建一个工作簿。
1. 在第一个工作表上添加一个Microsoft Word文档，一个Excel工作簿和一个PDF文档作为OLE对象。

|**带有OLE对象的模板文档（OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

然后提取OLE对象并将它们保存到硬盘上的相应文件类型。

### **下载并安装Aspose.Cells**

1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
1. 在您的开发计算机上安装它。

所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。

### **创建一个项目**

启动 Visual Studio.Net 并创建一个新的控制台应用程序。该示例将展示一个C#控制台应用程序，但你也可以使用VB.NET。

1. 添加引用
   1. 向项目添加Aspose.Cells组件的引用，例如向...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll添加引用。

### **从工作簿中提取OLE对象**

下面的代码实际完成了查找和提取OLE对象的工作。OLE对象（DOC、XLS和PDF文件）被保存到磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
