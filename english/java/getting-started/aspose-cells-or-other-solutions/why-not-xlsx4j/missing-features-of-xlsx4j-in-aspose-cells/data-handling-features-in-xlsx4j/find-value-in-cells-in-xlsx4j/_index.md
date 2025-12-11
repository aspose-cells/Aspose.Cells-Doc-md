---
title: Find Value in Cells in xlsx4j
type: docs
weight: 30
url: /java/find-value-in-cells-in-xlsx4j/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Find Value in Cells**
In Microsoft Excel, users can search for cells that contain specific data. For example, clicking **Edit** and then **Find** opens the Search dialog. The user enters a value and clicks **OK** to search for it. Excel highlights matching fields.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object
Workbook workbook = new Workbook("workbook.xls");

// Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.getWorksheets().get(0);

// Accessing the cells collection
Cells cells = worksheet.getCells();

// Instantiating FindOptions
FindOptions findOptions = new FindOptions();

// Finding the cell containing a string value that starts with "Or"
findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH", null, findOptions);

// Printing the name of the cell found after searching the worksheet
System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 
For more details, visit [Find or Search Data](/cells/java/find-or-search-data).
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
