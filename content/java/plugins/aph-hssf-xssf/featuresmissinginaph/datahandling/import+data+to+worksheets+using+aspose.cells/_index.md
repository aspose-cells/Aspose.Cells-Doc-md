---
title : "Import Data to Worksheets using Aspose.Cells" 
description : "" 
weight : 20630 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/datahandling/import+data+to+worksheets+using+aspose.cells/
---

# Aspose.Cells for Java : Import Data to Worksheets using Aspose.Cells


## Aspose.Cells - Import Data to Worksheets

Import Data from Arrays

**Java**

{{< code lang="java" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Obtaining the reference of the newly added worksheet by passing its sheet index
int sheetIndex = workbook.getWorksheets().add();
Worksheet worksheet= workbook.getWorksheets().get(sheetIndex);

//==================================================
//Creating an array containing names as string values
String[] names = new String[]{"laurence chen", "roman korchagin", "kyle huang"};

//Importing the array of names to 1st row and first column vertically
Cells cells = worksheet.getCells();
cells.importArray(names,0,0,false);
{{< /code >}}

Import Data from ArrayList

**Java**

ArrayList<String> list = new ArrayList<String>();//Add few names to the list as string valueslist.add("laurence chen");list.add("roman korchagin");list.add("kyle huang");//Importing the contents of ArrayList to 1st row and first column verticallycells.importArrayList(list,2,0,true);//==================================================//Saving the Excel fileworkbook.save(dataDir + "AsposeDataImport.xls");

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ImportDataToWorksheets.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ImportDataToWorksheets.java)

For more details, visit [Importing Data to Worksheets](http://docs.aspose.com:8082/docs/display/cellsjava/Importing+Data+to+Worksheets).

