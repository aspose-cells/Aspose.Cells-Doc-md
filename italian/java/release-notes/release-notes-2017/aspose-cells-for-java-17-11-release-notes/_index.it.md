---
title: Aspose.Cells for Java Note sulla versione 17.11
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-17-11-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 17.11.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42433|Proprietà ImageOrPrintOptions.PageIndex e ImageOrPrintOptions.Count necessarie per ottenere l'immagine delle pagine desiderate|Nuova caratteristica|
|CELLSJAVA-42427|L'esportazione delle griglie con bordi non visualizza le griglie all'interno del bordo nel rendering da Excel a HTML|Insetto|
|CELLSJAVA-42438|LightCellsDataProvider sta rimuovendo gli spazi iniziali e finali|Insetto|
|CELLSJAVA-42422|Nell'output PDF del grafico MS Excel viene utilizzato un carattere errato|Insetto|
|CELLSJAVA-42353|Alcune frecce o richiami mancano nell'HTML di output|Insetto|
|CELLSJAVA-42455|Manca il secondo commento dalla raccolta dei commenti del foglio di lavoro|Insetto|
|CELLSJAVA-42454|La creazione della cartella di lavoro sembra bloccarsi durante la lettura da un file XLSM|Insetto|
|CELLSJAVA-42450|La proprietà Style.QuotePrefix non funziona per il file XLSB|Insetto|
|CELLSJAVA-42445|L'impostazione dei dati dell'immagine influisce sull'altro grafico e viene visualizzato in modo errato|Insetto|
|CELLSJAVA-42444|Il metodo CheckBox.setName() funziona in MS Excel 2016 ma non funziona in MS Excel 2007|Insetto|
|CELLSJAVA-42443|I filtri MS Excel non vengono convertiti correttamente - Conversione da XLSB a XLSM|Insetto|
|CELLSJAVA-42442|La modifica del valore di ComboBoxActiveXControl non modifica il valore della cella collegata|Insetto|
|CELLSJAVA-42435|Cells.setColumnWidthPixel e Cells.setRowHeightPixel hanno comportamenti diversi|Insetto|
|CELLSJAVA-42431|L'estensione dell'intervallo della tabella modifica inaspettatamente il contenuto delle celle|Insetto|
|CELLSJAVA-42434|Eccezione: "java.lang.NumberFormatException" durante il caricamento di un formato di file HTML|Eccezione|
|CELLSJAVA-42448|Cells.deleteBlankRows sta causando l'eccezione "java.lang.ArrayIndexOutOfBoundsException: 1937"|Eccezione|
|CELLSJAVA-42426|Eccezione nel thread "main" java.lang.OutOfMemoryError: limite di overhead GC superato - File III|Eccezione|
|CELLSJAVA-42425|Eccezione nel thread "main" java.lang.OutOfMemoryError: limite di overhead GC superato - File II|Eccezione|
|CELLSJAVA-42424|Eccezione nel thread "main" java.lang.OutOfMemoryError: limite di overhead GC superato - File I|Eccezione|
|CELLSJAVA-42428|Chart.toImage risulta in java.lang.ArrayIndexOutOfBoundsException|Eccezione|
|CELLSJAVA-42452|Il salvataggio di una cartella di lavoro come PDF dopo RemoveUnusedStyles API produce un'eccezione CellsException|Eccezione|
|CELLSJAVA-42440|Si è verificato "java.lang.IllegalArgumentException: indice di riga non valido".|Eccezione|
|CELLSJAVA-42439|Eccezione: "java.lang.IllegalArgumentException: Invalid row index" al salvataggio di un formato di file XLSX|Eccezione|
|CELLSJAVA-42437|Eccezione: java.lang.NumberFormatException quando si salva nuovamente un formato di file XLSB|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il metodo Shape.GetResultOfSmartArt()**
Converti la smart art in una forma di gruppo.
### **Aggiunge la proprietà Shape.IsSmartArt**
Indica se la forma è smart art.
### **Aggiunge i metodi Workbook.ProtectSharedWorkbook() e Workbook.UnprotectSharedWorkbook()**
Protegge e rimuove la protezione della cartella di lavoro condivisa.
### **Aggiunge enum StyleModifyFlag.Spacing**
Specifica la spaziatura tra i caratteri all'interno di un'esecuzione di testo.
### **Aggiunge la proprietà PdfSaveOptions.IgnoreError**
Indica se è necessario nascondere l'errore durante il rendering.
### **Aggiunge la proprietà ImageOrPrintOptions.PageIndex**
Ottiene o imposta l'indice in base 0 della prima pagina da salvare.
### **Aggiunge la proprietà ImageOrPrintOptions.PageCount**
Ottiene o imposta il numero di pagine da salvare.
### **Aggiunge la proprietà XmlMap.RootElementName**
Ottiene il nome dell'elemento radice.
### **Aggiunge il metodo Worksheet.XmlMapQuery(string path, XmlMap xmlMap).**
Interroga le aree delle celle mappate/collegate al percorso specifico della mappa xml.
### **Aggiunge la proprietà LoadOptions.AutoFitterOptions**
Ottiene e imposta le opzioni di installazione automatica.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Converti la Smart Art in Group Shape](/cells/it/java/convert-the-smart-art-to-group-shape/)
- [Crea cartella di lavoro condivisa con Aspose.Cells](/cells/it/java/create-shared-workbook-with-aspose-cells/)
- [Determina se Shape è Smart Art Shape](/cells/it/java/determine-if-shape-is-smart-art-shape/)
- [Trova il nome dell'elemento radice della mappa Xml](/cells/it/java/find-the-root-element-name-of-xml-map/)
- [Ignora gli errori durante il rendering di Excel in Pdf](/cells/it/java/ignore-errors-while-rendering-excel-to-pdf/)
- [Proteggi con password o rimuovi la protezione della cartella di lavoro condivisa](/cells/it/java/password-protect-or-unprotect-the-shared-workbook/)
- [Query Cell Aree mappate su Xml Map Path utilizzando il metodo Worksheet.XmlMapQuery](/cells/it/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)
- [Eseguire il rendering della sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
