---
title: Infoga eller ta bort rader eller kolumner
type: docs
weight: 20
url: /sv/net/insert-or-delete-rows-or-columns/
---
Oavsett om vi skapar ett nytt kalkylblad från början eller om vi arbetar med ett befintligt kalkylblad, kan vi behöva lägga till extra rader eller kolumner i kalkylbladet för att ta emot mer data eller av någon annan anledning. Omvänt kan det också krävas att rader eller kolumner tas bort från angivna positioner i kalkylbladet.
## **Hantera rader/kolumner**
**Aspose.Cells** tillhandahåller en klass, arbetsbok som representerar en Excel-fil. Arbetsboksklass innehåller en kalkylbladssamling som gör det möjligt att komma åt varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen Worksheet. Kalkylbladsklassen tillhandahåller en Cells-samling som representerar alla celler i kalkylbladet.

**Cells**samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras mer i detalj nedan.
## **Infoga en rad**
 Utvecklare kan infoga en rad i kalkylbladet var som helst genom att anropa metoden InsertRow i samlingen Cells.**Infoga rad** metoden tar indexet för raden där den nya raden kommer att infogas.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Infoga flera rader**
Ibland kan utvecklare behöva infoga flera rader i kalkylbladet. Det kan göras genom att anropa metoden InsertRows i samlingen Cells. Metoden InsertRows tar två parametrar:

- **Radindex**, indexet för raden där de nya raderna kommer att infogas
- **Antal rader**, totalt antal rader som behöver infogas

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Ta bort en rad**
 Utvecklare kan ta bort en rad från kalkylbladet var som helst genom att anropa**Ta bort rad** metoden för samlingen Cells.**Ta bort rad** metoden tar indexet för raden som måste raderas.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Ta bort flera rader**
Om utvecklare behöver ta bort flera rader från kalkylbladet kan det också göras genom att anropa metoden DeleteRows i samlingen Cells. DeleteRows-metoden tar två parametrar:

- **Radindex**, indexet för raden där raderna kommer att tas bort.
- **Antal rader**, totalt antal rader som måste tas bort.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa metoden InsertColumn i samlingen Cells. Metoden InsertColumn tar indexet för den kolumn där den nya kolumnen kommer att infogas.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Ta bort en kolumn**
För att ta bort en kolumn från kalkylbladet på valfri plats kan utvecklare anropa metoden DeleteColumn för samlingen Cells. Metoden DeleteColumn tar indexet för den kolumn som ska tas bort.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
