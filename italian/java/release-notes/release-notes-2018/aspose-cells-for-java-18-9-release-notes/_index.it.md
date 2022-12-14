---
title: Aspose.Cells for Java 18.9 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-18-9-release-notes/
---
{{% alert color="primary" %}}

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.9.

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42715|Le formule non vengono recuperate come nel file MS Excel|Insetto|
|CELLSJAVA-42711|Il grafico in PDF non viene generato dal modello Excel|Insetto|
|CELLSJAVA-42710|Duplica il testo dell'elemento della legenda nel grafico nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-42706|L'output PDF non mostra l'etichetta del grafico|Insetto|
|CELLSJAVA-42700|Grafico a cascata non visualizzato correttamente dopo aver modificato i dati del grafico|Insetto|
|CELLSJAVA-42717|Cells.deleteRow funziona in modo errato|Insetto|
|CELLSJAVA-42716|Valore errato recuperato per lo stile del bordo|Insetto|
|CELLSJAVA-42709|Stile del bordo inferiore errato restituito per la cella unita|Insetto|
|CELLSJAVA-42705|MS Excel genera un errore durante il caricamento del file dopo aver impostato il filtro automatico|Insetto|
|CELLSJAVA-42703|Grafico non visualizzato durante la conversione di ODS in PDF|Insetto|
|CELLSJAVA-42702|bordi grigi vengono visualizzati dopo aver letto lo stile della cella nel foglio di lavoro|Insetto|
|CELLSJAVA-42699|IncollaTipo.VALORI_E_NUMBER_FORMATS non funziona correttamente|Insetto|
|CELLSJAVA-42646|Eccezione: "FormulaBuild Unknown formula token0" su Name.getRefersTo()|Eccezione|
|CELLSJAVA-42707|Il metodo Chart.calculate causa OutOfMemoryError|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

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

Specifica il modo in cui le CustomDocumentPropertyCollection vengono esportate nel file PDF.

### **Aggiunge la proprietà PdfSaveOptions.CustomPropertiesExport**

Ottiene o imposta un valore che determina il modo in cui CustomDocumentPropertyCollection viene esportato in un file PDF. Il valore predefinito è Nessuno.

### **Aggiunge la classe XmlDataBinding**

Rappresenta le informazioni sull'associazione dati Xml.

### **Aggiunge la proprietà ListObject.XmlMap**

Ottiene un oggetto XmlMap usato per questo elenco.

### **Aggiunge la proprietà XmlDataBinding.Url**

Ottiene l'URL di origine di questo data binding.

### **Aggiunge la proprietà XmlMap.DataBinding**

Ottiene un XmlDataBinding di questa mappa.
