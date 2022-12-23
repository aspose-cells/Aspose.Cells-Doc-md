---
title: Aspose.Cells for Java 21.3 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-21-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.3/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43400|Supporta la funzione UNIQUE()|
|CELLSJAVA-42863|Recupera il sottotitolo del grafico|
|CELLSJAVA-43401|Supporta il risultato di formattazione unificato per l'era giapponese per tutti i JDK|
|CELLSJAVA-43398|La formattazione condizionale non viene visualizzata correttamente nella conversione da ODS a HTML|
|CELLSJAVA-43388|Il file di output è danneggiato dopo aver copiato la cartella di lavoro|
|CELLSJAVA-43406|Problemi durante la conversione di HTML in Excel|
|CELLSJAVA-43399|CalculateFormula() crea molti valori di tipo di errore #VALUE|
|CELLSJAVA-43362|Problema di percentuale per le etichette durante la stampa dei grafici|
|CELLSJAVA-43384|Problema di percentuali per alcune etichette durante il rendering su PDF e la stampa di grafici|
|CELLSJAVA-43402|Genera l'immagine esatta del grafico dal file Excel|
|CELLSJAVA-43408|La parte superiore del grafico viene tagliata e la linea obliqua sale|
|CELLSJAVA-43412|CellsException nella conversione da xlsx a html|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà SignatureLine.Id.**

Ottiene o imposta l'identificatore per questa riga della firma.

### **Aggiunge la proprietà DigitalSignature.Id.**

Specifica un UUID che può essere incrociato con l'UUID della riga della firma memorizzata nel contenuto del documento.

### **Aggiunge la proprietà DigitalSignature.ProviderId.**

Specifica l'ID classe del provider della firma.

### **Aggiunge la proprietà DigitalSignature.Image.**

Specifica un'immagine per la firma digitale.

### **Aggiunge la proprietà DigitalSignature.Text.**

Specifica il testo della firma effettiva nella firma digitale.

### **Aggiunge il metodo Cells.ClearMergedCells().**

Rimuove tutte le celle unite.

### **Aggiunge il metodo Workbook.RemovePersonalInformation().**

Rimuove tutte le informazioni personali.

### **Aggiunge la proprietà WorkbookSettings.ForceFullCalculate.**

La proprietà indica a ms excel di eseguire il calcolo completo ogni volta che viene attivato un calcolo.

### **Aggiunge il costruttore DocxSaveOptions(Boolean).**

Rappresenta le opzioni di salvataggio dei file .docx.

### **Elimina la proprietà WorkbookSettings.IsWriteProtected obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.IsWriteProtected.

### **Elimina la proprietà WorkbookSettings.RecommendReadOnly obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.RecommendReadOnly.

### **Elimina la proprietà WorkbookSettings.WriteProtectedPassword obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.Password.
