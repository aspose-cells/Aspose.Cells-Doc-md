---
title: Gestisci fogli di lavoro
type: docs
weight: 20
url: /it/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Gli sviluppatori possono facilmente creare e gestire fogli di lavoro nei file Excel Microsoft a livello di codice usando Aspose.Cells flexible API. Questo argomento descrive gli approcci per l'aggiunta e la rimozione di fogli di lavoro nei file Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro.
## **Aggiunta di fogli di lavoro a un nuovo file Excel**
Per creare un nuovo file Excel a livello di codice:

1.  Crea un oggetto di[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe.
1.  Chiama il[Aggiungere](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) metodo del[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collezione. Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel. È possibile fare riferimento passando l'indice del foglio del nuovo foglio di lavoro al file[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collezione.
1. Ottenere un riferimento al foglio di lavoro.
1. Eseguire il lavoro sui fogli di lavoro.
1.  Salva il nuovo file Excel con i nuovi fogli di lavoro chiamando il file[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Accesso ai fogli di lavoro utilizzando l'indice dei fogli**
Il codice di esempio seguente mostra come accedere o ottenere qualsiasi foglio di lavoro specificandone l'indice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
 La rimozione dei fogli di lavoro per nome funziona bene quando il nome del foglio di lavoro è noto. Se non conosci il nome del foglio di lavoro, usa una versione sovraccaricata del file[RimuoviAt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)metodo che accetta l'indice del foglio di lavoro anziché il nome del foglio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
