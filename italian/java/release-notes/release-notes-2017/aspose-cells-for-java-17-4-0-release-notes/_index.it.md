---
title: Aspose.Cells for Java 17.4.0 Note di rilascio
type: docs
weight: 90
url: /it/java/aspose-cells-for-java-17-4-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.4.0/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41975|Supporta la formattazione DBNum (modello personalizzato).|Nuova caratteristica|
|CELLSJAVA-42237|L'accesso alla cella crea HTML con righe vuote|Aumento|
|CELLSJAVA-42236|Problema di prestazioni con l'ambiente multi-threading|Aumento|
|CELLSJAVA-42226|Limita a una cartella e alle sue sottocartelle per utilizzare i caratteri nel rendering images/PDF|Aumento|
|CELLSJAVA-42239|Errore di formato della stringa di input durante il caricamento di un HTML|Insetto|
|CELLSJAVA-42230|Un ulteriore attributo di allineamento viene generato durante la conversione da XLSX a HTML|Insetto|
|CELLSJAVA-42229|Esporta da XLSX a HTML: i simboli hash vengono generati al posto dei valori effettivi Cell|Insetto|
|CELLSJAVA-42218|HTML non è correttamente convertito in file Excel|Insetto|
|CELLSJAVA-42210|Parte della formattazione condizionale di DataBar è mancante nell'output HTML|Insetto|
|CELLSJAVA-41783|L'immagine di sfondo dovrebbe essere nel formato SVG ma è nel formato PNG|Insetto|
|CELLSJAVA-42253|Il valore della cella dipendente causa un errore in XLS|Insetto|
|CELLSJAVA-42222|La somma non è corretta dopo il calcolo della cartella di lavoro|Insetto|
|CELLSJAVA-42254|GridWebServlet?acw_ajax_si verifica un errore di chiamata durante il caricamento di GridWeb|Insetto|
|CELLSJAVA-42243|Da Excel a PDF - Quadrato assomiglia a Rettangolo|Insetto|
|CELLSJAVA-42242|Da Excel a PDF - Il cerchio ha l'aspetto di una forma ovale|Insetto|
|CELLSJAVA-42227|Il file immagine "x1.png" ha un bordo superiore aggiuntivo e un bordo inferiore mancante|Insetto|
|CELLSJAVA-42212|Problema di prestazioni durante l'esportazione da XLS a PDF|Insetto|
|CELLSJAVA-42246|Da Excel a HTML: l'allineamento del testo nell'etichetta dell'asse Y del grafico è errato|Insetto|
|CELLSJAVA-42223|I punti xy px del grafico radar restituiscono 0|Insetto|
|CELLSJAVA-42216|I valori associati dell'asse Y del grafico a bolle cambiano quando AxisScalingValuesIssue-2.xlsx viene convertito in PDF|Insetto|
|CELLSJAVA-42250|Errore di compilazione se il codice contiene la definizione di variabile con tipo CommandBar|Insetto|
|CELLSJAVA-42241|Excel a PDF - Le parentesi sono in arrivo nella riga successiva|Insetto|
|CELLSJAVA-42234|Il salvataggio del file XLSM come XLS rimuove l'azione macro dal pulsante|Insetto|
|CELLSJAVA-42233|Aggiorna il codice - Applicazione del formato 3D al grafico|Insetto|
|CELLSJAVA-42225|Impossibile impostare l'intervallo di input della forma|Insetto|
|CELLSJAVA-42224|Problema con l'ordinamento dei commenti|Insetto|
|CELLSJAVA-42221|Regressione critica con controlli personalizzati|Insetto|
|CELLSJAVA-42220|Problema con l'impostazione della visualizzazione layout di pagina per i file XLSB|Insetto|
|CELLSJAVA-42217|Dopo aver effettuato l'accesso a VbaModule tramite Aspose API, il file Excel risultante ha interrotto il progetto vba|Insetto|
|CELLSJAVA-42213|Il carattere sta cambiando involontariamente le sue dimensioni nel commento con un CR incorporato in esso|Insetto|
|CELLSJAVA-42231|L'eccezione si verifica durante l'inserimento di righe|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il metodo VbaProject.Protect(bool islockedForViewing,string password).**
Protegge o rimuove la protezione del progetto VBA.
### **Aggiunge la proprietà VbaProject.IsProtected**
Indica se il progetto vba è protetto.
### **Aggiunge la proprietà VbaProject.IslockedForViewing**
Indica se il progetto VBA è bloccato per la visualizzazione.
### **Aggiunge la proprietà CopyOptions.ExtendToAdjacentRange**
Indica se estendere gli intervalli durante la copia dell'intervallo in un intervallo adiacente.

{{< highlight "java" >}}

 Workbook wb = new Workbook("sample.xlsx");

Worksheet ws = wb.getWorksheets().get("Sheet1");

CopyOptions co = new CopyOptions();

co.setExtendToAdjacentRange(true);

Cells cells = ws.getCells();

cells.copyRows(cells, 0, 1, 1, co);

{{< /highlight >}}
### **Elimina il metodo Workbook.ValidateFormula(string formula) obsoleto**
### **Aggiunge la proprietà DataSorter.SortAsNumber**
Indica se ordinare qualcosa che assomiglia a un numero.
### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/java/specifying-sort-warning-while-sorting-data/)
- [Proteggi con password il progetto VBA della cartella di lavoro di Excel](/cells/it/java/password-protect-the-vba-project-of-excel-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/java/find-out-if-vba-project-is-protected/)
- [Controlla se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/java/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Specifica della formattazione del modello personalizzato DBNum](/cells/it/java/specifying-dbnum-custom-pattern-formatting/)
