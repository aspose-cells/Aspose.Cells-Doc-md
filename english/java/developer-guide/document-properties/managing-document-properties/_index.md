---
title: Managing Document Properties
type: docs
weight: 10
url: /java/managing-document-properties/
---

## **Introduction**

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

- System-defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
- User-defined (custom) properties: Custom properties defined by the end user in the form of name-value pair.

{{% alert color="primary" %}}

The most important point to know about built-in and custom properties is that built-in properties can be accessed and modified, but cannot be created or removed, however, custom document properties can be created and managed.

{{% /alert %}}

## **Managing Document Properties Using Microsoft Excel**

Microsoft Excel allows managing document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

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

## **Working with Document Properties Using Aspose.Cells**

Developers can dynamically manage the document properties using the Aspose.Cells APIs. This feature helps the developers to store useful information along with the file, such as when the file was received, processed, time-stamped and so on.

{{% alert color="primary" %}}

Aspose.Cells for Java directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for Java populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with the value, e.g 'Aspose.Cells for Java v17.9'.

Please note that you cannot instruct Aspose.Cells for Java to change or remove this information from output Documents.

{{% /alert %}}

### **Accessing Document Properties**

Aspose.Cells APIs support both types of document properties, built-in and custom. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class represents an Excel file and, like an Excel file, the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class can contain multiple worksheets, each represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class whereas the collection of worksheets is represented by the [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) class.

Use the [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) to access the file's document properties as described below.

- To access built-in document properties, use [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- To access custom document properties, use the [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Both the [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) and [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) return an instance of [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). This collection contains [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) objects, each of which represents a single built-in or custom document property.

It is up to the application requirement how to access a property, that is; by using the index or name of the property from the [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) as demonstrated in the example below.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

The [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) class allows to retrieve the name, value, and type of the document property:

- To get the property name, use [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- To get the property value, use [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) returns the value as an Object.
- To get the property type, use [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). This returns one of the [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType) enumeration values.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Adding or Removing Custom Document Properties**

As we have described earlier at the beginning of this topic, developers can't add or remove built-in properties because these properties are system-defined but it's possible to add or remove custom properties because these are user-defined.

### **Adding Custom Properties**

Aspose.Cells APIs have exposed the [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) method for the [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) class in order to add custom properties to the collection. The [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) method adds the property to the Excel file and returns a reference for the new document property as a [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) object.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configuring “Link to content” Custom Property**

To create a custom property linked to the content of a given range, call the [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent-java.lang.String-java.lang.String-) method and pass property name and source. You can check whether a property is configured as linked to content using the [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) property. Moreover, it is also possible to get the source range using the [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) property of the [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Removing Custom Properties**

To remove custom properties using Aspose.Cells, call the [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove-java.lang.String-) method and pass the name of the document property to be removed.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
{{< app/cells/assistant language="java" >}}