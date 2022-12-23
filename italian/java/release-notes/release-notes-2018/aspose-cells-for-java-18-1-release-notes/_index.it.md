---
title: Aspose.Cells for Java 18.1 Note di rilascio
type: docs
weight: 120
url: /it/java/aspose-cells-for-java-18-1-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.1.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42493|Fornire un'opzione per decidere se esportare le proprietà della cartella di lavoro (id problema principale: CELLSJAVA-42471)|Nuova caratteristica|
|CELLSJAVA-42491|Fornire un'opzione per decidere se esportare le proprietà del documento (id problema principale: CELLSJAVA-42471)|Nuova caratteristica|
|CELLSJAVA-42498|Crea un PdfBookmarkEntry per un foglio grafico|Nuova caratteristica|
|CELLSJAVA-42464|Correzione necessaria per tutti i controlli ActiveX (ID problema principale: CELLSJAVA-42442)|Aumento|
|CELLSJAVA-42490|Escludi gli stili inutilizzati durante l'esportazione del file Excel in HTML (id problema principale: CELLSJAVA-42471)|Aumento|
|CELLSJAVA-42473|Parti delle immagini sono troncate o mancanti e non corrispondono alle immagini originali|Insetto|
|CELLSJAVA-42469|L'immagine sporge dalla forma nell'output PDF|Insetto|
|CELLSJAVA-42461|La forma dell'elemento non è corretta nell'output HTML|Insetto|
|CELLSJAVA-42495|Da Excel a Html: il testo di wrapping viene ignorato|Insetto|
|CELLSJAVA-42489|XLSB il file viene danneggiato dopo l'apertura e il salvataggio|Insetto|
|CELLSJAVA-42487|HTML discrepanza di output - Problema con gli spazi|Insetto|
|CELLSJAVA-42471|Dati irrilevanti inclusi durante il salvataggio in HTML|Insetto|
|CELLSJAVA-42467|XLSB danneggiato dopo il nuovo salvataggio|Insetto|
|CELLSJAVA-42488|I numeri a 15 cifre non corrispondono a quelli presenti in MS Excel|Insetto|
|CELLSJAVA-42499|Margini e differenze di layout quando si confronta l'output PDF (di Aspose.Cells) con MS Excel generato PDF|Insetto|
|CELLSJAVA-42486|La funzione non funziona in Java - ResultSet|Insetto|
|CELLSJAVA-42500|NullPointerException si verifica durante il caricamento del file MS Excel|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà LoadOptions.ParsingPivotCachedRecords**
Indica se l'analisi dei record memorizzati nella cache pivot durante il caricamento del file. Il valore predefinito è false. Si applica solo ai formati di file Excel Xlsx, Xltx, Xltm, Xlsm e Xlsb.
### **Aggiunge la proprietà HtmlSaveOptions.ExcludeUnusedStyles**
Indica se escludere gli stili inutilizzati. Il valore predefinito è false. Se desideri importare il file HTML o Mht in Excel, mantieni il valore predefinito.
### **Aggiunge la proprietà HtmlSaveOptions.ExportDocumentProperties**
Indica se esportare le proprietà del documento. Il valore predefinito è true. Se desideri importare il file HTML o Mht in Excel, mantieni il valore predefinito.
### **Aggiunge la proprietà HtmlSaveOptions.ExportWorksheetProperties**
Indica se esportare le proprietà del foglio di lavoro. Il valore predefinito è true. Se desideri importare il file HTML o Mht in Excel, mantieni il valore predefinito.
### **Aggiunge la proprietà HtmlSaveOptions.ExportWorkbookProperties**
Indica se esportare le proprietà della cartella di lavoro. Il valore predefinito è true. Se desideri importare il file HTML o Mht in Excel, mantieni il valore predefinito.
### **Aggiunge il metodo PivotTable.GetChildren()**
Ottiene le tabelle pivot figlio che utilizzano i dati di questa tabella pivot come origine dati.
