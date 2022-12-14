---
title: Aspose.Cells for .NET 21.8 Note di rilascio
type: docs
weight: 5
url: /it/net/aspose-cells-for-net-21-8-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.8](https://www.nuget.org/packages/Aspose.Cells/21.8.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-48470|Supporta il ridimensionamento delle pagine del foglio di lavoro durante l'esportazione di file in HTML|Nuova caratteristica|
|CELLSNET-41286|Supporta mappe XML|Nuova caratteristica|
|CELLSNET-45255|Supporto per i numeri .number di Apple? formato del file|Nuova caratteristica|
|CELLSNET-47737| Supporto per la lettura dell'ultimo formato di file Apples .numbers|Nuova caratteristica|
|CELLSNET-48205|Aggiunta la funzione MS Excel per gestire il riempimento automatico (modello) per numeri, testo o date, ecc.|Nuova caratteristica|
|CELLSNET-48435|Unisci più spazi vuoti nell'output html.|Aumento|
|CELLSNET-46412|La licenza non funziona nella versione di rilascio dell'applicazione MVC quando viene distribuita sul server IIS|Aumento|
|CELLSNET-47888|SmartMarker appropriati necessari per ottenere l'output desiderato|Aumento|
|CELLSNET-48452|Supporta la lettura dei file dei numeri di forma immagine 09.|Aumento|
|CELLSNET-48372|Aspetta salva in html per il file XLSB|Prestazione|
|CELLSNET-48091|L'oggetto con rotazione è distorto.|Insetto|
|CELLSNET-48173|Sposta i testi nelle forme del diagramma|Insetto|
|CELLSNET-48241|La posizione del testo nella forma del pentagono è errata|Insetto|
|CELLSNET-48247|La freccia di flessione scompare durante la conversione in pdf.|Insetto|
|CELLSNET-48363|La posizione del rich text viene calcolata ripetutamente, provocando lo spostamento del testo verso l'alto.|Insetto|
|CELLSNET-47839|Shape to image Errore durante il salvataggio di XLSX in PDF|Insetto|
|CELLSNET-48312|Problema con il livello di zoom nell'output html.|Insetto|
|CELLSNET-48329|Problema di allineamento dell'immagine durante l'esportazione dell'intervallo in HTML|Insetto|
|CELLSNET-48333| Le colonne della tabella nell'intervallo con l'allineamento in basso vengono combinate nell'HTML convertito|Insetto|
|CELLSNET-48365| I filtri dei dati creati dai campi base della tabella pivot non funzionano|Insetto|
|CELLSNET-48359|Le macro vengono rimosse dopo la migrazione da XLS a XLSM|Insetto|
|CELLSNET-48448|L'origine dati del grafico con intervallo denominato non viene analizzata correttamente|Insetto|
|CELLSNET-47369|Punto del grafico mancante e forma schiacciata nell'immagine EMF generata|Insetto|
|CELLSNET-48497|Il file xlsx generato viene interrotto dopo aver collegato la cella a XmlMap|Insetto|
|CELLSNET-48132| Problema durante la modifica della posizione dell'etichetta dati del grafico a ciambella|Insetto|
|CELLSNET-48385|Da XLSX a TIFF: le barre del grafico non vengono visualizzate nell'output|Insetto|
|CELLSNET-48386|Nome del carattere errato per il nome del carattere dell'etichetta del segno di spunta dell'asse delle categorie|Insetto|
|CELLSNET-48503|L'allineamento del titolo dell'asse è spostato nel pdf di output|Insetto|
|CELLSNET-48509|Il grafico a volte non viene visualizzato in base alla posizione della legenda|Insetto|
|CELLSNET-48374|L'immagine inserita in un documento excel viene ridimensionata quando viene modificato il carattere predefinito|Insetto|
|CELLSNET-48384|Impostazione di Array su Range.Value : esce o fuori dai limiti dell'area di intervallo|Insetto|
|CELLSNET-48410|Allineamento automatico al centro quando si passa un elenco di stringhe con i marcatori intelligenti|Insetto|
|CELLSNET-48460|Le PowerQuery vengono perse dopo la sostituzione|Insetto|
|CELLSNET-48478|Il contenuto del file XML non viene caricato|Insetto|
|CELLSNET-48492|Problema con 100% Stacked Bar e l'unità principale e l'unità minore|Insetto|
|CELLSNET-48504|Indice di colonna non valido durante la conversione di XLSX|Insetto|
|CELLSNET-48512|La cancellazione del filtro automatico non funziona correttamente|Insetto|
|CELLSNET-48477|Il metodo PivotTable.CalculateData genera un'eccezione|Eccezione|
|CELLSNET-48395|Shape to image genera un'eccezione nell'ambiente docker per il file Display.xlsx|Eccezione|
|CELLSNET-48367|Eccezione generata quando PlotArea width è 0|Eccezione|
|CELLSNET-48172|"Errore da forma a immagine" durante la conversione di file Excel in PDF|Eccezione|
|CELLSNET-48490|"Operazioni matematiche risultano in abbondanza." eccezione quando si apre il file XLS|Eccezione|
|CELLSNET-48545|Eccezione sollevata durante la chiamata a Shape.UpdateSelectedValue()|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la classe AbstractInterruptMonitor.**

Fornisce AbstractInterruptMonitor come base delle implementazioni per il monitoraggio delle interruzioni. La classe InterruptMonitor diventa ora una sua implementazione. Il tipo di proprietà di InterruptMonitor per LoadOptions e Workbook ora diventa anche AbstractInterruptMonitor in modo che l'utente possa utilizzare la propria implementazione per controllare le operazioni che richiedono tempo.

### **Aggiunge la proprietà HtmlSaveOptions.WorksheetScalable.**

Indica se si esegue lo zoom avanti o indietro dell'html tramite il livello di zoom del foglio di lavoro durante il salvataggio del file in html, il valore predefinito è false.

### **Aggiunge il metodo override WorksheetCollection.GetRangeByName().**

Ottiene l'oggetto Range per nome da nomi o tabelle definiti.

### **Aggiunge il metodo Range.AutoFill().**

Riempie automaticamente i dati nell'intervallo.

### **Aggiunge l'enumerazione WarningType.IO.**

Rappresenta l'avviso di file danneggiato.

