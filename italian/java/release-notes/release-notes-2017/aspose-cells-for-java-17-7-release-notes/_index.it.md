---
title: Aspose.Cells for Java 17.7 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-17-7-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.7/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42322|Supporta la funzione Filtro avanzato (MS Excel) per visualizzare i record che soddisfano criteri complessi|Nuova caratteristica|
|CELLSJAVA-42336|ResultSet importa il valore zero anziché nullo nel file XLSX|Aumento|
|CELLSJAVA-42329|Miglioramenti necessari per i filtri di dati e le funzionalità di paging - Aspose.Cells.GridWeb (Java)|Aumento|
|CELLSJAVA-41616|SaveCustomStyleFile non è presente in GridWeb (Java)|Aumento|
|CELLSJAVA-42321|CellsHelper.setSignificantDigits() non dovrebbe essere una funzione statica (globale).|Aumento|
|CELLSJAVA-42327|Alcune forme sono distorte e modificate nel rendering da Excel a PDF|Insetto|
|CELLSJAVA-42290|I trattini e gli ndash inseriti nelle caselle di testo nei grafici non vengono visualizzati correttamente nel PDF del grafico|Insetto|
|CELLSJAVA-42338|Risultati errati quando si utilizzano le formule SOMMA.PIÙ.SE|Insetto|
|CELLSJAVA-42337|Aspose.Cells non è in grado di calcolare il valore della cella B4 del foglio di lavoro Calcoli|Insetto|
|CELLSJAVA-42330|Strano risultato durante la conversione da Excel a PDF o PDF/A utilizzando i thread|Insetto|
|CELLSJAVA-42331|Le modifiche al campo dell'autore del commento non vengono mantenute|Insetto|
|CELLSJAVA-42328|Restituito IconSet errato|Insetto|
|CELLSJAVA-42324|Lo sfondo del grafico non è presente dopo aver impostato i dati di un'immagine|Insetto|
|CELLSJAVA-42340|Eccezione nel thread "Thread-2" java.lang.OutOfMemoryError: limite di overhead GC superato|Eccezione|
|CELLSJAVA-42334|L'eccezione "Errore per ZipFile" viene generata quando si utilizza OutputFileStream|Eccezione|
|CELLSJAVA-42326|com.aspose.cells.CellsException: password non valida all'apertura del file Excel|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge i metodi GlobalizationSettings.GetBooleanValueString()/GetErrorValueString()**
Ottiene il valore della stringa di visualizzazione personalizzata per il valore booleano e di errore della cella durante la formattazione/il rendering.
### **Rimuove il metodo ValidationCollection.Add() obsoleto**
Usare invece il metodo ValidationCollection.Add(CellArea).
### **Aggiunge la proprietà PdfSaveOptions.CheckWorkbookDefaultFont**
Indica se provare a utilizzare prima il carattere predefinito della cartella di lavoro per mostrare i caratteri il cui carattere non è impostato correttamente.
### **Aggiunge la proprietà ImageOrPrintOptions.CheckWorkbookDefaultFont**
Indica se provare a utilizzare prima il carattere predefinito della cartella di lavoro per mostrare i caratteri il cui carattere non è impostato correttamente.
### **Aggiunge FileFormatType.Numbers, LoadFormat.Numbers e SaveFormat.Numbers enum**
Rappresenta il formato di file del foglio di calcolo Numbers di Apple Inc/.
### **Aggiunge il metodo Worksheet.AdvancedFilter()**
Filtra i dati utilizzando criteri complessi.
### **Aggiunge la proprietà WorkbookSettings.SignificantDigits**
Ottiene e imposta il numero di cifre significative.
### **Rende obsoleta la proprietà Validation.AreaList e aggiunge la proprietà Validation.Areas**
Ottiene tutta l'area che contiene le impostazioni di convalida dei dati.
### **Aggiunge la proprietà PageSetup.IsAutomaticPaperSize**
Indica se il formato carta è automatico.
### **Aggiunge il metodo FontSettingCollection.Replace()**
Sostituisce il testo della forma.
### **Aggiunge Cells.importResultSet(ResultSet rs, int rowIndex, int columnIndex, opzioni ImportTableOptions)/Cells.importResultSet(ResultSet rs, String startCell, opzioni ImportTableOptions)**
Supporta l'importazione di ResultSet con più opzioni.
### **Aggiunge la proprietà GridWorksheet.CustomColumnCaption**
Ottiene o imposta la didascalia di colonna personalizzata per il foglio di lavoro: Aspose.Cells.GridDesktop.
### **Aggiunge la proprietà GridWorksheet.CustomRowCaption**
Ottiene o imposta la didascalia della riga personalizzata per il foglio di lavoro: Aspose.Cells.GridDesktop.
### **Aggiunge il metodo GridDesktop.GetVersion()**
Ottieni la versione di rilascio.
### **Aggiunge la funzione GridWebInstance.resize() nel client GridWeb js, (GridWebInstance è l'oggetto di controllo GridWeb)**
Rende il controllo GridWeb compatibile con le dimensioni correnti della finestra del browser.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Leggi il foglio di calcolo dei numeri sviluppato da Apple Inc. utilizzando Aspose.Cells](/cells/it/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions in modo che abbia la priorità](/cells/it/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Importa i dati dall'oggetto ResultSet del database di Microsoft Access nel foglio di lavoro](/cells/it/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Implementa errori e valore booleano in russo o in qualsiasi altra lingua](/cells/it/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/)
- [Determinare se il formato carta del foglio di lavoro è automatico](/cells/it/java/determine-if-paper-size-of-worksheet-is-automatic/)


