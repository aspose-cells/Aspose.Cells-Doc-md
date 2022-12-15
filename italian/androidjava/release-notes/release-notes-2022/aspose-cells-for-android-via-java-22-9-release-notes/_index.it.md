---
title: Aspose.Cells for Android via Java 22.9 Note di rilascio
type: docs
weight: 4
url: /it/java/aspose-cells-for-android-via-java-22-9-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 22.9.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44721|Supporta l'ordinamento di PivotField tramite campo calcolato|
|CELLSJAVA-44811|Supporto per specificare i fogli da produrre durante l'esportazione in pdf/xps|
|CELLSJAVA-44194|La forma del disegno non viene visualizzata nel rendering da Excel a PDF|
|CELLSJAVA-44733|Esamina le regole di ms excel per visualizzare il bordo della cella quando la colonna adiacente è nascosta: il bordo della cella non è stato sincronizzato|
|CELLSJAVA-44777|Esporta le formule in html solo in base all'opzione HtmlSaveOptions.Exportformula|
|CELLSJAVA-44791|Migliora l'analisi della stringa html nella cella|
|CELLSJAVA-44695| Conversione errata in PDF da XLS con Line Callout a sinistra del foglio|
|CELLSJAVA-44700|campi calcolati della tabella pivot non vengono aggiornati durante l'aggiornamento dell'origine dati|
|CELLSJAVA-44705|Cell.getDependents() genera un'eccezione o non può fornire tutti i dipendenti|
|CELLSJAVA-44717|Problema con lo stile del bordo (linea).|
|CELLSJAVA-44707| la linea di confine non viene visualizzata|
|CELLSJAVA-44670| Problema con le formule nell'output HTML - Conversione da Excel a HTML|
|CELLSJAVA-44202|Quando si esporta in HTML, la legenda nel grafico non è la stessa di MS Excel|
|CELLSJAVA-44591|La rotazione del testo delle etichette non corrisponde a Excel nell'immagine di output del grafico|
|CELLSJAVA-44655|Impossibile visualizzare il grafico Treemap con valore negativo, causando il proseguimento dell'esecuzione|
|CELLSJAVA-44686|Il testo del titolo di chart(2016) non è corretto quando Title.IsAutoText è true|
|CELLSJAVA-44689|Regressione: problema relativo alla lingua della legenda del grafico a cascata|
|CELLSJAVA-44687|Problema grafico durante la combinazione dei file|
|CELLSJAVA-44736|Stile della tabella perso durante la copia del foglio|
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
|CELLSJAVA-44725| Eccezione "java.util.zip.ZipException: dimensione voce non valida (previsto 0 ma ottenuto 1053 byte)" durante la conversione di XLSX in PDF|
|CELLSJAVA-44763|Eccezione "java.lang.IllegalArgumentException: impossibile analizzare il numero dell'argomento: 1:X8" durante il caricamento del file Excel utilizzando "org.apache.commons.io.input.AutoCloseInputStream"|
|CELLSJAVA-44774|Errore durante il salvataggio in formato PDF: è richiesta un'indagine|
|CELLSJAVA-44842|Eccezione "java.lang.OutOfMemoryError: Java heap space" durante la conversione di un file XLSX in PDF|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. sul forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cells.GetDependentsInCalculation(int,int,bool)**

Ottiene tutte le celle il cui risultato calcolato dipende dalla cella specificata da riga e colonna in base alla catena di calcolo corrente. Per la cella che è vuota e non è stata istanziata nel modello di celle corrente, l'utente può utilizzare questo metodo invece di Cell.GetDependentsInCalculation(bool) perché il successivo deve prima istanziare l'oggetto cella nel modello di celle corrente.

### **Cambia il bordo sinistro/destro della cella per Cell.GetStyle() quando la colonna adiacente è nascosta**

Nelle versioni precedenti, se la colonna adiacente è nascosta per una cella, il bordo sinistro/destro di questa cella non verrà verificato con la cella adiacente, quindi il bordo restituito potrebbe essere diverso da quello mostrato nella finestra di dialogo di ms excel quando si imposta il bordo di questa cella. Da 22.7, facciamo in modo che il bordo restituito sia sempre il valore effettivo (che dovrebbe essere coerente con il bordo della sua cella adiacente) della cella per Cell.GetStyle(). Se l'utente ha bisogno di quanto mostrato per la cella in ms excel (quando la colonna adiacente è nascosta, il bordo mostrato potrebbe essere quello della successiva colonna visibile), l'utente può provare Cell.GetDisplayStyle().

### **Aggiungere le proprietà Range.Top, Range.Left, Range.Height e Range.Width.**

Ottiene la posizione e le dimensioni dell'intervallo in unità di punti.

### **Elimina la classe PowerQueryFormulaCollction e aggiungi la classe PowerQueryFormulaCollection.**

C'è un errore di battitura nella vecchia classe.

### **Aggiungere le proprietà HtmlSaveOptions.ExportPageFooters e HtmlSaveOptions.ExportPageHeaders.**

Indica se esportare intestazioni e piè di pagina durante il salvataggio come singolo file html.

### **Aggiunge la proprietà HtmlSaveOptions.ShowAllSheets.**

Indica se visualizzare tutti i fogli durante il salvataggio come singolo file html.

### **Rende obsoleta la proprietà HtmlSaveOptions.ExportHeadings e aggiunge la proprietà HtmlSaveOptions.ExportRowColumnHeadings.**

Utilizzare invece HtmlSaveOptions.ExportRowColumnHeadings.

### **Obsoleto Chart.ToImage(string, ImageFormat) e aggiunto Chart.ToImage(string, ImageType)**

Utilizzare invece Chart.ToImage(string, ImageType).

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