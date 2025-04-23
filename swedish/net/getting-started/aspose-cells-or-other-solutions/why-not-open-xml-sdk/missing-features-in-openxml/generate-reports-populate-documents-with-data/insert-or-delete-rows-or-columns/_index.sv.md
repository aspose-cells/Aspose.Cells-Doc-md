---
title: Infoga eller ta bort rader eller kolumner
type: docs
weight: 20
url: /sv/net/insert-or-delete-rows-or-columns/
---

Oavsett om vi skapar ett nytt kalkylblad från grunden eller arbetar med ett befintligt kalkylblad kan det hända att vi behöver lägga till extra rader eller kolumner i kalkylbladet för att rymma mer data eller av någon annan anledning. Å andra sidan kan det också vara nödvändigt att ta bort rader eller kolumner från angivna positioner i kalkylbladet.
## **Hantering av rader/kolumner**
**Aspose.Cells** tillhandahåller en klass, Workbook, som representerar en Excel-fil. Workbook-klassen innehåller en Worksheets-samling som gör det möjligt att komma åt varje kalkylblad i Excel-filen. Ett kalkylblad representeras av Worksheet-klassen. Worksheet-klassen tillhandahåller en Cells-samling som representerar alla celler i kalkylbladet.

Cells-samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan i mer detalj.
## **Infoga en rad**
Utvecklare kan infoga en rad i kalkylbladet vid valfri plats genom att anropa InsertRow-metoden i Cells-samlingen. InsertRow-metoden tar index för raden där den nya raden ska infogas.

{{< highlight csharp >}}

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
Ibland kan utvecklare behöva infoga flera rader i kalkylbladet. Det kan göras genom att anropa InsertRows-metoden i Cells-samlingen. InsertRows-metoden tar två parametrar:

- **Radindex**, index för raden varifrån de nya raderna ska infogas
- **Antal rader**, totalt antal rader som behöver infogas

{{< highlight csharp >}}

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
Utvecklare kan ta bort en rad från kalkylbladet vid valfri plats genom att anropa **DeleteRow**-metoden i Cells-samlingen. **DeleteRow**-metoden tar index för den rad som ska tas bort.

{{< highlight csharp >}}

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
Om utvecklare behöver ta bort flera rader från kalkylbladet kan det också göras genom att anropa DeleteRows-metoden i Cells-samlingen. DeleteRows-metoden tar två parametrar:

- **Radindex**, index för raden varifrån raderna ska tas bort.
- **Antal rader**, totalt antal rader som behöver tas bort.

{{< highlight csharp >}}

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
Utvecklare kan också infoga en kolumn i kalkylbladet vid valfri plats genom att anropa InsertColumn-metoden i Cells-samlingen. InsertColumn-metoden tar index för den kolumn där den nya kolumnen ska infogas.

{{< highlight csharp >}}

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
För att ta bort en kolumn från kalkylbladet vid valfri plats kan utvecklare anropa DeleteColumn-metoden i Cells-samlingen. DeleteColumn-metoden tar index för kolumnen som ska tas bort.

{{< highlight csharp >}}

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
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
