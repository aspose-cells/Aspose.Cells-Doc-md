---
title: Aggiunta di collegamenti ipertestuali per collegare i dati in Aspose.Cells
type: docs
weight: 10
url: /it/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.

Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}}

## **Aggiunta di Collegamenti Ipotestuali**

Tre tipi di collegamento ipertestuale possono essere aggiunti a una cella utilizzando Aspose.Cells:

- [Aggiungere un collegamento a un URL](#adding-link-to-a-url).
- [Aggiungere un collegamento a un'altra cella nello stesso file](#adding-a-link-to-a-cell-in-the-same-file).
- [Aggiungere un collegamento a un file esterno](#adding-a-link-to-an-external-file).

Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel utilizzando l'API o [fogli elettronici progettati](/cells/it/net/what-is-a-designer-spreadsheet/) (fogli elettronici in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells viene utilizzato per importarli in altri fogli elettronici).

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.

### **Aggiunta di un link a un URL**

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contiene una collezione [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Ogni elemento nella collezione degli collegamenti ipertestuali rappresenta un collegamento ipertestuale. Aggiungi collegamenti ipertestuali agli URL chiamando il metodo Aggiungi della collezione degli collegamenti ipertestuali. Il metodo Aggiungi richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamento ipertestuale
- URL, l'indirizzo URL.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Aggiunta di un link a una cella nello stesso file**

È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il metodo Add della collezione Hyperlink. Il metodo Add funziona sia per collegamenti interni che esterni. Una versione del metodo sovraccaricato accetta i seguenti parametri:

- Nome della cella, il nome della cella alla quale verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Aggiunta di un link a un file esterno**

È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il metodo Add della raccolta Hyperlinks. Il metodo Add richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Scarica il codice di esempio**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
