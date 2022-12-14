---
title: Lägg till hyperlänkar till Cells
type: docs
weight: 60
url: /sv/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells för .NET låter dig utföra nästan alla uppgifter via din applikation som en användare kan utföra i Microsoft Excel. Den här artikeln jämför hur man lägger till en hyperlänk till en cell i ett kalkylblad med VSTO och Aspose.Cells för .NET.

{{% /alert %}}

## **Lägger till hyperlänkar till Cells**

För att lägga till hyperlänkar till celler i ett kalkylblad, gör följande:

1. Konfigurera arbetsbladet:
 1. Instantiera ett applikationsobjekt.
 (Endast VSTO.)
 1. Lägg till en arbetsbok.
 1. Skaffa det första arket.
1. Lägg till text i cellerna som du ska lägga till en hyperlänk till.
1. Lägg till hyperlänk.
1. Spara dokumentet.

 Dessa steg visas i kodexemplen nedan. De första exemplen visar hur man använder[VSTO](/cells/sv/net/add-hyperlinks-to-cells/) med antingen C# eller Visual Basic för att lägga till en hyperlänk till en cell. Exemplen som följer visar hur man gör samma sak med hjälp av[Aspose.Cells för .NET](/cells/sv/net/add-hyperlinks-to-cells/), återigen med C# eller Visual Basic.

Kodexemplen genererar en Excel-fil som har en hyperlänk i cell A1 på det första kalkylbladet.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**En hyperlänk läggs till i cell A1.**

### **Lägger till hyperlänkar till Cells med VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Lägga till hyperlänkar till Cells med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
