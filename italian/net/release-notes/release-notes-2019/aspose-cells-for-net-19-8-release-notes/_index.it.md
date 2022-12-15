---
title: Aspose.Cells for .NET 19.8 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-19-8-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.8](https://www.nuget.org/packages/Aspose.Cells/19.8.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46823|Supporta l'algoritmo di firma digitale a curva ellittica (ECDSA) per P-384 e P-521|Nuova caratteristica|
|CELLSNET-46813|Supporto per l'estrazione di file OLE Embedded .MOL|Nuova caratteristica|
|CELLSNET-46822|Rilevamento della differenza tra collegamenti ipertestuali interni ed esterni|Nuova caratteristica|
|CELLSNET-42334|Aspose.Cells. Compatibilità GridWeb con MVC|Aumento|
|CELLSNET-46804|Migliora le prestazioni per il calcolo di matrici grandi con valori doppi|Prestazione|
|CELLSNET-46856|Il documento non viene salvato se salvato più di 10 volte|Prestazione|
|CELLSNET-46827|Contenuto mancante nella conversione da XLSX a ODS|Insetto|
|CELLSNET-46833|Le forme sono distorte nella conversione da Excel a PDF|Insetto|
|CELLSNET-46835|Le forme del disegno non vengono visualizzate correttamente nel rendering da Excel a PDF|Insetto|
|CELLSNET-46848|Problema con il rendering del testo arabo da Excel a PDF|Insetto|
|CELLSNET-44973|Impossibile impostare il colore di riempimento delle celle della tabella pivot|Insetto|
|CELLSNET-46818|Non tutti gli stili vengono esportati durante il salvataggio in HTML|Insetto|
|CELLSNET-46824|Tabella pivot danneggiata dopo l'aggiornamento dei dati di origine pivot|Insetto|
|CELLSNET-46820|Problemi relativi ai dati relativi al raggruppamento degli indicatori intelligenti|Insetto|
|CELLSNET-46840|Problema con il metodo Workbook.RemoveUnusedStyles|Insetto|
|CELLSNET-46853|Alcune colonne sono visualizzate in rosso nel rendering da Excel a PDF|Insetto|
|CELLSNET-46829|L'oggetto DBConnection non fornisce valore per DBConnection.ConnectionInfo|Insetto|
|CELLSNET-46830|Leggere e scrivere su Query|Insetto|
|CELLSNET-46841|Apertura di un file XLS specifico con errori Aspose|Insetto|
|CELLSNET-46845|Problemi nel comportamento di ImportTableOptions.InsertRows|Insetto|
|CELLSNET-46846|File Excel danneggiato dopo il nuovo salvataggio|Insetto|
|CELLSNET-46849|Problema con le connessioni dati esterne|Insetto|
|CELLSNET-46850|Raggruppamento dei dati non conservato durante l'utilizzo di Cells.DeleteRange()|Insetto|
|CELLSNET-46855|InsertRows divide erroneamente le righe raggruppate|Insetto|
|CELLSNET-46858|La conversione da XLSX a ODS cambia il carattere del testo nel libro di testo|Insetto|
|CELLSNET-46859|L'anteprima di stampa non mostra la casella di testo nel file ODS convertito da XLSX|Insetto|
|CELLSNET-46723|Viene generata un'eccezione quando si ottiene l'immagine da SheetRender per il file ODS crittografato|Eccezione|
|CELLSNET-46842|Il calcolo dei grafici su un Excel con un numero > int.MaxValue genera un errore|Eccezione|
|CELLSNET-46828|"IndexOutOfRangeException" quando si utilizza un marcatore intelligente con una tabella pivot e si salva la cartella di lavoro|Eccezione|
|CELLSNET-46814|Eccezione "L'indice era al di fuori dei limiti dell'array" durante la conversione di XLSX in PDF|Eccezione|
|CELLSNET-46831|Eccezione durante il rendering di un file Excel in PDF|Eccezione|
|CELLSNET-46844|Workbook.CalculateFormula() causa NullReferenceException|Eccezione|
|CELLSNET-46832|Eccezione "Valore stringa MsoLineDashStyle non valido" durante il caricamento di un formato di file XLSX|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la classe SheetPrintingPreview**
Anteprima di stampa del foglio di lavoro.
#### **Aggiunge la classe WorkbookPrintingPreview**
Anteprima di stampa della cartella di lavoro.
#### **Aggiunge la proprietà QueryTable.ExternalConnection.**
Ottiene la connessione dell'oggetto querytable.
#### **Aggiunge la proprietà Hyperlink.LinkType ed enum TargetModeType.**
Rappresenta il tipo di collegamento del collegamento ipertestuale.
