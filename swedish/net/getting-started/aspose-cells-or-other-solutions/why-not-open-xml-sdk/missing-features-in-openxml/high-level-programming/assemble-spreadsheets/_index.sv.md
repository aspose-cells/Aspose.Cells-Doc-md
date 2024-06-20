---
title: Montera kalkylblad
type: docs
weight: 10
url: /sv/net/assemble-spreadsheets/
---

Denna avsnitt beskriver hur du:

Skapa en ny Excel-fil från grunden och lägg till kalkylblad i den.

- Lägg till kalkylblad i designerkalkylblad.
- Få åtkomst till kalkylblad med hjälp av kalkylbladets namn.
- Ta bort ett kalkylblad från en Excel-fil med hjälp av dess kalkylbladsnamn.
- Ta bort ett kalkylblad från en Excel-fil med hjälp av dess kalkylbladsindex.
- Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Excel-fil. Workbook-klassen innehåller en Worksheets-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av Worksheet-klassen. Worksheet-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad.
## **Lägga till kalkylblad i en ny Excelfil**
För att skapa en ny Excel-fil programmatiskt:

- Skapa en instans av Workbook-klassen.
- Anropa Add-metoden i Worksheets-samlingen. Ett tomt kalkylblad läggs automatiskt till Excel-filen. Det kan refereras genom att skicka kalkylbladets index till Worksheets-samlingen.
- Hämta en kalkylbladsreferens.
- Utför arbete på kalkylbladen.
- Spara den nya Excel-filen med nya kalkylblad genom att skicka Använd metoden för klassen Workbook.

{{< highlight csharp >}}

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
## **Lägga till kalkylblad i ett designerkalkylblad**
Processen att lägga till kalkylblad i ett designerkalkylblad är densamma som att lägga till ett nytt kalkylblad, förutom att Excel-filen redan finns så den måste öppnas innan kalkylbladen läggs till. Ett designerkalkylblad kan öppnas med hjälp av Workbook-klassen.

{{< highlight csharp >}}

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
## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**
Få åtkomst till eller hämta vilket kalkylblad som helst genom att ange dess namn eller index.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Ta bort kalkylblad med hjälp av kalkylbladsnamn**
För att ta bort kalkylblad från en fil, anropa RemoveAt-metoden i Worksheets-samlingen. Skicka kalkylbladets namn till RemoveAt-metoden för att ta bort ett specifikt kalkylblad.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Ta bort kalkylblad med hjälp av kalkylbladsindex**
Att ta bort kalkylblad med namn fungerar bra när kalkylbladets namn är känt. Om du inte vet kalkylbladets namn, använd en överlagrad version av RemoveAt-metoden som tar kalkylbladets index istället för dess namn.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
