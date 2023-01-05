---
title: Pubblico API Modifiche Aspose.Cells 8.0.0
type: docs
weight: 10
url: /it/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Questa pagina elenca le modifiche API pubbliche introdotte in Aspose.Cells 8.0.0. Include non solo metodi pubblici nuovi e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influire sul codice esistente.

{{% /alert %}} 
## **Aggiunto MemorySetting a LoadOptions & WorkbookSettings**
A partire dalla v8.0.0 di Aspose.Cells for .NET abbiamo fornito le opzioni di utilizzo della memoria per considerazioni sulle prestazioni. La proprietà MemorySetting è ora disponibile nelle classi LoadOptions e WorkbookSettings.
##### **Esempio**
Dimostra come leggere un file Excel (di grandi dimensioni) in modalità ottimizzata.

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Illustra come scrivere un set di dati di grandi dimensioni in un foglio di lavoro in modalità ottimizzata.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottimizzazione della memoria mentre si lavora con file di grandi dimensioni](/cells/it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Le implementazioni di Row & Cell sono cambiate**
 Nelle versioni precedenti, gli oggetti Row e Cell venivano tenuti in memoria per rappresentare la riga e la cella corrispondenti in un foglio di lavoro. La stessa istanza è stata restituita ogni volta**RowCollection[indice int]** o**Cells[int riga, int colonna]** sono stati recuperati. Per considerazioni sulle prestazioni della memoria, solo le proprietà e i dati di Row e Cell verranno mantenuti nella memoria d'ora in avanti. Quindi, l'oggetto Row & Cell è diventato il wrapper delle suddette proprietà.
### **Esempio**
Dimostra come confrontare gli oggetti Cell e Row da ora in poi.

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Poiché gli oggetti Row e Cell vengono istanziati in base all'invocazione, non verranno mantenuti e gestiti in memoria dal componente Cells. Pertanto, dopo alcune operazioni di inserimento e cancellazione, gli indici Riga e Colonna potrebbero non essere aggiornati o, peggio ancora, questi oggetti diventerebbero non validi.
### **Esempio**
Ad esempio, il seguente frammento di codice restituirà risultati non validi utilizzando 8.0.0 e versioni successive,

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Con la nuova versione l'oggetto Cell non sarà più valido o farà riferimento ad A2 con un valore indesiderato. Per evitare tale situazione, ottenere nuovamente gli oggetti Row o Cell dalla raccolta di celle per recuperare il risultato corretto.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection non eredita più CollectionBase perché non è presente alcun oggetto Row nell'elenco interno.

{{% /alert %}}
## **Cell.StringValue Comportamento modificato**
 Nelle versioni precedenti, modello speciale_è stato ignorato durante la formattazione dei valori delle celle, dove il carattere speciale * produceva sempre un carattere nel risultato formattato. Da questa versione, abbiamo cambiato la logica per gestire i caratteri speciali_ e* per rendere il risultato formattato uguale a quello dell'applicazione Excel. Ad esempio, il formato di cella personalizzato "_(\$* #,##0.00_)" utilizzato per rappresentare il valore 123 ha prodotto il risultato come "$ 123.00". Con le nuove versioni, Cell.StringValue conterrà il risultato come "$123.00" che è lo stesso comportamento dell'applicazione Excel durante la copia della cella al testo o esportare a CSV.
## **Aggiunto CreatedTime a PdfSaveOptions**
Ora gli utenti possono ottenere o impostare l'ora di creazione PDF durante il salvataggio del foglio di calcolo su PDF durante l'utilizzo della classe PdfSaveOptions.
## **Aggiunto ShowFormulas al foglio di lavoro**
D'ora in poi, gli utenti possono utilizzare la proprietà booleana ShowFormulas offerta da Worksheet per cambiare la visualizzazione dalla formula al valore di un determinato foglio di lavoro.
## **Aggiunto Ooxml a FileFormatType**
Una nuova costante Ooxml è stata aggiunta alla classe FileFormatType per rappresentare il file XML aperto di Office crittografato come XLSX, DOCX, PPTX e altro.
## **FiltroColumnCollection obsoleto di AutoFilter**
Con Aspose.Cells for Java, la proprietà FilterColumnCollection è stata contrassegnata come obsoleta. Si suggerisce invece di utilizzare la proprietà AuotFilter.FilterColumns.
## **Sostituito SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Abbiamo sostanzialmente corretto l'errore di battitura nel nome della proprietà per SeriesCollection.SecondCatergoryData. È ora possibile utilizzare la proprietà SeriesCollection.SecondCategoryData, mentre la proprietà originale SeriesCollection.SecondCatergoryData è stata contrassegnata come obsoleta.
