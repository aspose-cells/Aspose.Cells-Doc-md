---
title: Diversi modi per aprire i file
linktitle: Diversi modi per aprire i file
type: docs
weight: 10
url: /it/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Con Aspose.Cells è possibile aprire file, ad esempio per recuperare dati, oppure utilizzare un template designer per velocizzare il processo di sviluppo. Aspose.Cells può aprire una gamma di file diversi, come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), file CSV o TabDelimited.

{{% /alert %}} 
## **Apertura di un file tramite un percorso**
 Gli sviluppatori possono aprire un file Microsoft Excel utilizzando il percorso del file sul computer locale specificandolo nel file[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)costruttore di classe. Basta passare il percorso nel costruttore come String. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Apertura di un file utilizzando uno stream**
 È anche possibile aprire un file Excel come flusso. Per fare ciò, usa una versione sovraccaricata del costruttore che accetta il*Flusso*oggetto che contiene il file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

