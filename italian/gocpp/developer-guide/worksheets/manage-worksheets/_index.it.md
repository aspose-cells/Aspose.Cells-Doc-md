---
title: Gestire i Fogli di Lavoro
type: docs
weight: 20
url: /it/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Gli sviluppatori possono facilmente creare e gestire fogli di lavoro nei file di Microsoft Excel utilizzando in modo programmato l'API flessibile di Aspose.Cells. Questo argomento descrive approcci per aggiungere e rimuovere fogli di lavoro nei file di Microsoft Excel.

{{% /alert %}}

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che consente l’accesso a ogni foglio di lavoro nel file Excel.

Una scheda di lavoro è rappresentata dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre un'ampia gamma di metodi per la gestione dei fogli di lavoro.

## **Aggiungere fogli di lavoro a un nuovo file Excel**

Per creare un nuovo file Excel in modo programmatico:

1. Crea un oggetto della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. Chiama il metodo [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) della collezione [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). Un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel. Può essere referenziato passando l’indice del nuovo foglio di lavoro alla collezione [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
1. Ottenere un riferimento al foglio di lavoro.
1. Lavorare sui fogli di lavoro.
1. Salva il nuovo file Excel con nuovi fogli di lavoro chiamando il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Accesso ai Fogli di Lavoro utilizzando l'Indice del Foglio**

Il codice di esempio seguente mostra come accedere o ottenere qualsiasi foglio di lavoro specificando il suo indice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**

Rimuovere fogli di lavoro per nome funziona bene quando si conosce il nome del foglio di lavoro. Se non si conosce il nome del foglio di lavoro, usare una versione sovraccaricata del metodo [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) che prende in input l’indice del foglio di lavoro invece del suo nome.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
