---
title: Importera/Exportera data från dokument
type: docs
weight: 10
url: /sv/net/import-export-data-from-document/
---

## **Importera data från dokument**

Data är samlingen av råa fakta och vi skapar kalkylblad eller rapporter för att presentera dessa råa fakta på ett mer meningsfullt sätt. Vanligtvis lägger vi till data i kalkylblad av oss själva men ibland behöver vi återanvända befintliga dataresurser och här uppstår behovet av att importera data till kalkylblad från olika datakällor. I det här ämnet diskuterar vi några tekniker för att importera data till kalkylblad från olika datakällor.

## **Importera data med Aspose.Cells**

När du använder **Aspose.Cells** för att öppna en Excel-fil importeras all data i filen automatiskt men Aspose.Cells stöder också att importera data från olika datakällor. Några av dessa datakällor listas nedan:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells tillhandahåller en klass, **Workbook** som representerar en Excel-fil. Workbook-klassen innehåller en Worksheets-samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av Worksheet-klassen. Worksheet-klassen tillhandahåller en Cells-samling.

Cells-samlingen tillhandahåller mycket användbara metoder för att importera data från olika datakällor.

### **Importera från Array**

Utvecklare kan importera data från en array till sina kalkylblad genom att anropa metoden **ImportArray** i Cells-samlingen. Det finns många överbelastade versioner av metoden ImportArray men en typisk överbelastning tar följande parametrar:

- Array, representerar arrayobjektet vars innehåll behöver importeras
- Radnummer, representerar radnumret för den första cellen där datan kommer att importeras
- Kolumnnummer, representerar kolumnnumret för den första cellen där datan kommer att importeras
- Är Vertikal, ett booleskt värde som specificerar att importera data vertikalt eller horisontellt

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importera från ArrayList**

Utvecklare kan importera data från en ArrayList till sina kalkylblad genom att anropa metoden **ImportArrayList** i Cells-samlingen. ImportArray metoden tar följande parametrar: **ArrayList** , representerar ArrayList-objektet vars innehåll behöver importeras

- Radnummer , representerar radnumret för den första cellen där datan kommer att importeras
- Kolumnnummer , representerar kolumnnumret för den första cellen där datan kommer att importeras
- Är Vertikal , ett booleskt värde som specificerar att importera data vertikalt eller horisontellt

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Importera från Anpassade Objekt**

Utvecklare kan importera data från en samling objekt till ett kalkylblad med hjälp av **ImportCustomObjects**. Du kan ange en lista med kolumner/egenskaper till metoden för att visa din önskade lista med objekt.

{{< highlight csharp >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **Importera från DataTable**

Utvecklare kan importera data från en **DataTable** till sina kalkylblad genom att anropa metoden **ImportDataTable** i Cells-samlingen. Det finns många överbelastade versioner av metoden **ImportDataTable** men en typisk överbelastning tar följande parametrar:**DataTable** , representerar **DataTable** objektet vars innehåll behöver importeras

- **Visas fältnamn**, specificerar om namnen på DataTables kolumner ska importeras till kalkylbladet som en första rad eller inte
- **Startcell** , representerar namnet på startcellen (dvs. "A1") från vilken datans innehåll ska importeras

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Ladda ned provkoden**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Exportera data från dokument**

Aspose.Cells underlättar inte bara för användarna att importera data till arbetsblad från externa datakällor utan tillåter dem också att exportera sin arbetsbladsdata till en **DataTable**. Som vi vet är **DataTable** en del av ADO.NET och används för att lagra data. När datan är lagrad i en **DataTable** kan den användas på något sätt enligt användarnas krav.

## **Exportera data till DataTable (.NET) med hjälp av Aspose.Cells**

Utvecklare kan enkelt exportera sin arbetsbladsdata till ett DataTable-objekt genom att anropa antingen ExportDataTable-metoden eller ExportDataTableAsString-metoden i Cells-klassen. Båda metoderna används i olika scenarier, vilka diskuteras nedan mer detaljerat.

### **Kolumner Innehållande Starkt Skriven Data**

Vi vet att en kalkylblad lagrar data som en sekvens av rader och kolumner. Om alla värden i kolumnerna i ett kalkylblad är starkt typade (det betyder att alla värden i en kolumn måste ha samma datatyp) kan vi exportera kalkylbladets innehåll genom att anropa metoden **ExportDataTable** i Cells-klassen. Metoden **ExportDataTable** tar följande parametrar för att exportera kalkylbladsdata som **DataTable** objekt: **Radnummer** , representerar radnumret för den första cellen från vilken datan kommer att exporteras

- **Kolumnnummer** , representerar kolumnnumret för den första cellen från vilken datan kommer att exporteras
- **Antal rader** , representerar antalet rader som ska exporteras
- **Antal kolumner** , representerar antalet kolumner som ska exporteras
- **Exportera kolumnnamn** , en boolesk egenskap som indikerar om datan i den första raden i kalkylbladet ska exporteras som kolumnnamn i DataTable eller inte

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **Kolumner som innehåller icke-strongly typed data**

Om alla värden i kolumnerna i ett kalkylblad inte är starkt typade (det betyder att värdena i en kolumn kan ha olika datatyper) kan vi exportera kalkylbladets innehåll genom att anropa metoden **ExportDataTableAsString** i Cells-klassen. Metoden **ExportDataTableAsString** tar samma uppsättning parametrar som metoden **ExportDataTable** för att exportera kalkylbladsdata som **DataTable** objekt.

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Ladda ned provkoden**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
