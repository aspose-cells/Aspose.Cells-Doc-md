---
title: 从工作簿中提取 OLE 对象
type: docs
weight: 110
url: /zh/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

有时，您确实需要从工作簿中提取 OLE 对象。 Aspose.Cells 支持提取和保存那些 Ole 对象。

本文展示了如何在 Visual Studio.Net 中创建一个控制台应用程序，并使用几行简单的代码从工作簿中提取不同的 OLE 对象。

{{% /alert %}}

## **从工作簿中提取 OLE 对象**

### **创建模板工作簿**

1. 在 Microsoft Excel 中创建了一个工作簿。
1. 在第一个工作表上添加一个 Microsoft Word 文档、一个 Excel 工作簿和一个 PDF 文档作为 OLE 对象。

|**带有 OLE 对象的模板文档 (OleFile.xls)**|
|:- |
|![待办事项：图像_替代_文本](extract-ole-objects-from-workbook_1.png)|

接下来提取 OLE 对象并将它们以各自的文件类型保存到硬盘。

### **下载并安装 Aspose.Cells**

1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. 在您的开发计算机上安装它。

所有 Aspose 组件在安装后都在评估模式下工作。评估模式没有时间限制，它只在生成的文档中注入水印。

### **创建项目**

开始**Visual Studio.Net**并创建一个新的控制台应用程序。此示例将显示 C# 控制台应用程序，但您也可以使用 VB.NET。

1. 添加引用
 1.在你的项目中添加对Aspose.Cells组件的引用，例如添加对...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用

### **提取 OLE 对象**

下面的代码执行查找和提取 OLE 对象的实际工作。 OLE 对象（DOC、XLS 和 PDF 文件）保存到磁盘。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
