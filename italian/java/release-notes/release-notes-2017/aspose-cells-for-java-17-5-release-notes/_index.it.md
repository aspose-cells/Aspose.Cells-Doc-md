---
title: Aspose.Cells for Java 17.5 Note di rilascio
type: docs
weight: 80
url: /it/java/aspose-cells-for-java-17-5-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.5/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41130|Cambia la lingua delle parole predefinite per la tabella pivot|Aumento|
|CELLSJAVA-42272|Opzioni per incorporare il collegamento ipertestuale in una cella di Excel|Aumento|
|CELLSJAVA-42283|NullPointerException si verifica quando il filtro esiste al di fuori dell'intervallo denominato|Insetto|
|CELLSJAVA-42282|La copia di un foglio di lavoro mostra le righe filtrate nel file di output HTML|Insetto|
|CELLSJAVA-42276|I contenuti sono mostrati in modo diverso (manca del testo) nei browser non IE (ad es. Google chrome) - Rendering da Excel a HTML|Insetto|
|CELLSJAVA-42247|La formattazione condizionale viene persa quando si aggiorna la tabella pivot nel foglio di calcolo|Insetto|
|CELLSJAVA-42257|Lo stile di formattazione condizionale non funziona|Insetto|
|CELLSJAVA-42202|La formula di Excel non funziona correttamente: viene visualizzata come 6 anziché 0|Insetto|
|CELLSJAVA-42286|Il salvataggio del file XLS con i grafici utilizza il 100% della CPU|Insetto|
|CELLSJAVA-42251|Il titolo è oscurato dalle etichette di tendenza nell'output PDF|Insetto|
|CELLSJAVA-42284|Workbook.getFonts() mostra caratteri aggiuntivi dopo aver ricaricato lo stesso foglio di calcolo|Insetto|
|CELLSJAVA-42281|Unione/Copia su fogli Excel: gli spazi all'inizio delle celle non vengono mantenuti|Insetto|
|CELLSJAVA-42280|Stringa non valida nel file: si verifica un errore all'apertura di un file Excel|Insetto|
|CELLSJAVA-42275|Nomi di alcuni parametri di metodi pubblici modificati nella versione più recente|Insetto|
|CELLSJAVA-42271|Worksheet.autoFitColumns() non funziona bene con le celle con interruzioni di riga|Insetto|
|CELLSJAVA-42266|L'ordinamento del file Excel contenente i commenti danneggia il file Excel di output|Insetto|
|CELLSJAVA-42265|L'ordinamento dei commenti causa l'errore "Excel ha trovato contenuto illeggibile..." all'apertura del file di output in MS Excel|Insetto|
|CELLSJAVA-42264|Problemi di pedice e apice nel file OpenOffice ODS durante la conversione in HTML o PDF|Insetto|
|CELLSJAVA-42268|Eccezione: "java.lang.NullPointerException" durante il rendering di un grafico in un'immagine|Eccezione|
|CELLSJAVA-42278|Eccezione: "java.lang.IndexOutOfBoundsException: Index: 12, Size: 12" durante il salvataggio nel formato file HTML|Eccezione|
|CELLSJAVA-42274|Eccezione: "java.lang.StringIndexOutOfBoundsException: Indice stringa fuori intervallo: 0" durante il caricamento di un file XLSX|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà ExportTableOptions.ExportAsHtmlString**
Esporta il valore stringa HTML delle celle in DataTable.
### **Aggiunge il metodo PageSetup.Copy(PageSetup source,CopyOptions copyOptions).**
Copia le impostazioni del Page Setup.
### **Aggiunge la proprietà ImportTableOptions.ShiftFirstRowDown**
Indica se spostare la prima riga verso il basso durante l'inserimento della tabella.
### **Aggiunge il metodo PageSetup.CustomPaperSize()**
Imposta il formato carta personalizzato, nell'unità di pollici.
### **Aggiunge la proprietà PageSetup.PrinterSettings**
Ottiene e imposta le impostazioni della stampante predefinita.
### **Aggiunge costanti PaperSizeType.CUSTOM**
Rappresenta il formato carta personalizzato.
### **Aggiunge le costanti PdfCompliance.PDF_A_1_A**
Rappresenta il formato PDF compatibile con PDFA-1a.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Converti il file Excel nel formato PDF compatibile con PDFA-1a](/cells/it/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Copia le impostazioni di impostazione della pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione](/cells/it/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Implementa il formato carta personalizzato del foglio di lavoro per il rendering](/cells/it/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel](/cells/it/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [Sposta la prima riga verso il basso quando inserisci le righe della tabella dati Cells](/cells/it/java/shift-first-row-down-when-inserting-cells-data-table-rows/)
