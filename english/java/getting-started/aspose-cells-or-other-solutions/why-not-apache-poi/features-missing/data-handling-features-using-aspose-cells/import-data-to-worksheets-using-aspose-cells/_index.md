---
title: Import Data to Worksheets using Aspose.Cells
type: docs
weight: 30
url: /java/import-data-to-worksheets-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Import Data to Worksheets**
Import Data from Arrays

**Java**

{{< highlight java >}}
 // Instantiating a Workbook object
 Workbook workbook = new Workbook();

 // Obtaining the reference of the newly added worksheet by passing its sheet index
 int sheetIndex = workbook.getWorksheets().add();
 Worksheet worksheet = workbook.getWorksheets().get(sheetIndex);

 // ==================================================

 // Creating an array containing names as string values
 String[] names = new String[]{"laurence chen", "roman korchagin", "kyle huang"};

 // Importing the array of names to the 1st row and first column vertically
 Cells cells = worksheet.getCells();
 cells.importArray(names, 0, 0, false);
{{< /highlight >}}

Import Data from ArrayList

**Java**

{{< highlight java >}}
 ArrayList<String> list = new ArrayList<String>();

 // Add a few names to the list as string values
 list.add("laurence chen");
 list.add("roman korchagin");
 list.add("kyle huang");

 // Importing the contents of the ArrayList to the 1st row and first column vertically
 cells.importArrayList(list, 2, 0, true);

 // ==================================================

 // Saving the Excel file
 workbook.save(dataDir + "AsposeDataImport.xls");
{{< /highlight >}}

## **Download Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ImportDataToWorksheets.java)
{{< app/cells/assistant language="java" >}}
