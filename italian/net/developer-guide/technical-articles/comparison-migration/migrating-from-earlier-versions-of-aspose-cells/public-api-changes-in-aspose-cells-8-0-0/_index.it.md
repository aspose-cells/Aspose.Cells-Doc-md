---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.0.0
type: docs
weight: 10
url: /it/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Questa pagina elenca i cambiamenti nell'API pubblica introdotti in Aspose.Cells 8.0.0. Include non solo nuovi metodi pubblici e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influenzare il codice esistente.

{{% /alert %}} 
## **Aggiunta MemorySetting a LoadOptions e WorkbookSettings**
A partire dalla v8.0.0 di Aspose.Cells for .NET abbiamo fornito le opzioni di utilizzo della memoria per considerazioni sulle prestazioni. La proprietà MemorySetting è ora disponibile nelle classi LoadOptions & WorkbookSettings.
##### **Esempio**
Dimostra come leggere un file Excel (di grandi dimensioni) in modalità ottimizzata.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Dimostra come scrivere un ampio dataset in un foglio di calcolo in modalità ottimizzata.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottimizzazione della memoria durante il lavoro con file di grandi dimensioni](/cells/it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Le implementazioni di Row e Cell sono cambiate**
Nelle versioni precedenti, gli oggetti Row e Cell venivano mantenuti in memoria per rappresentare la riga e la cella corrispondenti in un foglio di lavoro. La stessa istanza veniva restituita ogni volta che veniva recuperato **RowCollection[int index]** o **Cells[int row, int column]**. Per considerazioni sulle prestazioni della memoria, ora verranno mantenute in memoria solo le proprietà e i dati di Row e Cell. Pertanto, l'oggetto Row e Cell è diventato l'incapsulatore delle suddette proprietà.
### **Esempio**
Dimostra come confrontare gli oggetti Cell e Row da ora in poi.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Poiché gli oggetti Row e Cell vengono istanziati in base all'invocazione, non saranno più mantenuti e gestiti in memoria dal componente Cells. Pertanto, dopo alcune operazioni di inserimento e cancellazione, gli indici di riga e colonna potrebbero non essere aggiornati o, ancor peggio, questi oggetti diventano non validi.
### **Esempio**
Ad esempio, il seguente frammento di codice restituirà risultati non validi utilizzando la versione 8.0.0 e successiva.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Con la nuova versione, l'oggetto Cell diventerà non valido o farà riferimento a A2 con qualche valore indesiderato. Per evitare una situazione del genere, ottenere nuovamente gli oggetti Row o Cell dalla raccolta di celle per recuperare il risultato corretto.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection non eredita più da CollectionBase perché non c'è più l'oggetto Row nella sua lista interna.

{{% /alert %}}
## **Il comportamento di Cell.StringValue è cambiato**
Nelle versioni precedenti, il modello speciale _ veniva ignorato durante la formattazione dei valori delle celle, mentre il carattere speciale * produceva sempre un carattere nel risultato formattato. Da questa versione, abbiamo cambiato la logica per gestire i caratteri speciali _ e * per rendere il risultato formattato uguale a quello dell'applicazione Excel. Ad esempio, il formato personalizzato della cella "_(\$* #,##0.00_)" usato per rappresentare il valore 123 produceva il risultato come "$ 123.00". Con le nuove versioni, Cell.StringValue conterrà il risultato come "$123.00" che è lo stesso comportamento mostrato dall'applicazione Excel durante il copia della cella in testo o l'esportazione in CSV.
## **Aggiunto CreatedTime a PdfSaveOptions**
Ora gli utenti possono ottenere o impostare l'ora di creazione del PDF durante il salvataggio del foglio di calcolo in PDF utilizzando la classe PdfSaveOptions.
## **Aggiunto ShowFormulas a Worksheet**
Da ora in poi, gli utenti possono utilizzare la proprietà booleana ShowFormulas offerta da Worksheet per passare dalla visualizzazione della formula al valore di un determinato foglio di lavoro.
## **Aggiunto Ooxml a FileFormatType**
È stata aggiunta una nuova costante Ooxml alla classe FileFormatType per rappresentare il file open XML cifrato come XLSX, DOCX, PPTX e altro ancora.
## **La raccolta di filtri delle colonne di AutoFilter è stata resa obsoleta**
Con Aspose.Cells for Java, la proprietà FilterColumnCollection è stata contrassegnata come obsoleta. Si consiglia di utilizzare invece la proprietà AuotFilter.FilterColumns.
## **Sostituito SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Abbiamo corretto essenzialmente l'errore di battitura nel nome della proprietà per SeriesCollection.SecondCatergoryData. Ora puoi utilizzare la proprietà SeriesCollection.SecondCategoryData in avanti, mentre la proprietà originale SeriesCollection.SecondCatergoryData è stata contrassegnata come obsoleta.
