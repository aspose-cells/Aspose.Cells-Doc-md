---
title: Managing Document Properties
type: docs
weight: 30
url: /cpp/managing-document-properties/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenario**
Aspose.Cells allows you to work with built-in and custom document properties. Here is the Microsoft Excel interface for opening these document properties. Just click on **Advanced Properties** as shown in this screenshot to view them.

![todo:image_alt_text](managing-document-properties_1.png)

## **Managing Document Properties**
The following sample code loads the [sample Excel file](23166989.xlsx) and reads the built-in document properties, e.g., *Title* and *Subject*, and then changes them. It also reads the custom document property, i.e., *MyCustom1*, and then adds a new custom document property, i.e., *MyCustom5*, and writes the [output Excel file](23166986.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file.

![todo:image_alt_text](managing-document-properties_2.png)

### **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}

### **Console Output**
This is the console output of the above sample code when executed with the provided [sample Excel file](23166989.xlsx).

{{< highlight java >}}
Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.
{{< /highlight >}}

## **How to Access Document Properties**

Aspose.Cells APIs support both types of document properties, built-in and custom. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class represents an Excel file and, like an Excel file, the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) class can contain multiple worksheets, each represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet) class, whereas the collection of worksheets is represented by the [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) class.

Use the [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) to access the file's document properties as described below.

- To access built-in document properties, use [**WorksheetCollection::GetBuiltInDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getbuiltindocumentproperties/).
- To access custom document properties, use [**WorksheetCollection::GetCustomDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getcustomdocumentproperties/).

Both the [**WorksheetCollection::GetBuiltInDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getbuiltindocumentproperties/) and [**WorksheetCollection::GetCustomDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getcustomdocumentproperties/) return an instance of [**Aspose::Cells::Properties::DocumentPropertyCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentpropertycollection). This collection contains [**Aspose::Cells::Properties::DocumentProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty) objects, each of which represents a single built-in or custom document property.

It is up to the application requirement how to access a property, that is, by using the index or name of the property from the [**DocumentPropertyCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentpropertycollection) as demonstrated in the example below.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cpp" >}}

The [**Aspose::Cells::Properties::DocumentProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty) class allows you to retrieve the name, value, and type of the document property:

- To get the property name, use [**DocumentProperty::GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/getname).
- To get the property value, use [**DocumentProperty::GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/getvalue). [**DocumentProperty::GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/getvalue) returns the value as an object.
- To get the property type, use [**DocumentProperty::GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/gettype). This returns one of the [**PropertyType**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/propertytype) enumeration values. After you get the property type, use one of the **DocumentProperty.ToXXX** methods to obtain the value of the appropriate type instead of using [**DocumentProperty::GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/getvalue). The **DocumentProperty.ToXXX** methods are described in the table below.

{{% alert color="primary" %}}

The [**DocumentProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty) class also provides a set of methods that return the values of other data types.

{{% /alert %}}

|**Member Name**|**Description**|**ToXXX Method**|
| :- | :- | :- |
|Boolean|The property data type is Boolean|ToBool|
|Date|The property data type is DateTime. Note that Microsoft Excel stores only <br>the date portion; no time can be stored in a custom property of this type|ToDateTime|
|Float|The property data type is Double|ToDouble|
|Number|The property data type is Int32|ToInt|
|String|The property data type is String|ToString|

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cpp" >}}

## **How to Add or Remove Custom Document Properties**

As we described earlier, developers can't add or remove built-in properties because these properties are system-defined, but it is possible to add or remove custom properties because these are user‑defined.

## **How to Add Custom Properties**

Aspose.Cells APIs expose the [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/customdocumentpropertycollection/add/) method for the [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/customdocumentpropertycollection) class in order to add custom properties to the collection. The [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/customdocumentpropertycollection/add/) method adds the property to the Excel file and returns a reference for the new document property as an [**Aspose::Cells::Properties::DocumentProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty) object.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cpp" >}}

## **How to Configure “Link to content” Custom Property**

To create a custom property linked to the content of a given range, call the [**CustomDocumentPropertyCollection::AddLinkToContent**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/customdocumentpropertycollection/addlinktocontent/) method and pass the property name and source. You can check whether a property is configured as linked to content using the [**DocumentProperty::IsLinkedToContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/islinkedtocontent) property. Moreover, it is also possible to get the source range using the [**DocumentProperty::GetSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty/getsource) property of the [**DocumentProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentproperty) class.

We use a simple template Microsoft Excel file in the example. The workbook has a defined named range labeled **MyRange** which refers to a cell value.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cpp" >}}

## **How to Remove Custom Properties**

To remove custom properties using Aspose.Cells, call the [**DocumentPropertyCollection::Remove**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/documentpropertycollection/remove) method and pass the name of the document property to be removed.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
