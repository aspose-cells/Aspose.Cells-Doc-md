---
title: Sort Data in Worksheets
type: docs
weight: 230
url: /net/sort-data-in-worksheets/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Below is the comparison code example for VSTO and Aspose.Cells.
## **VSTO**
{{< highlight csharp >}}

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

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

  Workbook myWorkbook = new Workbook(fileName);

 Worksheet mySheet = myWorkbook.Worksheets[myWorkbook.Worksheets.ActiveSheetIndex];

 DataSorter sorter = myWorkbook.DataSorter;

 sorter.Order1 = Aspose.Cells.SortOrder.Ascending;

 sorter.Key1 = 0;

 sorter.Sort(mySheet.Cells, 0, 0, 10, 0);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **Download
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/SortDataInWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
