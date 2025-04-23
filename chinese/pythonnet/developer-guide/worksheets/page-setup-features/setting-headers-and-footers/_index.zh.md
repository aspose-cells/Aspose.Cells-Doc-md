---
title: 设置页眉和页脚
type: docs
weight: 30
url: /zh/python-net/setting-headers-and-footers/
description: 本文讲解了如何通过使用 Aspose.Cells for Python via .NET API 设置脚本命令，程序化地在Excel工作表的页眉和页脚插入图片。
keywords: Python Excel 库，Python 在Excel页眉页脚插入图片，使用Python设置Excel页眉页脚脚本命令。
---

{{% alert color="primary" %}}

页眉和页脚是显示在顶部边距下方或底部边距上方的文本行。还可以将页眉和页脚添加到工作表中。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。通过页面设置设置页眉和页脚。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells for Python via .NET 允许你在运行时向工作表添加页眉和页脚，但我们建议在预先设计好的文件中手动设置页眉和页脚以便打印。你可以使用Microsoft Excel作为图形界面工具来设置页眉和页脚，以节省精力和开发时间。Aspose.Cells for Python via .NET可以导入文件并保存设置。

为了在运行时添加页眉和页脚，Aspose.Cells for Python via .NET 提供了特殊的API调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是特殊命令，允许您设置页眉和页脚的格式。

|**脚本命令**|**描述**|
| :- | :- |
当前页号||&P|
图片||&G|
总页数||&N|
|&D|当前日期|
|&T|当前时间|
|&A|工作表名称|
|&F|文件名（不含路径）|
|&"\<FontName>"|表示字体名称。例如：&"Arial"|
|&"\<FontName>, \<FontStyle>"|表示带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|代表字体大小。例如：“&14abc”。但如果此命令后跟一个要在页眉中打印的普通数字，则应与字体大小用空格分隔。例如：“&14 123”。

### **如何设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) 类提供两种方法，[**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) 和 [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str)，用于向工作表添加页眉和页脚。这些方法只有两个参数：

- **Section** – 应放置页眉或页脚的部分。有三个部分：左、中、右，分别由0、1和2表示。
- **Script** – 用于页眉或页脚的脚本。此脚本包含对页眉或页脚进行格式化的脚本命令。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **如何在页眉或页脚插入图片**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) 类还有两个额外的方法，[**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) 和 [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes)，用于在页眉和页脚中添加图片。这些方法需要以下参数：

- **Section** – 图片将放置的页眉或页脚部分。有三个部分：左、中、右，分别由值0、1和2表示。
- **字节数组** – 图形数据（二进制数据应写入字节数组的缓冲区）。

执行以下代码并打开文件后，请通过以下方式检查工作表的页眉：

1. 在 **文件** 菜单上，选择 **页面设置**。将显示一个对话框。
1. 选择 **页眉/页脚** 选项卡。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
