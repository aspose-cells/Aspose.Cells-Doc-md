---
title: 设置页眉和页脚
type: docs
weight: 30
url: /zh/net/setting-headers-and-footers/
description: 本文详细介绍如何通过使用C# API或.NET库设置脚本命令来在Excel工作表的页眉和页脚中插入图像。
keywords: 在Excel页眉和页脚中插入图像的C#，设置Excel页眉和页脚脚本命令C#
---

{{% alert color="primary" %}}

页眉和页脚分别是显示在顶部边缘下方或底部边缘上方的文本行。也可以向工作表添加页眉和页脚。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。通过页面设置设置和管理页眉和页脚。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells允许您在运行时向工作表添加页眉和页脚，但我们建议在预先设计好的文件中手动设置页眉和页脚以供打印。您可以使用Microsoft Excel作为GUI工具来设置页眉和页脚，以节省工作量和开发时间。Aspose.Cells可以导入文件并保存设置。

要在运行时添加页眉和页脚，Aspose.Cells提供特殊的API调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是一种特殊命令，允许您设置页眉和页脚的格式。

|**脚本命令**|**描述**|
| :- | :- |
|&P|当前页面编号|
|&G|图片|
|&N|总页面数|
|&D|当前日期|
|&T|当前时间|
|&A|工作表名称|
|&F|文件名不带路径|
|&"\<FontName>"|表示字体名称。例如：＆"Arial"|
|&"\<FontName>, \<FontStyle>"|表示带样式的字体名称。例如：＆"Arial,Bold"|
|&\<FontSize>|表示字体大小。例如：“＆14abc”。但如果这个命令后面跟着要在页眉中打印的纯数字，则应该用一个空格字符与字体大小分隔开。例如：“＆14 123”。|

### **设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供两种方法，[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader)和[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter)，用于向工作表添加页眉和页脚。这些方法只接受两个参数：

- **Section** – 应放置页眉或页脚的部分。有三个部分：左侧、中间和右侧，分别用0、1和2表示。
- **Script** – 用于页眉或页脚的脚本。此脚本包含格式化页眉或页脚的脚本命令。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **在页眉或页脚中插入图像**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类有两个额外方法，[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture)和[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture)，用于将图片添加到页眉和页脚中。这些方法接受以下参数：

- **Section** – 图片将放置的页眉或页脚部分。有三个部分，left、center和right，分别由值 0、1和2表示。
- **Byte array** – 图形数据（二进制数据应写入字节数组的缓冲区）。

在执行以下代码并打开文件后，通过:

1. 在**文件**菜单上，选择**页面设置**。将显示一个对话框。
1. 选择**页眉/页脚**选项卡。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
