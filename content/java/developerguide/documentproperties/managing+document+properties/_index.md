---
title : "Managing Document Properties" 
description : "" 
weight : 12123 
toc : false
type: docs
url: /java/developerguide/documentproperties/managing+document+properties/
---

# Aspose.Cells for Java : Managing Document Properties


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Managing Document Properties Using Microsoft Excel](#managing-document-properties-using-microsoft-excel)
*   3 [Working with Document Properties Using Aspose.Cells](#working-with-document-properties-using-aspose.cells)
    *   3.1 [Accessing Document Properties](#accessing-document-properties)
    *   3.2 [Adding or Removing Custom Document Properties](#adding-or-removing-custom-document-properties)
    *   3.3 [Adding Custom Properties](#adding-custom-properties)
    *   3.4 [Configuring “Link to content” Custom Property](#configuring-“link-to-content”-custom-property)
    *   3.5 [Removing Custom Properties](#removing-custom-properties)
{{< /panel >}}
## Introduction

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

*   System-defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
*   User-defined (custom) properties: Custom properties defined by the end user in the form of name-value pair.

The most important point to know about built-in and custom properties is that built-in properties can be accessed and modified, but cannot be created or removed, however, custom document properties can be created and managed.

## Managing Document Properties Using Microsoft Excel

Microsoft Excel allows managing document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

1.  From the **File** menu, select **Info**.
    
{{< table style="table-striped" >}}
|Selecting Info Menu|
|:----|
|        ![image](https://docs2.aspose.com/cells/java/attachments/22546336/22773815.png)    2.  Click on **Properties** heading and select "Advanced Properties".        **Clicking Advanced Properties Selection**        ![image](https://docs2.aspose.com/cells/java/attachments/22546336/22773816.png)    3.  Manage the file's document properties.        **Properties Dialog**        ![image](https://docs2.aspose.com/cells/java/attachments/22546336/22773817.png)    |
{{< /table >}}

In the Properties dialog, there are different tabs, like General, Summary, Statistics, Contents, and Customs. Each tab helps configure different kinds of information related to the file. The Custom tab is used to manage custom properties.

## Working with Document Properties Using Aspose.Cells

Developers can dynamically manage the document properties using the Aspose.Cells APIs. This feature helps the developers to store useful information along with the file, such as when the file was received, processed, time-stamped and so on.

Aspose.Cells for Java directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for Java populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with the value, e.g 'Aspose.Cells for Java v17.9'.

Please note that you cannot instruct Aspose.Cells for Java to change or remove this information from output Documents.

### Accessing Document Properties

Aspose.Cells APIs support both types of document properties, built-in and custom. Aspose.Cells' [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class represents an Excel file and, like an Excel file, the [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class can contain multiple worksheets, each represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class whereas the collection of worksheets is represented by the [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) class.

Use the [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) to access the file's document properties as described below.

*   To access built-in document properties, use [WorksheetCollection.BuiltInDocumentProperties](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
*   To access custom document properties, use the [WorksheetCollection.CustomDocumentProperties](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Both the [WorksheetCollection.BuiltInDocumentProperties](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) and [WorksheetCollection.CustomDocumentProperties](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#CustomDocumentProperties) return an instance of [DocumentPropertyCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentPropertyCollection). This collection contains [DocumentProperty](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentProperty) objects, each of which represents a single built-in or custom document property.

It is up to the application requirement how to access a property, that is; by using the index or name of the property from the [DocumentPropertyCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentPropertyCollection) as demonstrated in the example below.

  
The [DocumentProperty](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentProperty) class allows to retrieve the name, value, and type of the document property:

*   To get the property name, use [DocumentProperty.Name](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#Name).
*   To get the property value, use [DocumentProperty.Value](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#Value). [DocumentProperty.Value](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#Value) returns the value as an Object.
*   To get the property type, use [DocumentProperty.Type](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#Type). This returns one of the [PropertyType](https://apireference.aspose.com/java/cells/com.aspose.cells/PropertyType) enumeration values.

### Adding or Removing Custom Document Properties

As we have described earlier at the beginning of this topic, developers can't add or remove built-in properties because these properties are system-defined but it's possible to add or remove custom properties because these are user-defined.

### Adding Custom Properties

Aspose.Cells APIs have exposed the [add](https://apireference.aspose.com/java/cells/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) method for the [CustomDocumentPropertyCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/CustomDocumentPropertyCollection) class in order to add custom properties to the collection. The [add](https://apireference.aspose.com/java/cells/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) method adds the property to the Excel file and returns a reference for the new document property as a [DocumentProperty](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentProperty) object.

### Configuring “Link to content” Custom Property

To create a custom property linked to the content of a given range, call the [CustomDocumentPropertyCollection.addLinkToContent](https://apireference.aspose.com/java/cells/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) method and pass property name and source. You can check whether a property is configured as linked to content using the [DocumentProperty.isLinkedToContent](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#IsLinkedToContent) property. Moreover, it is also possible to get the source range using the [Source](https://apireference.aspose.com/java/cells/com.aspose.cells/documentproperty#Source) property of the [DocumentProperty](https://apireference.aspose.com/java/cells/com.aspose.cells/DocumentProperty) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

### Removing Custom Properties

To remove custom properties using Aspose.Cells, call the [DocumentPropertyCollection.remove](https://apireference.aspose.com/java/cells/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) method and pass the name of the document property to be removed.

