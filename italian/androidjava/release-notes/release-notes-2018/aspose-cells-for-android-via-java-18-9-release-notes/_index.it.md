---
title: Aspose.Cells for Android via Java 18.9 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-android-via-java-18-9-release-notes/
---
{{% alert color="primary" %}}

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 18.9.

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42680|Disabilita la barra multifunzione della tabella pivot|Nuova caratteristica|
|CELLSJAVA-42568|Proteggi la cartella di lavoro e il foglio di lavoro nel file ODS|Nuova caratteristica|
|CELLSJAVA-42668|Supporta più valori quando si utilizza lo stile di classe (collegato a: CELLSJAVA-42635)|Aumento|
|CELLSJAVA-42627|Impossibile estrarre correttamente le immagini Smart Art - Conversione da forma a immagine (CELLSJAVA-42619)|Aumento|
|CELLSJAVA-42677|Problema di interruzione durante il salvataggio del processo di file XLSX|Aumento|
|CELLSJAVA-42687|Il collegamento ipertestuale non funziona quando viene fatto riferimento da un altro foglio|Aumento|
|CELLSJAVA-42672|Il documento di output PDF è troppo grande|Insetto|
|CELLSJAVA-42671|Problema di collegamenti ipertestuali durante la visualizzazione del file Excel di output nella versione giapponese di MS Excel|Insetto|
|CELLSJAVA-42667|Ottenere '#NUM!' per una cella con funzione IRR|Insetto|
|CELLSJAVA-42658|Le cartelle di lavoro con macro XL4 (XLSM) vengono danneggiate dopo il salvataggio|Insetto|
|CELLSJAVA-42656|AlternativeText restituisce il valore del commento Text|Insetto|
|CELLSJAVA-42635|Da HTML a XLS - Stile CSS ignorato|Insetto|
|CELLSJAVA-41176|Allineamento errato durante il rendering del foglio di calcolo nel formato PDF|Insetto|
|CELLSJAVA-42676|Dati della tabella spostati nella riga e nella colonna sbagliate durante la conversione da HTML al formato di file MS Excel|Insetto|
|CELLSJAVA-41670|La posizione dell'immagine del grafico è errata in Chrome e FireFox durante la conversione in HTML|Insetto|
|CELLSJAVA-41245|Il controllo Slicer non viene visualizzato durante la conversione del file Excel nel formato file HTML|Insetto|
|CELLSJAVA-42684|La linea verticale al centro del grafico non è disegnata correttamente nell'immagine renderizzata|Insetto|
|CELLSJAVA-42682|Il colore sfumato per le bolle negative non viene applicato nell'output PDF|Insetto|
|CELLSJAVA-42681|Titolo della categoria del grafico non mostrato correttamente nell'immagine|Insetto|
|CELLSJAVA-42695|Stile del bordo errato restituito per la cella unita|Insetto|
|CELLSJAVA-42694|Leggi la filigrana dal file Excel|Insetto|
|CELLSJAVA-42686|Il commento della proprietà contiene testo non necessario|Insetto|
|CELLSJAVA-42685|Proprietà "numero di revisione" non verificata correttamente|Insetto|
|CELLSJAVA-41485|Le macro nel file ODS non vengono mantenute nel formato file ODS generato|Insetto|
|CELLSJAVA-42715|Le formule non vengono recuperate come nel file Excel|Insetto|
|CELLSJAVA-42711|Il grafico in PDF non viene generato dal modello Excel|Insetto|
|CELLSJAVA-42710|Duplica il testo dell'elemento della legenda nel grafico in Excel alla conversione PDF|Insetto|
|CELLSJAVA-42706|L'output PDF non mostra l'etichetta del grafico|Insetto|
|CELLSJAVA-42700|Grafico a cascata non visualizzato correttamente dopo aver modificato i dati del grafico|Insetto|
|CELLSJAVA-42717|Cells.deleteRow funziona in modo errato|Insetto|
|CELLSJAVA-42716|Valore errato recuperato per lo stile del bordo|Insetto|
|CELLSJAVA-42709|Stile del bordo inferiore errato restituito per la cella unita|Insetto|
|CELLSJAVA-42705|Excel genera un errore durante il caricamento del file dopo aver impostato il filtro automatico|Insetto|
|CELLSJAVA-42703|Grafico non visualizzato durante la conversione da ODS a PDF|Insetto|
|CELLSJAVA-42702|I bordi grigi vengono visualizzati dopo aver letto lo stile della cella nel foglio di lavoro|Insetto|
|CELLSJAVA-42699|IncollaTipo.VALORI_E_NUMBER_FORMATS non funziona correttamente|Insetto|
|CELLSJAVA-42646|Eccezione: "FormulaBuild Unknown formula token0" su Name.getRefersTo()|Eccezione|
|CELLSJAVA-42707|Il metodo Chart.calculate causa OutOfMemoryError|Eccezione|
|CELLSJAVA-42673|Eccezione "java.lang.NumberFormatException" durante il caricamento di un file Excel|Eccezione|
|CELLSJAVA-42669|Eccezione "java.lang.NullPointerException" durante il calcolo delle formule nella cartella di lavoro|Eccezione|
|CELLSJAVA-42663|Chart.calculate() genera un'eccezione IndexOutOfBoundsException|Eccezione|
|CELLSJAVA-42655|Eccezione: "Codifica non valida: null" durante il caricamento di un file XLS - II|Eccezione|
|CELLSJAVA-42675|NumberFormatException sollevata durante il caricamento del file HTML nella cartella di lavoro|Eccezione|
|CELLSJAVA-42689|Eccezione NullPointerException sollevata durante la chiamata a CalculateFormula|Eccezione|
|CELLSJAVA-42678|Eccezione durante il rendering del foglio di lavoro nel formato file PNG|Eccezione|
|CELLSJAVA-42411|Errore in Cell: E22-Formula non valida - eccezione all'apertura del file MS Excel|Eccezione|
|CELLSJAVA-42691|NegativeArraySizeException durante la conversione da XLSX a HTML|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo sul forum di supporto Aspose.Cells.

### **Aggiunge enum StyleFlag.Alignments**

Rappresenta tutte le impostazioni di allineamento.

### **Aggiunge le proprietà WorkbookSettings.MaxRow e WorkbookSettings.MaxColumn**

Ottiene l'indice massimo di righe e colonne della cartella di lavoro.

### **Aggiunge la proprietà WriteProtection.Author**

Ottiene e imposta l'autore della protezione da scrittura.

### **Aggiunge la proprietà PdfSecurityOptions.AccessibilityExtractContent**

Autorizzazione a copiare o estrarre contenuti (a supporto dell'accessibilità agli utenti disabili o per altri scopi).

### **Aggiunge la classe SubtotalSetting**

Rappresenta l'impostazione del subtotale.

### **Aggiunge il metodo Cells.RetrieveSubtotalSetting(CellArea)**

Recupera l'impostazione del subtotale.

### **Aggiunge il metodo di sovraccarico Range.ExportDataTable(Aspose.Cells.ExportTableOptions).**

Supporta le opzioni di esportazione dell'intervallo.

### **Aggiunge la proprietà WebQueryConnection.IsSameSetting ed elimina la proprietà WebQueryConnection.IsFirstRow**

Utilizzare invece la proprietà WebQueryConnection.IsSameSetting.

### **Aggiunge la proprietà WebQueryConnection.IsXmlSourceData ed elimina la proprietà WebQueryConnection.IsSourceData**

Utilizzare invece la proprietà WebQueryConnection.IsXmlSourceData.

### **Aggiunge la proprietà Shape.IsEquation**

Indica se la forma contiene un'equazione.

### **Aggiunge l'overload Cells.CopyColumns(Int32,Int32,PasteOptions) e il metodo Cells.CopyRows(Int32,Int32,PasteOptions)**

Supporta le opzioni di incolla durante la copia di righe e colonne.

### **Aggiunge la proprietà Axis.IsAutoTickLabelSpacing**

Indica se la spaziatura dell'etichetta del segno di spunta è automatica.

### **Aggiunge i metodi CellsHelper.CreateSafeSheetName(string nameProposal)/CreateSafeSheetName(string nameProposal, char replaceChar)**

Metodi per comodità dell'utente per creare un nome di foglio valido.

### **Aggiunge Row.FirstDataCell**

Ottiene la prima cella non vuota nella riga.

### **Aggiunge l'enumerazione MapChartLabelLayout**

Rappresenta il tipo di layout dell'etichetta del grafico a mappa.

### **Aggiunge l'enumerazione MapChartProjectionType**

Rappresenta il tipo di proiezione del grafico a mappa.

### **Aggiunge l'enumerazione MapChartRegionType**

Rappresenta il tipo di regione del grafico a mappa.

### **Aggiunge l'enumerazione QuartileCalculationType**

Rappresenta il tipo di calcolo quartile del grafico.

### **Aggiunge la proprietà Series.LayoutProperties e la classe SeriesLayoutProperties**

Rappresenta le proprietà di layout della serie.

### **Aggiunge la proprietà TickLabels.IsAutomaticRotation**

Indica se la rotazione delle etichette di spunta è automatica.

### **Aggiunge l'enumerazione FilterOperatorType.BeginsWith, Contains, EndsWith e NotContains**

Rappresenta il tipo di operatore del filtro di testo.

### **Aggiunge il metodo Cell.GetDisplayStyle(bool).**

Ottiene lo stile di visualizzazione della cella.

### **Aggiunge il metodo GlobalizationSettings.GetStandardHeaderFooterFontStyleName(string localFontStyleName)**

Ottiene il nome dello stile del carattere inglese standard (regolare, grassetto, corsivo) per intestazione/piè di pagina in base al nome dello stile del carattere locale specificato.

### **Aggiunge l'enumerazione PdfCustomPropertiesExport**

Specifica il modo in cui CustomDocumentPropertyCollection viene esportato nel file PDF.

### **Aggiunge la proprietà PdfSaveOptions.CustomPropertiesExport**

Ottiene o imposta un valore che determina il modo in cui CustomDocumentPropertyCollection viene esportato nel file PDF. Il valore predefinito è Nessuno.

### **Aggiunge la classe XmlDataBinding**

Rappresenta le informazioni sull'associazione dati Xml.

### **Aggiunge la proprietà ListObject.XmlMap**

Ottiene un oggetto XmlMap usato per questo elenco.

### **Aggiunge la proprietà XmlDataBinding.Url**

Ottiene l'URL di origine di questo data binding.

### **Aggiunge la proprietà XmlMap.DataBinding**

Ottiene un XmlDataBinding di questa mappa.

{{% alert color="primary" %}}

Since the code base of Aspose.Cells for Android via Java matches the code of relevant .NET and Java version(s), most of the changes, enhancements and fixes included in the Aspose.Cells for .NET v18.7, Aspose.Cells for .NET v18.8, Aspose.Cells for .NET v18.9, Aspose.Cells for Java v18.7, Aspose.Cells for Java v18.8 e Aspose.Cells for Java v18.9 sono inclusi anche in questo Aspose.Cells for Android via Java v18.9.

{{% /alert %}}
