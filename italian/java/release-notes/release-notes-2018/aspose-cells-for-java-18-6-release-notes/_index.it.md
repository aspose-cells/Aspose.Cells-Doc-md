---
title: Aspose.Cells for Java 18.6 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-18-6-release-notes/
---
{{% alert color="primary" %}}

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.6.

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42339|Implementa l'ordinamento dei dati personalizzato nel rapporto della tabella pivot tramite le API Aspose.Cells|Nuova caratteristica|
|CELLSJAVA-42625|L'implementazione della funzione MS Excel 'Watch Window'|Nuova caratteristica|
|CELLSJAVA-42612|Impossibile estrarre il testo dal tipo di ingranaggio SmartArt|Nuova caratteristica|
|CELLSJAVA-42646|Eccezione: "FormulaBuild](/p token0 formula sconosciuta" su Name.getRefersTo()|Aumento|
|CELLSJAVA-42645|Eccezione: "FormulaBuild Più di un token nello stack..." su Cell.getFormula()|Aumento|
|CELLSJAVA-42516|Aspose.Cells accetta e corregge una formula non valida|Aumento|
|CELLSJAVA-42636|Alcune forme di disegno vengono spostate o visualizzate in modo errato nel rendering da Excel a HTML|Insetto|
|CELLSJAVA-42627|CELLSJAVA-42619 - Impossibile estrarre correttamente le immagini Smart Art|Insetto|
|CELLSJAVA-42618|La forma viene spostata per coprire i dati nel rendering da Excel a HTML|Insetto|
|CELLSJAVA-42628|Il calcolo delle formule è errato, ad esempio genera #DIV/0! errori|Insetto|
|CELLSJAVA-42615|Cell Il formato A3 non è corretto nell'HTML di output|Insetto|
|CELLSJAVA-42621|Scarse prestazioni durante la generazione di file PDF da un file MS Excel|Insetto|
|CELLSJAVA-42620|Da XLSX a TIFF - eccezione NoClassDefFoundError|Insetto|
|CELLSJAVA-42599|Le immagini vengono perse quando il file Excel viene convertito in PDF|Insetto|
|CELLSJAVA-42630|Il metodo Chart.calculate causa OutOfMemoryError|Insetto|
|CELLSJAVA-42623|La memoria aumenta nel rendering di file Excel in formato file PDF|Insetto|
|CELLSJAVA-42592|La dimensione del carattere è cambiata nel titolo del grafico a causa del metodo characters()|Insetto|
|CELLSJAVA-41860|L'effetto ombra viene modificato durante il nuovo salvataggio di XLS|Insetto|
|CELLSJAVA-42654|Conversione da Excel a PDF: la conversione non viene mai completata|Insetto|
|CELLSJAVA-42647|Impossibile ottenere o impostare un testo alternativo per la forma del commento|Insetto|
|CELLSJAVA-42644|Aspose.Cells si blocca durante la conversione di un file ml di foglio di calcolo (xml) in PDF con tag Styles a chiusura automatica|Insetto|
|CELLSJAVA-42632|Impossibile impostare un testo alternativo per la forma SmartArt|Insetto|
|CELLSJAVA-42631|getFirstVisibleRow() e getFirstVisibleColumn() restituiscono indici non validi|Insetto|
|CELLSJAVA-42624|I collegamenti ipertestuali con simboli codificati (come "%5c") vengono decodificati dopo il nuovo salvataggio|Insetto|
|CELLSJAVA-42638|Cell.getDisplayStringValue() genera java.lang.NullPointerException|Eccezione|
|CELLSJAVA-42652|java.lang.ArrayIndexOutOfBoundsException si è verificata durante il caricamento di un file XLS|Eccezione|
|CELLSJAVA-42650|Eccezione: "Codifica non valida: null" durante il caricamento di un file XLS|Eccezione|
|CELLSJAVA-42649|Eccezione: "Il conteggio di HPageBreaks non può essere maggiore di 1024" durante il caricamento di un file XLS|Eccezione|
|CELLSJAVA-42648|Eccezione: "Impossibile leggere i dati dell'immagine" su Picture.getData()|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge le classi Slicer, SlicerCollection, SlicerCache, SlicerCacheItem e SlicerCacheItemCollection**

Queste API vengono utilizzate per creare e modificare lo Slicer nel file.

### **Aggiunge le enumerazioni SlicerCacheItemSortType e SlicerStyleType**

Queste API vengono utilizzate per creare e modificare lo Slicer nel file.

### **Aggiunge le classi CellWatchCollection e CellWatch, aggiunge la proprietà Worksheet.CellWatches**

Aggiunge Cell Watch Item nella 'watch window'.

### **Aggiunge la classe CustomXmlShape e l'enumerazione MsoDrawingType.CustomXml**

Supporta il mantenimento della forma XML personalizzata.

### **Aggiunge l'enumerazione MsoDrawingType.SmartArt**

Rappresenta il tipo di forma grafica intelligente.

### **Aggiunge la proprietà Font.SchemeType e le enumerazioni FontSchemeType**

Ottiene e imposta il tipo di schema del carattere.

### **Aggiunge la proprietà CustomXmlPart.ID**

Ottiene e imposta l'ID della parte XML personalizzata.

### **Aggiunge il metodo CustomXmlPartCollection.SelectByID()**

Ottiene la parte XML personalizzata in base all'ID.

### **Aggiunge Range.Address, Range.CellCount, WholeColumn, Range.EntireRow e Range.GetOffset(System.Int32,System.Int32)**

Miglioramento per la gamma di elaborazione.

### **Aggiunge l'enumerazione ColorDepth e la proprietà ImageOrPrintOptions.TiffColorDepth**

Ottiene o imposta la profondità di bit da applicare solo quando si salvano le pagine nel formato Tiff.

### **Sovraccarica il metodo WorkbookRender.ToImage()**

Rende la cartella di lavoro in immagine in base all'indice della pagina.

### **Aggiunge il metodo Legend.LegendEntriesLabels()**

Ottiene le etichette delle voci della legenda dopo aver chiamato il metodo Chart.Calculate().

### **Aggiunge il metodo CustomFilter.SetCriteria(FilterOperatorType filterOperator, oggetto criteri).**

Imposta i criteri di filtro.

### **Fornisce nuove API per il supporto per ottenere/impostare formule in formato dipendente dalle impostazioni locali (la funzione FormulaLocal di Microsoft Interop)**

Cell.GetFormula(bool isR1C1, bool isLocal)
Cell.SetFormula(formula stringa, bool isR1C1, bool isLocal, valore oggetto)
Nome.GetRefersTo(bool isR1C1, bool isLocal)
Nome.SetRefersTo(stringa riferisce a, bool isR1C1, bool isLocal)
FormatCondition.GetFormula1(bool isR1C1, bool isLocal)
FormatCondition.SetFormula1(formula stringa, bool isR1C1, bool isLocal)
FormatCondition.GetFormula2(bool isR1C1, bool isLocal)
FormatCondition.SetFormula2(formula stringa, bool isR1C1, bool isLocal)
FormatCondition.GetFormula1(bool isR1C1, bool isLocal, int riga, int colonna)
FormatCondition.GetFormula2(bool isR1C1, bool isLocal, int riga, int colonna)
GlobalizationSettings.GetTableRowTypeOfHeaders()
GlobalizationSettings.GetTableRowTypeOfData()
GlobalizationSettings.GetTableRowTypeOfAll()
GlobalizationSettings.GetTableRowTypeOfTotals()
GlobalizationSettings.GetTableRowTypeOfCurrent()
GlobalizationSettings.GetErrorValueString(errore stringa)
GlobalizationSettings.GetBooleanValueString(bool bv)
GlobalizationSettings.GetLocalFunctionName(string standardName)
GlobalizationSettings.GetStandardFunctionName(string localName)
GlobalizationSettings.GetLocalBuiltInName(string standardName)
GlobalizationSettings.GetStandardBuiltInName(string localName)
GlobalizationSettings.ListSeparator
GlobalizationSettings.RowSeparatorOfFormulaArray
GlobalizationSettings.ColumnSeparatorOfFormulaArray
