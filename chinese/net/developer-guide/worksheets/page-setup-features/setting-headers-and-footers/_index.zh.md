---
title: 设置页眉和页脚
type: docs
weight: 30
url: /zh/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

页眉和页脚分别是显示在上边距下方或下边距上方的文本行。也可以向工作表添加页眉和页脚。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。页眉和页脚使用页面设置进行管理。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells 允许您在运行时向工作表添加页眉和页脚，但我们建议在预先设计的打印文件中手动设置页眉和页脚。您可以使用 Microsoft Excel 作为 GUI 工具来设置页眉和页脚，以节省工作量和开发时间。 Aspose.Cells 可以导入文件并保存设置。

要在运行时添加页眉和页脚，Aspose.Cells 提供特殊的 API 调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是允许您设置页眉和页脚格式的特殊命令。

|**脚本命令**|**描述**|
|:- |:- |
|&P|当前页码|
|＆G|照片|
|&N|总页数|
|&D|当前日期|
|&T|当前时间|
|＆一个|工作表名称|
|＆F|没有路径的文件名|
|&"\<FontName>"|表示字体名称。例如：&"宋体"|
|&"\<FontName>, \<FontStyle>"|表示带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|表示字体大小。例如：“&14abc”。但是，如果此命令后跟要在标题中打印的普通数字，则应使用空格字符将其与字体大小分隔开。例如：“&14 123”。|

### **设置页眉和页脚**

这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供了两个方法，[**设置标题**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader)和[**设置页脚**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter)用于向工作表添加页眉和页脚。这些方法只有两个参数：

- **部分** – 应该放置页眉或页脚的部分。分为左、中、右三部分，分别用0、1、2表示。
- **脚本**– 用于页眉或页脚的脚本。此脚本包含用于格式化页眉或页脚的脚本命令。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **将图像插入页眉或页脚**

这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类有两个额外的方法，[**设置页眉图片**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture)和[**设置页脚图片**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture)用于将图片添加到页眉和页脚中。这些方法采用参数：

- **部分**– 放置图片的页眉或页脚部分。共有左、中、右三个部分，分别用值 0、1 和 2 表示。
- **字节数组**– 图形数据（二进制数据应写入字节数组的缓冲区）。

执行下面的代码并打开文件后，通过以下方式检查工作表的标题：

1. 在**文件**菜单，选择**页面设置**.将显示一个对话框。
1. 选择**页眉页脚**标签。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
