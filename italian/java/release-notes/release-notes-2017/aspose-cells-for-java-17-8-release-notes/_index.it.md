---
title: Aspose.Cells for Java 17.8 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-17-8-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.8/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42356|Aggiungi una proprietà per indicare se generare o meno una pagina vuota quando non c'è niente da stampare|Nuova caratteristica|
|CELLSJAVA-42322|Supporta la funzione Filtro avanzato (MS Excel) per visualizzare i record che soddisfano criteri complessi|Nuova caratteristica|
|CELLSJAVA-42341|InterruptMonitor impiega più tempo per interrompere il processo di salvataggio della cartella di lavoro per un file di grandi dimensioni con tabella pivot|Aumento|
|CELLSJAVA-42358|La formula non viene visualizzata nel PDF risultante|Aumento|
|CELLSJAVA-42351|La formula WEEKDAY restituisce un valore errato nel calcolo della formula della cartella di lavoro|Aumento|
|CELLSJAVA-42332|Aspose.Cells non è in grado di convertire correttamente il file HTML mentre MS-Excel è in grado di convertirlo correttamente|Insetto|
|CELLSJAVA-42355|Per il numero 39 MS Excel formatta il valore negativo con '-' invece di '()' per l'Italia|Insetto|
|CELLSJAVA-42350|Il testo dell'etichetta viene spostato per il grafico a torta|Insetto|
|CELLSJAVA-42343|Vari stili del grafico a cascata non vengono visualizzati correttamente.|Insetto|
|CELLSJAVA-42342|Il grafico a cascata mostra sempre le linee di connessione|Insetto|
|CELLSJAVA-42352|La forma non viene aggiornata con il valore corretto|Insetto|
|CELLSJAVA-42349|Conversione da Excel a PDF impiccata per un file XLSX|Insetto|
|CELLSJAVA-42348|Impossibile importare il file XLSB (tramite API Aspose.Cells) nel database MS-Access|Insetto|
|CELLSJAVA-42357|L'eccezione si verifica quando si salva un file Excel in formato HTML|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HtmlSaveOptions.IsExportComments**
Indica se durante l'esportazione dei commenti durante il salvataggio del file in HTML, il valore predefinito è false.
### **Aggiunge la proprietà HtmlSaveOptions.DisableDownlevelRevealedComments**
Indica se disabilitare i commenti condizionali rivelati di livello inferiore durante l'esportazione del file in HTML, il valore predefinito è false.
### **Aggiunge la classe CustomImplementationFactory**
Fornisce API all'utente per estendere/migliorare la capacità del componente mediante alcune implementazioni speciali per alcune situazioni speciali. Attualmente non esiste alcuna implementazione personalizzata supportata nella versione for Java.
### **Aggiunge la proprietà CellsHelper.CustomImplementationFactory**
Ottiene/imposta l'istanza CustomImplementationFactory utilizzata dal componente celle.
### **Aggiunge il metodo Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection).**
Aggiunge la firma digitale a un file di foglio di calcolo OOXML già firmato (Excel2007 e versioni successive).
### **Aggiunge la proprietà ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**
Indica se emettere una pagina vuota quando non c'è niente da stampare.
### **Aggiunge il metodo GridCell.CreateComment**
Crea un oggetto commento per una cella.
### **Aggiunge il metodo GridCell.RemoveComment**
Rimuove l'oggetto commento della cella.
### **Aggiunge il metodo GridCell.GetComment**
Ottiene l'oggetto commento su questa cella.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Aggiungi la firma digitale a un file Excel già firmato](/cells/it/java/add-digital-signature-to-an-already-signed-excel-file/)
- [Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML](/cells/it/java/disable-downlevel-revealed-comments-while-saving-to-html/)
- [Esporta commenti durante il salvataggio del file Excel in Html](/cells/it/java/export-comments-while-saving-excel-file-to-html/)
- [Stampa pagina vuota quando non c'è niente da stampare](/cells/it/java/output-blank-page-when-there-is-nothing-to-print/)
- [Crea Rimuovi e ottieni commenti GridCell](/cells/it/java/create-remove-and-get-gridcell-comments/)
