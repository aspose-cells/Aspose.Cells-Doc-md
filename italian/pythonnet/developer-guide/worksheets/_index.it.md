---
title: Gestire i fogli di lavoro dei file di Microsoft Excel.
linktitle: Fogli di lavoro
type: docs
weight: 90
url: /it/python-net/manage-worksheets/
description: Questo articolo mostra come gestire i fogli di lavoro dei file di Microsoft Excel tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Python per Excel, Gestione dei fogli di lavoro dei file Microsoft Excel in Python, Aggiungi foglio di lavoro in Python, Rimuovi foglio di lavoro in Python, Come aggiungere fogli di lavoro a un nuovo file Excel in Python, Come aggiungere fogli di lavoro a un foglio di calcolo progettato in Python, Come accedere ai fogli di lavoro usando il nome del foglio in Python, Come rimuovere i fogli di lavoro usando il nome del foglio in Python, Come rimuovere i fogli di lavoro usando l indice del foglio in Python, Come attivare i fogli e rendere attiva una cella in Python.
---


{{% alert color="primary" %}}

I programmatori possono creare e gestire facilmente i fogli di lavoro nei file di Microsoft Excel in modo programmatico utilizzando l'API flessibile di Aspose.Cells. Questo argomento descrive gli approcci per aggiungere e rimuovere i fogli di lavoro nei file di Microsoft Excel.

{{% /alert %}}

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro.

## **Come aggiungere fogli di lavoro a un nuovo file Excel**

Per creare un nuovo file Excel in modo programmatico:

1. Creare un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Chiamare il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Viene automaticamente aggiunto un foglio di lavoro vuoto al file Excel. Può essere referenziato passando l'indice del foglio del nuovo foglio alla raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/).
1. Ottenere un riferimento al foglio di lavoro.
1. Lavorare sui fogli di lavoro.
1. Salvare il nuovo file Excel con nuovi fogli di lavoro chiamando il metodo [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Come aggiungere fogli di lavoro a un foglio di calcolo progettato**

Il processo di aggiunta di fogli di lavoro a un foglio di calcolo del designer è lo stesso di quello dell'aggiunta di un nuovo foglio di lavoro, tranne che il file Excel esiste già quindi dovrebbe essere aperto prima che i fogli di lavoro vengano aggiunti. Un foglio di calcolo del designer può essere aperto dalla classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Come accedere ai fogli di lavoro usando il nome del foglio**

Accedi a qualsiasi foglio di lavoro specificando il suo nome o indice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Come rimuovere i fogli di lavoro usando il nome del foglio**

Per rimuovere fogli di lavoro da un file, chiama il metodo [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Passa il nome del foglio al metodo [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) per rimuovere un foglio di lavoro specifico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Come rimuovere i fogli di lavoro usando l'indice del foglio**

La rimozione dei fogli di lavoro per nome funziona bene quando si conosce il nome del foglio di lavoro. Se non si conosce il nome del foglio di lavoro, utilizzare il metodo [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) che prende l'indice del foglio di lavoro invece del suo nome.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Come attivare i fogli e rendere attiva una cella nel foglio di lavoro**

A volte è necessario che un foglio di lavoro specifico sia attivo e visualizzato quando un utente apre un file Microsoft Excel in Excel. Allo stesso modo, potresti voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva.
Aspose.Cells è in grado di eseguire tutti questi compiti.

Un **foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.

Una **cella attiva** è una cella selezionata, la cella in cui i dati vengono inseriti quando si inizia a digitare. Solo una cella è attiva alla volta. La cella attiva è evidenziata da un bordo spesso.

### **Come attivare i fogli e rendere attiva una cella**

Aspose.Cells fornisce chiamate API specifiche per attivare un foglio e una cella. Ad esempio, la proprietà [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) è utile per impostare il foglio attivo in un foglio di lavoro.
Analogamente, la proprietà [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) è utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.

Per assicurarti che le barre di scorrimento orizzontali o verticali siano nella posizione dell'indice di riga e colonna che vuoi mostrare dati specifici, utilizza le proprietà [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) e [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

L'esempio seguente mostra come attivare un foglio di lavoro e rendere una cella attiva in esso. Nell'output generato, le barre di scorrimento verranno scorrere per fare in modo che la seconda riga e la seconda colonna siano la loro prima riga e colonna visibile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

