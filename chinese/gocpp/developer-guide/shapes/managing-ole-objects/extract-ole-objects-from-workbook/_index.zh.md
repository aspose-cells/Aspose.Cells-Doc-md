---
title: 用Golang通过C++从工作簿提取OLE对象
linktitle: 从工作簿中提取OLE对象
type: docs
weight: 110
url: /zh/go-cpp/extract-ole-objects-from-workbook/
description: 学习如何用Golang通过C++用Aspose.Cells从工作簿提取OLE对象。
---

{{% alert color="primary" %}}

有时，你需要从工作簿中提取OLE对象。Aspose.Cells支持提取和保存这些OLE对象。

本文展示了如何在Visual Studio中创建控制台应用程序，并使用少量代码从工作簿中提取不同的OLE对象。

{{% /alert %}}

## **从工作簿中提取OLE对象**

### **创建模板工作簿**

1. 在Microsoft Excel中创建一个工作簿。
1. 在第一个工作表上添加Microsoft Word文档、Excel工作簿和PDF文档作为OLE对象。

|**带有OLE对象的模板文档（OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

接下来，提取OLE对象并保存到硬盘，保留其各自的文件类型。

### **下载并安装Aspose.Cells**

1. [下载 Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)。
1. 在您的开发计算机上安装它。

所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。

### **创建一个项目**

启动**Visual Studio**并创建一个新的控制台应用程序。此示例将展示一个C++控制台应用程序。

1. 添加引用
   1. 向你的项目中添加对Aspose.Cells组件的引用，例如，添加对...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用。

### **从工作簿中提取OLE对象**

以下代码实际完成了查找和提取OLE对象的工作。OLE对象（DOC、XLS和PDF文件）会被保存到硬盘。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
