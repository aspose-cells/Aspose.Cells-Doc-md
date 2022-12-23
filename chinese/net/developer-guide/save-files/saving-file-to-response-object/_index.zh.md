---
title: 将文件保存到响应对象
type: docs
weight: 50
url: /zh/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells 使操作文件成为可能。本文介绍了将文件保存到响应对象的各种方式。

{{% /alert %}}

## **将文件保存到响应对象**

也可以动态生成文件并将其直接发送到客户端浏览器。为此，请使用一个特殊的重载版本**[保存](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**接受以下参数的方法：

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**目的。
- 文件名。
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**，输出文件的内容配置类型。
- **[保存选项](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, 文件格式类型

这**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**枚举确定发送到浏览器的文件是否提供直接在浏览器中自行打开或在与 .xls/.xlsx 或其他扩展名关联的应用程序中打开的选项。

枚举包含以下预定义的保存类型：

|**类型**|**描述**|
|:- |:- |
|附件|将电子表格发送到浏览器并作为与 .xls/.xlsx 或其他扩展名关联的附件在应用程序中打开|
|排队|将文档发送到浏览器并提供将电子表格保存到磁盘或在浏览器中打开的选项|

### **XLS 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **笔记**

由于对象“System.Web.HttpResponse”不包含在.NET5 和.Netstandard 中，
所以Aspose.Cells.NET5和.Netstandard版本不存在这个函数，可以参考下面的代码将文件保存到流中，然后对流进行操作。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

