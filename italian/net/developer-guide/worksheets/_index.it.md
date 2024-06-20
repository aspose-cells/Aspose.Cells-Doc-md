---
title: Gestire i fogli di lavoro dei file di Microsoft Excel.
linktitle: Fogli di lavoro
type: docs
weight: 90
url: /it/net/manage-worksheets/
description: Aggiungere un foglio di lavoro, rimuovere un foglio di lavoro e attivare un foglio utilizzando Aspose.Cells.
---


{{% alert color="primary" %}}

I programmatori possono creare e gestire facilmente i fogli di lavoro nei file di Microsoft Excel in modo programmatico utilizzando l'API flessibile di Aspose.Cells. Questo argomento descrive gli approcci per aggiungere e rimuovere i fogli di lavoro nei file di Microsoft Excel.

{{% /alert %}}

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro.

## **Aggiungere fogli di lavoro a un nuovo file Excel**

Per creare un nuovo file Excel in modo programmatico:

1. Creare un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Chiamare il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Viene automaticamente aggiunto un foglio di lavoro vuoto al file Excel. Può essere referenziato passando l'indice del foglio del nuovo foglio alla raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets).
1. Ottenere un riferimento al foglio di lavoro.
1. Lavorare sui fogli di lavoro.
1. Salvare il nuovo file Excel con nuovi fogli di lavoro chiamando il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**

Il processo di aggiunta di fogli di lavoro a un foglio di calcolo del designer è lo stesso di quello dell'aggiunta di un nuovo foglio di lavoro, tranne che il file Excel esiste già quindi dovrebbe essere aperto prima che i fogli di lavoro vengano aggiunti. Un foglio di calcolo del designer può essere aperto dalla classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Accesso ai fogli di lavoro utilizzando il nome del foglio**

Accedi a qualsiasi foglio di lavoro specificando il suo nome o indice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Rimozione dei fogli di lavoro utilizzando il nome del foglio**

Per rimuovere fogli di lavoro da un file, chiama il metodo [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Passa il nome del foglio al metodo [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) per rimuovere un foglio di lavoro specifico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**

La rimozione dei fogli di lavoro per nome funziona bene quando è noto il nome del foglio di lavoro. Se non conosci il nome del foglio di lavoro, utilizza una versione sovraccaricata del metodo [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) che prende l'indice del foglio di lavoro anziché il suo nome.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Attivare fogli e fare di una cella attiva nel foglio di lavoro**

A volte è necessario che un foglio di lavoro specifico sia attivo e visualizzato quando un utente apre un file Microsoft Excel in Excel. Allo stesso modo, potresti voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva.
Aspose.Cells è in grado di eseguire tutti questi compiti.

Un **foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.

Una **cella attiva** è una cella selezionata, la cella in cui i dati vengono inseriti quando si inizia a digitare. Solo una cella è attiva alla volta. La cella attiva è evidenziata da un bordo spesso.

### **Attivare fogli e rendere una cella attiva**

Aspose.Cells fornisce chiamate API specifiche per attivare un foglio e una cella. Ad esempio, la proprietà [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) è utile per impostare il foglio attivo in un foglio di lavoro.
Analogamente, la proprietà [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) è utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.

Per assicurarti che le barre di scorrimento orizzontali o verticali siano nella posizione dell'indice di riga e colonna che vuoi mostrare dati specifici, utilizza le proprietà [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) e [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

L'esempio seguente mostra come attivare un foglio di lavoro e rendere una cella attiva in esso. Nell'output generato, le barre di scorrimento verranno scorrere per fare in modo che la seconda riga e la seconda colonna siano la loro prima riga e colonna visibile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Argomenti avanzati**
- [Copia e Sposta Fogli di Lavoro](/cells/it/net/copying-and-moving-worksheets/)
- [Contare il numero di celle nel foglio di lavoro](/cells/it/net/count-number-of-cells-in-the-worksheet/)
- [Rilevamento di fogli di lavoro vuoti](/cells/it/net/detecting-empty-worksheets/)
- [Trova se il foglio di lavoro è un foglio di dialogo](/cells/it/net/find-if-the-worksheet-is-dialog-sheet/)
- [Ottieni l'ID univoco del foglio di lavoro](/cells/it/net/get-worksheet-unique-id/)
- [Creare, Manipolare o Rimuovere scenari dai fogli di lavoro](/cells/it/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestione interruzioni di pagina](/cells/it/net/managing-page-breaks/)
- [Funzionalità Impostazioni pagina](/cells/it/net/page-setup-features/)
- [Stampa copie multiple di un foglio di lavoro](/cells/it/net/print-multiple-copies-of-a-worksheet/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Visualizzazioni del foglio di lavoro](/cells/it/net/worksheet-views/)

