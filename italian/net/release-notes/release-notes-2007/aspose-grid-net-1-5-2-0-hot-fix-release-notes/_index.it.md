---
title: Aspose.Grid .Net 1.5.2.0 Note sulla versione dell'hotfix
type: docs
weight: 50
url: /it/net/aspose-grid-net-1-5-2-0-hot-fix-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Grid .Net 1.5.2.0 correzione rapida](https://downloads.aspose.com/cells/net/new-releases/aspose.grid-.net-1.5.2.0-hot-fix/)

{{% /alert %}} 

 Abbiamo rilasciato Aspose.Grid 1.5.2!

 Note di rilascio

 Aspose.Grid.Web

- Risolto: bug del colore di impostazione lato client
- Risolto: la proprietà TableStyle/TableItemStyle CssClass non ha effetto bug
- Supporto per la creazione di rapporti tabella pivot
- Supporta la selezione/copia/taglia/incolla/imposta lo stile multi-cella lato client
- Supporta le operazioni del menu di scelta rapida lato client: blocca/sblocca; inserire/eliminare riga/colonna; unire/separare le celle;
- Supporta i collegamenti ipertestuali (visualizzazione di testo o immagine, UrlLink o azione CellCommand)
- Proprietà aggiunte: ActiveCell, EnableClientColumnOperations, EnableClientFreeze, EnableClientMergeOperations, EnableClientRowOperations, SelectCells
- Metodi aggiunti: WebCells.GetColumnReadonly, WebCells.SetColumnReadonly, WebCells.GetRowReadonly, WebCells.SetRowReadonly
- Eventi aggiunti: SheetDataUpdated, LoadCustomData (per il ripristino dei dati in modalità Sessionless), CellCommand, ColumnDeleted, ColumnInserted, RowDeleted, RowInserted, PageIndexChanged
- Modificato: ora il percorso web del file client (/agw_client) e i file client (htc, gif, ecc.) non sono necessari nell'ambiente di distribuzione. Questi file sono ora incorporati nel controllo. Ciò semplifica le operazioni di distribuzione e aggiornamento.

 ` `Aspose.Grid.Desktop

 Migliorato:

- Testo dell'intestazione di colonna Supportato.
- Menu contestuale Supportato.
- Collegamenti ipertestuali, commenti, esportazione di immagini supportati.
- Pulsante Cell, casella di controllo, combox supportato.
- Supportati gli eventi CellClick, CellDoubleClick, CellKeyPressed.
- Applicazione dello stile all'intervallo di celle supportate.
- Convalida dei dati supportata.

 Fisso:

- Minimizzando la form che conteneva il controllo GridDesktop che impostava la proprietà Dock Fill, viene generata un'eccezione.
- Premendo il tasto "cancella", il controllo GridDesktop non genera l'evento CellDataChanged.
- Quando il numero di riga è maggiore di 4 numeri digitali, la larghezza dell'intestazione di riga non è sufficiente.
- Quando si carica da un file excel, il carattere del carattere immesso in una cella è diverso dal carattere della cella.
- Impossibile inserire Invio in una cella, ora utilizzare i tasti Control + Invio.
- Se non ci sono celle focalizzate, il controllo della casella di testo verrà posizionato nella posizione di errore quando si immette char.
- C'è un commento in una cella, quindi ha messo a fuoco la cella di destra; quando si punta sulla cella che contiene un commento, la cella focalizzata brillerà sempre.
- Nascondere la colonna della riga non funziona.
