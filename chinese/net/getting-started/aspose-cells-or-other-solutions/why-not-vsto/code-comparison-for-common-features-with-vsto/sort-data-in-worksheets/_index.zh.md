---
title: 对工作表中的数据进行排序
type: docs
weight: 230
url: /zh/net/sort-data-in-worksheets/
---

以下是VSTO和Aspose.Cells的比较代码示例。
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
## **下载
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/SortDataInWorksheets.Aspose.Cells.zip)
