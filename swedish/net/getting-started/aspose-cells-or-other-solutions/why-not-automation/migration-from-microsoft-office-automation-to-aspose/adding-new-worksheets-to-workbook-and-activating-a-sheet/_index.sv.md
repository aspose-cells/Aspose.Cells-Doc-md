---
title: Lägga till nya arbetsblad i arbetsboken och aktivera ett arbetsblad
type: docs
weight: 10
url: /sv/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

När du arbetar med en mallfil finns det ibland ett behov av att lägga till extra kalkylblad i arbetsboken för att samla in data. De nya cellerna kommer att fyllas med data på angivna positioner och platser i varje kalkylblad.

På samma sätt kan du behöva ett specifikt kalkylblad för att vara aktivt och visas först när filen öppnas i Microsoft Excel. Ett "aktivt ark" är det ark som du arbetar med i en arbetsbok. Namnet på fliken på det aktiva bladet är som standard fetstilt.

 Att lägga till kalkylblad och ställa in vilket blad som är aktivt är vanliga och enkla uppgifter som utvecklare behöver veta hur de ska utföra. I den här artikeln utför vi dessa uppgifter med hjälp av[VSTO](/cells/sv/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) och[Aspose.Cells for .NET](/cells/sv/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Lägga till arbetsblad och aktivera ett arbetsblad**
För detta migreringstips:

1. Lägg till nya kalkylblad i en befintlig Microsoft Excel-fil.
1. Fyll i data i cellerna i varje nytt kalkylblad.
1. Aktivera ett ark i arbetsboken.
1. Spara som Microsoft Excel-fil.

Nedan finns parallella kodavsnitt för VSTO (C#, VB) och Aspose.Cells for .NET (C#, VB), som visar hur man utför dessa uppgifter.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

använder Microsoft.VisualStudio.Tools.Applications.Runtime;

använder Excel = Microsoft.Office.Interop.Excel;

använder Office = Microsoft.Office.Core;

använder System.Reflection;

.......

//Instantiera Application-objektet.

Excel.Application excelApp = ny Excel.ApplicationClass();

//Ange sökvägen till mallens excel-fil.

string myPath = @"d:\test\My_Book1.xls";

//Öppna excel-filen.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Missing.Value, Missing.Value);

//Deklarera ett kalkylbladsobjekt.

Excel.Worksheet newWorksheet;

//Lägg till 5 nya kalkylblad i arbetsboken och fyll i lite data

//in i cellerna.

 för (int i = 1; i< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

använder Aspose.Cells;

.......

//Instantera en instans av licens och ställ in licensfilen

//genom dess väg

Aspose.Cells.Licenslicens = ny Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

//Ange sökvägen till mallens excel-fil.

string myPath =@"d:\test\My_Book1.xls";

//Instantiera en ny arbetsbok.

//Öppna excel-filen.

Workbook workbook = new Workbook(myPath);

//Deklarera ett kalkylbladsobjekt.

Arbetsblad newWorksheet;

//Lägg till 5 nya kalkylblad i arbetsboken och fyll i lite data

//in i cellerna.

 för (int i = 0; i< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
