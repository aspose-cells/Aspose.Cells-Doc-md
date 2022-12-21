---
title: ワークブックに新しいワークシートを追加し、VSTO および Aspose.Cells でシートをアクティブ化する
type: docs
weight: 30
url: /ja/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **移行のヒント:**
1. 新しいワークシートを既存の Microsoft Excel ファイルに追加します。
1. 新しい各ワークシートのセルにデータを入力します。
1. ワークブックでシートをアクティブにします。
1. Microsoft Excel ファイルとして保存します。

以下は、VSTO (C#) と Aspose.Cells for .NET (C#) の並列コード スニペットで、これらのタスクを達成する方法を示しています。

**VSTO**

{{< highlight "csharp" >}}

// アプリケーション オブジェクトを開始する

Excel.Application excelApp = アプリケーション;

// テンプレートの Excel ファイルのパスを指定します。

string myPath = "Book1.xls";

//エクセルファイルを開く。

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value);

//Worksheet オブジェクトを宣言します。

Excel.Worksheet newWorksheet;

// ワークブックに 5 つの新しいワークシートを追加し、いくつかのデータを入力します

//セルに。

for (int i = 1; i< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 //ライセンスのインスタンスをインスタンス化し、ライセンス ファイルを設定します

//そのパスを介して

Aspose.Cells.License ライセンス = 新しい Aspose.Cells.License();

license.SetLicense("Aspose.Total.lic");

// テンプレートの Excel ファイルのパスを指定します。

string myPath = "Book1.xls";

// 新しい Workbook をインスタンス化します。

//エクセルファイルを開く。

ワークブック ワークブック = 新しいワークブック(myPath);

//Worksheet オブジェクトを宣言します。

ワークシート newWorksheet;

// ワークブックに 5 つの新しいワークシートを追加し、いくつかのデータを入力します

//セルに。

for (int i = 0; i< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\)。ジップ）
