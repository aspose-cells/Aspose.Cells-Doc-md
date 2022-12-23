---
title: Aspose.Grid for .NET V2.0.1 Nuova versione Note sulla versione
type: docs
weight: 30
url: /it/net/aspose-grid-for-net-v2-0-1-new-release-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Grid for .NET V2.0.1 Nuova versione](https://downloads.aspose.com/cells/net/new-releases/aspose.grid-for-.net-v2.0.1-new-release/)

{{% /alert %}} 

 Abbiamo appena rilasciato Aspose.Grid v.

 Cosa è cambiato:

 Aspose.Grid.Desktop



 l Supporta l'importazione/esportazione nel formato di file Excel2007xlsx.

 l Supporta la lettura dello stile delle celle unite dal file excel.

 l Supporta Auto RowFilter e Custom RowFilter; aggiunta delle proprietà IgnoreCase e IsStartWithCriteria a GridColumn per personalizzare i comportamenti del filtro di riga automatico.

 l Aggiunge la proprietà CustomMsgTitle a Validation per personalizzare il titolo di MessageBox.

 l Aggiunge la proprietà RecalculateFormulas il cui valore predefinito è true; quando è impostato su false, l'assegnazione di qualsiasi valore a una cella non ricalcolerà la formula.

 l Aggiunge le proprietà Larghezza e Altezza a Commento.

 l Aggiunge la proprietà CommentFont a GridDesktop per impostare il carattere dei commenti.

 l Fornisce nuove versioni per l'elenco di overload del metodo Add per la classe CommentCollection per specificare la larghezza e l'altezza dei commenti.

 l Aggiunge la proprietà IsVisible al foglio di lavoro.

 Supporta la lettura/scrittura di CustomProperties di Worksheet in file Excel e l'aggiunta di proprietà CustomProperties di sola lettura a Worksheet.

 l Supporta la funzione/formula di vlookup.

 l Supporta le funzioni Annulla/Ripristina quando si modificano i valori delle celle.

 l Aggiunge la proprietà ContextMenuManager a GridDesktop per gestire il menu contestuale.

 l Aggiunge l'evento RowColumnHiddenChanged.

 l Supporta la selezione multipla di righe/colonne/regioni.

 l Supporta l'importazione/esportazione di riquadri congelati da/a file excel.

 l 36 correzioni e miglioramenti.

 Aspose.Grid.Web



 l 1 potenziamento.



 Problemi risolti in Aspose.Grid 2.0.1

|**ID problema** |**Componente** |**Sommario** |
|:- |:- |:- |
|7942 | Griglia.Desktop| Imposta il valore dei tipi Single o float su celle visualizzate vuote.|
|7970 | Griglia.Desktop| I bordi in basso a destra che non venivano mostrati normalmente.|
|7971 | Griglia.Desktop| Il bordo nero della cella focalizzata che non veniva mostrato normalmente.|
|7972 | Griglia.Desktop| Funzionalità demo genera un'eccezione del percorso file che dimostra la funzionalità Immagini.|
|7973 | Griglia.Desktop| Aggiunge il metodo SetSelectedIndex a ComboBox per evitare di ricalcolare tutte le formule.|
|7974 | Griglia.Desktop|La pressione di un tasto su ComboBox di una cella richiamerebbe la modifica.|
|7975 | Griglia.Desktop| Errore nella dimensione del carattere nella finestra di dialogo Formato Cell.|
|7976 | Griglia.Desktop| La cella attiva è stata modificata quando la convalida non è riuscita.|
|7977 | Griglia.Desktop| Incolla le celle più volte, il colore di sfondo di alcune celle viene impostato su blu.|
|7982 | Griglia.Desktop| Problema di prestazioni di ordinamento dei dati|
|7983 | Griglia.Desktop| Fa clic sulle righe di intestazione, l'altezza della riga / larghezza della colonna viene modificata.|
|7984 | Griglia.Desktop| Impossibile copiare il contenuto nella casella di input di una cella tramite ctrl+c.|
|7985 | Griglia.Desktop| Genera un'eccezione quando si modifica un valore sopra le righe bloccate.|
|7986 | Griglia.Desktop| Aggiorna tutti i riferimenti delle formule durante l'inserimento o l'eliminazione di righe o colonne.|
|7987 | Griglia.Desktop| Modifica il valore di una cella, verranno ricalcolate solo le relative formule e non tutte.|
|7988 | Griglia.Desktop| Problema di prestazioni per copiare/incollare/eliminare un numero di celle|
|7989 | Griglia.Desktop| Prestazioni per il calcolo delle formule di matrice|
|7990 | Griglia.Desktop| Calcola l'errore delle proprietà RowsCount / ColumnsCount durante l'accesso alle proprietà Cells / Rows / Columns del foglio di lavoro.|
|7991 | Griglia.Desktop| Prestazioni per ImportDataTable|
|7992 | Griglia.Desktop|Cambia l'altezza di hscrollbar e la larghezza di vscrollbar da 20 pixel a 16.|
|7993 | Griglia.Desktop| Aggiunge il metodo SetSelectedIndex a ComboBox per evitare di ricalcolare tutte le formule.|
|7994 | Griglia.Desktop| Modifica i colori delle linee della griglia, delle linee di intestazione e delle selezioni.|
|7995 | Griglia.Desktop| Calcola la larghezza visibile dell'errore di testo del disegno quando una cella ha esteso il proprio testo alle celle di destra.|
|7996 | Griglia.Desktop| Prestazioni per il rendering dei fogli di lavoro|
|7997 | Griglia.Desktop| I metodi SetFont e SetFontColor di GridRow non funzionano.|
|7998 | Griglia.Desktop| Un nome di cella non valido nella formula potrebbe causare un riferimento di cella non valido|
|7999 | Griglia.Desktop| Il comportamento durante la navigazione nelle celle tramite barre di scorrimento e tasti freccia.|
|8000 | Griglia.Desktop| Prestazioni di copia / incolla di un gran numero di celle, comprese molte formule|
|8001 | Griglia.Desktop| L'eccezione IComparer si verifica quando un valore di colonna conteneva tipi int e string per il filtro automatico dei dati|
|8003 | Griglia.Desktop| Utilizza l'oggetto FormulaError che ora restituisce un valore anziché generare un'eccezione|
|8004 | Griglia.Desktop| Il valore booleano in una cella non viene visualizzato come valore stringa.|
|8006 | Griglia.Desktop| Posizione della cella focalizzata nella modalità di selezione righe/colonne|
|8007 | Griglia.Desktop| Modifica del problema della cella focalizzata invisibile|
|8020 | Griglia.Desktop|Il motore delle formule calcola il valore null nel risultato di una stringa vuota.|
|8085 | Griglia.Desktop| Aggiorna l'errore delle formule durante l'eliminazione delle righe.|
|8289 | Griglia.Desktop| Migliora i messaggi di errore della formula.|
|8290 | Griglia.Web| Problema di prestazioni per molte formule di errore.|

