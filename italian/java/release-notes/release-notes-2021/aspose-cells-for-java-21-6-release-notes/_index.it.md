---
title: Aspose.Cells for Java 21.6 Note di rilascio
type: docs
weight: 7
url: /it/java/aspose-cells-for-java-21-6-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.6/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43466|CellsException: errore per ZipFile durante l'importazione di ods|
|CELLSJAVA-43463|La sequenza temporale è interrotta dopo il salvataggio del file|
|CELLSJAVA-43464|PivotField.hideItem() non ha effetto nel file di output|
|CELLSJAVA-43470|Il testo dopo un tag "br" all'interno di un tag "th" viene troncato durante l'importazione di un documento HTML|
|CELLSJAVA-43481|Ottenere la formula sbagliata da una cella|
|CELLSJAVA-43490|Le proprietà del documento non possono essere estratte|
|CELLSJAVA-43491|Il valore della formula che utilizza la tabella dati non può essere estratto correttamente|
|CELLSJAVA-43498|Il risultato formattato del valore numerico non è corretto per la locale zh_CN|
|CELLSJAVA-43451|Il contenuto del file Excel viene visualizzato in modo errato e la demo di ChangeStyle (primavera) non funziona correttamente|
|CELLSJAVA-43484|Il layout del contenuto non è coerente nel rendering da Excel a PDF|
|CELLSJAVA-43465|Mancano alcune serie di grafici durante la conversione di Excel in PDF|
|CELLSJAVA-43468|Problema con l'equazione della linea retta nel rendering da Excel a PDF|
|CELLSJAVA-43432|Il contenuto del grafico non corrispondeva durante il nuovo salvataggio di un formato di file XLS|
|CELLSJAVA-43475|Regressione: le celle a capo rigato vengono tagliate|
|CELLSJAVA-43478|Regressione: NUMERI in PDF, molti dati mancanti|
|CELLSJAVA-43485|Regressione: contenuto extra durante il rendering di PDF da ODS|
|CELLSJAVA-43492| La conversione di un file XML (SpreadsheetML) rimuove l'impostazione nascosta in "Definizione del nome" nell'output XLS e XLSX|
|CELLSJAVA-43486|NullPointerException durante la conversione di un documento HTML in una cartella di lavoro|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Modifica il comportamento della proprietà Cell.IsErrorValue.**

Nelle versioni precedenti, questa proprietà si applica solo alle celle della formula. Per renderlo coerente con altre proprietà, da 21.6 controlliamo anche le celle non formula e se il suo valore è un valore di errore, restituiamo anche true. L'utente può controllare prima la proprietà Cell.IsFormula se ha solo bisogno di controllare il valore di errore per le celle della formula.

### **Modifica il comportamento della proprietà Cell.Value.**

Nelle vecchie versioni, questa proprietà restituisce sempre l'oggetto DateTime se la cella è formattata come data ora e il suo valore è numerico. A partire da 21.6, questa proprietà restituisce il valore numerico stesso se supera il valore DateTime massimo valido. Con questa modifica l'oggetto restituito è coerente con quanto mostrato nella barra della formula di ms excel.

### **Aggiunge la proprietà Cell.IsNumericValue.**

Fornisce all'utente un modo comodo ed efficiente per verificare se il valore di una cella è un valore numerico (int, double, datetime).

### **Aggiunge metodi sovraccaricati di Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Supporto per impostare formule di matrice e formule condivise con valori predefiniti.

### **Aggiunge enum PdfFontEncoding.**

Rappresenta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà PdfSaveOptions.FontEncoding.**

Ottiene o imposta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà SlicerCacheItem.Value.**

Restituisce il testo dell'etichetta per l'elemento slicer. Sola lettura.

### **Aggiunge il metodo GlobalizationSettings.GetProtectionNameOfPivotTable().**

Ottiene il nome della protezione nella tabella pivot.

### **Aggiunge il metodo FileFormatUtil.FileFormatToSaveFormat.**

Converte il formato del file in formato di salvataggio.
