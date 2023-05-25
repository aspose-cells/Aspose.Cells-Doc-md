---
title: Aspose.Cells for Node.js via Java 23.1 Note di rilascio
type: docs
weight: 12
url: /it/nodejs-java/aspose-cells-for-node-js-via-java-23-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Node.js via Java 23.1](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-23.1/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSJAVA-44172|Supporta l'interruzione durante il calcolo delle formule per una cella|
|CELLSJAVA-45029|Supporta lo zoom del foglio, blocca i riquadri durante l'esportazione e l'importazione di html|
|CELLSJAVA-45034|Come codificare/utilizzare l'opzione flag filtro riga 1|
|CELLSJAVA-45003|Da XLS a HTML: la forma del rettangolo è distorta|
|CELLSJAVA-45004|Da XLS a HTML: immagine tagliata e spostata fuori posto|
|CELLSJAVA-44364|Differenza di valori tra un file Excel e il file PDF (tramite Aspose.Cells) convertito|
|CELLSJAVA-45026|Virgolette doppie " dal file XLSX non mostrato nel file PDF convertito|
|CELLSJAVA-45035|La funzione DATEDIF non funziona correttamente con gli anni bisestili|
|CELLSJAVA-45008|Elementi della legenda del grafico tagliati nell'immagine di output|
|CELLSJAVA-45036|Regressione: il grafico è stato ridimensionato in modo errato|
|CELLSJAVA-45017|non è possibile cambiare foglio di lavoro nel progetto demo Java per il file con password|
|CELLSJAVA-44942|Colori persi durante l'esportazione di un grafico in EMF|
|CELLSJAVA-45005|Il carattere con il nome completo del carattere non viene selezionato durante la conversione in pdf|
|CELLSJAVA-45033|Il foglio di lavoro sull'immagine EMF non è corretto dopo aver impostato l'opzione di risoluzione|
|CELLSJAVA-44971|Le immagini non possono essere visualizzate durante il caricamento del flusso html|
|CELLSJAVA-45020|HTML in EXCEL: stili modificati|
|CELLSJAVA-45021|"com.aspose.cells.CellsException: riferimento al foglio non valido per il nome definito" durante il rendering di un file Excel in PDF|
|CELLSJAVA-45025|ArrayIndexOutOfBoundsException al salvataggio della cartella di lavoro|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la classe PivotGlobalizationSettings.**

La classe gestisce tutte le impostazioni di globalizzazione relative alla tabella pivot.

###  **Rimuove il metodo GlobalizationSettings.GetOtherName().**

Questo metodo non è più stato referenziato, non ha alcun effetto anche se l'utente lo implementa in GlobalizationSettings. Quindi lo rimuoviamo ora. L'utente deve invece utilizzare il metodo ChartGlobalizationSettings.GetOtherName().

###  **Rimuove i metodi GlobalizationSettings.GetColumnLablesName()/GetRowLablesName().**

Utilizzare PivotGlobalizationSettings.GetTextOfColumnLabels()/GetTextOfRowLabels().

###  **Rende obsoleti tutti i metodi sulla tabella pivot in GlobalizationSettings.**

Utilizzare i metodi corrispondenti in PivotGlobalizationSettings.

###  **Aggiunge il metodo SetStyle() per la classe Row e Column.**

Supporta l'impostazione di uno stile personalizzato per l'intera riga/colonna. Per l'impostazione dello stile personalizzato, la differenza tra SetStyle() e ApplyStyle() è che SetStyle() non modifica le impostazioni di stile per le celle esistenti.

###  **Aggiunge la proprietà HasCustomStyle per le classi Cell, Row e Column.**

Indica se la cella, riga o colonna è stata impostata con impostazioni di stile personalizzate (diverse da quella predefinita che eredita).

###  **Aggiunge la proprietà JsonSaveOptions.AlwaysExportAsJsonObject.**

Indica se esportare sempre i file Excel come oggetto Json anche se è presente un solo foglio di lavoro.

###  **Aggiunge la classe RevisionHeader e la proprietà RevisionLog.MetadataTable.**

Supporta l'ottenimento e l'impostazione delle proprietà del registro delle revisioni.

###  **Aggiunge il metodo Style.GetTwoColorGradientSetting() e rende obsoleto il metodo Style.GetTwoColorGradient().**

Utilizzare invece il metodo Style.GetTwoColorGradientSetting().

###  **Rende obsoleto JsonUtility.ExportRangeToJson(Range,ExportRangeToJsonOptions) e aggiunge JsonUtility.ExportRangeToJson(Range, JsonSaveOptions)**

Usare invece il metodo ExportRangeToJson(Range, JsonSaveOptions).

###  **Aggiunge la proprietà Charts.Axis.CustomUnit.**

Specifica un valore personalizzato per l'unità di visualizzazione.

###  **Proprietà Charts.Axis.CustUnit obsoleta.**

Utilizzare invece Charts.Axis.CustomUnit.

###  **Aggiunge la proprietà Charts.Chart.PlotVisibleCellsOnly.**

Indica se tracciare solo le celle visibili.

###  **Proprietà Charts.Chart.PlotVisibleCells obsoleta.**

Utilizzare invece Charts.Chart.PlotVisibleCellsOnly.

###  **Rimuove la proprietà ShapeFormat.FillFormat.**

Utilizzare invece la proprietà ShapeFormat.Fill.

###  **Rimuove la proprietà ShapeFormat.Outline.**

Utilizzare invece la proprietà ShapeFormat.Line.