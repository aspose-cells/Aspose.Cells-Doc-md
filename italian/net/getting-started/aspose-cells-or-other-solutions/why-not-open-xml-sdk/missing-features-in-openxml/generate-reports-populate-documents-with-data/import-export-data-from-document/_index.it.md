---
title: Importa ed esporta dati dal documento
type: docs
weight: 10
url: /it/net/import-export-data-from-document/
---

## **Importa dati dal documento**

I dati sono la raccolta di fatti grezzi e creiamo documenti di fogli di calcolo o report per presentare questi fatti grezzi in modo più significativo. Normalmente aggiungiamo dati ai fogli di calcolo da soli, ma a volte dobbiamo riutilizzare risorse dati esistenti e qui nasce la necessità di importare dati nei fogli di lavoro da diverse fonti di dati. In questo argomento, discuteremo alcune tecniche per importare dati nei fogli di lavoro da diverse fonti di dati.

## **Importare dati utilizzando Aspose.Cells**

Quando si utilizza **Aspose.Cells** per aprire un file Excel, tutti i dati nel file vengono importati automaticamente ma Aspose.Cells supporta anche l'importazione di dati da diverse fonti di dati. Alcune di queste fonti di dati sono elencate di seguito:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells fornisce una classe, **Workbook** che rappresenta un file Excel. La classe Workbook contiene una raccolta di Worksheets che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una raccolta di celle.

La raccolta di celle fornisce metodi molto utili per importare dati da diverse fonti di dati.

### **Importazione da Array**

Gli sviluppatori possono importare dati da un array nei loro fogli di lavoro chiamando il metodo **ImportArray** della raccolta Cells. Ci sono molte versioni sovraccaricate del metodo ImportArray ma un sovraccarico tipico richiede i seguenti parametri:

- Array, rappresenta l'oggetto array i cui contenuti devono essere importati
- Numero di riga, rappresenta il numero di riga della prima cella dove i dati saranno importati
- Numero di colonna, rappresenta il numero di colonna della prima cella dove i dati saranno importati
- È Verticale, un valore booleano che specifica di importare i dati verticalmente o orizzontalmente

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

### **Importazione da ArrayList**

Gli sviluppatori possono importare dati da un ArrayList nei loro fogli di lavoro chiamando il metodo **ImportArrayList** della raccolta Cells. Il metodo ImportArray richiede i seguenti parametri: **ArrayList** , rappresenta l'oggetto ArrayList i cui contenuti devono essere importati

- Numero di riga, rappresenta il numero di riga della prima cella dove i dati saranno importati
- Numero di colonna, rappresenta il numero di colonna della prima cella dove i dati saranno importati
- È Verticale, un valore booleano che specifica di importare i dati verticalmente o orizzontalmente

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

### **Importazione da Oggetti Personalizzati**

Gli sviluppatori possono importare dati da una collezione di oggetti in un foglio di lavoro usando **ImportCustomObjects**. È possibile fornire una lista di colonne/proprietà al metodo per visualizzare la lista desiderata di oggetti.

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

### **Importazione da DataTable**

Gli sviluppatori possono importare dati da un **DataTable** nei loro fogli di lavoro chiamando il metodo **ImportDataTable** della raccolta Cells. Ci sono molte versioni sovraccaricate del metodo **ImportDataTable** ma un sovraccarico tipico richiede i seguenti parametri:**DataTable** , rappresenta l'oggetto **DataTable** i cui contenuti devono essere importati

- **È Mostrato Nome Campo**, specifica se i nomi delle colonne del DataTable devono essere importati nel foglio di lavoro come prima riga o meno
- **Cella di Inizio** , rappresenta il nome della cella di inizio (cioè "A1") da dove importare i contenuti del DataTable

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

## **Scarica il codice di esempio**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Esporta dati dal documento**

Aspose.Cells non solo facilita ai suoi utenti l'importazione di dati nei fogli di lavoro da fonti dati esterne ma consente loro anche di esportare i dati del loro foglio di lavoro in un **DataTable**. Come sappiamo, **DataTable** fa parte di ADO.NET e viene utilizzato per contenere dati. Una volta che i dati sono memorizzati in un **DataTable**, possono essere utilizzati in qualsiasi modo secondo le esigenze degli utenti.

## **Esportazione di dati su DataTable (.NET) utilizzando Aspose.Cells**

Gli sviluppatori possono facilmente esportare i dati del loro foglio di lavoro in un oggetto DataTable chiamando il metodo ExportDataTable o ExportDataTableAsString della classe Cells. Entrambi i metodi sono utilizzati in scenari diversi, che vengono discussi di seguito in maggior dettaglio.

### **Colonne contenenti dati fortemente tipizzati**

Sappiamo che un foglio di calcolo memorizza i dati come una sequenza di righe e colonne. Se tutti i valori nelle colonne di un foglio di lavoro sono fortemente tipizzati (ciò significa che tutti i valori in una colonna devono avere lo stesso tipo di dati) allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo **ExportDataTable** della classe Cells. Il metodo **ExportDataTable** richiede i seguenti parametri per esportare i dati del foglio di lavoro come oggetto **DataTable**: **Numero di riga**, rappresenta il numero di riga della prima cella da cui verranno esportati i dati

- **Numero di colonna**, rappresenta il numero di colonna della prima cella da cui verranno esportati i dati
- **Numero di righe**, rappresenta il numero di righe da esportare
- **Numero di colonne**, rappresenta il numero di colonne da esportare
- **Esporta Nomi Colonne**, una proprietà booleana che indica se i dati nella prima riga del foglio di lavoro dovrebbero essere esportati come nomi delle colonne del DataTable o meno

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

### **Colonne contenenti dati non fortemente tipizzati**

Se tutti i valori nelle colonne di un foglio di lavoro non sono fortemente tipizzati (ciò significa che i valori in una colonna possono avere tipi di dati diversi) allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo **ExportDataTableAsString** della classe Cells. Il metodo **ExportDataTableAsString** prende lo stesso set di parametri del metodo **ExportDataTable** per esportare i dati del foglio di lavoro come oggetto **DataTable**.

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

## **Scarica il codice di esempio**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
