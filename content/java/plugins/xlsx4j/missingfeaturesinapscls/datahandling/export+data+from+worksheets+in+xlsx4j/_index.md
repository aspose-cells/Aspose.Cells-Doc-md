---
title : "Export Data from Worksheets in xlsx4j" 
description : "" 
weight : 20665 
toc : false
type: docs
url: /java/plugins/xlsx4j/missingfeaturesinapscls/datahandling/export+data+from+worksheets+in+xlsx4j/
---

# Aspose.Cells for Java : Export Data from Worksheets in xlsx4j


## Aspose.Cells - Export Data from Worksheets

Aspose.Cells not only lets its users import data to worksheets from external data sources but also allow them to export worksheet data to an array.

**Java**

{{< code lang="java" >}}
//Creating a file stream containing the Excel file to be opened
FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Instantiating a Workbook object
Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.getWorksheets().get(0);

//Exporting the contents of 7 rows and 2 columns starting from 1st cell to Array.
Object dataTable [][] = worksheet.getCells().exportArray(4,0,7,8);

for (int i = 0 ; i < dataTable.length ; i++)
{
	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));
}
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

For more details, visit [Exporting Data from Worksheets](http://docs.aspose.com:8082/docs/display/cellsjava/Exporting+Data+from+Worksheets).

