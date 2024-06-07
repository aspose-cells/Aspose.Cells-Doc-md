---
title: 保存文件到响应对象
type: docs
weight: 50
url: /zh/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells使得可以操纵文件并将其保存到响应对象。该文章解释了可以将文件保存到响应对象的各种方式。

{{% /alert %}}

## **将文件保存到响应对象**

也可以动态生成文件并直接发送到客户端浏览器。为此，使用接受以下参数的**[Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**方法的特殊重载版本：

- ASP.NET **[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)** 对象。
- 文件名。
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**，输出文件的内容-配置类型。
- **[SaveOptions](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**，文件格式类型。

**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)** 枚举确定发送到浏览器的文件是否提供在浏览器中直接打开或在与.xls/.xlsx或其他扩展名相关联的应用程序中打开的选项。

该枚举包含以下预定义保存类型：

|**类型**|**描述**|
| :- | :- |
|附件|将电子表格发送到浏览器，在与.xls/.xlsx或其他扩展名相关联的附件中打开应用程序|
|内联|将文档发送到浏览器并提供选项将电子表格保存到磁盘或在浏览器内打开|

### **XLS 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF 文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **注意**

由于对象“System.Web.HttpResponse”未包含在.NET5和.Netstandard中，
因此，在 Aspose.Cells .NET5 和 .Netstandard 版本中不存在此功能，您可以参考以下代码将文件保存到流中，然后对流执行操作。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

