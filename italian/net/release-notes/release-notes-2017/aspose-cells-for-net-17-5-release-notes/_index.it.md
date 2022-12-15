---
title: Aspose.Cells for .NET 17.5 Note di rilascio
type: docs
weight: 80
url: /it/net/aspose-cells-for-net-17-5-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 17.5](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.5/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-41365|Supporta la conformità PDF/A-1a in PdfSaveOptions|Nuova caratteristica|
|CELLSNET-45347|Rimuovi le impostazioni della stampante esistenti nel file Excel|Nuova caratteristica|
|CELLSNET-45340|Implementa le opzioni Dimensione pagina personalizzata per il foglio di lavoro|Nuova caratteristica|
|CELLSNET-45327|Supporta l'esportazione dei dati delle celle HTML in DataTable|Nuova caratteristica|
|CELLSNET-45316|Supporta il funzionamento di GridWeb quando la modalità di stato della sessione ASP.NET è SQL Server|Nuova caratteristica|
|CELLSNET-45350|Errore OutOfMemory durante il rendering dell'immagine|Prestazione|
|CELLSNET-45341|La conversione di XLS in SpreadsheetML con filtri corrompe il file di output|Prestazione|
|CELLSNET-45217|Il salvataggio di Excel in PDF ruota l'immagine|Insetto|
|CELLSNET-45306|Stili errati durante il salvataggio in HTML con prefisso css|Insetto|
|CELLSNET-45304|L'allineamento del testo ruotato verticalmente è errato nell'HTML di output|Insetto|
|CELLSNET-45299|Il testo non entra nella cella durante il salvataggio come HTML|Insetto|
|CELLSNET-45288|Si è verificata un'eccezione durante il caricamento di un file HTML|Insetto|
|CELLSNET-45274|I dati della tabella pivot non vengono aggiornati correttamente|Insetto|
|CELLSNET-45336|Il metodo di calcolo della cartella di lavoro non è in grado di calcolare la formula XIRR - II|Insetto|
|CELLSNET-45333|I valori nelle celle M114 e N114 non sono corretti dopo il calcolo della formula della cartella di lavoro|Insetto|
|CELLSNET-45318|Il metodo di calcolo della cartella di lavoro non è in grado di calcolare la formula XIRR|Insetto|
|CELLSNET-45310|Più utenti riscontrano problemi in GridWeb quando lo stato della sessione è fuori processo|Insetto|
|CELLSNET-45324|La posizione dei caratteri non è allineata al centro durante il rendering di un file Excel in PDF|Insetto|
|CELLSNET-45339|Il file convertito da ODS a XML (SpreadsheetML) non viene aperto da MS Excel|Insetto|
|CELLSNET-45326|Cell.HtmlString non evidenzia correttamente il colore del carattere nidificato|Insetto|
|CELLSNET-45325|Le convalide dei dati risultano strane dopo l'inserimento di nuove righe|Insetto|
|CELLSNET-45322|Il metodo Cells.ImportDataTable è stato modificato|Insetto|
|CELLSNET-45314|La proprietà CopyOptions.ExtendToAdjacentRange non funziona|Insetto|
|CELLSNET-45312|Il file Excel finale è diverso dal file Excel originale|Insetto|
|CELLSNET-45303|Le forme (rettangoli, linee, ecc.) non vengono più unite durante il salvataggio successivo dal formato file XLSX al formato XLS|Insetto|
|CELLSNET-45301|L'apertura e il salvataggio del file Excel rende l'allineamento errato|Insetto|
|CELLSNET-45297|L'apertura e il salvataggio del file XLSM con una versione più recente lo danneggiano|Insetto|
|CELLSNET-45296|La rimozione di tutti i commenti da una cartella di lavoro provoca errori all'apertura in Excel|Insetto|
|CELLSNET-45308|Traduci "Altro" di Grafico a torta|Insetto|
|CELLSNET-45298|Le voci della legenda non sono nascoste correttamente nel grafico combinato|Insetto|
|CELLSNET-45313|Eccezione durante l'aggiunta di un campo calcolato alla tabella pivot|Eccezione|
|CELLSNET-45307|Errore da forma a immagine durante il rendering del foglio di lavoro in immagine|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà ExportTableOptions.ExportAsHtmlString**
Esporta il valore della stringa HTML delle celle in DataTable.
#### **Aggiunge il metodo PageSetup.Copy(PageSetup source,CopyOptions copyOptions).**
Copia le impostazioni del Page Setup.
#### **Aggiunge la proprietà ImportTableOptions.ShiftFirstRowDown**
Indica se spostare la prima riga verso il basso durante l'inserimento della tabella.
#### **Aggiunge il metodo PageSetup.CustomPaperSize()**
Imposta il formato carta personalizzato, nell'unità di pollici.
#### **Aggiunge la proprietà PageSetup.PrinterSettings**
Ottiene e imposta le impostazioni della stampante predefinita.
#### **Aggiunge enum PaperSizeType.Custom**
Rappresenta il formato carta personalizzato.
#### **Aggiunge enum PdfCompliance.PdfA1a**
Rappresenta il formato PDF compatibile con PDFA-1a.


#### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Converti file Excel in formato PDF compatibile con PDFA-1a](/cells/it/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Copia le impostazioni di impostazione della pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione](/cells/it/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Implementa il formato carta personalizzato del foglio di lavoro per il rendering](/cells/it/net/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel](/cells/it/net/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [Sposta la prima riga verso il basso quando inserisci le righe della tabella dati Cells](/cells/it/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [Esporta il valore stringa HTML di Cells nel DataTable](/cells/it/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Funzionamento di GridWeb quando la modalità dello stato della sessione ASP.NET è SQL Server](/cells/it/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)
- [Abilita diverse modalità GridWeb](/cells/it/net/enable-different-gridweb-modes/)


