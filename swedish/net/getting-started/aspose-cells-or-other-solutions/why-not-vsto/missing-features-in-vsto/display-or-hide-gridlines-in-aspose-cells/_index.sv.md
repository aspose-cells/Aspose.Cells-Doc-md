---
title: Visa eller dölj rutnät i Aspose.Cells
type: docs
weight: 50
url: /sv/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler, så att det är lätt att mata in data i särskilda celler. Gridlines gör det möjligt för oss att se ett kalkylblad som en samling celler, där varje cell är lätt att identifiera.

{{% /alert %}}

## **Styra rutnätets synlighet**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att kontrollera synligheten för rutnät, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) fast egendom.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk** värde.

 Ett komplett exempel ges nedan som visar användningen av[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) egendom av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass för att dölja rutnätet för det första kalkylbladet i Excel-filen.

I skärmdumpen nedan kan du se att Book1.xls-filen innehåller tre arbetsblad: Blad1, Blad2 och Blad3. Alla kalkylblad har rutnät.

**Book1.xls: kalkylbladsvy före ändring** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Book1.xls-filen öppnas genom att använda klassen Workbook och rutnätslinjerna på det första kalkylbladet är dolda. Den ändrade filen sparas som output.xls.

**Output.xls: kalkylblad efter modifiering** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Ladda ner exempelkod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
