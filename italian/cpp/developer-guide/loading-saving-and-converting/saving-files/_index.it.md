---
title: Salvataggio dei file
type: docs
weight: 20
url: /it/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells rende possibile creare e salvare file e manipolare file esistenti. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}} 
## **Diversi modi per salvare i file**
Aspose.Cells fornisce il [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel e fornisce i metodi necessari per lavorare con file Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilizzato per salvare file Excel. Il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) ha molte sovraccariche utilizzate per salvare file in modi diversi. Il formato del file in cui viene salvato è deciso dall'enumerazione [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **Salvataggio del file in una determinata posizione**
Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato desiderato del file (dall'enumerazione [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) quando si chiama il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) dell'oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Salvataggio del file su flusso**
Per salvare i file su un flusso, creare un oggetto MemoryStream o FileStream e salvare il file su tale oggetto flusso chiamando il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) dell'oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Specificare il formato del file desiderato utilizzando l'enumerazione [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) quando si chiama il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Salvataggio del file in PDF**
Per salvare il contenuto desiderato in un file PDF utilizzando la libreria Aspose.Cells for C++, creare un nuovo oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) o costruire un oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) leggendo un file Excel esistente, e quindi [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) il file in PDF chiamando il metodo Save dell'oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Quando si chiama il metodo Save, utilizzare l'enumerazione [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) per specificare il formato del file desiderato.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
