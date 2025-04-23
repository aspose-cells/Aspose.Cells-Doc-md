---
title: Diverse modalità per aprire i file
linktitle: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells, puoi aprire file, ad esempio per recuperare dati o usare un modello di progettazione per accelerare lo sviluppo. Aspose.Cells può aprire una vasta gamma di file diversi, come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), CSV o file delimitati da tab.

{{% /alert %}}

## **Apertura di un file tramite un percorso**

Gli sviluppatori possono aprire un file Microsoft Excel usando il suo percorso sul computer locale specificandolo nel costruttore della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Passare il percorso come stringa nel costruttore. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Apertura di un file tramite stream**

È anche possibile aprire un file Excel come stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che accetta l'oggetto *Stream* che contiene il file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
