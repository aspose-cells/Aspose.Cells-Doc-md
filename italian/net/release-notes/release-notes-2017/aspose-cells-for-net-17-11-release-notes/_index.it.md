---
title: Aspose.Cells for .NET Note sulla versione 17.11
type: docs
weight: 20
url: /it/net/aspose-cells-for-net-17-11-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for .NET 17.11.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-45748|Funzionalità simile a XmlMapQuery necessaria come disponibile in MS Excel|Nuova caratteristica|
|CELLSNET-45747|Proprietà associata necessaria per XMLMaps per ottenere il RootElementName per la mappa|Nuova caratteristica|
|CELLSNET-45709|La scala diventa più piccola - Problema con i caratteri|Nuova caratteristica|
|CELLSNET-45743|Proteggi cartella di lavoro condivisa: imposta o modifica la password|Nuova caratteristica|
|CELLSNET-45737|Supporto PasteType per Aspose.Cells.GridDesktop durante le azioni Copia/Incolla|Nuova caratteristica|
|CELLSNET-45755|Impossibile ottenere il testo delle forme Smart Art|Aumento|
|CELLSNET-45720|La tabella pivot impiega troppo tempo per aggiornare i dati|Prestazione|
|CELLSNET-45680|La direzione della forma è errata quando viene convertita in formato immagine|Insetto|
|CELLSNET-45679|Le forme delle stelle non vengono visualizzate correttamente nel PDF di output|Insetto|
|CELLSNET-45669|I caratteri si sovrappongono durante la conversione in immagine|Insetto|
|CELLSNET-45665|Alcuni elementi del disegno sono invertiti mentre altri sono spostati a destra|Insetto|
|CELLSNET-43912|Posizione degli oggetti linea modificata durante il rendering del foglio di calcolo in PDF|Insetto|
|CELLSNET-45715|Opzioni tabella pivot - Mostra la riga dei valori - viene abilitata al nuovo salvataggio|Insetto|
|CELLSNET-45671|Valori totali mancanti per i campi calcolati durante l'aggiornamento/calcolo dei dati della tabella pivot|Insetto|
|CELLSNET-45650|Errore nell'espansione dei dati nelle colonne appropriate durante il salvataggio di un formato di file MHTML in un file Excel|Insetto|
|CELLSNET-45721|LightCellsDataProvider sta rimuovendo gli spazi iniziali e finali|Insetto|
|CELLSNET-45719|Il calcolo della formula risolve la formula in modo imprevisto in errore|Insetto|
|CELLSNET-45724|Il salvataggio di Excel come PDF riduce la larghezza della colonna|Insetto|
|CELLSNET-45712|La legenda del grafico non è presente nel PDF di output|Insetto|
|CELLSNET-45710|La formattazione dei numeri nel grafico viene persa dopo il salvataggio di un file Excel come PDF|Insetto|
|CELLSNET-45708|Il file PDF creato da Aspose.Cells causa un errore in Adobe Acrobat Reader|Insetto|
|CELLSNET-45684|Da grafico a immagine o PDF - Il grafico a linee 3D non è corretto o è ruotato|Insetto|
|CELLSNET-45760|La convalida non viene copiata correttamente da un foglio di lavoro a un altro|Insetto|
|CELLSNET-45758|La proprietà Style.QuotePrefix non funziona per il formato di file XLSB|Insetto|
|CELLSNET-45757|La cartella di lavoro specifica di Excel viene nascosta dopo l'apertura e il salvataggio|Insetto|
|CELLSNET-45754|Le colonne sono state espanse in modo imprevisto nella cartella di lavoro unita|Insetto|
|CELLSNET-45749|La stringa HTML con più caratteri corrompe il file Excel di output|Insetto|
|CELLSNET-45739|Il file SpreadsheetML quando salvato nuovamente tramite Aspose.Cells contiene impostazioni di protezione aggiuntive applicate|Insetto|
|CELLSNET-45738|AutoFitColumns interrompe la formattazione HTML nel file Excel di output|Insetto|
|CELLSNET-45734|MS Excel richiede un messaggio di errore all'apertura del file di output|Insetto|
|CELLSNET-45733|Il carattere della casella di testo viene modificato dopo aver separato le forme|Insetto|
|CELLSNET-45714|L'altezza della riga diventa troppo grande dopo l'adattamento automatico delle righe|Insetto|
|CELLSNET-45735|Problema con CellColor quando si utilizza il menu di scelta rapida per modificare|Insetto|
|CELLSNET-45707|Eccezione quando si usa PivotTable.RefreshData|Eccezione|
|CELLSNET-45728|L'indice era fuori dall'intervallo durante il salvataggio come pagina PDF|Eccezione|
|CELLSNET-45704|Workbook.Save() ha esito negativo con un'eccezione quando si usa Aspose.Cells come processo Web di Azure|Eccezione|
|CELLSNET-45753|Quando XLSB viene convertito in PDF, si verifica System.ArgumentOutOfRangeException|Eccezione|
|CELLSNET-45751|La proprietà ExportTableOptions.Indexes utilizzata nel metodo ExportDataTable() causa un'eccezione|Eccezione|
|CELLSNET-45726|Eccezione durante il caricamento del file XLS di output (con oggetti OLE, immagini, ecc. esclusi)|Eccezione|
|CELLSNET-45723|R1C1Formula genera un'eccezione se la formula contiene il carattere "[" ]|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo Shape.GetResultOfSmartArt()**
Converti la smart art in una forma di gruppo.
#### **Aggiunge la proprietà Shape.IsSmartArt**
Indica se la forma è smart art.
#### **Metodo Workbook.ProtectSharedWorkbook() e Workbook.UnprotectSharedWorkbook()**
Protegge e rimuove la protezione della cartella di lavoro condivisa.
#### **Aggiunge enum StyleModifyFlag.Spacing**
Specifica la spaziatura tra i caratteri all'interno di un'esecuzione di testo.
#### **Aggiunge la proprietà PdfSaveOptions.IgnoreError**
Indica se è necessario nascondere l'errore durante il rendering.
#### **Aggiunge la proprietà ImageOrPrintOptions.PageIndex**
Ottiene o imposta l'indice in base 0 della prima pagina da salvare.
#### **Aggiunge la proprietà ImageOrPrintOptions.PageCount**
Ottiene o imposta il numero di pagine da salvare.
#### **Aggiunge la proprietà XmlMap.RootElementName**
Ottiene il nome dell'elemento radice.
#### **Aggiunge il metodo Worksheet.XmlMapQuery(string path, XmlMap xmlMap).**
Interroga le aree delle celle mappate/collegate al percorso specifico della mappa xml.
#### **Aggiunge la proprietà GridDesktop.PasteType**
Ottiene o imposta quale tipo di incolla applicare per l'azione incolla, disponibile solo quando EnableClipboardCopyPaste è false.
#### **Aggiunge la proprietà LoadOptions.AutoFitterOptions**
Ottiene e imposta le opzioni di installazione automatica.
#### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Converti la Smart Art in Group Shape](/cells/it/net/convert-the-smart-art-to-group-shape/)
- [Crea cartella di lavoro condivisa con Aspose.Cells](/cells/it/net/create-shared-workbook-with-aspose-cells/)
- [Determina se Shape è Smart Art Shape](/cells/it/net/determine-if-shape-is-smart-art-shape/)
- [Trova il nome dell'elemento radice della mappa Xml](/cells/it/net/find-the-root-element-name-of-xml-map/)
- [Ignora gli errori durante il rendering di Excel in Pdf](/cells/it/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Proteggi con password o rimuovi la protezione della cartella di lavoro condivisa](/cells/it/net/password-protect-or-unprotect-the-shared-workbook/)
- [Query Cell Aree mappate su Xml Map Path utilizzando il metodo Worksheet.XmlMapQuery](/cells/it/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)
- [Eseguire il rendering della sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Copia e incolla comportamento delle proprietà EnableClipboardCopyPaste e PasteType GridDesktop](/cells/it/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/)


