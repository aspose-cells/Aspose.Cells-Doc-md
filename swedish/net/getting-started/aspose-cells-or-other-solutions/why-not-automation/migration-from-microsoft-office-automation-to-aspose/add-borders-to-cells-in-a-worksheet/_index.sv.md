---
title: Lägg till ramar till celler i ett kalkylblad
type: docs
weight: 50
url: /sv/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET låter dig utföra nästan vilka uppgifter som helst genom din applikation som en användare kan utföra i Microsoft Excel. Aspose.Cells är effektiv och robust och har fördelen att fungera oberoende av Microsoft Automation. Den här artikeln visar hur man lägger till ramar till celler i ett kalkylblad med hjälp av Aspose.Cells for .NET jämfört med VSTO.

{{% /alert %}}

## **Lägga till ramar till celler**

För att lägga till ramar i celler i ett kalkylblad, följ följande steg:

1. Ställ in kalkylbladet:
   1. Instantiera en Applikationsobjekt.
      (Endast VSTO.)
   1. Lägg till en arbetsbok.
   1. Hämta det första arket.
   1. Lägg till text i de celler som du ska lägga till ramar till.
1. Lägg till ramar:
   1. Definiera en omfattning.
   1. Applicera en ramstil på omfattningen.
      Upprepa för varje omfattning och varje ramstil du vill ställa in. Detta exempel tillämpar hårstrån, tunna, medelstora och tjocka linjer.
1. Avsluta:
   1. Justera kolumnen där cellerna finns för att passa texten snyggt.
   1. Spara dokumentet.

Dessa steg visas i koden nedan. De första kodexemplen visar hur du implementerar dem med antingen C# eller Visual Basic med [VSTO](/cells/sv/net/add-borders-to-cells-in-a-worksheet/). Efter VSTO-exemplen följer exempel som visar hur man utför samma steg med [Aspose.Cells for .NET](/cells/sv/net/add-borders-to-cells-in-a-worksheet/), igen med antingen C# eller Visual Basic. Aspose.Cells kodexempel är mycket kortare eftersom Aspose.Cells är optimerat för effektiv kodning.

Koden genererar en Excelfil med ett antal celler på det första arket, var och en med en annan ram:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Celler med tillämpade ramar.**

### **Lägga till ramar med VSTO**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

### **Lägga till ramar med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
