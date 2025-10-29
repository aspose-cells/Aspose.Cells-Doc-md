---
title: 从工作簿中提取OLE对象
type: docs
weight: 110
url: /zh/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

有时，你确实需要从工作簿中提取 OLE 对象。Aspose.Cells for Python via .NET 支持提取和保存这些 Ole 对象。

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

### **使用 Aspose.Cells for Python Excel 库提取 OLE 对象**

下面的代码实际完成了查找和提取OLE对象的工作。OLE对象（DOC、XLS和PDF文件）被保存到磁盘上。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
