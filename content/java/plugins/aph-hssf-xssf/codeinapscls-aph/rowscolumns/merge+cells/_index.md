---
title : "Merge Cells" 
description : "" 
weight : 20611 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/codeinapscls-aph/rowscolumns/merge+cells/
---

# Aspose.Cells for Java : Merge Cells


## Aspose.Cells - Merge Cells

The `Cells` class has some useful methods for the task. For example, the `merge` method merges the cells into a single cell within a specified range of the cells.

**Java**

{{< code lang="java" >}}
//Create a Workbook.
Workbook wbk = new Workbook();

//Create a Worksheet and get the first sheet.
Worksheet worksheet = wbk.getWorksheets().get(0);

//Create a Cells object to fetch all the cells.
Cells cells = worksheet.getCells();

//Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5,2,2,3);

//Input data into C6 Cell.
worksheet.getCells().get(5,2).setValue("This is a test of merging");

//Save the Workbook.
wbk.save(dataDir + "merge_Aspose.xls");
{{< /code >}}

## Apache POI SS - HSSF XSSF - Merge Cells

`Sheet.addMergedRegion` can be used to Merge Cells.

**Java**

{{< code lang="java" >}}
Workbook wb = new HSSFWorkbook();
Sheet sheet = wb.createSheet("new sheet");

Row row = sheet.createRow((short) 1);
Cell cell = row.createCell((short) 1);
cell.setCellValue("This is a test of merging");

sheet.addMergedRegion(new CellRangeAddress(
        1, //first row (0-based)
        1, //last row  (0-based)
        1, //first column (0-based)
        2  //last column  (0-based)
));
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/mergecells/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/mergecells)

For more details, visit [Merging and Unmerging (Splitting) Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Merging+and+Unmerging+%28Splitting%29+Cells).

