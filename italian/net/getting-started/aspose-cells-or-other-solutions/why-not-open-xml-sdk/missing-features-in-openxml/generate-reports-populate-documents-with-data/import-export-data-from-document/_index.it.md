---
title: Importa Esporta i dati dal documento
type: docs
weight: 10
url: /it/net/import-export-data-from-document/
---
## **Importa i dati dal documento**

dati sono la raccolta di fatti grezzi e creiamo fogli di calcolo o report per presentare questi fatti grezzi in modo più significativo. Normalmente, aggiungiamo i dati ai fogli di calcolo da soli, ma a volte abbiamo bisogno di riutilizzare le risorse di dati esistenti e qui nasce la necessità di importare i dati nei fogli di calcolo da diverse fonti di dati. In questo argomento verranno illustrate alcune tecniche per importare dati in fogli di lavoro da diverse origini dati.

## **Importazione dei dati utilizzando Aspose.Cells**

 Quando usi**Aspose.Cells** per aprire un file Excel, tutti i dati nel file vengono importati automaticamente ma Aspose.Cells supporta anche l'importazione di dati da diverse fonti di dati. Alcune di queste fonti di dati sono elencate di seguito:

- **Vettore**
- **Lista di array**
- **Tabella dati**
- **Colonna dati**
- **Visualizzazione dati**
- **DataGrid**
- **DataReader**
- **Vista a griglia**

 Aspose.Cells offre un corso,**Cartella di lavoro** che rappresenta un file Excel. La classe Workbook contiene una raccolta di fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe del foglio di lavoro fornisce una raccolta Cells.

La raccolta Cells fornisce metodi molto utili per importare dati da diverse fonti di dati.

### **Importazione dall'array**

 Gli sviluppatori possono importare dati da un array nei propri fogli di lavoro chiamando il metodo**ImportArray** metodo della raccolta Cells. Esistono molte versioni di overload del metodo ImportArray, ma un tipico overload accetta i seguenti parametri:

- Array, rappresenta l'oggetto array il cui contenuto deve essere importato
- Numero di riga, rappresenta il numero di riga della prima cella in cui verranno importati i dati
- Numero colonna, rappresenta il numero di colonna della prima cella in cui verranno importati i dati
- È verticale, un valore booleano che specifica di importare i dati verticalmente o orizzontalmente

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importazione da ArrayList**

 Gli sviluppatori possono importare dati da un ArrayList ai propri fogli di lavoro chiamando il metodo**ImportArrayList** metodo della raccolta Cells. Il metodo ImportArray accetta i seguenti parametri:**Lista di array** , rappresenta l'oggetto ArrayList di cui è necessario importare il contenuto

- Row Number , rappresenta il numero di riga della prima cella in cui verranno importati i dati
- Numero colonna , rappresenta il numero di colonna della prima cella in cui verranno importati i dati
- Is Vertical , un valore booleano che specifica di importare i dati verticalmente o orizzontalmente

{{< highlight "csharp" >}}

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

### **Importazione da oggetti personalizzati**

 Gli sviluppatori possono importare i dati dalla raccolta di oggetti in un foglio di lavoro utilizzando**Importa oggetti personalizzati**. È possibile fornire un elenco di colonne/proprietà al metodo per visualizzare l'elenco di oggetti desiderato.

{{< highlight "csharp" >}}

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

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

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

 Gli sviluppatori possono importare dati da a**Tabella dati** ai loro fogli di lavoro chiamando il**Importa tabella dati** metodo della raccolta Cells. Esistono molte versioni sovraccaricate di**Importa tabella dati** metodo ma un sovraccarico tipico accetta i seguenti parametri:**Tabella dati** , rappresenta il**Tabella dati** oggetto i cui contenuti devono essere importati

- **Viene visualizzato il nome del campo**, specifica se i nomi delle colonne di DataTable devono essere importati o meno nel foglio di lavoro come prima riga
- **Inizio Cell** rappresenta il nome della cella iniziale (es. "A1") da cui importare il contenuto della DataTable

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

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

## **Esporta i dati dal documento**

 Aspose.Cells non solo facilita ai suoi utenti l'importazione di dati in fogli di lavoro da fonti di dati esterne, ma consente anche loro di esportare i dati del foglio di lavoro in un**Tabella dati** . Come lo sappiamo**Tabella dati** è la parte di ADO.NET e viene utilizzato per contenere i dati. Una volta che i dati sono stati archiviati in un file**Tabella dati**, può essere utilizzato in qualsiasi modo in base alle esigenze degli utenti.

## **Esportazione di dati in DataTable (.NET) utilizzando Aspose.Cells**

Gli sviluppatori possono facilmente esportare i dati del foglio di lavoro in un oggetto DataTable chiamando il metodo ExportDataTable o ExportDataTableAsString della classe Cells. Entrambi i metodi vengono utilizzati in diversi scenari, descritti di seguito in modo più dettagliato.

### **Colonne contenenti dati fortemente tipizzati**

 Sappiamo che un foglio di calcolo memorizza i dati come una sequenza di righe e colonne. Se tutti i valori nelle colonne di un foglio di lavoro sono fortemente tipizzati (ciò significa che tutti i valori in una colonna devono avere lo stesso tipo di dati), allora possiamo esportare il contenuto del foglio di lavoro chiamando il**ExportDataTable** metodo della classe Cells.**ExportDataTable** Il metodo accetta i seguenti parametri per esportare i dati del foglio di lavoro come**Tabella dati** oggetto:**Numero riga** , rappresenta il numero di riga della prima cella da cui verranno esportati i dati

- **Numero di colonna** , rappresenta il numero di colonna della prima cella da cui verranno esportati i dati
- **Numero di righe** , rappresenta il numero di righe da esportare
- **Numero di colonne** rappresenta il numero di colonne da esportare
- **Esporta nomi di colonne** , una proprietà booleana che indica se i dati nella prima riga del foglio di lavoro devono essere esportati o meno come nomi di colonna della DataTable

{{< highlight "csharp" >}}

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

 Se tutti i valori nelle colonne di un foglio di lavoro non sono fortemente tipizzati (ciò significa che i valori in una colonna possono avere i diversi tipi di dati), allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo**ExportDataTableAsString** metodo della classe Cells.**ExportDataTableAsString** Il metodo accetta lo stesso set di parametri di quello di**ExportDataTable** metodo per esportare i dati del foglio di lavoro come**Tabella dati** oggetto.

{{< highlight "csharp" >}}

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
