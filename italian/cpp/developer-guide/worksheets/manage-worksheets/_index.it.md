---
title: Gestire i Fogli di Lavoro
type: docs
weight: 20
url: /it/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Gli sviluppatori possono facilmente creare e gestire fogli di lavoro nei file di Microsoft Excel utilizzando in modo programmato l'API flessibile di Aspose.Cells. Questo argomento descrive approcci per aggiungere e rimuovere fogli di lavoro nei file di Microsoft Excel.

{{% /alert %}} 

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta di [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro.
## **Aggiungere fogli di lavoro a un nuovo file Excel**
Per creare un nuovo file Excel in modo programmatico:

1. Creare un oggetto della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
1. Chiamare il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) della raccolta [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). Viene aggiunto automaticamente un foglio di lavoro vuoto al file Excel. Può essere referenziato passando l'indice del foglio di lavoro nuovo alla raccolta [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
1. Ottenere un riferimento al foglio di lavoro.
1. Lavorare sui fogli di lavoro.
1. Salvare il nuovo file Excel con i nuovi fogli di lavoro chiamando il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Accesso ai Fogli di Lavoro utilizzando l'Indice del Foglio**
Il codice di esempio seguente mostra come accedere o ottenere qualsiasi foglio di lavoro specificando il suo indice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**
La rimozione dei fogli di lavoro per nome funziona bene quando si conosce il nome del foglio di lavoro. Se non si conosce il nome del foglio di lavoro, utilizzare una versione sovraccaricata del metodo [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) che prende l'indice del foglio del foglio di lavoro invece del nome del foglio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
