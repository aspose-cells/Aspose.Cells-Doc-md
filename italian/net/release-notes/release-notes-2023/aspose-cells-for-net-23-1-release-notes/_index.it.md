---
title: Aspose.Cells for .NET 23.1 Note di rilascio
type: docs
weight: 12
url: /it/net/aspose-cells-for-net-23-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 23.1](https://www.nuget.org/packages/Aspose.Cells/23.1.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSNET-50111|Supporta l'interruzione durante il calcolo delle formule|
|CELLSNET-52496|Supporto per modificare lo stile predefinito di riga/colonna senza modificare le impostazioni di stile delle celle esistenti|
|CELLSNET-52505|Supporta nuove funzioni HSTACK/VSTACK|
|CELLSNET-52429|Supporto per ottenere l'autore e la data e l'ora delle revisioni|
|CELLSNET-52337|Supporta le formule CHOOSECOLS e CHOOSEROWS Excel 365|
|CELLSNET-52498| Migliora SaveOptions.HasHeaderRow quando converti xlsx in json|
|CELLSNET-52499|JSON valore manca quando un foglio è vuoto|
|CELLSNET-52500|JsonSaveOptions.SkipEmptyRows non funziona correttamente|
|CELLSNET-52502|Esporta sempre Excel come JObject durante la conversione da Excel a JSON|
|CELLSNET-52418|Il riempimento della forma non è corretto durante la conversione in pdf|
|CELLSNET-52420| Le forme e le immagini vengono deformate in Excel al rendering PDF dopo la copia del foglio|
|CELLSNET-52437|Ombra errata durante la conversione dell'immagine in pdf|
|CELLSNET-52494|Errore di spostamento del segno di freccia durante la conversione del file Excel in PDF|
|CELLSNET-52442|SOMMA.SE restituisce 4 invece di 0 dal motore di calcolo della formula Aspose.Cells|
|CELLSNET-52441|L'immagine convertita dal grafico non è la stessa di MS Excel|
|CELLSNET-52486|Vulnerabilità della sicurezza - CVE-2021-24112|
|CELLSNET-52410|Immagine a SVG - Il testo è sovrapposto per la barra orizzontale per le etichette della data dell'immagine del grafico|
|CELLSNET-52366| Linee più spesse e bordo mancante durante il salvataggio di XLSB in un'immagine|
|CELLSNET-52395|Il file Excel (XLS) è danneggiato al nuovo salvataggio tramite Aspose.Cells|
|CELLSNET-52435|Supporta i criteri di filtro durante l'apertura e il salvataggio di html|
|CELLSNET-52440|L'intervallo del pivottable non è lo stesso di MS Excel durante la conversione del pivottable in pdf|
|CELLSNET-52458|Il contenuto e la formattazione dei fogli vengono modificati durante la copia|
|CELLSNET-52493|Eccezione "L'elemento è già stato aggiunto". al salvataggio da XLS a XLSX|
|CELLSNET-48991|Il riferimento non impostato su un'istanza di un oggetto. eccezione quando si apre il file ODS|
|CELLSNET-52419|L'eccezione di indice fuori intervallo si verifica dopo la copia del foglio e la conversione in pdf|
|CELLSNET-52433|Eccezione "File danneggiato" durante il caricamento di un file XLSX con un collegamento ipertestuale|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la classe PivotGlobalizationSettings.**

La classe gestisce tutte le impostazioni di globalizzazione relative alla tabella pivot.

###  **Rimuove il metodo GlobalizationSettings.GetOtherName().**

Questo metodo non è più stato referenziato, non ha alcun effetto anche se l'utente lo implementa in GlobalizationSettings. Quindi lo rimuoviamo ora. L'utente deve invece utilizzare il metodo ChartGlobalizationSettings.GetOtherName().

###  **Rimuove i metodi GlobalizationSettings.GetColumnLablesName()/GetRowLablesName().**

Utilizzare PivotGlobalizationSettings.GetTextOfColumnLabels()/GetTextOfRowLabels().

###  **Rende obsoleti tutti i metodi sulla tabella pivot in GlobalizationSettings.**

Utilizzare i metodi corrispondenti in PivotGlobalizationSettings.

###  **Aggiunge i metodi GetStyle()/SetStyle() per la classe Row e Column.**

Supporta per ottenere/impostare uno stile personalizzato per l'intera riga/colonna. Per l'impostazione dello stile personalizzato, la differenza tra SetStyle() e ApplyStyle() è che SetStyle() non modifica le impostazioni di stile per le celle esistenti.

###  **Aggiunge la proprietà HasCustomStyle per le classi Cell, Row e Column.**

Indica se la cella, riga o colonna è stata impostata con impostazioni di stile personalizzate (diverse da quella predefinita che eredita).

###  **Proprietà Row.Style e Column.Style obsolete**

Utilizzare invece Row.GetStyle() e Column.GetStyle().

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
