---
title: Aspose.Cells for .NET 20.2 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-20-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.2](https://www.nuget.org/packages/Aspose.Cells/20.2.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47113|Conversione delimitata da pipe/da CSV a JSON|Nuova caratteristica|
|CELLSNET-47141|Il collegamento tra la tabella pivot e la connessione esterna|Nuova caratteristica|
|CELLSNET-47135|Aspose.Cells non considera la formula/funzione avanzata TEXTJOIN() come Formula|Aumento|
|CELLSNET-47126|Aspose.Cells elimina "volatileDependencies.xml" dal file con le formule RTD durante l'aggiornamento del file XLSX|Aumento|
|CELLSNET-47159|Troppo tempo per PivotTable.CalculateStyle|Prestazione|
|CELLSNET-42065|La percentuale di pivot calcolata in precedenza si interrompe dopo il pivot.CalculateData()|Insetto|
|CELLSNET-47102|"#" visualizzato dopo la conversione di Excel in PDF nel formato personalizzato Tempo negativo (h:mm)|Insetto|
|CELLSNET-47118|Valore errato 'TRUE' recuperato da Cell invece del valore 'FALSE'|Insetto|
|CELLSNET-47125|Gli spazi vengono persi dalla formula quando vengono recuperati utilizzando Aspose.Cells for .NET|Insetto|
|CELLSNET-47149|Il calcolo della formula è diverso in Aspose.Cells e MS Excel|Insetto|
|CELLSNET-47108|Formattazione condizionale non visualizzata in GridDesktop|Insetto|
|CELLSNET-47134|L'inserimento della colonna richiede troppo tempo in Aspose.Cells.GridDesktop|Insetto|
|CELLSNET-47138|GridDesktop impiega molto tempo per caricare file di grandi dimensioni|Insetto|
|CELLSNET-47043|Impossibile selezionare una cella per il foglio protetto in GridDesktop|Insetto|
|CELLSNET-47117|Aspose.Cells 20.1 Il tipo XAdES non è definito durante la lettura di file precedentemente firmati con firme XAdES|Insetto|
|CELLSNET-47081|Rendering del grafico in PDF|Insetto|
|CELLSNET-47085|Il grafico non viene visualizzato correttamente quando la direzione del testo delle etichette degli assi è "Pila"|Insetto|
|CELLSNET-47112|La conversione dal grafico all'immagine non riesce|Insetto|
|CELLSNET-47133|Incoerenza durante l'esportazione in PDF|Insetto|
|CELLSNET-47107|L'oggetto di formattazione condizionale fornisce risultati errati per l'attributo IsAboveAverage|Insetto|
|CELLSNET-47114|La cartella di lavoro RemoveExternalLinks genera un documento danneggiato|Insetto|
|CELLSNET-47139|Il file ODS con la formula del collegamento esterno mostra fogli di lavoro aggiuntivi|Insetto|
|CELLSNET-47145|L'intervallo denominato scompare dopo l'apertura e il salvataggio del file ODS|Insetto|
|CELLSNET-47146|Il file non viene aperto|Insetto|
|CELLSNET-47147|Problema nome codice foglio|Insetto|
|CELLSNET-47153|I grafici ODS cambiano dopo il salvataggio|Insetto|
|CELLSNET-47157|Numero errato di collegamenti esterni|Insetto|
|CELLSNET-47164|Proprietà IsItalic rilevata in modo diverso rispetto a MS Excel|Insetto|
|CELLSNET-47169|CategoryType.CategoryScale non impostato nel grafico ParetoLine|Insetto|
|CELLSNET-47122|Eccezione "Indice fuori intervallo" durante l'aggiornamento delle tabelle pivot|Eccezione|
|CELLSNET-47156|IndexOutOfRangeException durante l'accesso a ExternalLink.IsReferred o IsVisible|Eccezione|
|CELLSNET-47140|Eccezione durante il caricamento di ODS in GridDesktop|Eccezione|
|CELLSNET-47105|Eccezione durante l'importazione di dati XML in cui una colonna nella tabella non è mappata|Eccezione|
|CELLSNET-47170|Eccezione "Cast non valido da 'DateTime' a 'Double'" durante il salvataggio di un file Excel in PDF|Eccezione|
|CELLSNET-47152|Worksheet.Cells.EndCellInRow che restituisce un errore per il file|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo Workbook.ParseFormulas(bool ignoreError).**
Analizza tutte le formule che non sono state analizzate quando sono state caricate o impostate su una cella.
#### **Aggiunge la proprietà PivotTable.ExternalConnectionDataSource.**
Ottiene l'origine dati della connessione esterna.
#### **Aggiunge FileFormatType.Numbers35 enum.**
Rappresenta i file numero 3.5 dall'ufficio 2014. Solo per lanciare il formato del file durante la lettura.
#### **Aggiunge la proprietà LoadOptions.CheckDataValid.**
Indica se i dati sono validi durante il caricamento dei file.
#### **Aggiunge la proprietà GridDesktop.GridMemorySetting.**
Ottiene o imposta l'opzione di memoria per il caricamento dei fogli di lavoro.
