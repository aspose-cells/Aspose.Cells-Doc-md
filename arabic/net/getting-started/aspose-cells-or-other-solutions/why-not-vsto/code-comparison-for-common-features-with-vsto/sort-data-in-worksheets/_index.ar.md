---
title: فرز البيانات في أوراق العمل
type: docs
weight: 230
url: /ar/net/sort-data-in-worksheets/
---

أدناه مقارنة لأمثلة الرمز المصدري لـ VSTO و Aspose.Cells.
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
## **تحميل
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/SortDataInWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
