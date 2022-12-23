---
title: Visa eller dölj rullningslister i Aspose.Cells
type: docs
weight: 70
url: /sv/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Rullningslister är mycket använda för att navigera i innehållet i alla filer. Normalt finns det två typer av rullningslister:

- Vertikala rullningslister
- Horisontella rullningslister

Microsoft Excel tillhandahåller även horisontella och vertikala rullningslister så att användare kan rulla igenom kalkylbladets innehåll. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för båda typerna av rullningslister i Excel-filer.

{{% /alert %}}

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för rullningslister använder du[**Arbetsbok Inställningar**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) klass'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) egenskaper.[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) är booleska egenskaper, vilket innebär att dessa egenskaper endast kan lagras**Sann** eller**falsk** värden.

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, döljer båda rullningslisterna och sedan sparar den ändrade filen som output.xls .

Skärmdumpen nedan visar filen Book1.xls som innehåller båda rullningslisterna. Den modifierade filen sparas som output.xls-fil, även visad nedan.

**Book1.xls: Excel-fil före eventuell ändring**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Ladda ner provkod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
