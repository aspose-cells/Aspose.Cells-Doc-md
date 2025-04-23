---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.0.0
type: docs
weight: 20
url: /it/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Questa pagina elenca i cambiamenti nell'API pubblica introdotti in Aspose.Cells 8.0.0. Include non solo nuovi metodi pubblici e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influenzare il codice esistente.

{{% /alert %}} 
## **Aggiunta MemorySetting a LoadOptions e WorkbookSettings**
A partire dalla v8.0.0 di Aspose.Cells for Java abbiamo fornito le opzioni di utilizzo della memoria per considerazioni sulle prestazioni. La proprietà MemorySetting è ora disponibile nelle classi LoadOptions e WorkbookSettings.
### **Esempio**
Dimostra come leggere un file Excel (di grandi dimensioni) in modalità ottimizzata.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Dimostra come scrivere un ampio dataset in un foglio di calcolo in modalità ottimizzata.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Ottimizzare la Memoria durante il Lavoro con File di Grandi Dimensioni](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Le implementazioni di Row e Cell sono cambiate**
Nelle versioni precedenti, gli oggetti Row e Cell venivano mantenuti in memoria per rappresentare la riga e la cella corrispondenti in un foglio di lavoro. La stessa istanza veniva restituita ogni volta che veniva recuperato **RowCollection[int index]** o **Cells[int row, int column]**. Per considerazioni sulle prestazioni della memoria, ora verranno mantenute in memoria solo le proprietà e i dati di Row e Cell. Pertanto, l'oggetto Row e Cell è diventato l'incapsulatore delle suddette proprietà.
### **Esempio**
Dimostra come confrontare gli oggetti Cell e Row da ora in poi.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Poiché gli oggetti Row e Cell vengono istanziati in base all'invocazione, non saranno più mantenuti e gestiti in memoria dal componente Cells. Pertanto, dopo alcune operazioni di inserimento e cancellazione, gli indici di riga e colonna potrebbero non essere aggiornati o, ancor peggio, questi oggetti diventano non validi.
### **Esempio**
Ad esempio, il seguente frammento di codice restituirà risultati non validi utilizzando la versione 8.0.0 e successiva.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Con la nuova versione, l'oggetto Cell diventerà non valido o farà riferimento a A2 con qualche valore indesiderato. Per evitare una situazione del genere, ottenere nuovamente gli oggetti Row o Cell dalla raccolta di celle per recuperare il risultato corretto.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection non eredita più da CollectionBase perché non c'è più l'oggetto Row nella sua lista interna.

{{% /alert %}}
## **Il comportamento di Cell.StringValue è cambiato**
Nelle versioni precedenti, il modello speciale _ veniva ignorato durante la formattazione dei valori delle celle, mentre il carattere speciale * produceva sempre un unico carattere nel risultato formattato. Da questa versione, abbiamo cambiato la logica per gestire i caratteri speciali _ e * per rendere il risultato formattato uguale a quello dell'applicazione Excel. Ad esempio, il formato personalizzato della cella "_(\$* #,##0.00_)" utilizzato per rappresentare il valore 123 produceva il risultato come "$ 123.00". Con le nuove versioni, Cell.StringValue conterrà il risultato come "$123.00", che è lo stesso comportamento dell'applicazione Excel durante la copia della cella in testo o l'esportazione in CSV.
## **Aggiunto CreatedTime a PdfSaveOptions**
Ora gli utenti possono ottenere o impostare l'ora di creazione del PDF durante il salvataggio del foglio di calcolo in PDF utilizzando la classe PdfSaveOptions.
## **Aggiunto ShowFormulas a Worksheet**
D'ora in poi, gli utenti possono utilizzare la proprietà booleana ShowFormulas offerta da Worksheet per passare dalla visualizzazione della formula al valore di un dato foglio di lavoro.
## **Aggiunto Ooxml a FileFormatType**
È stata aggiunta una nuova costante Ooxml alla classe FileFormatType per rappresentare il file open XML cifrato come XLSX, DOCX, PPTX e altro ancora.
## **La raccolta di filtri delle colonne di AutoFilter è stata resa obsoleta**
Con Aspose.Cells for Java, il metodo getFilterColumnCollection è stato contrassegnato come obsoleto. Si consiglia di utilizzare il metodo AuotFilter.getFilterColumns al suo posto.
## **Sostituito SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Abbiamo corretto essenzialmente l'errore di battitura nel nome del metodo per SeriesCollection.getSecondCatergoryData. È possibile utilizzare ora il metodo SeriesCollection.getSecondCategoryData, mentre il metodo originale SeriesCollection.getSecondCatergoryData è stato contrassegnato come obsoleto.
{{< app/cells/assistant language="java" >}}
