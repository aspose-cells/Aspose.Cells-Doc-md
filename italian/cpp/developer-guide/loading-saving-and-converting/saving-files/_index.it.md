---
title: Salvataggio di file
type: docs
weight: 20
url: /it/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells rende possibile creare e salvare file e manipolare file esistenti. In questo articolo vengono spiegati i vari modi in cui è possibile salvare i file.

{{% /alert %}} 
##  **Diversi modi per salvare i file**
 Aspose.Cells fornisce il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft e fornisce i metodi necessari per lavorare con i file Excel. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe fornisce il file[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodo utilizzato per salvare file Excel. IL[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Il metodo ha molti sovraccarichi utilizzati per salvare i file in diversi modi. Il formato file in cui viene salvato il file viene deciso da[Salva formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)enumerazione.
##  **Salvataggio del file in una posizione**
Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato file desiderato (da[Salva formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerazione) quando si chiama il file[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) dell'oggetto[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Salvataggio del file nello streaming**
 Per salvare i file in un flusso, crea un oggetto MemoryStream o FileStream e salva il file in quell'oggetto flusso chiamando il metodo[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) dell'oggetto[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodo. Specificare il formato file desiderato utilizzando il file[Salva formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerazione quando si chiama il file[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
