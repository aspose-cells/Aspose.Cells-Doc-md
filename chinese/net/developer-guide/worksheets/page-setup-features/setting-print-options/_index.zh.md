---
title: 设置打印选项
type: docs
weight: 40
url: /zh/net/setting-print-options/
description: 本文演示如何使用 C# API 和 .NET 库在程序中设置 Excel 工作表页面设置功能的打印选项。您可以设置打印区域、打印标题和页面顺序。
keywords: 设置 Excel 打印区域 c#，设置 Excel 打印标题 c#，设置 Excel 页面顺序 c#
---

{{% alert color="primary" %}}

Microsoft Excel 的页面设置提供多个打印选项 (也称为工作表选项)，允许用户控制工作表页的打印方式。

{{% /alert %}}

## **设置打印选项**

这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 实现草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

Aspose.Cells支持Microsoft Excel提供的所有打印选项，开发人员可以使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供的属性轻松配置这些选项以用于工作表。如何使用这些属性在下面更详细地讨论。

### **设置打印范围**

默认情况下，打印区域包含所有包含数据的工作表区域。开发人员可以建立工作表的特定打印区域。

要选择特定的打印区域，请使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类的[**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)属性。将定义打印区域的单元格范围分配给此属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **设置打印标题**

Aspose.Cells允许您指定要在打印的工作表的所有页面上重复的行和列标头。为此，请使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类的[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)和[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)属性。

将重复的行或列由其行号或列号传递定义。例如，行定义为$1:$2，列定义为$A:$B。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类还提供几个其他属性以设置常规打印选项，如下所示：

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines):定义是否打印网格线或不打印的布尔属性。
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings):定义是否打印行和列标题或不打印的布尔属性。
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite):定义是否以黑白模式打印工作表或不打印的布尔属性。
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)：定义是否在工作表上显示打印注释或在工作表末尾显示。
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft)：定义是否打印不带图形的工作表的布尔属性。
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)：定义是否打印单元格错误为显示、空白、破折号或 N/A。

要设置[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)属性，Aspose.Cells还提供了两个枚举，[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)和[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)，分别包含要分配给[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)属性的预定义值。

[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)枚举中的预定义值列在下面，并附有描述。

|**打印注释类型**|**描述**|
| :- | :- |
|PrintInPlace|指定将注释打印为工作表上显示的样式。|
|PrintNoComments|指定不打印注释。|
|PrintSheetEnd|指定在工作表末尾打印注释。|

[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)枚举的预定义值列在下面，并附有描述。



|**打印错误类型**|**描述**|
| :- | :- |
|PrintErrorsBlank|指定不打印错误。|
|PrintErrorsDash|指定将错误打印为“- -”。|
|PrintErrorsDisplayed|指定将错误打印为显示的样式。|
|PrintErrorsNA|指定将错误打印为“#N/A”。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **设置页面顺序**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供[**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)属性，用于对要打印的工作表的多个页面进行排序。有两种可能性对页面进行排序。

- **先向下再向右：** 在打印任何页面向右之前，将所有页面向下打印。
- **先向右再向下：** 在打印下方页面之前以从左到右的顺序打印页面。

Aspose.Cells提供了一个枚举，[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)，其中包含所有预定义的顺序类型。

[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)枚举的预定义值如下所示。

|**打印顺序类型**|**描述**|
| :- | :- |
|DownThenOver|表示打印顺序为先向下，然后向上。|
|OverThenDown|表示打印顺序为向上，然后向下。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
