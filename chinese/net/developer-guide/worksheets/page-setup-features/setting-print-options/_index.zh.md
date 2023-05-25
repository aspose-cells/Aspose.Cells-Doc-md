---
title: 设置打印选项
type: docs
weight: 40
url: /zh/net/setting-print-options/
description: 本文演示如何使用 C# API 和 .NET 库以编程方式设置 Excel 工作表页面设置功能的打印选项。您可以设置打印区域、打印标题和页序。
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

Microsoft Excel 的页面设置设置提供了多个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。

{{% /alert %}}

##  **设置打印选项**

这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 达到草稿质量。
- 打印评论。
- 打印单元错误。
- 定义页面排序。

 Aspose.Cells 支持 Microsoft Excel 提供的所有打印选项，开发人员可以使用 Excel 提供的属性轻松地为工作表配置这些选项[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级。下面将更详细地讨论如何使用这些属性。

###  **设置打印区域**

默认情况下，打印区域包含工作表中包含数据的所有区域。开发人员可以建立工作表的特定打印区域。

要选择特定的打印区域，请使用[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**打印区域**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)财产。将定义打印区域的单元格范围分配给此属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **设置打印标题**

Aspose.Cells 允许您指定行和列标题以在打印的工作表的所有页面上重复。为此，请使用[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**打印标题列**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)和[**打印标题行**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)特性。

将重复的行或列通过传递它们的行号或列号来定义。例如，行定义为 $1:$2，列定义为 $A:$B。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **设置其他打印选项**

这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类还提供了几个其他属性来设置常规打印选项，如下所示：

- [**打印网格线**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)一个布尔属性，定义是否打印网格线。
- [**打印标题**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings)定义是否打印行和列标题的布尔属性。
- [**黑与白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite)：一个布尔属性，定义是否以黑白模式打印工作表。
- [**打印评论**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)：定义是在工作表上还是在工作表末尾显示打印注释。
- [**打印草稿**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft)一个布尔属性，定义是否打印没有图形的工作表。
- [**打印错误**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)定义是否将单元格错误打印为显示、空白、破折号或 N/A。

设置[**打印评论**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**打印错误**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)属性，Aspose.Cells还提供了两个枚举，[**打印注释类型**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)， 和[**打印错误类型**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)包含要分配给的预定义值[**打印评论**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**打印错误**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)分别属性。

中的预定义值[**打印注释类型**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)下面列出了枚举及其描述。

|**打印注释类型**|**描述**|
| :- | :- |
|就地打印|指定打印工作表上显示的注释。|
|打印无评论|指定不打印注释。|
|打印页结束|指定在工作表末尾打印注释。|

的预定义值[**打印错误类型**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)下面列出了枚举及其描述。



|**打印错误类型**|**描述**|
| :- | :- |
|打印错误空白|指定不打印错误。|
|PrintErrorsDash|指定将错误打印为“--”。|
|显示打印错误|指定打印显示的错误。|
|打印错误NA|指定将错误打印为“#N/A”。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **设置页面顺序**

这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供了[**命令**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)用于订购要打印的工作表的多页的属性。有两种可能性可以按如下方式对页面进行排序。

- **下来然后结束：**在向右打印任何页面之前先向下打印所有页面。
- **然后向下：**在打印下面的页面之前先从左到右打印页面。

 Aspose.Cells 提供枚举，[**打印订单类型**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)包含所有预定义的订单类型。

的预定义值[**打印订单类型**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)列举如下。

|**打印订单类型**|**描述**|
| :- | :- |
|先下后上|将打印顺序表示为向下然后结束。|
|过后|表示打印顺序为 over 然后 down。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
