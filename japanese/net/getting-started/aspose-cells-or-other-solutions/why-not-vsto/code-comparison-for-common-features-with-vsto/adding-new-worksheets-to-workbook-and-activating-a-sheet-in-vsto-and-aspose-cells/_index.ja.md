---
title: VSTOとAspose.Cellsで新しいワークシートをワークブックに追加し、シートをアクティブ化する
type: docs
weight: 30
url: /ja/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---

## **移行のヒント：**
1. 既存のMicrosoft Excelファイルに新しいワークシートを追加します。
1. 各新しいワークシートのセルにデータを入力します。
1. ブック内のシートをアクティブにします。
1. Microsoft Excelファイルとして保存します。

以下は、これらのタスクを達成するためのVSTO（C#）およびAspose.Cells for .NET（C#）用の並行コードスニペットです。

**VSTO**

{{< highlight csharp >}}

 //intiate application object

Excel.Application excelApp = Application;

//Specify the template excel file path.

string myPath = "Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Declare a Worksheet object.

Excel.Worksheet newWorksheet;

//Add 5 new worksheets to the workbook and fill some data

//into the cells.

for (int i = 1; i < 6; i++){

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

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file

//through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Total.lic");

//Specify the template excel file path.

string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Declare a Worksheet object.

Worksheet newWorksheet;

//Add 5 new worksheets to the workbook and fill some data

//into the cells.

for (int i = 0; i < 5; i++){

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
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
