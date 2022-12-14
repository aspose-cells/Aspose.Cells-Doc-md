---
title: Aspose.Cells for .NET 17.10 Note di rilascio
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 17.10](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.10/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-45695|Imposta il formato numerico per le celle nella tabella dati del grafico|Nuova caratteristica|
|CELLSNET-45666|Ottieni il campo SheetId del foglio di lavoro di Excel|Nuova caratteristica|
|CELLSNET-45664|Lettura e scrittura Collegamento esterno di file XLSB|Nuova caratteristica|
|CELLSNET-45660|Rendering da foglio a immagine - Problema di allineamento per i caratteri asiatici|Aumento|
|CELLSNET-45408|Il valore scompare o cambia colore durante la conversione in PDF|Insetto|
|CELLSNET-45696|L'affettatrice non si sposta verso il basso nel foglio durante l'inserimento delle righe|Insetto|
|CELLSNET-45675|Errore nel calcolo delle formule (che coinvolgono "SUMPRODUCT" e "TRASPOSE")|Insetto|
|CELLSNET-45651|Le dimensioni della casella di testo cambiano quando si utilizza il carattere cinese nella cartella di lavoro nel rendering in PDF|Insetto|
|CELLSNET-45678|Caratteri parzialmente mancanti durante la conversione in immagine|Insetto|
|CELLSNET-45667|Le etichette della linea di tendenza non vengono aggiornate in MS Excel quando modifichiamo manualmente il valore di origine nelle celle|Insetto|
|CELLSNET-45620|Il colore e l'intervallo tra la scala sono diversi per il grafico 3D|Insetto|
|CELLSNET-45397|Aspose.Cells riconosce i caratteri nel grafico in modo errato|Insetto|
|CELLSNET-45700|Riquadro del componente aggiuntivo MS Excel 2016 rimosso dal file dopo l'apertura/salvataggio di Aspose.Cells|Insetto|
|CELLSNET-45693|Il foglio di lavoro non è più protetto nel file di output nella conversione da SpreadsheetML a XLSX|Insetto|
|CELLSNET-45691|Il documento è danneggiato durante il nuovo salvataggio|Insetto|
|CELLSNET-45690|Gli stili sembrano essere trasferiti in modo errato per alcune celle: conversione da SpreadsheetML a XLSX|Insetto|
|CELLSNET-45688|La colonna della data non è ordinata correttamente|Insetto|
|CELLSNET-45687|Le proprietà di protezione dei fogli di lavoro non vengono trasferite da SpreadsheetML|Insetto|
|CELLSNET-45683|L'elemento SpreadsheetML AllowSort non funziona nell'output XLSX|Insetto|
|CELLSNET-45682|MS Excel richiede un messaggio di errore "Excel ha trovato contenuto illeggibile..."|Insetto|
|CELLSNET-45676|Il documento è danneggiato durante il nuovo salvataggio a causa dello spazio di non interruzione nel nome del foglio di lavoro|Insetto|
|CELLSNET-45673|Stile di allineamento applicato a SpredsheetML|Insetto|
|CELLSNET-45670|Cells il colore viene perso durante la conversione in immagine|Insetto|
|CELLSNET-45692|GridWeb non separa le righe facendo clic sul pulsante "+".|Insetto|
|CELLSNET-45654|Il commento aggiunto alla cella non viene recuperato sul lato client - Aspose.Cells.GridWeb|Insetto|
|CELLSNET-45645|L'eccezione si verifica all'apertura di BUDGET RH 3_0.xlsm in GridWeb|Insetto|
|CELLSNET-45657|La stringa di input non era in un formato corretto - Eccezione sul metodo Pivot.CalculateData()|Eccezione|
|CELLSNET-45703|Eccezione durante la conversione del file XLSM nel formato file XLS|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo AbstractCalculationMonitor.Interrupt(string).**
Consente agli utenti di interrompere l'avanzamento dei calcoli delle formule.
#### **Aggiunge l'enumerazione HtmlCrossType.MSExport**
Visualizza la stringa come MS Excel che esporta HTML.
#### **Aggiunge la proprietà Worksheet.TabId**
Ottiene l'identificatore interno del foglio.
#### **Aggiunge enum OLEDBCommandType.None**
Il tipo di comando non è specificato.
#### **Aggiunge enum ConnectionDataSourceType**
Rappresenta il tipo di connessione dell'origine dati.
#### **Proprietà ExternalConnection.Credentials e ExternalConnection.ReConnectionMethod obsolete**
Usare invece la proprietà ExternalConnection.CredentialsMethodType e ExternalConnection.ReconnectionMethodType.
#### **Proprietà WebQueryConnection.EditPage obsoleta**
Utilizzare invece la proprietà WebQueryConnection.EditWebPage.
#### **Aggiunge la proprietà Seris.ValuesFormatCode**
Rappresenta il codice del formato numerico dei valori della serie.
#### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Impostare il codice del formato dei valori della serie di grafici](/cells/it/net/set-the-values-format-code-of-chart-series/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Leggere e scrivere la connessione esterna del file XLSB](/cells/it/net/read-and-write-external-connection-of-xls-and-xlsb-files/)
- [Interrompere o annullare il calcolo della formula della cartella di lavoro](/cells/it/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType](/cells/it/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
