---
title: Visa eller dölj rutnät i Aspose.Cells
type: docs
weight: 50
url: /sv/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Alla Excel-ark har som standard rutnät. De hjälper till att avgränsa celler, så att det är lätt att mata in data i särskilda celler. Rutnäten gör det möjligt för oss att se ett arbetsblad som en samling celler, där varje cell är lätt identifierbar.

{{% /alert %}}

## **Kontrollera synligheten av rutnäten**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) -samling som möjliggör åtkomst till varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för hantering av ett arbetsblad. För att kontrollera synligheten av rutnäten använd [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassens [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) egendom. [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) är en boolesk egendom, vilket innebär att den endast kan lagra ett **true** eller **false** värde.

Ett komplett exempel ges nedan som visar användningen av [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) egenskapen hos klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) för att dölja rutnäten på det första arbetsbladet i Excel-filen.

På skärmdumpen nedan kan du se att filen Book1.xls innehåller tre arbetsblad: Sheet1, Sheet2 och Sheet3. Alla arbetsblad har rutnäten.

** Book1.xls: arbetsboksvy före ändring ** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Filen Book1.xls öppnas genom att använda klassen Workbook och rutnäten på det första arbetsbladet döljs. Den modifierade filen sparas som output.xls.

**Output.xls: kalkylblad efter ändring** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Ladda ned provkoden**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
