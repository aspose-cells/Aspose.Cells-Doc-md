---
title: 从工作簿中提取OLE对象
type: docs
weight: 110
url: /zh/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

有时，您确实需要从工作簿中提取OLE对象。Aspose.Cells支持提取和保存这些 Ole 对象。

本文展示如何在Visual Studio.Net中创建控制台应用程序，并使用简短的代码行从工作簿中提取不同的OLE对象。

{{% /alert %}}

## **从工作簿中提取OLE对象**

### **创建一个模板工作簿**

1. 在 Microsoft Excel 中创建一个工作簿。
1. 在第一个工作表上添加一个 Microsoft Word 文档、一个 Excel 工作簿和一个 PDF 文档作为OLE对象。

|**带有OLE对象的模板文档（OleFile.xls）**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

接下来提取OLE对象并按其各自的文件类型保存到硬盘。

### **下载并安装 Aspose.Cells**

1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
1. 在开发计算机上安装它。

所有Aspose组件在安装时都以评估模式运行。评估模式没有时间限制，只会在生成的文档中插入水印。

### **创建一个项目**

启动 **Visual Studio.Net** 并创建一个新的控制台应用程序。 本示例将展示一个C#控制台应用程序，但您也可以使用 VB.NET。

1. 添加引用
   1. 向您的项目添加对Aspose.Cells组件的引用，例如向...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll添加一个引用。

### **提取OLE对象**

下面的代码执行实际的查找和提取OLE对象的工作。 OLE对象（DOC、XLS和PDF文件）将保存到磁盘。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
