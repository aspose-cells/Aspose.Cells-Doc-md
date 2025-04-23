---
title: セルテキストの回転
type: docs
weight: 100
url: /ja/net/rotating-cell-text/
---

{{% alert color="primary" %}}

時には、列の見出しはセルのデータよりもはるかに幅広いです。これによりページ上に不必要な余白が生じます。このような場合、テキストを垂直に回転させて水平スペースを節約することができます。Microsoft Excel では、テキストの回転は簡単です。幸いなことに、開発者は自分のアプリケーション内でプログラム上でテキストを回転させることも可能です。

この記事では、[Aspose.Cells for .NET](/cells/ja/net/rotating-cell-text/)を使用したセル内のテキストの回転方法と[VSTO](/cells/ja/net/rotating-cell-text/)を使用した同様の方法の比較を行います。

{{% /alert %}}

## **セル内のテキストの回転**

ワークシートのセルでテキストを回転させるには、次の手順を実行します：

1. ワークブックを作成し、ワークシートを取得します。
1. サンプルテキストを追加します。
1. テキストを書式設定します：回転、背景色を追加します。
1. ファイルを保存します。

本文に続くコードサンプルでは、最初に[VSTO](/cells/ja/net/rotating-cell-text/)を使用してこれらの手順を実行する方法(C# または Visual Basic を使用)を示し、次に [Aspose.Cells](/cells/ja/net/rotating-cell-text/)を使用してこれらの手順を実行する方法(C# または Visual Basic を使用)を示します。

この記事のコード例では、以下に示す出力を生成します。
**回転したテキストを持つセル。**

![todo:image_alt_text](rotating-cell-text_1.png)

### **VSTOを使用したテキストの回転**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 2] = "Aspose Heading";

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

#### **Aspose.Cells for .NETを使用したテキストの回転**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
