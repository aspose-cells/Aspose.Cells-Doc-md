---
title: Inserisci o elimina righe o colonne
type: docs
weight: 20
url: /it/net/insert-or-delete-rows-or-columns/
---
Sia che stiamo creando un nuovo foglio di lavoro da zero o stiamo lavorando su un foglio di lavoro esistente, potremmo aver bisogno di aggiungere ulteriori righe o colonne nel foglio di lavoro per contenere più dati o per qualche altro motivo. Al contrario, potrebbe anche essere necessario eliminare righe o colonne da posizioni specificate del foglio di lavoro.
## **Gestione di righe/colonne**
**Aspose.Cells** fornisce una classe, Workbook che rappresenta un file Excel. La classe Workbook contiene una raccolta di fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe del foglio di lavoro fornisce una raccolta Cells che rappresenta tutte le celle del foglio di lavoro.

**Cells**collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.
## **Inserimento di una riga**
 Gli sviluppatori possono inserire una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo InsertRow della raccolta Cells.**InserisciRiga** Il metodo accetta l'indice della riga in cui verrà inserita la nuova riga.

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
## **Inserimento di più righe**
A volte, gli sviluppatori potrebbero dover inserire più righe nel foglio di lavoro. Può essere fatto chiamando il metodo InsertRows della raccolta Cells. Il metodo InsertRows accetta due parametri:

- **Indice di riga**, l'indice della riga da cui verranno inserite le nuove righe
- **Numero di righe**, numero totale di righe da inserire

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
## **Eliminazione di una riga**
 Gli sviluppatori possono eliminare una riga dal foglio di lavoro in qualsiasi posizione chiamando il metodo**Elimina riga** metodo della raccolta Cells.**Elimina riga** Il metodo prende l'indice della riga che deve essere cancellata.

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
## **Eliminazione di più righe**
Se gli sviluppatori devono eliminare più righe dal foglio di lavoro, è possibile farlo anche chiamando il metodo DeleteRows della raccolta Cells. Il metodo DeleteRows accetta due parametri:

- **Indice di riga**, l'indice della riga da cui verranno eliminate le righe.
- **Numero di righe**, il numero totale di righe da eliminare.

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
## **Inserimento di una colonna**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo InsertColumn della raccolta Cells. Il metodo InsertColumn prende l'indice della colonna in cui verrà inserita la nuova colonna.

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
## **Eliminazione di una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, gli sviluppatori possono chiamare il metodo DeleteColumn della raccolta Cells. Il metodo DeleteColumn accetta l'indice della colonna da eliminare.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
