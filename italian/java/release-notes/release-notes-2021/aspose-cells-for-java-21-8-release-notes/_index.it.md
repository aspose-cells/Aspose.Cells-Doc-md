---
title: Aspose.Cells for Java 21.8 Note di rilascio
type: docs
weight: 5
url: /it/java/aspose-cells-for-java-21-8-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.8/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42494|Grande quantità di stili inutilizzati generati nella sezione CSS|
|CELLSJAVA-43576|valori del testo grafico non vengono visualizzati durante la conversione da XLSX a PDF|
|CELLSJAVA-43483|Il testo dopo un tag "br" all'interno di un tag "em" non viene enfatizzato durante la conversione di un documento HTML in una cartella di lavoro|
|CELLSJAVA-43526|IllegalArgumentException: indice di colonna non valido|
|CELLSJAVA-43557|Colore errato quando si salva come html|
|CELLSJAVA-43567|Regressione: formula MDURATION non calcolata correttamente|
|CELLSJAVA-43583|L'operatore di potenza "^" non funziona per i calcoli delle formule|
|CELLSJAVA-43549|Immagine mancante nell'output PDF|
|CELLSJAVA-43566|Caratteri predefiniti su MacOS Big Sur|
|CELLSJAVA-42579|Le etichette degli assi non vengono visualizzate correttamente - Allineamento a destra mancante durante il salvataggio di Excel in Pdf|
|CELLSJAVA-43554|Il testo del datatable del grafico non viene mostrato nell'immagine di output|
|CELLSJAVA-43556|Da XLSX a PDF: titolo del diagramma incompleto|
|CELLSJAVA-40051|Supporto Apple iWork|
|CELLSJAVA-43119|Conversione in PDF - Formato file Number3.5 non supportato dal 2014|
|CELLSJAVA-43538|Il grafico senza dati causa il danneggiamento di XLSX dopo il salvataggio con Aspose Cells|
|CELLSJAVA-43547|AutoFitRow modifica l'altezza standard del foglio di lavoro|
|CELLSJAVA-43591|Errore durante l'apertura del file in MS Excel salvato da Aspose.Cells|
|CELLSJAVA-43523|CellsException per la lettura del nome della macro della forma: formula non valida|
|CELLSJAVA-43565|"java.lang.ClassCastException" durante la lettura del file XLSB con LightCells|
|CELLSJAVA-43546|NullPointerException durante l'estrazione del nome della serie del grafico|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la classe AbstractInterruptMonitor.**

Fornisce AbstractInterruptMonitor come base delle implementazioni per il monitoraggio delle interruzioni. La classe InterruptMonitor diventa ora una sua implementazione. Il tipo di proprietà di InterruptMonitor per LoadOptions e Workbook ora diventa anche AbstractInterruptMonitor in modo che l'utente possa utilizzare la propria implementazione per controllare le operazioni che richiedono tempo.

### **Aggiunge la proprietà HtmlSaveOptions.WorksheetScalable.**

Indica se ingrandire o ridurre l'html tramite il livello di zoom del foglio di lavoro durante il salvataggio del file in html, il valore predefinito è false.

### **Aggiunge il metodo override WorksheetCollection.GetRangeByName().**

Ottiene l'oggetto Range per nome da nomi o tabelle definiti.

### **Aggiunge il metodo Range.AutoFill().**

Riempie automaticamente i dati nell'intervallo.

### **Aggiunge l'enumerazione WarningType.IO.**

Rappresenta l'avviso di file danneggiato.
