---
title: Gestisci fogli di lavoro
type: docs
weight: 20
url: /it/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Gli sviluppatori possono creare e gestire facilmente fogli di lavoro nei file Excel Microsoft a livello di codice utilizzando Aspose.Cells flessibile API. Questo argomento descrive gli approcci per aggiungere e rimuovere fogli di lavoro nei file Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fornisce un'ampia gamma di metodi per la gestione dei fogli di lavoro.
##  **Aggiunta di fogli di lavoro a un nuovo file Excel**
Per creare un nuovo file Excel a livello di codice:

1.  Crea un oggetto del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe.
1.  Chiama il[Aggiungere](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) metodo del[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collezione. Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel. È possibile farvi riferimento passando l'indice del nuovo foglio di lavoro al file[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collezione.
1. Ottieni un riferimento al foglio di lavoro.
1. Eseguire il lavoro sui fogli di lavoro.
1. Salva il nuovo file Excel con nuovi fogli di lavoro chiamando il file[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) classe[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Accesso ai fogli di lavoro utilizzando l'indice dei fogli**
Il codice di esempio seguente mostra come accedere o ottenere qualsiasi foglio di lavoro specificandone l'indice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
 La rimozione dei fogli di lavoro per nome funziona bene quando il nome del foglio di lavoro è noto. Se non conosci il nome del foglio di lavoro, utilizza una versione sovraccaricata di[RimuoviAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)metodo che accetta l'indice del foglio di lavoro invece del nome del foglio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
