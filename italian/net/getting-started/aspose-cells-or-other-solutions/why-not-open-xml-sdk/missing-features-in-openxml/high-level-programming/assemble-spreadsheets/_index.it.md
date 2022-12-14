---
title: Assemblare fogli di calcolo
type: docs
weight: 10
url: /it/net/assemble-spreadsheets/
---
Questa sezione descrive come:

Crea un nuovo file Excel da zero e aggiungi un foglio di lavoro.

- Aggiungi fogli di lavoro ai fogli di lavoro del designer.
- Accedi ai fogli di lavoro utilizzando il nome del foglio.
- Rimuovi un foglio di lavoro da un file Excel usando il nome del foglio.
- Rimuovi un foglio di lavoro da un file Excel utilizzando il relativo indice del foglio.
- Aspose.Cells fornisce una classe, Workbook che rappresenta un file Excel. La classe Workbook contiene una raccolta di fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro.
## **Aggiunta di fogli di lavoro a un nuovo file Excel**
Per creare un nuovo file Excel a livello di codice:

- Creare un oggetto della classe Workbook.
- Chiamare il metodo Add della raccolta Worksheets. Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel *. È possibile fare riferimento passando l'indice del foglio del nuovo foglio di lavoro alla raccolta Fogli di lavoro.
- Ottenere un riferimento al foglio di lavoro.
- Eseguire il lavoro sui fogli di lavoro.
- Salvare il nuovo file Excel con nuovi fogli di lavoro chiamando il metodo Save della classe Workbook.

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
## **Aggiunta di fogli di lavoro a un foglio di calcolo di Designer**
Il processo di aggiunta di fogli di lavoro a un foglio di lavoro del progettista è uguale a quello di aggiunta di un nuovo foglio di lavoro, tranne per il fatto che il file Excel esiste già, quindi deve essere aperto prima dell'aggiunta dei fogli di lavoro. Un foglio di calcolo del designer può essere aperto dalla classe Workbook.

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
## **Accesso ai fogli di lavoro utilizzando il nome del foglio**
Accedi o ottieni qualsiasi foglio di lavoro specificandone il nome o l'indice.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Rimozione di fogli di lavoro utilizzando il nome del foglio**
Per rimuovere i fogli di lavoro da un file, chiama il metodo RemoveAt della raccolta Worksheets. Passare il nome del foglio al metodo RemoveAt per rimuovere un foglio di lavoro specifico.

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
## **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
La rimozione dei fogli di lavoro per nome funziona bene quando il nome del foglio di lavoro è noto. Se non conosci il nome del foglio di lavoro, usa una versione di overload del metodo RemoveAt che accetta l'indice del foglio di lavoro invece del nome del foglio.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
