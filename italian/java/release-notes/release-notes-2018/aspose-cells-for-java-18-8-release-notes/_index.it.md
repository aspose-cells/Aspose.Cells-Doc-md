---
title: Aspose.Cells for Java 18.8 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-18-8-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.8.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42680|Disabilita la barra multifunzione della tabella pivot|Nuova caratteristica|
|CELLSJAVA-42568|Proteggi la cartella di lavoro e il foglio di lavoro nel file ODS|Nuova caratteristica|
|CELLSJAVA-42677|Problema di interruzione durante il salvataggio del processo di file XLSX|Aumento|
|CELLSJAVA-42687|Il collegamento ipertestuale non funziona quando viene fatto riferimento da un altro foglio|Aumento|
|CELLSJAVA-41176|Allineamento errato durante il rendering del foglio di calcolo in formato PDF|Insetto|
|CELLSJAVA-42676|I dati della tabella sono stati spostati in righe e colonne errate durante la conversione dal formato di file HTML a MS Excel|Insetto|
|CELLSJAVA-41670|La posizione dell'immagine del grafico è errata in Chrome e FireFox durante la conversione in HTML|Insetto|
|CELLSJAVA-41245|Il controllo Slicer non viene visualizzato durante la conversione di file Excel in formato file HTML|Insetto|
|CELLSJAVA-42684|La linea verticale al centro del grafico non è disegnata correttamente nell'immagine renderizzata|Insetto|
|CELLSJAVA-42682|Il colore sfumato per le bolle negative non viene applicato nell'output PDF|Insetto|
|CELLSJAVA-42681|Titolo della categoria del grafico non mostrato correttamente nell'immagine|Insetto|
|CELLSJAVA-42695|Stile del bordo errato restituito per la cella unita|Insetto|
|CELLSJAVA-42694|Leggi la filigrana dal file Excel|Insetto|
|CELLSJAVA-42686|Il commento della proprietà contiene testo non necessario|Insetto|
|CELLSJAVA-42685|Proprietà "numero di revisione" non verificata correttamente|Insetto|
|CELLSJAVA-41485|Le macro nel file ODS non vengono mantenute nel formato del file ODS generato|Insetto|
|CELLSJAVA-42691|NegativeArraySizeException durante la conversione di XLSX in HTML|Eccezione|
|CELLSJAVA-42675|NumberFormatException sollevata durante il caricamento del file HTML nella cartella di lavoro|Eccezione|
|CELLSJAVA-42689|Eccezione NullPointerException sollevata durante la chiamata a CalculateFormula|Eccezione|
|CELLSJAVA-42678|Eccezione durante il rendering del foglio di lavoro nel formato di file PNG|Eccezione|
|CELLSJAVA-42411|Errore in Cell: E22-Formula non valida - eccezione all'apertura del file MS Excel|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
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
### **Aggiunge l'overload Cells.CopyColumns(Int32,Int32,PasteOptions) e il metodo Cels.CopyRows(Int32,Int32,PasteOptions)**
Supporta le opzioni di incolla durante la copia di righe e colonne.
### **Aggiunge la proprietà Axis.IsAutoTickLabelSpacing**
Indica se la spaziatura dell'etichetta del segno di spunta è automatica.
