---
title: 管理文档属性
type: docs
weight: 10
url: /zh/java/managing-document-properties/
---

## **介绍**

Microsoft Excel提供了向电子表格文件添加属性的功能。这些文档属性提供有用的信息，并分为以下2类。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题，作者姓名，文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称 - 值对的形式定义的自定义属性。

{{% alert color="primary" %}}

关于内置和自定义属性最重要的一点是，内置属性可以被访问和修改，但不能创建或删除，但是可以创建和管理自定义文档属性。

{{% /alert %}}

## **使用Microsoft Excel管理文档属性**

Microsoft Excel允许以所见即所得的方式管理Excel文件的文档属性。 请按照以下步骤在Excel 2016中打开**属性**对话框。

1. 从**文件**菜单中选择**信息**。

|**选择信息菜单**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. 单击**属性**标题，然后选择“高级属性”。

|**单击高级属性选择**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. 管理文件的文档属性。

|**属性对话框**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
在属性对话框中，有不同的选项卡，如常规，摘要，统计信息，内容和自定义。每个选项卡都有助于配置与文件相关的不同类型信息。自定义选项卡用于管理自定义属性。

## **使用Aspose.Cells处理文档属性**

开发人员可以使用Aspose.Cells API动态管理文档属性。该功能帮助开发人员存储有用的信息，例如文件接收、处理、时间戳等等。

{{% alert color="primary" %}}

Aspose.Cells for Java直接在输出文档中写入有关API和版本号的信息。 例如，在将文档渲染为PDF时，Aspose.Cells for Java将**Application**字段填充为'Aspose.Cells'，将**PDF Producer**字段填充为值，如'Aspose.Cells for Java v17.9'。

请注意，您不能指示Aspose.Cells for Java更改或删除输出文档中的这些信息。

{{% /alert %}}

### **访问文档属性**

Aspose.Cells API支持内置和自定义文档属性两种类型。Aspose.Cells的 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类表示一个Excel文件，就像Excel文件一样，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类可以包含多个工作表，每个工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示，而工作表集合由 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 类表示。

使用 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 访问文件的文档属性，如下所述。

- 要访问内置文档属性，请使用 [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)。
- 要访问自定义文档属性，请使用[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)。

[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)和[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)都返回[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)的一个实例。 此集合包含[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)个对象，每个对象表示单个内置或自定义文档属性。

如何访问属性取决于应用程序的需求，即：是否使用 [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) 中的属性索引或名称，如下例所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) 类允许检索文档属性的名称、值和类型：

- 获取属性名称，使用 [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name)。
- 获取属性值，使用 [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)。[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) 将该值作为一个对象返回。
- 要获取属性类型，请使用 [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type)。这将返回 [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType) 枚举值之一。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **添加或删除自定义文档属性**

正如我们在本主题开头所述，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些是用户定义的。

### **添加自定义属性**

Aspose.Cells API 已经在 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) 类中暴露了 [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) 方法，以便向集合添加自定义属性。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) 方法将属性添加到 Excel 文件，并返回一个新文档属性的参考作为 [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) 对象。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **配置“链接到内容”自定义属性**

要创建链接到给定范围内容的自定义属性，请调用 [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) 方法并传递属性名称和源。您可以使用 [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) 属性检查属性是否配置为链接到内容。此外，还可以使用 [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) 类的 [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) 属性获取源范围。

在示例中，我们使用一个简单的模板Microsoft Excel文件。工作簿中定义了一个名为 **MyRange** 的命名范围，它指向一个单元格值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **删除自定义属性**

要使用 Aspose.Cells 删除自定义属性，请调用 [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String) 方法并传递要删除的文档属性名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
