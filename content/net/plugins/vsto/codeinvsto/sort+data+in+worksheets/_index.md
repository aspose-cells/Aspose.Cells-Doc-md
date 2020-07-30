---
title : "Sort Data in Worksheets" 
description : "" 
weight : 16811 
toc : false
type: docs
url: /net/plugins/vsto/codeinvsto/sort+data+in+worksheets/
---

# Aspose.Cells for .NET : Sort Data in Worksheets


Below is the comparison code example for VSTO and Aspose.Cells.

#### VSTO

{{< code lang="cs" >}}
  Excel.Workbook myWorkbook = this.Application.Workbooks.Open(fileName);
  Excel.Worksheet mySheet = myWorkbook.ActiveSheet;
  Excel.Range Colors = mySheet.get_Range("A1", "A10");
  Colors.Sort(
  Colors.Rows[1], Excel.XlSortOrder.xlAscending,
  Colors.Rows[2], missing, Excel.XlSortOrder.xlAscending,
  missing, Excel.XlSortOrder.xlAscending,
  Excel.XlYesNoGuess.xlNo, missing, missing,
  Excel.XlSortOrientation.xlSortColumns,
  Excel.XlSortMethod.xlPinYin,
  Excel.XlSortDataOption.xlSortNormal,
  Excel.XlSortDataOption.xlSortNormal,
  Excel.XlSortDataOption.xlSortNormal);
{{< /code >}}

#### Aspose.Cells

{{< code lang="cs" >}}
 Workbook myWorkbook = new Workbook(fileName);
 Worksheet mySheet = myWorkbook.Worksheets[myWorkbook.Worksheets.ActiveSheetIndex];
 DataSorter sorter = myWorkbook.DataSorter;
 sorter.Order1 = Aspose.Cells.SortOrder.Ascending;
 sorter.Key1 = 0;
 sorter.Sort(mySheet.Cells, 0, 0, 10, 0);
 myWorkbook.Save(fileName);
{{< /code >}}

#### Download

*   [CodePlex](https://asposevsto.codeplex.com/downloads/get/1459768)
*   [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/SortDataInWorksheets.Aspose.Cells.zip)

