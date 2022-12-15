---
title: Aspose.Cells for Python via Java 22.9 Note di rilascio
type: docs
weight: 4
url: /it/python-java/aspose-cells-for-python-via-java-22-9-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Python via Java 22.9](https://releases.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.9/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44194|La forma del disegno non viene visualizzata nel rendering da Excel a PDF|
|CELLSJAVA-44864|Il caricamento simultaneo di cartelle di lavoro genera errori "File danneggiato".|
|CELLSJAVA-44327|Bordi e meno linee mostrate nelle fette di torta in bianco e nero nel grafico per il rendering dell'immagine|
|CELLSJAVA-44591|La rotazione del testo delle etichette non corrisponde a Excel nell'immagine di output del grafico|
|CELLSJAVA-44775|Etichette del grafico sovrapposte nel rendering del grafico all'immagine|
|CELLSJAVA-44860|la visualizzazione del testo della cella non è la stessa di Excel in alcune aree unite|
|CELLSJAVA-44832|Vengono emesse più pagine invece di una pagina come in Excel durante la conversione in pdf|
|CELLSJAVA-44812|Impossibile ridurre l'area del tracciato per il grafico|
|CELLSJAVA-44831|MS Word richiede un errore "Word ha trovato contenuto illeggibile in..." quando si apre il DOCX convertito dal file XLSX da Aspose.Cells for Java|
|CELLSJAVA-44833|Il colore del testo non viene applicato a parole diverse o parte del contenuto nel file Excel di output quando si utilizza il metodo Cell.setHtmlString()|
|CELLSJAVA-44852| Il bordo non è corretto quando il file Excel statico viene convertito in HTML|
|CELLSJAVA-44856| Conversione da Excel a HTML - Sparkline (mini grafico) non viene visualizzato/renderizzato|
|CELLSJAVA-44859|Alcune formattazioni Html non funzionano per le celle del foglio di lavoro in un file Excel esistente|
|CELLSJAVA-44842|Eccezione "java.lang.OutOfMemoryError: Java heap space" durante la conversione di un file XLSX in PDF|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge i metodi Cell.SetTableFormula(...).**

Supporto per impostare formule per intervallo di celle per creare una tabella dati a due variabili e una tabella dati a una variabile.

### **Aggiunge il metodo Cell.SetDynamicArrayFormula(string arrayFormula, FormulaParseOptions options, object[][] values, boolcalculateRange, boolcalculateValue, CalculationOptions copts)**

Supporto per impostare la formula dell'array dinamico con opzioni personalizzate per il calcolo, specialmente quando ci sono funzioni che richiedono il motore personalizzato dell'utente per il calcolo nella formula.

### **Aggiunge il metodo Workbook.RefreshDynamicArrayFormulas(bool calcola, CalculationOptions copts)**

Supporto per l'aggiornamento delle formule di matrice dinamica con opzioni personalizzate per il calcolo, in particolare quando sono presenti funzioni che richiedono il motore personalizzato dell'utente per le funzioni di calcolo nelle formule di matrice dinamica.

### **Aggiunge la proprietà ChartFrame.TextOptions.**

Rappresenta le opzioni di carattere del testo del grafico.

### **Aggiunge la proprietà ExportRangeToJsonOptions.ExportEmptyCells.**

Indica se esportare null se le celle sono vuote.

### **Aggiungere il costruttore NumbersLoadOptions.**

Rappresenta le opzioni di caricamento dei numeri.

### **Aggiunge enum LoadNumbersTableType.**

Rappresenta il tipo di caricamento multi tabelle in un foglio di lavoro del Mac .numbers.

### **Aggiunge la proprietà ProtectedRange.IsProtectedWithPassword.**

Indica se l'intervallo è protetto da password.

### **Aggiunge le proprietà ImportTableOptions.ExportCaptionAsFieldName**

Indica se esportare la didascalia come nome campo durante l'importazione della tabella dati.

### **Aggiunge la proprietà TextOptions.LanguageCode.**

Ottiene e imposta il codice della lingua del tipo di carattere.

### **Aggiunge enum PresetThemeGradientType.**

Rappresenta il tipo di sfumatura del tema preimpostato.

### **Aggiunge il metodo GradientFill.SetPresetThemeGradient().**

Imposta il tipo di sfumatura del tema preimpostato.

### **Aggiunge i metodi di override Style.SetBorder().**

Imposta i bordi con vari tipi di colore.

### **Aggiunge i metodi Range.SetOutlineBorder() e Range.SetOutlineBorders()**

Imposta i bordi dell'intervallo con vari tipi di colore.