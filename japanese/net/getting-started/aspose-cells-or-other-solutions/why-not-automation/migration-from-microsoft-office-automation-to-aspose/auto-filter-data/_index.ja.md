---
title: データの自動フィルタリング
type: docs
weight: 120
url: /ja/net/auto-filter-data/
---

{{% alert color="primary" %}}

範囲内のデータを理解するためには、データを並べ替えたりフィルタリングしたりする方が、順序なしのデータの列を見るよりも簡単です。並び替えは、昇順または降順でデータを整理して特定の値を見つけやすくします。データのフィルタリングでは、特定の値のみを表示できます。たとえば、販売レコードの中の特定のアイテムに焦点を当てるのに役立ちます。

Microsoft Excelのユーザーは、列に自動フィルタを適用することができます。自動フィルタは、列データを並べ替えまたはフィルタリングするためのメニューを列の上部に追加します。この機能は、VSTOまたはAspose.Cells for .NETを使用するExcelスプレッドシートを扱う開発者にも利用できます。

{{% /alert %}}

## **自動データフィルタリング**

列に自動フィルタリングを適用するには:

1. ワークブックを作成する。
1. ワークシートを取得する。
1. サンプルデータを追加します。
1. 自動フィルターを適用します。
1. 表示を魅力的にするために列を自動調整します。
1. スプレッドシートを保存します。

この記事のコードサンプルは、これらの手順を[C#またはVisual Basic](/cells/ja/net/auto-filter-data/)を使用してVSTOで実行する方法、または[C#またはVisual Basic](/cells/ja/net/auto-filter-data/)を使用してApose.Cellsで行う方法を示しています。

### **VSTOでデータの自動フィルタリング**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**VSTOで自動フィルタリングが適用されました** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Aspose.Cells for .NETでデータの自動フィルタリング**

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Aspose.Cells for .NETで自動フィルタリングが適用されました** 

![todo:image_alt_text](auto-filter-data_2.png)
