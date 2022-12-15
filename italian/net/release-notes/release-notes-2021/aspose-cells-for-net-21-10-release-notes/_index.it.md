---
title: Aspose.Cells for .NET 21.10 Note di rilascio
type: docs
weight: 3
url: /it/net/aspose-cells-for-net-21-10-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.10](https://www.nuget.org/packages/Aspose.Cells/21.10.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-49192| Problema con il recupero di intervalli (RefersTo) con una funzione offset|Nuova caratteristica|
|CELLSNET-49132|Apri i file con la tabella HTML all'interno come file XLS|Nuova caratteristica|
|CELLSNET-49173|Supporta la proprietà Range.CurrentRegion|Nuova caratteristica|
|CELLSNET-49015|Aggiorna collegamento ipertestuale(Foglio1!A1) quando si modifica il nome del foglio di lavoro.|Aumento|
|CELLSNET-49021|La formattazione condizionale di ods viene persa in MS Excel se il tipo è "Contiene testo"|Aumento|
|CELLSNET-49280|Supporta l'intervallo di riempimento automatico con il tipo di riempimento|Aumento|
|CELLSNET-49413|Rimuovi le forme invisibili durante il rendering dell'HTML|Aumento|
|CELLSNETCORE-135|L'applicazione si interrompe durante il calcolo di file di grandi dimensioni e UDF|Prestazione|
|CELLSNET-49124|Pulsanti di opzione sfocati durante la conversione di XLSM in HTML|Insetto|
|CELLSNET-49115|Calcolo errato degli operatori nella formula quando gli operandi sono intervalli|Insetto|
|CELLSNETCORE-132|Grafico distorto creato in Html convertito|Insetto|
|CELLSNETCORE-141|Testo mancante, allineamento errato del testo e percentuali mancanti nel grafico|Insetto|
|CELLSNET-49067|Problema con il recupero e l'impostazione del colore della scheda in GridDesktop|Insetto|
|CELLSNET-49069|Aspose.Cells.GridWeb SessionMode non funziona|Insetto|
|CELLSNET-49118|Problema con l'importazione XML|Insetto|
|CELLSNET-49195|La conversione da XLSX a HTML non conserva la sequenza di caratteri invisibili|Insetto|
|CELLSNET-49245|L'immagine si sposta in file XLS specifici durante il rendering in HTML|Insetto|
|CELLSNET-49246|L'immagine non è visibile durante la conversione di un file XLSX specifico in HTML|Insetto|
|CELLSNET-49334| Problema con il testo del carattere nel campo del piè di pagina per il rendering di Excel|Insetto|
|CELLSNET-49393|Impossibile importare correttamente il file XML nel file modello|Insetto|
|CELLSNETCORE-226|Spazi bianchi non necessari resi durante la conversione da Excel a EMF|Insetto|
|CELLSNET-49091|Il nodo "strCache" mancante in un XML|Insetto|
|CELLSNET-49161|Non è più possibile copiare i nomi dei caratteri corretti dell'etichetta di spunta dell'asse dei valori|Insetto|
|CELLSNET-49191|Impossibile mostrare i valori percentuali nell'etichetta dati|Insetto|
|CELLSNET-49305|Mancano alcune etichette dati nel grafico|Insetto|
|CELLSNET-49374|La linea del grafico è diversa con la funzione Chart.ToImage rispetto a Excel|Insetto|
|CELLSNET-48613|Una risorsa che non rientra nell'intervallo selezionato non deve essere esportata in HTML|Insetto|
|CELLSNET-49027|Distorsione del colore e del layout della pagina del documento|Insetto|
|CELLSNET-49145|Informazioni DataMashup non recuperate dal file Excel|Insetto|
|CELLSNET-49146|La filigrana nel file Excel non può essere generata e visualizzata correttamente|Insetto|
|CELLSNET-49239|L'effetto ombra viene applicato alle immagini durante la conversione da XLSM a XLS|Insetto|
|CELLSNET-49244|La formattazione condizionale dell'icona viene persa durante il salvataggio come html|Insetto|
|CELLSNET-49328|Errore durante la copia dei fogli di lavoro|Insetto|
|CELLSNET-49365|Il testo viene ritagliato nell'output della stampante dopo la chiamata a AutoFitRows|Insetto|
|CELLSNET-49366|Problema con i campi di input di convalida dei dati Cell in formato XLSB|Insetto|
|CELLSNETCORE-269|Nella tabella HTML viene aggiunta una riga errata con un'altezza elevata|Insetto|
|CELLSNETCORE-270|Problemi con HtmlString Font quando Excel è stato salvato come HTML una volta|Insetto|
|CELLSNET-49375|Problema durante l'aggiornamento della tabella pivot dopo l'aggiunta di dati|Insetto|
|CELLSNET-49194|Eccezione durante il caricamento del file excel|Eccezione|
|CELLSNET-49363|Il metodo CalculateData sulla tabella pivot genera un'eccezione|Eccezione|
|CELLSNET-49373|"La stringa di input non era in un formato corretto." eccezione quando si apre il file XLSX|Eccezione|
|CELLSNET-49394|Eccezione nulla quando si apre il file NUMBERS|Eccezione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Aggiunge il metodo di overload Name.GetRefersTo().**

Ottiene l'espressione della formula basata sulla cella specificata.

### **Aggiunge il metodo di overload Range.AutoFill().**

Riempi automaticamente l'intervallo target con il tipo di riempimento.

### **Aggiunge la proprietà Comment.IsThreadedComment.**

Indica se questo commento è un commento con thread.

### **Aggiunge la proprietà HtmlSaveOptions.IgnoreInvisibleShapes.**

Indica se inserire forme invisibili durante il salvataggio di html.

### **Aggiunge la proprietà Range.CurrentRegion.**

Restituisce un intervallo delimitato da qualsiasi combinazione di righe e colonne vuote.

### **Aggiunge la classe AxisBins.**

 Rappresenta i contenitori degli assi per i grafici a istogrammi.

### **Metodo obsoleto SheetRender.GetPageSize(int pageIndex)**

Usare invece SheetRender.GetPageSizeInch(int pageIndex).

### **Aggiunge il metodo SheetRender.GetPageSizeInch(int pageIndex)**

Ottieni la dimensione della pagina dell'immagine di output? in unità di pollice.

### **Metodo obsoleto WorkbookRender.GetPageSize(int pageIndex)**

Usare invece WorkbookRender.GetPageSizeInch(int pageIndex).

### **Aggiunge il metodo WorkbookRender.GetPageSizeInch(int pageIndex)**

Ottieni l'immagine di output delle dimensioni della pagina? in unità di pollici.

