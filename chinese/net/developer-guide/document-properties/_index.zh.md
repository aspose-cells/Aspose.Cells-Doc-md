---
title: 管理文档属性
linktitle: 文档属性
type: docs
weight: 80
url: /zh/net/managing-document-properties/
description: 通过Aspose.Cells for NET APIs管理文档属性方法。
keywords: 如何在C#中管理文档属性，使用C#获取或设置文档属性，通过C#添加或删除文档属性，通过C#插入或删除文档属性，通过Aspose.Cells for NET APIs访问文档属性。
---


## **介绍**

Microsoft Excel提供了向电子表格文件添加属性的功能。这些文档属性提供有用信息，分为以下2类。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称-值对的形式定义的自定义属性。

{{% alert color="primary" %}}

关于内建属性和自定义属性，最重要的一点是内建属性可以被访问和修改，但不能被创建或移除。然而，自定义属性可以被创建和管理。

{{% /alert %}}

## **如何使用Microsoft Excel管理文档属性**

Microsoft Excel允许您以所见即所得的方式管理Excel文件的文档属性。请按照以下步骤在Excel 2016中打开**属性**对话框。

1. 从**文件**菜单中选择**信息**。

|**选择信息菜单**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. 点击**属性**标题并选择"高级属性"。

|**单击高级属性选择**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. 管理文件的文档属性。

|**属性对话框**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
在属性对话框中，有不同的选项卡，如常规、摘要、统计、内容和自定义。每个选项卡都可以帮助配置文件相关的不同信息。自定义选项卡用于管理自定义属性。

## **如何使用Aspose.Cells处理文档属性**

开发人员可以使用Aspose.Cells API动态管理文档属性。此功能帮助开发人员存储有用信息，如文件接收时间、处理时间戳等。

{{% alert color="primary" %}}

Aspose.Cells for .NET直接在输出文档中写入API和版本号的信息。例如，将文档呈现为PDF时，Aspose.Cells for .NET会将 **Application** 字段填充为 'Aspose.Cells'，将 **PDF Producer** 字段填充为 'Aspose.Cells v17.9' 等值。

请注意，您不能指示Aspose.Cells for .NET更改或删除输出文档中的此信息。

{{% /alert %}}

### **如何访问文档属性**

Aspose.Cells API支持内建和自定义文档属性。Aspose.Cells的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类代表Excel文件，类似于Excel文件，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类可以包含多个工作表，每个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示，而工作表的集合由[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)类表示。

使用[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)如下访问文件的文档属性。

- 要访问内建文档属性，请使用[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)。
- 要访问自定义文档属性，请使用[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)。

[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)和[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)都返回[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)的实例。此集合包含[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)对象，每个对象代表一个单独的内建或自定义文档属性。

应用程序要求如何访问属性取决于;即通过从[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)中的索引或属性名称来访问属性，如下面的示例所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)类允许检索文档属性的名称、值和类型:

- 要获取属性名称，请使用[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name)。
- 要获取属性值，请使用[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)。[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) 将值作为对象返回。
- 要获取属性类型，请使用[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type)。这将返回[**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)枚举值之一。获取属性类型后，请使用**DocumentProperty.ToXXX** 方法之一获取适当类型的值，而不是使用[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)。**DocumentProperty.ToXXX** 方法在下表中描述。

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)类还提供了一系列返回其他数据类型值的方法。

{{% /alert %}}

|**成员名称**|**描述**|**ToXXX方法**|
| :- | :- | :- |
|Boolean|属性数据类型为布尔值|ToBool|
|Date|属性数据类型为日期时间。请注意，Microsoft Excel仅存储日期部分，无法在此类型的自定义属性中存储时间|ToDateTime|
|Float|属性数据类型为双精度浮点数|ToDouble|
|Number|属性数据类型为Int32|ToInt|
|String|属性数据类型为字符串|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **如何添加或删除自定义文档属性**

正如我们在本主题开头所述的那样，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些是用户定义的。

### **如何添加自定义属性**

Aspose.Cells API已经为[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)类公开了[**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)方法，以便将自定义属性添加到集合中。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)方法将属性添加到Excel文件，并返回新文档属性的引用，作为[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **如何配置'链接到内容'自定义属性**

要创建与给定范围的内容链接的自定义属性，请调用[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)方法并传递属性名称和来源。您可以使用[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)属性检查属性是否配置为链接到内容。此外，还可以使用[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)类的[**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)属性获取源范围。

我们在示例中使用了一个简单的模板Microsoft Excel文件。工作簿有一个命名范围标记为**MyRange**，它指向单元格值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **如何移除自定义属性**

要使用Aspose.Cells删除自定义属性，调用[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)方法并传递要移除的文档属性的名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **高级主题**
- [在文档信息面板中可见的自定义属性](/cells/zh/net/adding-custom-properties-visible-inside-document-information-panel/)
- [设置内置文档属性的ScaleCrop和LinksUpToDate属性](/cells/zh/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [使用内置文档属性指定Excel文件的文档版本](/cells/zh/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [使用内置文档属性指定Excel文件的语言](/cells/zh/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
