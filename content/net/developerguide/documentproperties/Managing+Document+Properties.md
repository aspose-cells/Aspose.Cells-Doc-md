+++
title = "Managing Document Properties" 
description = "" 
weight = 12140 
+++

Aspose.Cells for .NET : Managing Document Properties  

# Aspose.Cells for .NET : Managing Document Properties



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#ManagingDocumentProperties-Introduction)
*   2 [Managing Document Properties Using Microsoft Excel](#ManagingDocumentProperties-ManagingDocumentPropertiesUsingMicrosoftExcel)
*   3 [Working with Document Properties Using Aspose.Cells](#ManagingDocumentProperties-WorkingwithDocumentPropertiesUsingAspose.Cells)
    *   3.1 [Accessing Document Properties](#ManagingDocumentProperties-AccessingDocumentProperties)
    *   3.2 [Adding or Removing Custom Document Properties](#ManagingDocumentProperties-AddingorRemovingCustomDocumentProperties)
    *   3.3 [Adding Custom Properties](#ManagingDocumentProperties-AddingCustomProperties)
    *   3.4 [Configuring “Link to content” Custom Property](#ManagingDocumentProperties-Configuring“Linktocontent”CustomProperty)
    *   3.5 [Removing Custom Properties](#ManagingDocumentProperties-RemovingCustomProperties)
{{< /panel >}}
## Introduction

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

*   System-defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
*   User-defined (custom) properties: Custom properties defined by the end user in the form of name-value pair.

The most important point to know about built-in and custom properties is that built-in properties can be accessed and modified, but not created or removed. However, custom properties can be created and managed.

## Managing Document Properties Using Microsoft Excel

Microsoft Excel allows you to manage the document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

1.  From the **File** menu, select **Info**.
    
{{< table style="table-striped" >}}
|Selecting Info Menu|
|:----|
|        ![](https://docs2.aspose.com/cells/net/attachments/22546332/22773812.png)    2.  Click on **Properties** heading and select "Advanced Properties".        **Clicking Advanced Properties Selection**        ![](https://docs2.aspose.com/cells/net/attachments/22546332/22773813.png)    3.  Manage the file's document properties.        **Properties Dialog**        ![](https://docs2.aspose.com/cells/net/attachments/22546332/22773814.png)    |
{{< /table >}}

In the Properties dialog, there are different tabs, like General, Summary, Statistics, Contents, and Customs. Each tab helps configure different kinds of information related to the file. The Custom tab is used to manage custom properties.

## Working with Document Properties Using Aspose.Cells

Developers can dynamically manage the document properties using the Aspose.Cells APIs. This feature helps the developers to store useful information along with the file, such as when the file was received, processed, time-stamped and so on.

Aspose.Cells for .NET directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for .NET populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with the value, e.g 'Aspose.Cells v17.9'.

Please note that you cannot instruct Aspose.Cells for .NET to change or remove this information from output Documents.

### Accessing Document Properties

Aspose.Cells APIs support both types of document properties, built-in and custom. Aspose.Cells' [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class represents an Excel file and, like an Excel file, the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class can contain multiple worksheets, each represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class whereas the collection of worksheets is represented by the [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) class.

Use the [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) to access the file's document properties as described below.

*   To access built-in document properties, use [WorksheetCollection.BuiltInDocumentProperties](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
*   To access custom document properties, use [WorksheetCollection.CustomDocumentProperties](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Both the [WorksheetCollection.BuiltInDocumentProperties](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/properties/builtindocumentproperties) and [WorksheetCollection.CustomDocumentProperties](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/properties/customdocumentproperties) return the instance of [Aspose.Cells.Properties.DocumentPropertyCollection](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentpropertycollection). This collection contains [Aspose.Cells.Properties.DocumentProperty](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty) objects, each of which represents a single built-in or custom document property.

It is up to the application requirement how to access a property, that is; by using the index or name of the property from the [DocumentPropertyCollection](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentpropertycollection) as demonstrated in the example below.

  
The [Aspose.Cells.Properties.DocumentProperty](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty) class allows to retrieve the name, value, and type of the document property:

*   To get the property name, use [DocumentProperty.Name](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/name).
*   To get the property value, use [DocumentProperty.Value](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/value). [DocumentProperty.Value](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/value) returns the value as an Object.
*   To get the property type, use [DocumentProperty.Type](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/type). This returns one of the [PropertyType](https://apireference.aspose.com/net/cells/aspose.cells.properties/propertytype) enumeration values. After you get the property type, use one of the **DocumentProperty.ToXXX** methods to obtain the value of the appropriate type instead of using [DocumentProperty.Value](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/value). The **DocumentProperty.ToXXX** methods are described in the table below.

The [DocumentProperty](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty) class also provides a set of methods that return the values of other data types.

{{< table style="table-striped" >}}
|Member Name|Description|ToXXX Method|
|:----|:----|:----|
|Boolean|The property data type is Boolean|ToBool|
|Date|The property data type is DateTime. Note that Microsoft Excel stores only the date portion, no time can be stored in a custom property of this type|ToDateTime|
|Float|The property data type is Double|ToDouble|
|Number|The property data type is Int32|ToInt|
|String|The property data type is String|ToString
{{< /table >}}

### Adding or Removing Custom Document Properties

As we have described earlier at the beginning of this topic, developers can't add or remove built-in properties because these properties are system-defined but it's possible to add or remove custom properties because these are user-defined.

### Adding Custom Properties

Aspose.Cells APIs have exposed the [Add](https://apireference.aspose.com/net/cells/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) method for the [CustomDocumentPropertyCollection](https://apireference.aspose.com/net/cells/aspose.cells.properties/customdocumentpropertycollection) class in order to add custom properties to the collection. The [Add](https://apireference.aspose.com/net/cells/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) method adds the property to the Excel file and returns a reference for the new document property as an [Aspose.Cells.Properties.DocumentProperty](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty) object.

### Configuring “Link to content” Custom Property

To create a custom property linked to the content of a given range, call the [CustomDocumentPropertyCollection.AddLinkToContent](https://apireference.aspose.com/net/cells/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) method and pass property name and source. You can check whether a property is configured as linked to content using the [DocumentProperty.IsLinkedToContent](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/islinkedtocontent) property. Moreover, it is also possible to get the source range using the [Source](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty/properties/source) property of the [DocumentProperty](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentproperty) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

### Removing Custom Properties

To remove custom properties using Aspose.Cells, call the [DocumentPropertyCollection.Remove](https://apireference.aspose.com/net/cells/aspose.cells.properties/documentpropertycollection/methods/remove) method and pass the name of the document property to be removed.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [File-Info.png](https://docs2.aspose.com/cells/net/attachments/22546332/22773812.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [PropertiesDialog.png](https://docs2.aspose.com/cells/net/attachments/22546332/22773814.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Properties-AdvancedProperties.png](https://docs2.aspose.com/cells/net/attachments/22546332/22773813.png) (image/png)  

