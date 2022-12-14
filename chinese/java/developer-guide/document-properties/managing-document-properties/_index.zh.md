---
title: 管理文档属性
type: docs
weight: 10
url: /zh/java/managing-document-properties/
---
## **介绍**

Microsoft Excel 提供了向电子表格文件添加属性的功能。这些文档属性提供了有用的信息，分为 2 个类别，详述如下。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称-值对的形式定义的自定义属性。

{{% alert color="primary" %}}

了解内置和自定义属性最重要的一点是内置属性可以访问和修改，但不能创建或删除，但是可以创建和管理自定义文档属性。

{{% /alert %}}

## **使用 Microsoft Excel 管理文档属性**

Microsoft Excel 允许以所见即所得的方式管理 Excel 文件的文档属性。请按照以下步骤打开**特性**Excel 2016 中的对话框。

1. 来自**文件**菜单，选择**信息**.

|**选择信息菜单**|
|:- |
|![待办事项：图片_替代_文本](managing-document-properties_1.png)|
1. 点击**特性**标题并选择“高级属性”。

|**单击高级属性选择**|
|:- |
|![待办事项：图片_替代_文本](managing-document-properties_2.png)|
1. 管理文件的文档属性。

|**属性对话框**|
|:- |
|![待办事项：图片_替代_文本](managing-document-properties_3.png)|
在 Properties 对话框中，有不同的选项卡，如 General、Summary、Statistics、Contents 和 Customs。每个选项卡都有助于配置与文件相关的不同类型的信息。自定义选项卡用于管理自定义属性。

## **使用 Aspose.Cells 处理文档属性**

开发人员可以使用 Aspose.Cells API 动态管理文档属性。此功能可帮助开发人员将有用的信息与文件一起存储，例如文件的接收、处理时间、时间戳等。

{{% alert color="primary" %}}

 Aspose.Cells for Java 直接在输出文件中写入API和Version Number的信息。例如，在将文档呈现为 PDF 时，Aspose.Cells for Java 会填充**应用**值为“Aspose.Cells”的字段和**PDF制作器**具有值的字段，例如“Aspose.Cells for Java v17.9”。

请注意，您不能指示 Aspose.Cells for Java 更改或从输出文档中删除此信息。

{{% /alert %}}

### **访问文档属性**

Aspose.Cells API 支持两种类型的文档属性，内置的和自定义的。 Aspose.Cells'[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类表示一个 Excel 文件，并且与 Excel 文件一样，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类可以包含多个工作表，每个工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类，而工作表的集合由[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)班级。

使用[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)访问文件的文档属性，如下所述。

- 要访问内置文档属性，请使用[**工作表集合.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- 要访问自定义文档属性，请使用[**工作表集合.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

这俩[**工作表集合.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)和[**工作表集合.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)返回一个实例[**文档属性集合**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection).这个集合包含[**文档属性**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)对象，每个对象代表一个内置或自定义的文档属性。

如何访问属性取决于应用程序要求，即；通过使用属性的索引或名称[**文档属性集合**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)如下例所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

这[**文档属性**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)类允许检索文档属性的名称、值和类型：

- 要获取属性名称，请使用[**文档属性.名称**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- 要获取属性值，请使用[**文档属性.值**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**文档属性.值**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)将值作为对象返回。
- 要获取属性类型，请使用[**文档属性.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) .这将返回其中一个[**财产种类**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)枚举值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **添加或删除自定义文档属性**

正如我们之前在本主题开头所述，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为它们是用户定义的。

### **添加自定义属性**

 Aspose.Cells API暴露了[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) 的方法[**自定义文档属性集合**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection)类以便将自定义属性添加到集合中。这[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) 方法将属性添加到 Excel 文件并返回新文档属性的引用作为[**文档属性**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)目的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **配置“内容链接”自定义属性**

要创建链接到给定范围内容的自定义属性，请调用[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) 方法并传递属性名称和来源。您可以使用[**文档属性.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent)财产。此外，还可以使用[**资源**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source)的财产[**文档属性**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)班级。

我们在示例中使用一个简单的模板 Microsoft Excel 文件。工作簿有一个定义的命名范围标记**我的范围**这是指单元格值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **删除自定义属性**

要使用 Aspose.Cells 删除自定义属性，请调用[**DocumentPropertyCollection.删除**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)方法并传递要删除的文档属性的名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
