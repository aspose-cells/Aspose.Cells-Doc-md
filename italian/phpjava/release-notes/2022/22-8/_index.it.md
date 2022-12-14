---
title: Aspose.Cells per PHP tramite Java 22.8 Note di rilascio
type: docs
weight: 5
url: /it/php-java/aspose-cells-for-php-via-java-22-8-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells per PHP tramite Java 22.8](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.8/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44811|Supporto per specificare i fogli da produrre durante l'esportazione in pdf/xps|
|CELLSJAVA-44777|Esporta le formule in html solo in base all'opzione HtmlSaveOptions.Exportformula|
|CELLSJAVA-44791|Migliora l'analisi della stringa html nella cella|
|CELLSJAVA-44740|L'impostazione della data prima del 1581 su una cella ha generato una stringa di data errata|
|CELLSJAVA-44758|Copia il foglio di lavoro tra le cartelle di lavoro, il formato della cella è anomalo|
|CELLSJAVA-44796|Aspose.Cells il motore di calcolo delle formule produce ?#N/A? valori per determinate celle|
|CELLSJAVA-44798|Bug di formattazione 0.99999999999999999 con "#" personalizzato per JDK8 o versioni successive|
|CELLSJAVA-44773|I dati sono incasinati quando si apre un documento Excel con colonne nascoste in GridWeb (Java)|
|CELLSJAVA-44781|esaminare il problema di ridimensionamento della riga quando si ridimensiona a un'altezza molto ridotta|
|CELLSJAVA-44787|Bordo inferiore perso nell'ultima riga della cartella di lavoro|
|CELLSJAVA-44761|Utilizzo eccessivo della memoria durante la conversione del file Excel in HTML|
|CELLSJAVA-44801|La conversione da Excel a PDF utilizzando Aspose.Cells for Java v22.7 causa caratteri confusi|
|CELLSJAVA-44741|L'interruzione di riga non è corretta nell'output xlsx dopo aver impostato la stringa html nella cella|
|CELLSJAVA-44776|Lo stile della riga dell'intestazione della tabella viene perso durante la copia del foglio|
|CELLSJAVA-44789|Problema con la sostituzione della stringa di caratteri della casella di testo inserita nel foglio di calcolo di Excel|
|CELLSJAVA-44792| Salvataggio infinito della cartella di lavoro in formato HTML (2892)|
|CELLSJAVA-44763|Eccezione "java.lang.IllegalArgumentException: impossibile analizzare il numero dell'argomento: 1:X8" durante il caricamento del file Excel utilizzando "org.apache.commons.io.input.AutoCloseInputStream"|
|CELLSJAVA-44774|Errore durante il salvataggio in formato PDF: è richiesta un'indagine|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiungere il metodo FontSettingCollection.Replace().**

Sostituisci il testo della forma.

### **Aggiungere la proprietà ShapeTextAlignment.NumberOfColumns.**

Ottiene e imposta il numero di colonne del testo della forma.

### **Aggiungere la proprietà HtmlSaveOptions.ExportCommentsType.**

Ottiene e imposta il tipo di commenti di esportazione in html.

### **Aggiungere la classe base PaginatedSaveOptions per PdfSaveOptions e XpsSaveOptions.**

Rappresenta le opzioni per l'impaginazione.

### **Aggiungi gruppo di fogli di classe.**

Descrive una serie di fogli.

### **Aggiungere la proprietà PaginatedSaveOptions.SheetSet.**

Ottiene o imposta i fogli di cui eseguire il rendering.

### **Aggiungere la proprietà ImageOrPrintOptions.SheetSet.**

Ottiene o imposta i fogli di cui eseguire il rendering.

### **Aggiungere la proprietà GridWeb.IgnoreStyleWithNoData.**

Ottiene o imposta se GridWeb ignora la visualizzazione di righe o colonne che non contengono valori di cella ma hanno ancora uno stile

### **Proprietà ImageOrPrintOptions.SaveFormat obsoleta.**

Per Tiff/Svg, utilizza ImageType; Per Xps, utilizza Workbook.Save(string, SaveOptions) con XpsSaveOptions.

### **Costruttore obsoleto XpsSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore XpsSaveOptions().

### **Costruttore obsoleto SvgSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore SvgSaveOptions().

### **Rimuovere il costruttore PdfSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore PdfSaveOptions().
