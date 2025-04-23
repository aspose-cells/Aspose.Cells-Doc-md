---
title: Assemblare fogli di calcolo
type: docs
weight: 10
url: /it/net/assemble-spreadsheets/
---

Questa sezione descrive come:

Creare un nuovo file Excel da zero e aggiungere un foglio di lavoro ad esso.

- Aggiungi fogli di lavoro a fogli di calcolo di progettazione.
- Accedere ai fogli di lavoro usando il nome del foglio.
- Rimuovere un foglio di lavoro da un file Excel utilizzando il suo nome foglio.
- Rimuovere un foglio di lavoro da un file Excel utilizzando il suo indice di foglio.
- Aspose.Cells fornisce una classe, Workbook che rappresenta un file Excel. La classe Workbook contiene una raccolta di fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro.
## **Aggiungere fogli di lavoro a un nuovo file Excel**
Per creare un nuovo file Excel in modo programmatico:

- Creare un oggetto della classe Workbook.
- Chiamare il metodo Aggiungi della raccolta di fogli di lavoro. Viene aggiunto automaticamente un foglio di lavoro vuoto al file Excel. Può essere referenziato passando l'indice di foglio del nuovo foglio di lavoro alla raccolta di fogli di lavoro.
- Ottenere un riferimento al foglio di lavoro.
- Svolgere lavori sui fogli di lavoro.
- Salva il nuovo file Excel con nuovi fogli di lavoro chiamando il metodo Salva della classe Workbook.

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
## **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**
Il processo di aggiunta di fogli di lavoro a un foglio di calcolo predefinito è identico a quello di aggiunta di un nuovo foglio di lavoro, tranne che il file Excel esiste già quindi dovrebbe essere aperto prima che siano aggiunti i fogli di lavoro. Un foglio di calcolo di progettazione può essere aperto dalla classe Workbook.

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
## **Accesso ai fogli di lavoro utilizzando il nome del foglio**
Accedi o ottieni qualsiasi foglio di lavoro specificando il suo nome o indice.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Rimozione dei fogli di lavoro utilizzando il nome del foglio**
Per rimuovere fogli di lavoro da un file, chiamare il metodo RimuoviAt della raccolta Fogli di lavoro. Passa il nome del foglio al metodo RimuoviAt per rimuovere un foglio di lavoro specifico.

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
## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**
La rimozione dei fogli di lavoro per nome funziona bene quando si conosce il nome del foglio di lavoro. Se non si conosce il nome del foglio di lavoro, utilizzare una versione sovraccaricata del metodo RimuoviAt che prende l'indice del foglio di lavoro invece del suo nome foglio.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
