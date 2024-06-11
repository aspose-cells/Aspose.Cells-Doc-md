---
title: 设置打印选项
type: docs
weight: 40
url: /zh/net/setting-print-options/
description: 本文演示了如何使用C＃ API和.NET库以编程方式设置Excel工作表页面设置功能的打印选项。您可以设置打印区域、打印标题和页面顺序。
keywords: 在C#中设置Excel打印区域，设置Excel打印标题，设置Excel页面顺序
---

{{% alert color="primary" %}}

Microsoft Excel的页面设置提供了几个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。

{{% /alert %}}

## **设置打印选项**

这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

Aspose.Cells支持Microsoft Excel提供的所有打印选项，并且开发人员可以轻松地使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供的属性来配置工作表的这些选项。下面更详细地讨论了如何使用这些属性。

### **设置打印区域**

默认情况下，打印区域包括包含数据的工作表的所有区域。开发人员可以为工作表确定特定的打印区域。

要选择特定的打印区域，请使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类的[**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)属性。将定义打印区域的单元格范围分配给此属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **设置打印标题**

Aspose.Cells允许您指定要在打印的工作表的所有页面上重复显示的行和列标题。为此，请使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类的[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)和[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类还提供了几个其他属性，以设置一般的打印选项，如下：

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)：一个布尔属性，定义是否打印网格线或不打印。
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings)：一个布尔属性，定义是否打印行和列标题或不打印。
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite)：一个布尔属性，定义是否以黑白模式打印工作表或不打印。
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)：定义是否在工作表上显示打印批注还是在工作表末尾显示。
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft)：一个布尔属性，定义是否打印不带图形的工作表。
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)：定义是否按显示的方式、空白、短横线或N/A打印单元格错误。

要设置[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)属性，Aspose.Cells还提供了两个枚举[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)和[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)，其中包含要分配给[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)和[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)属性的预定义值。

[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)枚举中的预定义值如下所示。

|**打印备注类型**|**描述**|
| :- | :- |
|PrintInPlace|指定将批注打印为显示在工作表上的形式。
|PrintNoComments|指定不打印批注。
|PrintSheetEnd|指定将批注打印在工作表末尾。

[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) 枚举的预定义值如下所示，并附有其描述。



|**打印错误类型**|**描述**|
| :- | :- |
|PrintErrorsBlank|指定不打印错误。|
|PrintErrorsDash|指定打印错误为"--"。|
|PrintErrorsDisplayed|指定打印错误为显示的形式。|
|PrintErrorsNA|指定打印错误为"#N/A"。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **设置页面顺序**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) 类提供了[**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) 属性，用于对工作表的多个页面进行打印排序。有两种排序页面的可能性如下。

- **先向下再向右：** 在打印右侧页面之前，将所有页面向下打印。
- **先向右再向下：** 在打印下方页面之前，从左到右打印页面。

Aspose.Cells提供一个枚举[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)，其中包含所有预定义的排序类型。

[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) 枚举的预定义值如下所示。

|**打印顺序类型**|**描述**|
| :- | :- |
|DownThenOver|表示打印顺序为先向下再向右。|
|OverThenDown|表示打印顺序为先向右再向下。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
