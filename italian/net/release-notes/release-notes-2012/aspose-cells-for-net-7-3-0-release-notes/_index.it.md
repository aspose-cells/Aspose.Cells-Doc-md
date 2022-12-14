---
title: Aspose.Cells for .NET 7.3.0 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-7-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 7.3.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.0/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells per .NETv7.3.0 per gli utenti!



\1) Aspose.Cells 



 Nuove caratteristiche

 40701 - Supporta la lettura e la scrittura di file MHT

- Supporta mappe XML



 Miglioramenti

- Mono problema di versione supportato
- Impossibile utilizzare la formula come parametro di
- Le funzioni personalizzate possono restituire intervalli che possono essere utilizzati su SUM
- Applicazione di temi ai grafici
- Problema con Formula che fa riferimento a un'immagine



 Eccezioni

- Il totale parziale genera un errore di runtime
- L'eccezione viene generata quando si chiama il metodo Cell.GetPrecedents()
- Eccezione "Indice riga iniziale non valida" durante il subtotale



 Insetti

- XPS di SheetRender e problema relativo al formato numerico personalizzato
- Gli elementi della legenda del grafico vanno a capo quando si salva come immagine
- I grafici dei bug sheet non vengono visualizzati
- Un problema con il metodo Cells.ExportDataTableAsString() e la formattazione personalizzata
- Un problema serio con la tabella pivot
- L'utilizzo del metodo Workbook.CalculateFormula() su più cartelle di lavoro al volo dà #VALORE
- Il rendering PDF di forme aziendali (testo all'interno) non è piacevole
- Problema con il sommario XLS basato sul numero di pagine stampate

 -La conversione PDF perde i valori delle aree denominate

- Fare riferimento a celle con valori da formule di matrice non funziona

 -Cells Problema di formattazione

- Problema con la formula che fa riferimento a un'immagine
- Le formule di matrice in SpreadsheetML non vengono trasferite durante la conversione in XLSX
- Errore relativo alla perdita degli intervalli denominati in XLSM



 \2) Aspose.Cells.GridWeb



 Insetti

- Un problema con i collegamenti ipertestuali CellCommand
- Cell.La convalida genera una regressione InvalidOperationException
- Aspose.Cells. Il controllo GridWeb si arresta in modo anomalo per un file Excel


