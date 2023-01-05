---
title: Filtrera data automatiskt
type: docs
weight: 120
url: /sv/net/auto-filter-data/
---
{{% alert color="primary" %}}

För att få en förståelse för vilken data som finns i ett intervall är det ofta lättare att sortera och filtrera data än att titta på kolumner med oordnad data. Sortering organiserar data i antingen stigande eller fallande ordning, vilket gör det lättare att hitta specifika värden. Genom att filtrera data kan du bara visa vissa värden. Det hjälper till att fokusera på särskilda artiklar i försäljningsregister, till exempel.

Användare av Microsoft Excel kan tillämpa automatisk filtrering på kolumner. Automatisk filtrering lägger till en meny högst upp i kolumnen, från vilken du kan sortera kolumndata. Den här funktionen är också tillgänglig för utvecklare som arbetar med Excel-kalkylblad, antingen via VSTO eller Aspose.Cells for .NET.

{{% /alert %}}

## **Automatisk filtrering av data**

Så här tillämpar du automatisk filtrering på en kolumn:

1. Skapa en arbetsbok.
1. Skaffa ett arbetsblad.
1. Lägg till exempeldata.
1. Använd autofilter.
1. Autopassa kolumner för att göra skärmen attraktiv.
1. Spara kalkylarket.

 Kodexemplen i den här artikeln visar hur du utför dessa steg med[VSTO](/cells/sv/net/auto-filter-data/) med antingen C# eller Visual Basic, eller med[Apose.Cells](/cells/sv/net/auto-filter-data/), igen med antingen C# eller Visual Basic.

### **Automatisk filtrering av data med VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Auto-filter applicerat med VSTO** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Automatisk filtrering av data med Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Autofilter applicerat med Aspose.Cells for .NET** 

![todo:image_alt_text](auto-filter-data_2.png)
