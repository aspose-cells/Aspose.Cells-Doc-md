---
title: Pubblico API Modifiche Aspose.Cells 8.0.0
type: docs
weight: 20
url: /it/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Questa pagina elenca le modifiche API pubbliche introdotte in Aspose.Cells 8.0.0. Include non solo metodi pubblici nuovi e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influire sul codice esistente.

{{% /alert %}} 
## **Aggiunto MemorySetting a LoadOptions & WorkbookSettings**
A partire dalla v8.0.0 di Aspose.Cells for Java abbiamo fornito le opzioni di utilizzo della memoria per considerazioni sulle prestazioni. La proprietà MemorySetting è ora disponibile nelle classi LoadOptions e WorkbookSettings.
### **Esempio**
Dimostra come leggere un file Excel (di grandi dimensioni) in modalità ottimizzata.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Illustra come scrivere un set di dati di grandi dimensioni in un foglio di lavoro in modalità ottimizzata.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottimizzazione della memoria mentre si lavora con file di grandi dimensioni](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)S.

{{% /alert %}}
## **Le implementazioni di Row & Cell sono cambiate**
 Nelle versioni precedenti, gli oggetti Row e Cell venivano tenuti in memoria per rappresentare la riga e la cella corrispondenti in un foglio di lavoro. La stessa istanza è stata restituita ogni volta**RowCollection[indice int]** o**Cells[int riga, int colonna]** sono stati recuperati. Per considerazioni sulle prestazioni della memoria, solo le proprietà e i dati di Row e Cell verranno mantenuti nella memoria d'ora in avanti. Quindi, l'oggetto Row & Cell è diventato il wrapper delle suddette proprietà.
### **Esempio**
Dimostra come confrontare gli oggetti Cell e Row da ora in poi.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Poiché gli oggetti Row e Cell vengono istanziati in base all'invocazione, non verranno mantenuti e gestiti in memoria dal componente Cells. Pertanto, dopo alcune operazioni di inserimento e cancellazione, gli indici Riga e Colonna potrebbero non essere aggiornati o, peggio ancora, questi oggetti diventerebbero non validi.
### **Esempio**
Ad esempio, il seguente frammento di codice restituirà risultati non validi utilizzando 8.0.0 e versioni successive,

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Con la nuova versione l'oggetto Cell non sarà più valido o farà riferimento ad A2 con un valore indesiderato. Per evitare tale situazione, ottenere nuovamente gli oggetti Row o Cell dalla raccolta di celle per recuperare il risultato corretto.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection non eredita più CollectionBase perché non è presente alcun oggetto Row nell'elenco interno.

{{% /alert %}}
## **Cell.StringValue Comportamento modificato**
 Nelle versioni precedenti, modello speciale_è stato ignorato durante la formattazione dei valori delle celle, dove il carattere speciale * produceva sempre un carattere nel risultato formattato. Da questa versione, abbiamo cambiato la logica per gestire i caratteri speciali_ e* per rendere il risultato formattato uguale a quello dell'applicazione Excel. Ad esempio, il formato di cella personalizzato "_(\$* #,##0.00_)" utilizzato per rappresentare il valore 123 ha prodotto il risultato come "$ 123.00". Con le nuove versioni, Cell.StringValue conterrà il risultato come "$123.00" che è lo stesso comportamento dell'applicazione Excel durante la copia della cella in testo o esportare in CSV.
## **Aggiunto CreatedTime a PdfSaveOptions**
Ora gli utenti possono ottenere o impostare l'ora di creazione del PDF durante il salvataggio del foglio di calcolo in PDF durante l'utilizzo della classe PdfSaveOptions.
## **Aggiunto ShowFormulas al foglio di lavoro**
D'ora in poi, gli utenti possono utilizzare la proprietà booleana ShowFormulas offerta da Worksheet per cambiare la visualizzazione tra formula e valore di un determinato foglio di lavoro.
## **Aggiunto Ooxml a FileFormatType**
Una nuova costante Ooxml è stata aggiunta alla classe FileFormatType per rappresentare il file XML aperto di Office crittografato come XLSX, DOCX, PPTX e altro.
## **FiltroColumnCollection obsoleto di AutoFilter**
Con Aspose.Cells for Java, il metodo getFilterColumnCollection è stato contrassegnato come obsoleto. Si suggerisce invece di utilizzare il metodo AuotFilter.getFilterColumns.
## **Sostituito SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Abbiamo sostanzialmente corretto l'errore di battitura nel nome del metodo per SeriesCollection.getSecondCatergoryData. È possibile utilizzare il metodo SeriesCollection.getSecondCategoryData ora in poi, mentre il metodo originale SeriesCollection.getSecondCatergoryData è stato contrassegnato come obsoleto.
