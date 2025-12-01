---
title: Manage Document Properties with Node.js via C++
linktitle: Document Properties
type: docs
weight: 80
url: /nodejs-cpp/managing-document-properties/
description: Learn how to Manage Document Properties through the Aspose.Cells for Node.js via C++ APIs.
keywords: How to Manage Document Properties in Node.js via C++, Get or Set Document Properties using Node.js via C++, Add or Delete Document Properties via Node.js via C++, Insert or Remove Document Properties with Node.js via C++, How to Access Document Properties using Aspose.Cells for Node.js via C++ APIs.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## **Introduction**

Microsoft Excel provides the ability to add properties to spreadsheet files. These document properties provide useful information and are divided into 2 categories as detailed below.

- System-defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
- User-defined (custom) properties: Custom properties defined by the end user in the form of name-value pair.

{{% alert color="primary" %}}

The most important point to know about built-in and custom properties is that built-in properties can be accessed and modified, but not created or removed. However, custom properties can be created and managed.

{{% /alert %}}

## **How to Manage Document Properties Using Microsoft Excel**

Microsoft Excel allows you to manage the document properties of the Excel files in a WYSIWYG manner. Please follow the below steps to open the **Properties** dialog in Excel 2016.

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

Developers can dynamically manage the document properties using the Aspose.Cells APIs. This feature helps the developers to store useful information along with the file, such as when the file was received, processed, time-stamped and so on.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for Node.js via C++ populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with the value, e.g 'Aspose.Cells v17.9'.

Please note that you cannot instruct Aspose.Cells for Node.js via C++ to change or remove this information from output Documents.

{{% /alert %}}

### **How to Access Document Properties**

Aspose.Cells APIs support both types of document properties, built-in and custom. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class represents an Excel file and, like an Excel file, the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class can contain multiple worksheets, each represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class whereas the collection of worksheets is represented by the [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) class.

Use the [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) to access the file's document properties as described below.

- To access built-in document properties, use [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- To access custom document properties, use [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Both the [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) and [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) return the instance of [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). This collection contains [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) objects, each of which represents a single built-in or custom document property.

It is up to the application requirement how to access a property, that is; by using the index or name of the property from the [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) as demonstrated in the example below.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

The [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) class allows to retrieve the name, value, and type of the document property:

- To get the property name, use [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- To get the property value, use [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) returns the value as an Object.
- To get the property type, use [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). This returns one of the [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/) enumeration values. After you get the property type, use one of the **DocumentProperty.ToXXX** methods to obtain the value of the appropriate type instead of using [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). The **DocumentProperty.ToXXX** methods are described in the table below.

{{% alert color="primary" %}}

The [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) class also provides a set of methods that return the values of other data types.

{{% /alert %}}

|**Member Name**|**Description**|**ToXXX Method**|
| :- | :- | :- |
|Boolean|The property data type is Boolean|ToBool|
|Date|The property data type is DateTime. Note that Microsoft Excel stores only <br>the date portion, no time can be stored in a custom property of this type|ToDateTime|
|Float|The property data type is Double|ToDouble|
|Number|The property data type is Int32|ToInt|
|String|The property data type is string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **How to Add or Remove Custom Document Properties**

As we have described earlier at the beginning of this topic, developers can't add or remove built-in properties because these properties are system-defined but it's possible to add or remove custom properties because these are user-defined.

### **How to Add Custom Properties**

Aspose.Cells APIs have exposed the [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) method for the [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) class in order to add custom properties to the collection. The [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) method adds the property to the Excel file and returns a reference for the new document property as an [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) object.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **How to Configure “Link to content” Custom Property**

To create a custom property linked to the content of a given range, call the [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) method and pass property name and source. You can check whether a property is configured as linked to content using the [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--) property. Moreover, it is also possible to get the source range using the [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) property of the [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **How to Remove Custom Properties**

To remove custom properties using Aspose.Cells, call the [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) method and pass the name of the document property to be removed.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Advance topics**
- [Adding Custom Properties visible inside Document Information Panel](/cells/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties](/cells/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specify Document Version of the Excel File using BuiltIn Document Properties](/cells/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specify the Language of the Excel File using BuiltIn Document Properties](/cells/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="nodejs-cpp" >}}
