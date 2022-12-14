---
title: Gestisci fogli di lavoro di Microsoft file Excel.
linktitle: Fogli di lavoro
type: docs
weight: 90
url: /it/net/manage-worksheets/
description: Aggiungi foglio di lavoro, rimuovi foglio di lavoro e foglio attivo utilizzando Aspose.Cells.
---
{{% alert color="primary" %}}

Gli sviluppatori possono facilmente creare e gestire i fogli di lavoro nei file Excel Microsoft a livello di codice usando Aspose.Cells' flexible API. Questo argomento descrive gli approcci per l'aggiunta e la rimozione di fogli di lavoro nei file Excel Microsoft.

{{% /alert %}}

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro.

## **Aggiunta di fogli di lavoro a un nuovo file Excel**

Per creare un nuovo file Excel a livello di codice:

1.  Crea un oggetto di[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe.
1.  Chiama il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) metodo del[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) classe. Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel. È possibile fare riferimento passando l'indice del foglio del nuovo foglio di lavoro al file[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collezione.
1. Ottenere un riferimento al foglio di lavoro.
1. Eseguire il lavoro sui fogli di lavoro.
1.  Salva il nuovo file Excel con i nuovi fogli di lavoro chiamando il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**Salva**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Aggiunta di fogli di lavoro a un foglio di calcolo di Designer**

 Il processo di aggiunta di fogli di lavoro a un foglio di lavoro del progettista è uguale a quello di aggiunta di un nuovo foglio di lavoro, tranne per il fatto che il file Excel esiste già, quindi deve essere aperto prima dell'aggiunta dei fogli di lavoro. Un foglio di calcolo del designer può essere aperto dal file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Accesso ai fogli di lavoro utilizzando il nome del foglio**

Accedi a qualsiasi foglio di lavoro specificandone il nome o l'indice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Rimozione di fogli di lavoro utilizzando il nome del foglio**

Per rimuovere i fogli di lavoro da un file, chiama il file[**RimuoviAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) metodo di[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) classe. Passa il nome del foglio al file[**RimuoviAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)metodo per rimuovere un foglio di lavoro specifico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**

 La rimozione dei fogli di lavoro per nome funziona bene quando il nome del foglio di lavoro è noto. Se non conosci il nome del foglio di lavoro, usa una versione sovraccaricata del file[**RimuoviAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)metodo che accetta l'indice del foglio di lavoro anziché il nome del foglio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Attivazione di fogli e creazione di un Cell attivo nel foglio di lavoro**

A volte, è necessario che un foglio di lavoro specifico sia attivo e visualizzato quando un utente apre un file Excel Microsoft in Excel. Allo stesso modo, potresti voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva.
Aspose.Cells è in grado di svolgere tutte queste attività.

 Un**foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.

 Un**Cellula attiva** è una cella selezionata, la cella in cui vengono inseriti i dati quando inizi a digitare. È attiva solo una cella alla volta. La cella attiva è evidenziata da un bordo spesso.

### **Attivare Fogli e rendere attivo uno Cell**

Aspose.Cells prevede chiamate specifiche API per l'attivazione di un foglio e di una cella. Ad esempio, il[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)è utile per impostare il foglio attivo in una cartella di lavoro.
Allo stesso modo,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)La proprietà viene utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.

Per assicurarti che le barre di scorrimento orizzontali o verticali si trovino nella posizione dell'indice di riga e colonna in cui desideri mostrare dati specifici, utilizza il[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) e[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)proprietà.

L'esempio seguente mostra come attivare un foglio di lavoro e creare una cella attiva al suo interno. Nell'output generato, le barre di scorrimento verranno fatte scorrere per rendere la seconda riga e la seconda colonna come prima riga e colonna visibili.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Argomenti avanzati**
- [Copiare e spostare fogli di lavoro](/cells/it/net/copying-and-moving-worksheets/)
- [Contare il numero di celle nel foglio di lavoro](/cells/it/net/count-number-of-cells-in-the-worksheet/)
- [Rilevamento di fogli di lavoro vuoti](/cells/it/net/detecting-empty-worksheets/)
- [Trova se il foglio di lavoro è Foglio di dialogo](/cells/it/net/find-if-the-worksheet-is-dialog-sheet/)
- [Ottieni l'ID univoco del foglio di lavoro](/cells/it/net/get-worksheet-unique-id/)
- [Crea, manipola o rimuovi scenari dai fogli di lavoro](/cells/it/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestione delle interruzioni di pagina](/cells/it/net/managing-page-breaks/)
- [Funzioni di impostazione della pagina](/cells/it/net/page-setup-features/)
- [Stampa più copie di un foglio di lavoro](/cells/it/net/print-multiple-copies-of-a-worksheet/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Viste del foglio di lavoro](/cells/it/net/worksheet-views/)

