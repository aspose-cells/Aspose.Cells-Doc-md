---
title: Manage Document Properties
linktitle: Document Properties
type: docs
weight: 80
url: /python-net/managing-document-properties/
description: Learn how to Manage Document Properties through the Aspose.Cells for Python via .NET APIs.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for Python via .NET APIs.
---


## **Introduction**

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

- System-defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
- User-defined (custom) properties: Custom properties defined by the end user in the form of name-value pair.

{{% alert color="primary" %}}

The most important point to know about built-in and custom properties is that built-in properties can be accessed and modified, but not created or removed. However, custom properties can be created and managed.

{{% /alert %}}

## **How to Manage Document Properties Using Microsoft Excel**

Microsoft Excel allows you to manage the document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

1. From the **File** menu, select **Info**.

|**Selecting Info Menu**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Click on **Properties** heading and select "Advanced Properties".

|**Clicking Advanced Properties Selection**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Manage the file's document properties.

|**Properties Dialog**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
In the Properties dialog, there are different tabs, like General, Summary, Statistics, Contents, and Customs. Each tab helps configure different kinds of information related to the file. The Custom tab is used to manage custom properties.

## **How to Work with Document Properties Using Aspose.Cells**

Developers can dynamically manage the document properties using the Aspose.Cells for Python via .NET APIs. This feature helps the developers to store useful information along with the file, such as when the file was received, processed, time-stamped and so on.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for Python via .NET populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with the value, e.g 'Aspose.Cells for Python via .NET v17.9'.

Please note that you cannot instruct Aspose.Cells for Python via .NET to change or remove this information from output Documents.

{{% /alert %}}


### **How to Add or Remove Custom Document Properties**

As we have described earlier at the beginning of this topic, developers can't add or remove built-in properties because these properties are system-defined but it's possible to add or remove custom properties because these are user-defined.

### **How to Add Custom Properties**

Aspose.Cells for Python via .NET APIs have exposed the [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) method for the [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) class in order to add custom properties to the collection. The [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) method adds the property to the Excel file and returns a reference for the new document property as an [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty) object.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Advance topics**
- [Adding Custom Properties visible inside Document Information Panel](/cells/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties](/cells/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specify Document Version of the Excel File using BuiltIn Document Properties](/cells/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specify the Language of the Excel File using BuiltIn Document Properties](/cells/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

