---
title: Aspose.Cells for Java 21.7 Note di rilascio
type: docs
weight: 6
url: /it/java/aspose-cells-for-java-21-7-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.7/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43477|Firma digitalmente un progetto di codice VBA con certificato utilizzando Aspose.Cells for Java|
|CELLSJAVA-40452|Ottieni intervalli di dati e dettagli esterni|
|CELLSJAVA-42494|Grande quantità di stili inutilizzati generati nella sezione CSS|
|CELLSJAVA-41121|SheetRender non esegue correttamente il rendering del diagramma di flusso|
|CELLSJAVA-43331|Testo mancante nel cerchio durante la conversione da XLS a HTML|
|CELLSJAVA-43507|Quando si esegue svg per inserire excel sotto java, esce in modo anomalo.|
|CELLSJAVA-41887|I dati percentuali di una tabella pivot non vengono visualizzati correttamente in HTML|
|CELLSJAVA-43482|Apici e pedici non formattati correttamente durante la conversione di un documento HTML in una cartella di lavoro|
|CELLSJAVA-43501|Valore errato letto utilizzando la funzione getStringValue()|
|CELLSJAVA-43515|Problema con la formula MDURATION|
|CELLSJAVA-43528|La data e l'ora di creazione e la data di aggiornamento non possono essere estratte|
|CELLSJAVA-43529|Impossibile estrarre BuiltInDocumentProperties|
|CELLSJAVA-43530|I risultati delle proprietà di data e ora sono diversi|
|CELLSJAVA-41693|L'equazione in una casella di testo non viene visualizzata in PDF|
|CELLSJAVA-43487|Testo non centrato nel PDF di output nella conversione da Excel a PDF|
|CELLSJAVA-42867|Le forme non vengono recuperate nel formato di file ODS|
|CELLSJAVA-42895|L'output PNG del grafico MS Excel presenta discrepanze|
|CELLSJAVA-43015|Problema con SheetRender.toImage() durante l'utilizzo del metodo setPrintArea()|
|CELLSJAVA-43258|Il grafico indica che l'audacia dei caratteri cambia dopo la copia della cartella di lavoro|
|CELLSJAVA-43436|Aspose Cells ignora l'asse y invertito nel diagramma|
|CELLSJAVA-43510|Il grafico è incasinato dopo aver salvato nuovamente il file Excel utilizzando Aspose.Cells for Java|
|CELLSJAVA-43532|Problema durante l'estrazione dei nomi delle serie di grafici|
|CELLSJAVA-43474|Gli oggetti di forma sono cambiati durante il caricamento e il salvataggio del file XLS|
|CELLSJAVA-43493|Viene recuperato l'autore del commento errato|
|CELLSJAVA-43527|Aspose.Cells for Java NullPointerException|
|CELLSJAVA-43506|Eccezione password non valida|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà PasteOptions.OperationType e PasteOperationType enum .**

 Ottiene e imposta il tipo di operazione quando si incolla l'intervallo.

### **Aggiunge il metodo PivotFormatCondition.AddColumnAreaCondition(PivotField columnField) .**

Aggiunge il limite del formato condizionale della tabella pivot nei campi della colonna.

### **Aggiunge il metodo PivotFormatCondition.AddColumnAreaCondition(String fieldName).**

Aggiunge il limite del formato condizionale della tabella pivot nei campi della colonna.

### **Aggiunge il metodo PivotFormatCondition.AddRowAreaCondition(PivotField rowField) .**

Aggiunge il limite del formato condizionale della tabella pivot nei campi riga.

### **Aggiunge il metodo PivotFormatCondition.AddRowAreaCondition(String fieldName).**

Aggiunge il limite del formato condizionale della tabella pivot nei campi riga.

### **Aggiunge il metodo PivotFormatCondition.AddDataAreaCondition(PivotField dataField) .**

Aggiunge il limite del formato condizionale della tabella pivot nei campi dati.

### **Aggiunge il metodo PivotFormatCondition.AddDataAreaCondition(String fieldName).**

Aggiunge il limite del formato condizionale della tabella pivot nei campi dati.

### **Aggiunge il metodo PivotFormatCondition.SetConditionalAreas().**

Imposta le aree condizionali dell'oggetto PivotFormatCondition.

### **Aggiunge il metodo SeriesCollection.Add(boolean,boolean).**

Aggiunge serie con un intervallo.

### **Aggiunge il metodo SetSeriesNames().**

Imposta un intervallo come nome della serie.
