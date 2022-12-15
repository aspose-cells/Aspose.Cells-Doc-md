---
title: Aspose.Cells for .NET 21.4 Note di rilascio
type: docs
weight: 9
url: /it/net/aspose-cells-for-net-21-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.4](https://www.nuget.org/packages/Aspose.Cells/21.4.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47891|Supporto per ottenere lo stile di visualizzazione con l'abilitazione della cache|Nuova caratteristica|
|CELLSNET-47922|Renderizza i dati con le coordinate della cella nella conversione da Excel a HTML|Aumento|
|CELLSNET-47924|Implementa Crypto con l'API di BouncyCastle|Aumento|
|CELLSNET-47951|Supporta mappe XML tramite XSD|Aumento|
|CELLSNET-47206|Raggruppamento di dati con indicatori intelligenti orizzontali e origine dati nidificata|Aumento|
|CELLSNET-47888|SmartMarker appropriati necessari per ottenere l'output desiderato|Aumento|
|CELLSNET-47918|Righe comprimibili insieme a marcatori intelligenti|Aumento|
|CELLSNET-47953|Supporta l'aggiunta di immagini .webp ai file .xlsx.|Aumento|
|CELLSNET-47916|Il tag in stile HTML consuma 4 GB di memoria e si arresta in modo anomalo durante il caricamento nella cartella di lavoro|Prestazione|
|CELLSNET-46869|WordArts e forme non vengono visualizzate correttamente in PDF|Insetto|
|CELLSNET-47890|Le linee andranno alla deriva durante la conversione Pdf|Insetto|
|CELLSNET-47858|Le forme non vengono visualizzate correttamente in HTML e PDF|Insetto|
|CELLSNET-47907|Il posizionamento del grafico viene modificato durante la conversione di Excel in HTML|Insetto|
|CELLSNET-47856|Problema di conversione da XLSX a PDF con tabelle pivot|Insetto|
|CELLSNET-47846|Implementazione di GridWeb incompatibile con i componenti DevExpress recenti|Insetto|
|CELLSNET-47923|Visualizzazione del layout di pagina non corretta per la cartella di lavoro con carattere predefinito diverso da Calibri|Insetto|
|CELLSNET-47965| Conversione da Excel a PDF - Pagine del documento confuse|Insetto|
|CELLSNET-46161|Il testo obliquo non viene visualizzato correttamente nel PDF di output|Insetto|
|CELLSNET-47917|Etichette del grafico a torta incasinate in PDF generate dal foglio di lavoro di Excel|Insetto|
|CELLSNET-47919|Valore massimo errato estratto dai grafici|Insetto|
|CELLSNET-46363|La struttura nidificata non viene importata correttamente in XLSX|Insetto|
|CELLSNET-47838|La tavolozza dei colori del grafico nativo non viene conservata|Insetto|
|CELLSNET-47910|Range.Copy aggiorna in modo errato la formattazione condizionale|Insetto|
|CELLSNET-47931|Style.SetBorder() si arresta in modo anomalo quando vengono impostate più opzioni contemporaneamente|Insetto|
|CELLSNET-47937|La proprietà dei metadati dell'autore non viene aggiornata|Insetto|
|CELLSNET-47958|Foglio mancante nella cartella di lavoro caricata|Insetto|
|CELLSNET-47976|Formato non implementato durante l'utilizzo di FontSettings|Insetto|
|CELLSNET-47935|Viene generata un'eccezione durante la chiamata a PivotTable.CalculateData()|Eccezione|
|CELLSNET-47940|Viene generata un'eccezione quando si apre un file mht speciale.|Eccezione|
|CELLSNET-47944|Eccezione nulla durante la conversione della forma affettatrice in immagine|Eccezione|
|CELLSNET-47932|Eccezione nulla durante il caricamento di un file xlsx speciale con una formula strana.|Eccezione|
|CELLSNET-47963|Il parametro non è un'eccezione valida durante il rendering dell'intervallo in PNG|Eccezione|
|CELLSNET-47967|Errore di overflow durante il salvataggio di un file XLS|Eccezione|
|CELLSNET-47921|Eccezione nulla durante il caricamento di un file xlsx speciale|Eccezione|
|CELLSNET-47945|Eccezione nulla durante il caricamento di un file html speciale|Eccezione|
|CELLSNET-47949|Quando viene generata una nuova cartella di lavoro, viene generata un'eccezione di unità secondaria non valida|Eccezione|
|CELLSNET-47950|NullReferenceException durante il salvataggio di una cartella di lavoro copiata|Eccezione|
|CELLSNET-47961|Eccezione nulla quando pivotCacheRecords1.xml non esiste.|Eccezione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Aggiunge i metodi StartAccessCache()/CloseAccessCache() per la cartella di lavoro e il foglio di lavoro.**

Fornire agli utenti la possibilità di accedere ai dati in modalità batch con prestazioni migliori.

### **Aggiunge le proprietà TxtSaveOptions.ExportQuotePrefix e TxtLoadOptions.TreatQuotePrefixAsValue.**

Fornisci agli utenti la possibilità di decidere come fare con la prima virgoletta singola del valore della cella durante l'esportazione/importazione di file CSV/TSV.

### **Aggiunge i metodi GlobalizationSettings.GetCollationKey(string,bool) e Compare(string,string,bool).**

Fornisci agli utenti la possibilità di sovrascrivere le regole predefinite del confronto tra stringhe. Per alcune impostazioni locali o valori di stringa, la regola predefinita del confronto delle stringhe potrebbe non essere quella prevista (il risultato di alcune funzionalità, come il calcolo della formula, l'ordinamento, ecc., è diverso da quello che dovrebbe essere ottenuto in ms excel). In tal caso, l'utente può sovrascrivere tali metodi con la regola prevista (ad esempio, l'utente può utilizzare l'implementazione della libreria icu).

### **Aggiunge enum ImageType.WebP.**

Rappresenta l'immagine Weppy.

### **Aggiunge il metodo OleObject.SetEmbeddedObject().**

Per verificare se l'icona di aggiornamento automatico.

### **Aggiunge la proprietà WorkbookDesigner.LineByLine.**

Indica se elaborare i marcatori intelligenti riga per riga.

### **Aggiunge la proprietà HtmlSaveOptions.ExportCellCoordinate?.**

Indica se esportare coordinate Excel di celle non vuote durante il salvataggio del file in html. Il valore predefinito è false. Se desideri importare l'output html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà AutoFitterOptions.DefaultEditLanguage.**

 Ottiene o imposta la lingua di modifica predefinita.

