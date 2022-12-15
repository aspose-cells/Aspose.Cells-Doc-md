---
title: Sätt ihop kalkylblad
type: docs
weight: 10
url: /sv/net/assemble-spreadsheets/
---
Det här avsnittet beskriver hur du:

Skapa en ny Excel-fil från början och lägg till ett kalkylblad till den.

- Lägg till kalkylblad till designerkalkylblad.
- Få åtkomst till kalkylblad med bladets namn.
- Ta bort ett kalkylblad från en Excel-fil med dess arknamn.
- Ta bort ett kalkylblad från en Excel-fil med hjälp av dess arkindex.
- Aspose.Cells tillhandahåller en klass, arbetsbok som representerar en Excel-fil. Klassen Workbook innehåller en kalkylbladssamling som gör det möjligt att komma åt varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen Worksheet. Klassen Worksheet tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad.
## **Lägga till kalkylblad till en ny Excel-fil**
Så här skapar du en ny Excel-fil programmatiskt:

- Skapa ett objekt av klassen Workbook.
- Anropa Lägg till metoden i samlingen arbetsblad. Ett tomt kalkylblad läggs automatiskt till i Excel-filen *. Det kan refereras till genom att skicka arkindexet för det nya kalkylbladet till kalkylbladssamlingen.
- Skaffa en kalkylbladsreferens.
- Utför arbete på arbetsbladen.
- Spara den nya Excel-filen med nya kalkylblad genom att anropa Workbook-klassens Spara-metod.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Lägga till kalkylblad till ett designerkalkylblad**
Processen att lägga till kalkylblad till ett designerkalkylblad är densamma som att lägga till ett nytt kalkylblad, förutom att Excel-filen redan finns så bör öppnas innan kalkylblad läggs till. Ett designerkalkylblad kan öppnas av klassen Workbook.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn**
Få åtkomst till eller få ett kalkylblad genom att ange dess namn eller index.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Ta bort kalkylblad med Sheet Name**
För att ta bort kalkylblad från en fil, anropa kalkylbladssamlingens RemoveAt-metoden. Skicka arknamnet till metoden RemoveAt för att ta bort ett specifikt kalkylblad.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Ta bort kalkylblad med Sheet Index**
Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av RemoveAt-metoden som tar kalkylbladets arkindex istället för dess arknamn.

{{< highlight "csharp" >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
