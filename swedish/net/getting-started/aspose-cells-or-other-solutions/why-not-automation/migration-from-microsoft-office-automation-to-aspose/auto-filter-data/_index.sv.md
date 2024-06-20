---
title: Automatisk filterdata
type: docs
weight: 120
url: /sv/net/auto-filter-data/
---

{{% alert color="primary" %}}

Att förstå vilka data som finns i en serie, är det ofta lättare att sortera och filtrera datan än att titta på kolumner av oordnad data. Sortering organiserar data antingen i stigande eller fallande ordning, vilket gör det lättare att hitta specifika värden. Att filtrera datan tillåter dig att endast visa vissa värden. Det hjälper till att fokusera på specifika poster i försäljningsposter, till exempel.

Användare av Microsoft Excel kan tillämpa automatisk filtrering på kolumner. Automatisk filtrering lägger till en meny längst upp i kolumnen, varifrån du kan sortera eller filtrera kolumndata. Denna funktion är också tillgänglig för utvecklare som arbetar med Excel-ark, antingen genom VSTO eller Aspose.Cells for .NET.

{{% /alert %}}

## **Automatisk filtrering av data**

För att tillämpa automatisk filtrering på en kolumn:

1. Skapa en arbetsbok.
1. Hämta ett arbetsblad.
1. Lägg till exempeldata.
1. Tillämpa automatisk filtrering.
1. Justera kolumnbredderna för att göra visningen attraktiv.
1. Spara kalkylarket.

Kodproverna i den här artikeln visar hur man utför dessa steg med [VSTO](/cells/sv/net/auto-filter-data/) med antingen C# eller Visual Basic, eller genom att använda [Apose.Cells](/cells/sv/net/auto-filter-data/), också med antingen C# eller Visual Basic.

### **Automatisk filtrering av data med VSTO**

**C#**

{{< highlight csharp >}}

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

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

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

**Automatiskt filter tillämpat med VSTO** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Automatisk filtrering av data med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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

**Automatiskt filter tillämpat med Aspose.Cells for .NET** 

![todo:image_alt_text](auto-filter-data_2.png)
