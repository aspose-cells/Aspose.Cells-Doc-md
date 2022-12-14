---
title: Aspose.Cells for .NET 20.10 Note di rilascio
type: docs
weight: 7
url: /it/net/aspose-cells-for-net-20-10-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.10](https://www.nuget.org/packages/Aspose.Cells/20.10.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47625|Verifica la password per i file crittografati|Nuova caratteristica|
|CELLSNET-47601|Renderizza righe e colonne extra in HTML senza disturbare formule/riferimenti per assomigliare all'output con MS Excel|Nuova caratteristica|
|CELLSNET-47619|Aspose Grafico SetChartDataRange Problema|Aumento|
|CELLSNET-47632|Struttura e differenza di ordine in OLE dell'input e dell'output dopo il salvataggio del file|Aumento|
|CELLSNET-47644|Diverse connessioni esterne recuperate rispetto a MS Excel|Aumento|
|CELLSNET-47652|Problemi di spaziatura dei caratteri quando si imposta il formato dei caratteri|Aumento|
|CELLSNET-47623|Operazione di salvataggio lenta con molte formule nel file|Prestazione|
|CELLSNET-47606|L'applicazione si blocca durante la conversione di Excel in PDF|Prestazione|
|CELLSNET-47611|Problema di calcolo della formula IRR|Insetto|
|CELLSNET-47616|Elimina intervallo che si comporta in modo diverso tra v20.8 e v20.9|Insetto|
|CELLSNETCORE-83|Il file Excel non è stato visualizzato correttamente in GridWeb|Insetto|
|CELLSNETCORE-86|Problema di visualizzazione della forma in GridWeb|Insetto|
|CELLSNET-47597|Le aree di riempimento sono molto diverse rispetto al file sorgente|Insetto|
|CELLSNET-47614|Alcuni simboli mancano nel PDF di output nel rendering da Excel a PDF|Insetto|
|CELLSNET-47636|Conversione da Excel a PDF: il risultato passa sulla pagina con orientamento orizzontale|Insetto|
|CELLSNET-47637|Conversione del problema da Excel a PDF con Calibri Light|Insetto|
|CELLSNET-42982|Le dimensioni e il layout del grafico sono stati modificati dopo Workbook.Combine|Insetto|
|CELLSNET-47594|Opzione per ottenere informazioni PlotBy e OnAction simili a MS Excel|Insetto|
|CELLSNET-47595|Il grafico non è stato mantenuto correttamente nel file Excel durante il caricamento e il salvataggio|Insetto|
|CELLSNET-47599|AddControlRefrernce non aggiunge un riferimento a MS Forms 2.0|Insetto|
|CELLSNET-47600|I nomi dei controlli del modulo e poche altre proprietà sono diversi rispetto a MS Excel|Insetto|
|CELLSNET-47613|LTR e RTL non vengono conservati dopo il caricamento e il salvataggio con il file XLSB|Insetto|
|CELLSNET-47615|Il file Power Point incorporato nel file Excel non può essere aperto dopo il salvataggio|Insetto|
|CELLSNET-47645|Messaggio di riparazione generato da MS Excel dopo aver caricato e salvato i file Excel con Aspose.Cells|Insetto|
|CELLSNET-47647|Messaggio di riparazione generato da Excel durante la conversione XLSB->XLSX->XLSB|Insetto|
|CELLSNET-47648|Il file XLSB è danneggiato dopo la conversione (XLSB->XLSX-XLSB)|Insetto|
|CELLSNET-47658|La dimensione del carattere viene arrotondata quando è stata specificata l'impostazione Simbolo decimale con regione|Insetto|
|CELLSNETCORE-81|L'opzione "Testo a capo" non viene conservata nel file XLSB dopo il caricamento e il salvataggio|Insetto|
|CELLSNETCORE-82|Il foglio specifico all'interno del file XLSB si interrompe dopo il caricamento e il salvataggio|Insetto|
|CELLSNETCORE-84|Informazioni sullo stile restituite insieme al testo dell'intestazione|Insetto|
|CELLSNETCORE-85|Cells.InsertCutCells corrompe le note|Insetto|
|CELLSNET-47544|Mancano le immagini e la posizione del testo era errata durante il rendering di Excel in Linux|Insetto|
|CELLSNET-47571|La conversione HTML da XLS entra in un ciclo di conversione continuo|Insetto|
|CELLSNET-47583|PivotTable.TableRange2 fornisce un valore errato per la tabella pivot|Insetto|
|CELLSNET-47584|Aspose.Cells La conversione da HTML a Excel non mostrava immagini|Insetto|
|CELLSNET-47609|Diagram non viene mostrato in html quando il foglio non ha altro contenuto|Insetto|
|CELLSNET-47633|La tabella pivot con le date non si aggiorna correttamente|Insetto|
|CELLSNET-47635|L'affettatrice su un tavolo diverso genera un file danneggiato|Insetto|
|CELLSNET-47620|Da forma a immagine Errore durante il salvataggio in PDF|Eccezione|
|CELLSNET-47608|NullReferenceException durante il caricamento di XLSX|Eccezione|
|CELLSNET-47624|System.ArgumentException durante il caricamento del file crittografato in XLAM|Eccezione|
|CELLSNET-47630|L'argomento specificato non rientrava nell'intervallo di eccezioni di valori validi durante l'eliminazione della colonna|Eccezione|
|CELLSNET-47649|L'eccezione viene sollevata durante la lettura di DBConnection.PowerQueryFormula dal file XLSX|Eccezione|
|CELLSNET-47655|CellsException durante la conversione da Excel a PDF|Eccezione|
|CELLSNETCORE-80|Impossibile trasmettere l'eccezione dell'oggetto durante la conversione di XLSB in XLSM|Eccezione|
|CELLSNET-47593|Eccezione quando si tenta di aprire un particolare HTM|Eccezione|
|CELLSNET-47656|Errore da forma a immagine durante la conversione di XLSB in PDF|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge ExceptionType.Permission enum**

Rappresenta ExceptionType.Permission.

### **Aggiunge la proprietà ExternalConnection.PowerQueryFormula.**

Ottiene la definizione della formula di query di alimentazione.

### **Aggiunge il metodo FileFormatUtil.VerifyPassword.**

Verifica se la password è valida per il file.

### **Aggiunge il metodo VbaProject.Copy().**

Copia il progetto VBA.

### **Aggiunge la proprietà XlsSaveOptions.MatchColor.**

Indica se corrispondere al colore se il colore non è nella tavolozza durante il salvataggio del file .xls.

### **Elimina la proprietà Series.Line obsoleta.**

Utilizzare invece la proprietà Series.Border.
