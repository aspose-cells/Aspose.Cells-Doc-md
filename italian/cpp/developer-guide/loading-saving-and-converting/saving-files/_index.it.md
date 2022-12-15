---
title: Salvataggio di file
type: docs
weight: 20
url: /it/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells consente di creare e salvare file e di manipolare file esistenti. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}} 
## **Diversi modi per salvare i file**
 Aspose.Cells fornisce il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Microsoft Excel e fornisce i metodi necessari per lavorare con i file Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe fornisce il[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) metodo utilizzato per salvare i file Excel. Il[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Il metodo ha molti overload che vengono utilizzati per salvare i file in modi diversi. Il formato di file in cui viene salvato il file è deciso dal file[SalvaFormato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)enumerazione.
## **Salvataggio del file in una posizione**
 Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato file desiderato (da[SalvaFormato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)enumerazione) quando si chiama il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) dell'oggetto[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Salvataggio del file nello streaming**
 Per salvare i file in un flusso, creare un oggetto MemoryStream o FileStream e salvare il file in quell'oggetto flusso chiamando il metodo[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) dell'oggetto[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) metodo. Specificare il formato di file desiderato utilizzando il file[SalvaFormato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumerazione quando si chiama il[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
