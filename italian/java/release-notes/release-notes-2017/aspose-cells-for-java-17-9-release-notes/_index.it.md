---
title: Aspose.Cells for Java 17.9 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-17-9-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.9/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42391|La larghezza Cell mostrata nel PDF risultante non è la stessa del file Excel quando si utilizza la funzione "Mostra formula"|Nuova caratteristica|
|CELLSJAVA-42379|Implementa la destinazione denominata durante il rendering nell'output PDF (query sui segnalibri)|Nuova caratteristica|
|CELLSJAVA-42401|Devi enumerare tutte le forme per impostare correttamente l'ordine Z della forma|Aumento|
|CELLSJAVA-42368|Imposta il nome del controllo ActiveX (ListBox)|Aumento|
|CELLSJAVA-42369|L'output HTML del documento Excel contiene valori hash anziché valori effettivi|Insetto|
|CELLSJAVA-42366|Il salvataggio di "2.2 CompleteEmail.html" nel formato XLSX genera un file corrotto|Insetto|
|CELLSJAVA-42365|Il caricamento di "2.1 CompleteEmail.html" nell'oggetto cartella di lavoro genera NullPointerException|Insetto|
|CELLSJAVA-42381|Il calcolo della cartella di lavoro è errato per la formula di ricerca di Excel|Insetto|
|CELLSJAVA-42380|La formula di matrice nel foglio viene calcolata in modo diverso tramite Aspose.Cells|Insetto|
|CELLSJAVA-42370|Collegamenti ipertestuali e contenuti PDF errati|Insetto|
|CELLSJAVA-42395|Rendering - L'immagine del grafico non è corretta|Insetto|
|CELLSJAVA-42393|Le etichette dell'asse delle categorie mancano durante la conversione di Excel in PDF|Insetto|
|CELLSJAVA-42384|Il colore delle barre negative non è corretto quando Excel viene convertito in PDF|Insetto|
|CELLSJAVA-42378|Il colore della barra è cambiato durante la conversione di Excel in PDF quando si utilizza setCrossAt()|Insetto|
|CELLSJAVA-42377|Il valore delle unità principali dell'asse nel grafico viene restituito errato|Insetto|
|CELLSJAVA-42364|Le etichette dati dall'intervallo di celle non vengono visualizzate quando vengono esportate in PDF|Insetto|
|CELLSJAVA-42359|Etichette dati mancanti per una serie con valori barra pari a 100|Insetto|
|CELLSJAVA-42314|Il grafico è vuoto nel PNG di output|Insetto|
|CELLSJAVA-42313|Il grafico è vuoto nel PDF di output|Insetto|
|CELLSJAVA-42374|Riferimenti di caratteri analizzati in modo errato da Aspose Cells|Insetto|
|CELLSJAVA-42373|La copia della cartella di lavoro e il successivo salvataggio danneggiano il file Excel di output|Insetto|
|CELLSJAVA-42392|Eccezione "com.aspose.cells.CellsException: contenuto excel sconosciuto!" sulla creazione di un'istanza di un file Excel crittografato|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HTMLLoadOptions.LoadStyleStrategy**
Indica la strategia per applicare lo stile ai valori analizzati durante la conversione del valore stringa in numero o DateTime.
### **Aggiunge la classe AbstractCalculationMonitor**
Fornisce API agli utenti per monitorare l'avanzamento del calcolo della formula.
### **Aggiunge la proprietà CalculationOptions.CalculationMonitor**
Consente all'utente di fornire un'implementazione personalizzata per monitorare l'avanzamento del calcolo della formula.
### **Aggiunge enum GridlineType**
Enumera il tipo di griglia.
### **Aggiunge la proprietà ImageOrPrintOptions.GridlineType**
Ottiene o imposta il tipo di griglia.
### **Aggiunge la proprietà PdfSaveOptions.GridlineType**
Ottiene o imposta il tipo di griglia.
### **Aggiunge i metodi Name.GetRanges(bool) e Name.GetRange(bool).**
Per la maggior parte degli oggetti Nome semplici, ad esempio intervalli denominati con riferimenti assoluti, il riferimento del nome non deve essere calcolato ripetutamente. Quindi GetRanges(false)/GetRange(false) non ricalcolerà l'oggetto Name quando si ottengono gli intervalli corrispondenti e quindi le prestazioni potrebbero essere migliorate in modo significativo se tali metodi vengono chiamati ripetutamente.
### **Aggiunge la proprietà PdfBookmarkEntry.DestinationName**
Ottiene o imposta il nome della destinazione. Se il nome della destinazione è impostato, la destinazione sarà definita come una destinazione denominata con questo nome.
### **Aggiunge il metodo DataSorter.AddKey()**
Aggiunge l'indice di colonna ordinato e l'ordinamento con l'elenco di ordinamento personalizzato.
### **Aggiunge il metodo Picture.Copy()**
Copia le impostazioni da un'altra immagine.
### **Aggiunge il metodo Shape.ToFrontOrBack()**
Porta la forma in primo piano o la manda in secondo piano.
### **Aggiunge enum ConnectionDataSourceType.Table**
Rappresenta la tabella come origine dati della connessione.
### **Aggiunge il metodo PageSetup.SetFitToPages()**
Imposta il numero di pagine a cui verrà ridimensionato il foglio di lavoro quando viene stampato.
### **Aggiunge la proprietà PdfSaveOptions.StreamProvider e l'enumerazione ResourceLoadingType**
Ottiene e imposta il tipo di caricamento della risorsa esterna.
### **Aggiunge i metodi VbaModuleCollection.AddDesignerStorage() e GetDesignerStorage()**
Ottiene e imposta l'archiviazione della finestra di progettazione del progetto VBA.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Aggiungi segnalibri PDF con destinazioni denominate](/cells/it/java/add-pdf-bookmarks-with-named-destinations/)
- [Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering in PDF](/cells/it/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione](/cells/it/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Crea Rimuovi e ottieni commenti GridCell](/cells/it/java/create-remove-and-get-gridcell-comments/)
- [Invia la forma davanti o dietro all'interno del foglio di lavoro](/cells/it/java/send-shape-front-or-back-inside-the-worksheet/)
- [Ordina i dati nella colonna con l'elenco di ordinamento personalizzato](/cells/it/java/sort-data-in-column-with-custom-sort-list/)
