---
title: Roterande Cell Text
type: docs
weight: 100
url: /sv/net/rotating-cell-text/
---
{{% alert color="primary" %}}

Ibland är en kolumnrubrik mycket bredare än data i cellerna nedan. Detta kan orsaka onödigt blanksteg på sidan. En lösning är att rotera texten vertikalt så att den tar mindre horisontellt utrymme. I Microsoft Excel är det lätt att rotera text. Lyckligtvis är det möjligt att rotera text programmässigt också, så att utvecklare kan rotera etiketter i de kalkylblad som de skapar i sina applikationer.

 Den här artikeln tittar på hur man roterar text i celler med hjälp av[Aspose.Cells för .NET](/cells/sv/net/rotating-cell-text/) jämfört med att göra samma sak med[VSTO](/cells/sv/net/rotating-cell-text/).

{{% /alert %}}

## **Roterande text i Cells**

För att rotera text i en cell på ett kalkylblad, utför följande steg:

1. Skapa en arbetsbok och få ett arbetsblad.
1. Lägg till exempeltext.
1. Formatera texten: rotera, lägg till bakgrundsfärg.
1. Spara filen.

 Kodexemplen som följer visar hur du utför dessa steg först[VSTO](/cells/sv/net/rotating-cell-text/) , med antingen C# eller Visual Basic, och sedan in[Aspose.Cells](/cells/sv/net/rotating-cell-text/)återigen med antingen C# eller Visual Basic.

Kodexemplen i den här artikeln ger utdata som visas nedan.
**En cell med roterad text.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Roterande text med VSTO**

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

#### **Roterande text med Aspose.Cells för .NET**

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
