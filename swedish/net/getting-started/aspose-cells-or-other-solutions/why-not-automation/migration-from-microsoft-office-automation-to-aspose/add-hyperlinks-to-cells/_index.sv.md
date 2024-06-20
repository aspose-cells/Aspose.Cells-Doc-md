---
title: Lägg till hyperlänkar till celler
type: docs
weight: 60
url: /sv/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET tillåter dig att utföra nästan alla uppgifter genom din applikation som en användare kan utföra i Microsoft Excel. Den här artikeln jämför hur man lägger till en hyperlänk till en cell i ett kalkylblad med VSTO och Aspose.Cells for .NET.

{{% /alert %}}

## **Lägga till hyperlänkar till celler**

För att lägga till hyperlänkar till celler i ett kalkylblad, följ följande steg:

1. Ställ in kalkylbladet:
   1. Instantiera en Applikationsobjekt.
      (Endast VSTO.)
   1. Lägg till en arbetsbok.
   1. Hämta det första arket.
   1. Lägg till text i cellerna som du kommer att lägga till en hyperlänk till.
1. Lägg till hyperlänk.
1. Spara dokumentet.

Dessa steg visas i kodexemplen nedan. De första exemplen visar hur man använder [VSTO](/cells/sv/net/add-hyperlinks-to-cells/) med antingen C# eller Visual Basic för att lägga till en hyperlänk till en cell. Exemplen som följer visar hur man gör samma sak med [Aspose.Cells for .NET](/cells/sv/net/add-hyperlinks-to-cells/), igen med C# eller Visual Basic.

Kodexemplen genererar en Excelfil med en hyperlänk i cell A1 på det första arket.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**En hyperlänk läggs till cell A1.**

### **Lägga till hyperlänkar till celler med VSTO**

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

### **Lägga till hyperlänkar till celler med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
