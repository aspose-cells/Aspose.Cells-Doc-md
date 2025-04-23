---
title: Rotera celltext
type: docs
weight: 100
url: /sv/net/rotating-cell-text/
---

{{% alert color="primary" %}}

Ibland är en kolumnrubrik mycket bredare än datan i cellerna nedan. Detta kan orsaka onödigt mellanrum på sidan. En lösning är att rotera texten vertikalt så att den tar mindre horisontell plats. I Microsoft Excel är det enkelt att rotera text. Som tur är det också möjligt att rotera text programmatiskt, så att utvecklare kan rotera etiketter i kalkylbladen de skapar inom sina applikationer.

Den här artikeln tittar på hur man roterar text i celler med [Aspose.Cells for .NET](/cells/sv/net/rotera-celltext/) jämfört med att göra samma sak med [VSTO](/cells/sv/net/rotera-celltext/).

{{% /alert %}}

## **Rotera text i celler**

För att rotera text i en cell på en arbetsblad, följ följande steg:

1. Skapa en arbetsbok och hämta ett arbetsblad.
1. Lägg till exempeltext.
1. Formatera texten: rotera, lägg till bakgrundsfärg.
1. Spara filen.

Kodexemplen nedan visar hur man utför dessa steg först i [VSTO](/cells/sv/net/rotera-celltext/), med antingen C# eller Visual Basic, och sedan i [Aspose.Cells](/cells/sv/net/rotera-celltext/), igen med antingen C# eller Visual Basic.

De kodexempel i den här artikeln ger utmatningen som visas nedan.
**En cell med roterad text.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Rotera text med VSTO**

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

#### **Roterande text med Aspose.Cells for .NET**

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
