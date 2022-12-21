---
title: 自動フィルター データ
type: docs
weight: 120
url: /ja/net/auto-filter-data/
---
{{% alert color="primary" %}}

範囲内のデータを理解するには、多くの場合、順序付けされていないデータの列を見るよりも、データを並べ替えてフィルター処理する方が簡単です。並べ替えにより、データが昇順または降順で整理されるため、特定の値を見つけやすくなります。データをフィルタリングすると、特定の値のみを表示できます。たとえば、販売記録の特定のアイテムに焦点を当てるのに役立ちます。

Microsoft Excel のユーザーは、列に自動フィルターを適用できます。自動フィルター処理により、列の上部にメニューが追加され、そこから列データをフィルター処理できます。この機能は、VSTO または Aspose.Cells for .NET を通じて、Excel スプレッドシートを使用する開発者も利用できます。

{{% /alert %}}

## **データの自動フィルタリング**

列に自動フィルタリングを適用するには:

1. ワークブックを作成します。
1. ワークシートを取得します。
1. サンプルデータを追加します。
1. オートフィルターを適用します。
1. 列を自動調整して表示を魅力的にします。
1. スプレッドシートを保存します。

この記事のコード サンプルは、以下を使用してこれらの手順を実行する方法を示しています。[VSTO](/cells/ja/net/auto-filter-data/) C# または Visual Basic を使用するか、[Apose.Cells](/cells/ja/net/auto-filter-data/)、再び C# または Visual Basic を使用します。

### **VSTO によるデータの自動フィルタリング**

**C#**

{{< highlight "csharp" >}}

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

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

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

**VSTO で適用されるオートフィルター** 

![todo:画像_代替_文章](auto-filter-data_1.png)

### **Aspose.Cells for .NET によるデータの自動フィルタリング**

**C#**

{{< highlight "csharp" >}}

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

**Aspose.Cells for .NET でオートフィルター適用** 

![todo:画像_代替_文章](auto-filter-data_2.png)
