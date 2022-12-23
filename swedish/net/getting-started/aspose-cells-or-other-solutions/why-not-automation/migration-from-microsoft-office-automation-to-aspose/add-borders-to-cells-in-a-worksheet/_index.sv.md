---
title: Lägg till gränser till Cells i ett kalkylblad
type: docs
weight: 50
url: /sv/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET låter dig utföra nästan alla uppgifter via din applikation som en användare kan utföra i Microsoft Excel. Aspose.Cells är prestanda och robust och har den extra fördelen att arbeta oberoende av Microsoft Automation. Den här artikeln visar hur du lägger till kanter till celler i ett kalkylblad med Aspose.Cells for .NET jämfört med VSTO.

{{% /alert %}}

## **Lägger till gränser till Cells**

För att lägga till kanter till celler i ett kalkylblad, gör följande:

1. Konfigurera arbetsbladet:
 1. Instantiera ett applikationsobjekt.
 (Endast VSTO.)
 1. Lägg till en arbetsbok.
 1. Skaffa det första arket.
 1. Lägg till text i cellerna som du ska lägga till kanter till.
1. Lägg till kanter:
 1. Definiera ett intervall.
1. Använd en kantstil på intervallet.
 Upprepa för varje område och varje kantstil du vill ställa in. Detta exempel gäller hårlinjer, tunna, medelstora och tjocka linjer.
1. Avsluta:
 1. Anpassa kolumnen som cellerna är i automatiskt för att passa texten snyggt.
 1. Spara dokumentet.

 Dessa steg visas i koden nedan. De första kodexemplen visar hur man implementerar dem med hjälp av[VSTO](/cells/sv/net/add-borders-to-cells-in-a-worksheet/) med antingen C# eller Visual Basic. Efter VSTO-exemplen finns exempel som visar hur man utför samma steg med hjälp av[Aspose.Cells for .NET](/cells/sv/net/add-borders-to-cells-in-a-worksheet/), återigen med antingen C# eller Visual Basic. Aspose.Cells-kodexemplen är mycket kortare eftersom Aspose.Cells är optimerad för effektiv kodning.

Koden genererar en Excel-fil med ett antal celler på det första arket, var och en med olika ramar:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Cells med gränser applicerade.**

### **Lägga till gränser med VSTO**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Lägger till gränser med Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
