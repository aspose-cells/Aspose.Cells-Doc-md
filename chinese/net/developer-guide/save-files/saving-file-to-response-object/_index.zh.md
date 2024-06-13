---
title: 将文件保存到响应对象
type: docs
weight: 50
url: /zh/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells可以操作文件。本文解释了可以将文件保存到响应对象的各种方法。

{{% /alert %}}

## **将文件保存到响应对象**

还可以动态生成文件并直接发送到客户端浏览器。 为此，使用接受以下参数的 [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) 方法的特殊重载版本：

- ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) 对象。
- 文件名。
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)，输出文件的 content-disposition 类型。
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)，文件格式类型

[**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) 枚举确定发送到浏览器的文件是否提供直接在浏览器中打开或在与 .xls/.xlsx 或其他扩展名相关联的应用程序中打开的选项。

该枚举包含以下预定义的保存类型：

|**类型**|**描述**|
| :- | :- |
|附件|将电子表格发送到浏览器，并作为与.xls/.xlsx或其他扩展名相关联的附件在应用程序中打开|
|内置|将文档发送到浏览器，并提供选项将电子表格保存到磁盘或在浏览器中打开|

### **XLS文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **注意**

由于未在.NET5和.Netstandard中包含"System.Web.HttpResponse"对象，
因此，在Aspose.Cells .NET5和.Netstandard版本中不存在此函数，您可以参考以下代码将文件保存到流中，然后对流进行操作。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

