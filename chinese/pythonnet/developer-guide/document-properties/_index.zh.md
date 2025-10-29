---
title: 管理文档属性
linktitle: 文档属性
type: docs
weight: 80
url: /zh/python-net/managing-document-properties/
description: 了解如何通过 Aspose.Cells for Python via .NET API 管理文档属性。
keywords: 如何在 C# 中管理文档属性，获取或设置文档属性，添加或删除文档属性，以及如何用 C# 插入或移除文档属性，使用 Aspose.Cells for Python via .NET API 访问文档属性。
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

开发者可以使用 Aspose.Cells for Python via .NET API 动态管理文档属性。这一功能帮助开发者在文件中存储有用信息，比如收到文件时间、处理时间、时间戳等。

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 直接在输出文件中写入 API 和版本信息。例如，将文档渲染为 PDF 时，Aspose.Cells for Python via .NET 会在“应用程序”字段填写 'Aspose.Cells'，在“PDF 生成器”字段填写如 'Aspose.Cells for Python via .NET v17.9'。

请注意，您不能指示 Aspose.Cells for Python via .NET 从输出文档中更改或删除这些信息。

{{% /alert %}}


### **如何添加或删除自定义文档属性**

正如我们在本主题开头所述的那样，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些是用户定义的。

### **如何添加自定义属性**

Aspose.Cells for Python via .NET API 提供了 [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) 方法用于 [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) 类，以向集合添加自定义属性。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) 方法将属性添加到 Excel 文件，并返回新文档属性的引用作为 [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty) 对象。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **高级主题**
- [在文档信息面板中可见的自定义属性](/cells/zh/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [设置内置文档属性的ScaleCrop和LinksUpToDate属性](/cells/zh/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [使用内置文档属性指定Excel文件的文档版本](/cells/zh/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [使用内置文档属性指定Excel文件的语言](/cells/zh/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

{{< app/cells/assistant language="python-net" >}}
