---
title: Diversi modi per aprire i file
linktitle: Diversi modi per aprire i file
type: docs
weight: 10
url: /it/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Con Aspose.Cells è possibile aprire file, ad esempio per recuperare dati, oppure utilizzare un template designer per velocizzare il processo di sviluppo. Aspose.Cells può aprire una serie di file diversi, ad esempio fogli di calcolo Excel Microsoft (file XLS, XLSX, XLSM, XLSB), CSV o file TabDelimited.

{{% /alert %}} 
##  **Apertura di un file tramite un percorso**
 Gli sviluppatori possono aprire un file Excel Microsoft utilizzando il relativo percorso file sul computer locale specificandolo nel campo[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)costruttore di classi. Passa semplicemente il percorso nel costruttore come String. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Apertura di un file utilizzando uno stream**
 È anche possibile aprire un file Excel come flusso. Per fare ciò, utilizzare una versione sovraccaricata del costruttore che accetta il file*Flusso*oggetto che contiene il file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

