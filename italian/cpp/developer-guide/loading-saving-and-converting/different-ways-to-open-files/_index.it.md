---
title: Diverse modalità per aprire i file
linktitle: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Con Aspose.Cells è possibile aprire i file, ad esempio per recuperare dati, o utilizzare un modello di progettazione per accelerare il processo di sviluppo. Aspose.Cells può aprire una serie di file diversi, come fogli di calcolo di Microsoft Excel (XLS, XLSX, XLSM, XLSB), file CSV o TabDelimited.

{{% /alert %}} 
## **Apertura di un file tramite un percorso**
Gli sviluppatori possono aprire un file di Microsoft Excel utilizzando il percorso del file sul computer locale specificandolo nel costruttore della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Basta passare il percorso nel costruttore come String. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Apertura di un file utilizzando uno stream**
È anche possibile aprire un file Excel come stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che accetta l'oggetto *Stream* che contiene il file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

