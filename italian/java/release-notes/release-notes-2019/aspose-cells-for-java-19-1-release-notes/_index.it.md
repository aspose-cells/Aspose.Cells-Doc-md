---
title: Aspose.Cells for Java 19.1 Note di rilascio
type: docs
weight: 120
url: /it/java/aspose-cells-for-java-19-1-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.1.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41026|Supporta Excel 95/5.0 (file XLS)|Nuova caratteristica|
|CELLSJAVA-42778|Eccezione "style textRotation deve essere compreso tra 0 e 180" durante il caricamento di XLSM|Aumento|
|CELLSJAVA-42290|Mdashes e ndash inseriti in TextBox nei grafici non vengono visualizzati correttamente nel grafico PDF|Insetto|
|CELLSJAVA-42750|Impossibile recuperare gli elementi dei campi della pagina nel rapporto di tabella pivot|Insetto|
|CELLSJAVA-42783|Problema con il testo barrato nel formato file HTML generato|Insetto|
|CELLSJAVA-42784|I dati in alcune celle (ad es. G7, H7, ecc.) non vengono visualizzati allo stesso modo del file originale in Excel in HTML/conversione immagine|Insetto|
|CELLSJAVA-42797|Alcuni stili non vengono visualizzati nell'input HTML|Insetto|
|CELLSJAVA-42807|Il calcolo della formula/funzione "ISOWEEKNUM" non è lo stesso di MS Excel|Insetto|
|CELLSJAVA-42794|Da ODS a XLSX - Il colore del testo è cambiato|Insetto|
|CELLSJAVA-42795|Da ODS a XLSX - Carattere barrato non conservato correttamente|Insetto|
|CELLSJAVA-42796|Da ODS a XLSX - Le dimensioni della casella di testo sono state modificate|Insetto|
|CELLSJAVA-42798|ODS -> XLSX - Il collegamento ipertestuale è funzionale ma mostrato come testo normale|Insetto|
|CELLSJAVA-42802|Da ODS a XLSX, le percentuali vengono perse nel grafico a barre|Insetto|
|CELLSJAVA-42803|Contorno "SummaryRowBelow" non influenzato durante il salvataggio nel formato file XLSB|Insetto|
|CELLSJAVA-42757|CellsException durante la conversione dei file|Eccezione|
|CELLSJAVA-42799|Eccezione "java.lang.ArrayIndexOutOfBoundsException: -32768" durante il caricamento di un formato di file XLSX|Eccezione|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException durante il caricamento di una cartella di lavoro|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il metodo PivotTable.ShowReportFilterPageByName(string fieldName).**
Mostra tutte le pagine del filtro del report in base al nome del PivotField, il PivotField deve trovarsi nei PageField.
### **Aggiunge il metodo PivotTable.ShowReportFilterPageByIndex(int posIndex).**
Mostra tutte le pagine del filtro del report in base all'indice di posizione nei PageField.
### **Aggiunge il metodo PivotTable.ShowReportFilterPage(PivotField pageField).**
Mostra tutte le pagine del filtro del report in base a PivotField, il PivotField deve trovarsi nei PageField.
### **Aggiunge la classe DataSorterKey e DataSorterKeyCollection**
Rappresenta la chiave dell'ordinatore di dati.
### **Aggiunge il metodo DataSorter.AddKey(Int32,SortOnType,SortOrder,Object)**
Aggiunge la chiave di ordinamento come il colore di sfondo della cella, il colore del carattere.
### **Aggiunge la proprietà Aspose.Cells.DataSorter.Keys**
Ottiene tutte le chiavi dell'ordinatore dati.
### **Aggiunge l'enumerazione SortOnType**
Rappresenta il tipo di dati ordinati.
### **Aggiunge la classe ODSLoadOptions**
Rappresenta le opzioni di caricamento del file ODS.
### **Aggiunge la proprietà HTMLLoadOptions.ProgId**
Ottiene l'ID del programma di creazione del file. utilizzato solo per i file MHT.
### **Aggiunge la proprietà PdfSaveOptions.TextCrossType**
Ottiene o imposta la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
### **Aggiunge la classe enum TextCrossType**
Enumera la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
### **Aggiunge i metodi WorksheetCollection.RegisterAddInFunction()**
Sostituzione di Cell.SetAddInFormula(), un modo più conveniente ed efficiente per gli utenti di aggiungere e utilizzare funzioni aggiuntive.
### **Metodo Cell.SetAddInFormula() obsoleto**
Si prega di registrare le funzioni addin in primo luogo da WorksheetCollection.RegisterAddInFunction() e quindi impostare la formula per Cell da Cell.Formula/Cell.SetFormula() invece.
