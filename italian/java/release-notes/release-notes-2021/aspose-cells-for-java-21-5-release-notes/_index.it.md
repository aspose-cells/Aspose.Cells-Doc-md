---
title: Aspose.Cells for Java 21.5 Note di rilascio
type: docs
weight: 8
url: /it/java/aspose-cells-for-java-21-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.5/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43452|Il calendario giapponese che utilizza una funzione di Excel non viene letto correttamente|
|CELLSJAVA-43420| Testo ruotato allineato in modo errato quando salvato come HTML|
|CELLSJAVA-43450|Problema di aggiornamento della tabella pivot|
|CELLSJAVA-43444|Regressione: getLastSavedUniversalTime restituisce una data errata|
|CELLSJAVA-43446|Cells Eccezione modifiche alla traccia|
|CELLSJAVA-43448|Regressione: riferimento non valido per l'elenco|
|CELLSJAVA-43457|Ciclo infinito durante il salvataggio della cartella di lavoro copiata|
|CELLSJAVA-43442|Problema con l'ordinamento dei dati quando si fa clic sui collegamenti di intestazione nella demo primaverile di GridWeb|
|CELLSJAVA-43443|Problema con la modalità di modifica in GridWeb Java|
|CELLSJAVA-43455|I caratteri non sono incorporati in PDF per i caratteri non ASCII durante l'impostazione di EmbedStandardWindowsFonts su false|
|CELLSJAVA-43449|Impossibile cambiare la famiglia di caratteri degli elementi del grafico da "Calibri" ad "Aktiv Grotesk"|
|CELLSJAVA-43454|Le etichette dell'asse X sono tagliate|
|CELLSJAVA-43445|Regressione: dati di riga mancanti per i file .numbers|
|CELLSJAVA-43459|NullPointerException in getFormulaLocal() con impostazioni di globalizzazione personalizzate|
|CELLSJAVA-43447| Si è verificata l'eccezione "java.lang.NullPointerException" durante l'utilizzo del file di stile personalizzato in GridWeb|
|CELLSJAVA-43439|NegativeArraySizeException si verifica al caricamento della cartella di lavoro|
|CELLSJAVA-43453|NullPointerException sul metodo Workbook.save|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Slicer.AddPivotConnection(PivotTable pivot).**

Aggiunge la connessione alla tabella pivot per l'affettatrice.

### **Aggiunge il metodo Slicer.RemovePivotConnection(PivotTable pivot).**

Rimuove la connessione PivotTable dell'affettatrice.

### **Aggiunge la proprietà TxtSaveOptions.ExportAllSheets.**

Indica se esportare tutti i fogli di lavoro nel file. Il valore dafaut è falso come MS Excel.

### **Aggiunge FileFormatType.Numbers09 enum.**

Rappresenta il formato file .numbers 09. E FileFormatType.Number rappresenterà il tipo di formato di file latest.numbers in un secondo momento.

### **Aggiunge il metodo WorkbookSettings.SetPageOrientationType().**

Imposta il tipo di orientamento della pagina di stampa per l'intero file.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisAutomatic obsoleta.**

Usare invece l'enumerazione DataBarAxisPosition.Automatic.

### **Elimina DataBarAxisPosition.DataBarAxisMidpointe num obsoleto.**

Usare invece l'enumerazione DataBarAxisPosition.Midpoint.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisNone obsoleta.**

Usare invece l'enumerazione DataBarAxisPosition.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderNone obsoleta.**

Usare invece l'enumerazione DataBarBorderType.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderSolid obsoleta.**

Usare invece l'enumerazione DataBarBorderType.Solid.

### **Elimina l'enumerazione DataBarFillType.DataBarFillGradient obsoleta.**

Usare invece l'enumerazione DataBarFillType.Gradient.

### **Elimina l'enumerazione DataBarFillType.DataBarFillSolid obsoleta.**

Usare invece l'enumerazione DataBarFillType.Solid.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarColor obsoleta.**

Usare invece l'enumerazione DataBarNegativeColorTypeColor.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarSameAsPositive obsoleta.**

Usare invece l'enumerazione DataBarNegativeColorType.SameAsPositive.

### **Elimina l'enumerazione OleObject.FileFormatType obsoleta.**

Usare invece l'enumerazione OleObject.FileFormatType.

### **Elimina l'enumerazione DynamicFilterType.Februray obsoleta.**

Utilizzare invece l'enumerazione DynamicFilterType.February.

### **Aggiunge il metodo GridCells.MoveRange().**

Sposta l'intervallo.

### **Aggiunge il metodo GridCells.InsertRange().**

Inserisce un intervallo con l'opzione di spostamento.

### **Aggiunge il metodo GridCells.DeleteRange().**

Elimina un intervallo con l'opzione di spostamento.
