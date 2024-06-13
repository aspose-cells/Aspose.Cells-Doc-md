---
title: 管理文档属性
type: docs
weight: 10
url: /zh/java/managing-document-properties/
---

## **介绍**

Microsoft Excel提供了向电子表格文件添加属性的功能。这些文档属性提供有用信息，分为以下2类。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称-值对的形式定义的自定义属性。

{{% alert color="primary" %}}

关于内置和自定义属性最重要的一点是，可以访问和修改内置属性，但无法创建或移除，然而，可以创建和管理自定义文档属性。

{{% /alert %}}

## **使用Microsoft Excel管理文档属性**

Microsoft Excel允许以所见即所得的方式管理Excel文件的文档属性。请按以下步骤在Excel 2016中打开“属性”对话框。

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

## **使用Aspose.Cells管理文档属性**

开发人员可以使用Aspose.Cells API动态管理文档属性。此功能帮助开发人员存储有用信息，如文件接收时间、处理时间戳等。

{{% alert color="primary" %}}

Aspose.Cells for Java 直接在输出文档中写入有关 API 和版本号的信息。例如，当将文档呈现为 PDF 时，Aspose.Cells for Java 会将 **应用程序** 字段的值填充为 'Aspose.Cells'，**PDF 生产者** 字段的值为例如 'Aspose.Cells for Java v17.9'。

请注意，您无法指示 Aspose.Cells for Java 更改或删除输出文档中的此信息。

{{% /alert %}}

### **访问文档属性**

Aspose.Cells API支持内建和自定义文档属性。Aspose.Cells的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类代表Excel文件，类似于Excel文件，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类可以包含多个工作表，每个工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示，而工作表的集合由[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)类表示。

使用[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)如下访问文件的文档属性。

- 要访问内建文档属性，请使用[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)。
- 要访问自定义文档属性，请使用[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)。

[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)和[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)都返回[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)的实例。这个集合包含[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)对象，每个对象表示单个内置或自定义文档属性。

应用程序要求如何访问属性取决于;即通过从[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)中的索引或属性名称来访问属性，如下面的示例所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)类允许检索文档属性的名称、值和类型:

- 要获取属性名称，请使用[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name)。
- 要获取属性值，请使用[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)。[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) 将值作为对象返回。
- 要获取属性类型，请使用[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). 这将返回[**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)枚举值之一。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **添加或删除自定义文档属性**

正如我们在本主题开头所述的那样，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些是用户定义的。

### **添加自定义属性**

Aspose.Cells API已经为[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection)类公开了[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean))方法，以便向集合添加自定义属性。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean))方法为Excel文件添加属性并以[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)对象的形式返回新文档属性的引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **配置“链接到内容”自定义属性**

要创建与给定范围的内容链接的自定义属性，请调用[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String))方法并传递属性名称和来源。您可以使用[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent)属性检查属性是否配置为链接到内容。此外，还可以使用[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)类的[**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source)属性获取源范围。

我们在示例中使用了一个简单的模板Microsoft Excel文件。工作簿有一个命名范围标记为**MyRange**，它指向单元格值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **移除自定义属性**

要使用Aspose.Cells删除自定义属性，调用[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String))方法并传递要移除的文档属性的名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
