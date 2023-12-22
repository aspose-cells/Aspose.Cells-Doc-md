---
title: 管理文档属性
linktitle: 文档属性
type: docs
weight: 80
url: /zh/net/managing-document-properties/
description: 了解如何通过 Aspose.Cells for NET API 管理文档属性。
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **介绍**

Microsoft Excel 提供了向电子表格文件添加属性的功能。这些文档属性提供了有用的信息，并分为 2 类，如下所述。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称-值对的形式定义的自定义属性。

{{% alert color="primary" %}}

了解内置属性和自定义属性最重要的一点是内置属性可以访问和修改，但不能创建或删除。但是，可以创建和管理自定义属性。

{{% /alert %}}

##  **如何使用 Microsoft Excel 管理文档属性**

Microsoft Excel 允许您以所见即所得的方式管理 Excel 文件的文档属性。请按照以下步骤打开**特性**Excel 2016 中的对话框。

1. 来自**文件**菜单，选择*信息**。

|**选择信息菜单**|
| :- |
|![待办事项：图像_替代_文本](managing-document-properties_1.png)|
1. 点击**特性**标题并选择“高级属性”。

|**单击高级属性选择**|
| :- |
|![待办事项：图像_替代_文本](managing-document-properties_2.png)|
1. 管理文件的文档属性。

|**属性对话框**|
| :- |
|![待办事项：图像_替代_文本](managing-document-properties_3.png)|
在“属性”对话框中，有不同的选项卡，例如“常规”、“摘要”、“统计信息”、“内容”和“自定义”。每个选项卡有助于配置与文件相关的不同类型的信息。自定义选项卡用于管理自定义属性。

##  **如何使用 Aspose.Cells 处理文档属性**

开发人员可以使用 Aspose.Cells API 动态管理文档属性。此功能可帮助开发人员将有用的信息与文件一起存储，例如文件的接收时间、处理时间、时间戳等。

{{% alert color="primary" %}}

 Aspose.Cells for .NET 直接将API和版本号的信息写入输出文档中。例如，将 Document 渲染为 PDF 时，将填充 Aspose.Cells for .NET**应用**值为“Aspose.Cells”的字段和**PDF 制片人**具有值的字段，例如“Aspose.Cells v17.9”。

请注意，您无法指示 Aspose.Cells for .NET 更改或从输出文档中删除此信息。

{{% /alert %}}

###  **如何访问文档属性**

Aspose.Cells API 支持两种类型的文档属性：内置属性和自定义属性。 Aspose.Cells'[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类代表一个 Excel 文件，与 Excel 文件一样，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类可以包含多个工作表，每个工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类，而工作表的集合由[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)班级。

使用[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)访问文件的文档属性，如下所述。

- 要访问内置文档属性，请使用[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- 要访问自定义文档属性，请使用[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

这俩[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)和[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)返回实例[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)。该合集包含[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)对象，每个对象代表一个内置或自定义文档属性。

如何访问属性取决于应用程序的要求，即；通过使用属性的索引或名称[**文档属性集合**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)如下例所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

这[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)类允许检索文档属性的名称、值和类型：

- 要获取属性名称，请使用[**文档属性.名称**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- 要获取属性值，请使用[**文档属性.值**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**文档属性.值**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)以对象形式返回值。
- 要获取属性类型，请使用[**文档属性.类型**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type)。这将返回其中之一[**财产种类**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)枚举值。获取属性类型后，使用其中之一**文档属性.ToXXX**方法来获取适当类型的值，而不是使用[**文档属性.值**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)。这**文档属性.ToXXX**方法如下表所述。

{{% alert color="primary" %}}

这[**文件属性**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)类还提供了一组返回其他数据类型的值的方法。

{{% /alert %}}

|**成员名字**|**描述**|**ToXXX方法**|
| :- | :- | :- |
|布尔值|属性数据类型为布尔值|布尔值|
|日期|属性数据类型为 DateTime。请注意，Microsoft Excel 仅存储<br>日期部分，这种类型的自定义属性中不能存储时间|至今时间|
|漂浮|属性数据类型为 Double|至双倍|
|数字|属性数据类型为 Int32|至整数|
|String|属性数据类型为 String|转字符串|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **如何添加或删除自定义文档属性**

正如我们前面在本主题开头所描述的，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些属性是用户定义的。

###  **如何添加自定义属性**

 Aspose.Cells API 已暴露[**添加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)方法为[**自定义文档属性集合**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)类以便将自定义属性添加到集合中。这[**添加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)方法将该属性添加到 Excel 文件并返回新文档属性的引用作为[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)目的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **如何配置“内容链接”自定义属性**

要创建链接到给定范围内容的自定义属性，请调用[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)方法并传递属性名称和来源。您可以使用以下命令检查属性是否配置为链接到内容[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)财产。此外，还可以使用以下方式获取源范围[**来源**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)的财产[**文件属性**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)班级。

我们在示例中使用一个简单的模板 Microsoft Excel 文件。该工作簿有一个已定义的命名范围，标记为**我的范围**它指的是一个单元格值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **如何删除自定义属性**

要使用 Aspose.Cells 删除自定义属性，请调用[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)方法并传递要删除的文档属性的名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **高级主题**
- [添加文档信息面板中可见的自定义属性](/cells/zh/net/adding-custom-properties-visible-inside-document-information-panel/)
- [设置内置文档属性的 ScaleCrop 和 LinksUpToDate 属性](/cells/zh/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [使用内置文档属性指定 Excel 文件的文档版本](/cells/zh/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [使用内置文档属性指定 Excel 文件的语言](/cells/zh/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
