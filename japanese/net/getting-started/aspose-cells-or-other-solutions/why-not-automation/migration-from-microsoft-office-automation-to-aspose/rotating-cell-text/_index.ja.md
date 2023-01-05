---
title: 回転 Cell テキスト
type: docs
weight: 100
url: /ja/net/rotating-cell-text/
---
{{% alert color="primary" %}}

場合によっては、列ヘッダーが下のセルのデータよりもはるかに広いことがあります。これにより、ページに不要な空白が生じる可能性があります。解決策の 1 つは、テキストを垂直方向に回転させて、横方向のスペースを少なくすることです。 Microsoft Excel では文字の回転が簡単にできます。幸いなことに、プログラムでテキストを回転させることもできるため、開発者はアプリケーション内で作成したスプレッドシートでラベルを回転させることができます。

この記事では、を使用してセル内のテキストを回転する方法について説明します[Aspose.Cells for .NET](/cells/ja/net/rotating-cell-text/)で同じことをするのと比較して[VSTO](/cells/ja/net/rotating-cell-text/).

{{% /alert %}}

## **Cells のテキストの回転**

ワークシートのセル内のテキストを回転するには、次の手順を実行します。

1. ワークブックを作成し、ワークシートを取得します。
1. サンプル テキストを追加します。
1. テキストの書式設定: 回転、背景色の追加。
1. ファイルを保存します。

以下のコード サンプルは、最初にこれらの手順を実行する方法を示しています。[VSTO](/cells/ja/net/rotating-cell-text/) 、C# または Visual Basic を使用して、[Aspose.Cells](/cells/ja/net/rotating-cell-text/)、再び C# または Visual Basic を使用します。

この記事のコード例では、以下に示す出力が得られます。
**テキストが回転したセル。**

![todo:画像_代替_文章](rotating-cell-text_1.png)

### **VSTO を使用したテキストの回転**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2]= "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Aspose.Cells for .NET でテキストを回転させる**

**C#**

{{< highlight "csharp" >}}

 // Instantiate a new Workbook.
 
 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
