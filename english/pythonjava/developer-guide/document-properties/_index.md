---
title: Manage Document Properties
linktitle: Document Properties
type: docs
weight: 80
url: /python-java/managing-document-properties/
description: Learn how to manage document properties through the Aspose.Cells for Python via Java APIs.
keywords: How to Manage Document Properties in Python via Java, Get or Set Document Properties using Python via Java, Add or Delete Document Properties via Python via Java, Insert or Remove Document Properties with Python via Java, How to Access Document Properties using Aspose.Cells for Python via Java APIs.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

- System-defined (built‐in) properties: Built‐in properties contain general information about the document like document title, author name, document statistics and so on.
- User-defined (custom) properties: Custom properties defined by the end user in the form of name‐value pairs.

{{% alert color="primary" %}}

The most important point to know about built‐in and custom properties is that built‐in properties can be accessed and modified, but not created or removed. However, custom properties can be created and managed.

{{% /alert %}}

## **How to Manage Document Properties Using Microsoft Excel**

Microsoft Excel allows you to manage the document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

1. From the **File** menu, select **Info**.

|**Selecting Info Menu**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
2. Click on **Properties** heading and select "Advanced Properties".

|**Clicking Advanced Properties Selection**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
3. Manage the file's document properties.

|**Properties Dialog**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|

In the Properties dialog, there are different tabs, like General, Summary, Statistics, Contents, and Custom. Each tab helps configure different kinds of information related to the file. The Custom tab is used to manage custom properties.

## **How to Work with Document Properties Using Aspose.Cells**

Developers can dynamically manage the document properties using the Aspose.Cells APIs. This feature helps developers to store useful information along with the file, such as when the file was received, processed, time‐stamped, and so on.

{{% alert color="primary" %}}

Aspose.Cells for Python via Java directly writes the information about API and version number in output documents. For example, upon rendering the document to PDF, Aspose.Cells for Python via Java populates **Application** field with the value 'Aspose.Cells' and **PDF Producer** field with the value, e.g., 'Aspose.Cells v17.9'.

Please note that you cannot instruct Aspose.Cells for Python via Java to change or remove this information from output documents.

{{% /alert %}}

### **How to Access Document Properties**

Aspose.Cells APIs support both types of document properties, built‐in and custom. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook) class represents an Excel file and, like an Excel file, the [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook) class can contain multiple worksheets, each represented by the [**Worksheet**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet) class, whereas the collection of worksheets is represented by the [**WorksheetCollection**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection) class.

Use the [**WorksheetCollection**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection) to access the file's document properties as described below.

- To access built‐in document properties, use [**WorksheetCollection.getBuiltInDocumentProperties**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection#BuiltInDocumentProperties).
- To access custom document properties, use [**WorksheetCollection.getCustomDocumentProperties**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection#CustomDocumentProperties).

Both the [**WorksheetCollection.getBuiltInDocumentProperties**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection#BuiltInDocumentProperties) and [**WorksheetCollection.getCustomDocumentProperties**](https://reference.aspose.com/cells/python-java/asposecells.api/worksheetcollection#CustomDocumentProperties) return an instance of [**.DocumentPropertyCollection**](https://reference.aspose.com/cells/python-java/asposecells.api/documentpropertycollection). This collection contains [**.DocumentProperty**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty) objects, each of which represents a single built‐in or custom document property.

It is up to the application requirement how to access a property, that is, by using the index or name of the property from the [**DocumentPropertyCollection**](https://reference.aspose.com/cells/python-java/asposecells.api/documentpropertycollection) as demonstrated in the example below.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-Files-Utility-AccessingDocumentProperties.py" >}}

The [**.DocumentProperty**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty) class allows you to retrieve the name, value, and type of the document property:

- To get the property name, use [**DocumentProperty.getName**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Name).
- To get the property value, use [**DocumentProperty.getValue**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Value). [**DocumentProperty.getValue**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Value) returns the value as an object.
- To get the property type, use [**DocumentProperty.getType**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Type). This returns one of the [**PropertyType**](https://reference.aspose.com/cells/python-java/asposecells.api/propertytype) enumeration values. After you get the property type, use one of the **DocumentProperty.ToXXX** methods to obtain the value of the appropriate type instead of using [**DocumentProperty.getValue**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Value). The **DocumentProperty.ToXXX** methods are described in the table below.

{{% alert color="primary" %}}

The [**DocumentProperty**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty) class also provides a set of methods that return the values of other data types.

{{% /alert %}}

|**Member Name**|**Description**|**ToXXX Method**|
| :- | :- | :- |
|Boolean|The property data type is Boolean|ToBool|
|Date|The property data type is DateTime. Note that Microsoft Excel stores only <br>the date portion; no time can be stored in a custom property of this type|ToDateTime|
|Float|The property data type is Double|ToDouble|
|Number|The property data type is Int32|ToInt|
|String|The property data type is String|ToString|

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-Files-Utility-AccessingValueOfDocumentProperties.py" >}}

### **How to Add or Remove Custom Document Properties**

As we described earlier, developers can't add or remove built‐in properties because these properties are system‐defined, but it is possible to add or remove custom properties because these are user‐defined.

### **How to Add Custom Properties**

Aspose.Cells APIs expose the [**add**](https://reference.aspose.com/cells/python-java/asposecells.api/customdocumentpropertycollection#add(java.lang.String,%20java.lang.String)) method for the [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-java/asposecells.api/customdocumentpropertycollection) class in order to add custom properties to the collection. The [**add**](https://reference.aspose.com/cells/python-java/asposecells.api/customdocumentpropertycollection#add(java.lang.String,%20java.lang.String)) method adds the property to the Excel file and returns a reference for the new document property as an [**DocumentProperty**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty) object.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-Files-Utility-AddingDocumentProperties.py" >}}

### **How to Configure “Link to content” Custom Property**

To create a custom property linked to the content of a given range, call the [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/python-java/asposecells.api/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) method and pass the property name and source. You can check whether a property is configured as linked to content using the [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#IsLinkedToContent) property. Moreover, it is also possible to get the source range using the [**getSource**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty#Source) property of the [**DocumentProperty**](https://reference.aspose.com/cells/python-java/asposecells.api/documentproperty) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-Files-Utility-ConfigureLinktoContentDocumentProperty.py" >}}

### **How to Remove Custom Properties**

To remove custom properties using Aspose.Cells, call the [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/python-java/asposecells.api/customdocumentpropertycollection#remove(java.lang.String)) method and pass the name of the document property to be removed.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-Files-Utility-RemovingCustomProperties.py" >}}
<!--
## **Advanced topics**
- [Adding Custom Properties visible inside Document Information Panel](/cells/python-java/adding-custom-properties-visible-inside-document-information-panel/)
- [Setting ScaleCrop and LinksUpToDate properties of Built‐In Document Properties](/cells/python-java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specify Document Version of the Excel File using Built‐In Document Properties](/cells/python-java/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specify the Language of the Excel File using Built‐In Document Properties](/cells/python-java/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="csharp" >}}-->