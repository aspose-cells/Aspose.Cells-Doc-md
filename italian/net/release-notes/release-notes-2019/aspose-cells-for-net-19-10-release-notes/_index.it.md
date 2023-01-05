---
title: Aspose.Cells for .NET Note sulla versione 19.10
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-19-10-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.10](https://www.nuget.org/packages/Aspose.Cells/19.10.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46926|PageSavingCallback durante il salvataggio su TIFF|Nuova caratteristica|
|CELLSNET-46927|IMailMergeDataSource equivalente per Cells|Nuova caratteristica|
|CELLSNET-46903|Modifica dello stile su ContentTypeProperties|Aumento|
|CELLSNET-46954|Aumenta l'eccezione simile a Excel invece di sospendere il programma|Prestazione|
|CELLSNET-46896|Il grafico a imbuto scompare|Insetto|
|CELLSNET-46934|Ritardo e utilizzo della memoria durante la conversione nel formato file PDF|Insetto|
|CELLSNET-43416|L'ordinamento del campo pivot viene modificato dopo il rendering del foglio di calcolo in PDF|Insetto|
|CELLSNET-44686|Ordinamento pivot non applicato durante l'estrazione del grafico|Insetto|
|CELLSNET-46793|Un problema con le tabelle pivot|Insetto|
|CELLSNET-46882|Problema durante il raggruppamento della tabella pivot per data e il salvataggio come PDF|Insetto|
|CELLSNET-46935|Testo a capo non visualizzato in HTML|Insetto|
|CELLSNET-46940|I bordi della tabella non vengono visualizzati correttamente in HTML|Insetto|
|CELLSNET-46939|Supporto per la funzione TEXTJOIN()|Insetto|
|CELLSNET-46237|Cell Il formato non si attacca|Insetto|
|CELLSNET-46245|Taglia/Incolla non copia il nome di Cell nella nuova posizione in GridDesktop|Insetto|
|CELLSNET-46910|Le convalide dei dati dell'elenco (elenco a discesa) non funzionano con la matrice Aspose.Cells.GridWeb|Insetto|
|CELLSNET-46943|Funzione ImportXML Dati della tabella prelevati da record errati|Insetto|
|CELLSNET-46899|L'aspetto del grafico a imbuto cambia (carattere del titolo, formato numerico, larghezza del grafico)|Insetto|
|CELLSNET-46900|Lo schema dei colori del grafico della mappa cambia|Insetto|
|CELLSNET-46902|L'opzione Elimina riga manualmente è disabilitata nella tabella dopo aver popolato il file Excel utilizzando ImportData|Insetto|
|CELLSNET-46916|Inserisci intervallo sta causando il danneggiamento del file|Insetto|
|CELLSNET-46919|File danneggiato quando si passa al formato file XLSB da XLSX|Insetto|
|CELLSNET-46925|Problema durante l'estrazione dell'oggetto OLE da XLSX|Insetto|
|CELLSNET-46928|Conholdate Problema di licenza totale|Insetto|
|CELLSNET-46929|L'orientamento (titolo) dell'etichetta dell'asse del grafico è stato modificato durante la copia dei fogli di lavoro|Insetto|
|CELLSNET-46933|L'apertura e il salvataggio di un file XLS rimuove tutti i documenti e le proprietà personalizzate|Insetto|
|CELLSNET-46945|Estendi intervallo. Rimuovi duplicati|Insetto|
|CELLSNET-46948|Prestazioni Range.Copy per grandi volumi|Insetto|
|CELLSNET-46949|Gli oggetti OLE diventano immagini durante la copia dei fogli di lavoro|Insetto|
|CELLSNET-46941|Salva con nome HTML genera un'eccezione quando la cella contiene un riferimento a un file|Eccezione|
|CELLSNET-46952|Eccezione durante la chiamata a Workbook.RemoveUnusedStyles()|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo Cells.RemoveDuplicates()**
Rimuove i dati duplicati dell'intervallo.
#### **Aggiunge la proprietà OleObject.FullObjectBin**
Ottiene i dati binari dell'oggetto ole incorporati completi nel file modello.
#### **Aggiunge la proprietà ContentTypeProperty.IsNillable**
Indica se la proprietà può essere nulla.
#### **Aggiungere il metodo WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Imposta l'origine dati per Smart Marker Designer.
#### **Aggiunge la proprietà ImageOrPrintOptions.PageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
#### **Aggiunge la proprietà ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Indica se sostituire solo il carattere del carattere quando il carattere della cella non è compatibile con esso.
