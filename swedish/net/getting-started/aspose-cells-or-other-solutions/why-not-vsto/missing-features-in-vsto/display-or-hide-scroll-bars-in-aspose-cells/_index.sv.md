---
title: Visa eller dölj rullningsfält i Aspose.Cells
type: docs
weight: 70
url: /sv/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

Bildrullningsfält används för att navigera genom innehållet i vilken fil som helst. Normalt sett finns det två typer av bildrullningsfält:

- Vertikala bildrullningsfält
- Horisontella bildrullningsfält

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.

{{% /alert %}}

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) tillhandahåller ett brett utbud av egenskaper och metoder för hantering av en Excel-fil. För att kontrollera synligheten av rullningsfält använd [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) klassens [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) egenskaper. [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) är booleska egenskaper, vilket innebär att dessa egenskaper endast kan lagra **true** eller **false** värden.

Nedan är komplett kod som öppnar en Excel-fil, book1.xls, döljer både rullningsfält och sparar sedan den modifierade filen som output.xls.

Skärmdumpen nedan visar filen Book1.xls som innehåller båda rullningsfälten. Den modifierade filen sparas som output.xls-fil, också visas nedan.

**Book1.xls: Excel-fil innan någon ändring**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Ladda ned provkoden**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
