---
title: Aspose.Cells for .NET 20.7 Note di rilascio
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-20-7-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.7](https://www.nuget.org/packages/Aspose.Cells/20.7.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47432|Aggiunto il supporto per i criteri FilterString()|Nuova caratteristica|
|CELLSNET-47410|Tipo di foglio errato restituito per Foglio macro internazionale|Nuova caratteristica|
|CELLSNET-47463|Supporta il loop su tutti i PivotField con un normale per ogni loop|Aumento|
|CELLSNET-47408|Esamina i problemi relativi al caricamento di due file sincronizzati in aspose.cells.app|Aumento|
|CELLSNET-47441|Collegamenti di controllo del modulo rimossi in Office 365|Aumento|
|CELLSNET-47473|Controlla se la struttura o la finestra della cartella di lavoro è protetta da una password.|Aumento|
|CELLSNET-47433|Worksheet.Cells.RemoveDuplicates non funziona o richiede troppo tempo.|Prestazione|
|CELLSNET-46753|WorkbookDesigner.Process() si blocca per dati di grandi dimensioni|Prestazione|
|CELLSNET-47379|Conversione da HTML a Excel - Mancano i bordi quando definiti in CSS|Insetto|
|CELLSNET-47394|La legenda del grafico contenente le date ha un formato diverso nell'output PDF|Insetto|
|CELLSNET-47400|Formato condizionale diverso da quello impostato in Excel|Insetto|
|CELLSNET-47402|Tabelle pivot non aggiornate|Insetto|
|CELLSNET-47404|I caratteri cinesi sono illeggibili durante il caricamento del file .mht.|Insetto|
|CELLSNET-47411|Impossibile creare una copia di XLSB|Insetto|
|CELLSNET-47427|Il contenuto viene spostato durante l'esportazione in HTML|Insetto|
|CELLSNET-47471|I formati CellAreas di Conditional non sono corretti dopo l'aggiornamento e il calcolo della tabella pivot|Insetto|
|CELLSNET-47426|Valore errato della regola di convalida dei dati|Insetto|
|CELLSNET-47456|GetValidation().IgnoreBlank non funziona|Insetto|
|CELLSNET-47472|Problema di prestazioni con l'impostazione della funzione di formula condivisa nelle versioni più recenti|Insetto|
|CELLSNET-47443|I filtri automatici non funzionano correttamente in Aspose.Cells.GridDesktop|Insetto|
|CELLSNET-47460|La stampa di GridWeb su Firefox recente (versioni: 77 e 78) non funziona|Insetto|
|CELLSNET-47461|La selezione di più celle in GridWeb non funziona sulle ultime versioni di Firefox|Insetto|
|CELLSNET-47417|L'altezza della cella è insufficiente in Excel per il rendering PDF|Insetto|
|CELLSNET-47437|PDF convertito da XLS genera un errore in Acrobat Reader|Insetto|
|CELLSNET-47423|Le etichette dell'asse dei valori e dell'asse delle categorie nei grafici non vengono visualizzate nella conversione da Excel a PDF|Insetto|
|CELLSNET-47429|Il grafico Sunburst con colore di riempimento personalizzato e nessuna etichetta dati genera un errore nel metodo ToImage|Insetto|
|CELLSNET-47438|Colore del grafico a dispersione Da Excel a PDF conversione|Insetto|
|CELLSNET-47401|I valori della tabella sono cambiati dopo l'eliminazione delle righe|Insetto|
|CELLSNET-47407|I file uniti sono danneggiati.|Insetto|
|CELLSNET-47412|Tipo di grafico errato restituito per alcuni grafici|Insetto|
|CELLSNET-47413|Titolo del grafico mancante per alcuni grafici|Insetto|
|CELLSNET-47415|CopyRows non usa i valori dell'intervallo denominato di destinazione nelle formule|Insetto|
|CELLSNET-47420|Diversi risultati di ChartType.Line in XLS e XLSX|Insetto|
|CELLSNET-47425|Priorità della regola di formattazione condizionale non corretta per il tipo DataBar|Insetto|
|CELLSNET-47430|Incollando la formattazione di un intervallo, nella destinazione è stato incollato un intervallo vuoto|Insetto|
|CELLSNET-47431|La modifica della formattazione del numero Cells aggiunge inaspettatamente i bordi|Insetto|
|CELLSNET-47435|Errore durante l'aggiornamento del parametro in DataMashup > PowerQueryFormula|Insetto|
|CELLSNET-47444|Nome della serie errato letto dal grafico Waterfall|Insetto|
|CELLSNET-47447|Impossibile recuperare il formato numerico dell'asse del grafico|Insetto|
|CELLSNET-47454|Diverse altezze di riga con lo stesso valore in pixel|Insetto|
|CELLSNET-47459|Le dimensioni del grafico vengono modificate dopo la riconversione da .xlsx a .xlsb|Insetto|
|CELLSNET-47462|Errore durante l'importazione di JSON in Excel|Insetto|
|CELLSNET-47465|Stile della tabella perso durante il salvataggio del file XLS|Insetto|
|CELLSNET-47477|Produttori intelligenti FieldName ha un punto|Insetto|
|CELLSNET-47439|Eccezione di riferimento null durante l'applicazione dello stile|Eccezione|
|CELLSNET-47446|Indice della riga iniziale non valido durante la rimozione del foglio di lavoro|Eccezioni|
|CELLSNET-47466|NullReferenceException al caricamento di XLSX|Eccezioni|
|CELLSNET-47476|Riferimento oggetto non impostato su un'istanza di un'eccezione oggetto durante il caricamento di XLSX|Eccezioni|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo Cells.RemoveDuplicates().**
Metodo sovraccarico di Cells.RemoveDuplicates(...) per comodità dell'utente per rimuovere le righe duplicate nell'intero foglio.
#### **Aggiunge la proprietà TickLabels.DisplayNumberFormat.**
Ottiene e imposta il formato del numero di visualizzazione delle etichette dei segni di graduazione.
#### **Aggiunge il metodo Cells.GetViewRowHeight() e Cells.GetViewRowHeightInch().**
Ottiene l'altezza della riga della vista.
#### **Aggiunge enum SheetType.InternationalMacro.**
Aggiunge un nuovo tipo di foglio: macro internazionale.
#### **Aggiunge il metodo PivotFieldCollection.GetEnumerator().**
Ottiene un enumeratore sugli elementi di questa raccolta nella sequenza corretta.
#### **Aggiunge il metodo PivotItemCollection.GetEnumerator().**
Ottiene un enumeratore sugli elementi di questa raccolta nella sequenza corretta.
#### **Aggiunge la proprietà Workbook.IsWorkbookProtectedWithPassword.**
Indica se la struttura e la finestra sono protette da password.
#### **Aggiungere le classi PowerQueryFormulaParameters e PowerQueryFormulaParameter**
Rappresenta i parametri della formula di query avanzata.
