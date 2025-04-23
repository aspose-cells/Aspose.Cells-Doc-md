---
title: Salvataggio dei file
type: docs
weight: 20
url: /it/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells consente di creare e salvare file e di manipolare file esistenti. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}}

## **Diversi modi per salvare i file**

Aspose.Cells fornisce il [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), che rappresenta un file Microsoft Excel e offre i metodi necessari per lavorare con i file Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) fornisce il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) utilizzato per salvare i file Excel. Il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) ha molte sovrapposizioni che vengono usate per salvare i file in modi diversi. Il formato del file in cui il file viene salvato è deciso dall'enumerazione [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **Salvataggio del file in una determinata posizione**

Per salvare i file in una posizione di archiviazione, specifica il nome del file (completo del percorso di archiviazione) e il formato file desiderato (dall'enumerazione [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)) chiamando il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) dell'oggetto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Salvataggio del file su flusso**

Per salvare i file in uno stream, crea un oggetto MemoryStream o FileStream e salva il file in quell'oggetto stream chiamando il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) dell'oggetto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Specifica il formato del file desiderato usando l'enumerazione [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) quando chiami il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Salvataggio del file in PDF**

Per salvare il contenuto desiderato in un file PDF utilizzando la libreria Aspose.Cells for Go via C++, crea un nuovo oggetto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) oppure costruisci un [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) leggendo un file Excel esistente, e poi [sava](https://reference.aspose.com/cells/go-cpp/workbook/save/) il file in PDF chiamando il metodo Save dell'oggetto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Quando chiami il metodo Save, usa l'enumerazione [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) per specificare il formato del file desiderato.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
