---
title: Converti file XLSX in formato PDF con Golang tramite C++
linktitle: Converti il file XLSX nel Formato PDF
type: docs
weight: 30
url: /it/go-cpp/convert-xlsx-file-to-pdf-format/
description: Impara come convertire i file Excel in formato PDF utilizzando Aspose.Cells for C++ con alta precisione e accuratezza.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) rappresenta documenti indipendentemente dal software, hardware e sistema operativo utilizzati per creare quei documenti. Un file PDF può contenere qualsiasi combinazione di testo, grafica e immagini in modo indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio rispetto al file originale.

A volte, hai bisogno di convertire un file Microsoft Excel in PDF. Per questo, è richiesta una soluzione rapida, sicura, precisa e affidabile che consenta di distribuire documenti PDF in tutto il mondo. Ci sono numerosi strumenti di conversione che possono eseguire questo compito. Ma devi assicurarti che il layout del documento Excel originale sia mantenuto nel file PDF di output. Immagini, grafici, forme, formattazione dei dati, font, attributi, colori, impostazioni di pagina, orientamento del testo, bordi, grafici, ecc., devono essere resi con precisione e accuratezza. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Microsoft Excel (contenente immagini, grafici, formattazione, ecc.) possa essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in C++ che converte un file Excel in PDF utilizzando l'API di Aspose.Cells. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

## **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. Il libro contiene fogli di lavoro con grafici e immagini. Ogni foglio contiene diversi tipi di formattazione utilizzando font, attributi, colori, effetti di ombreggiatura e bordi. Nel primo foglio c’è un grafico a colonne e nell’ultimo un’immagine.

### **Il file Excel di modello**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come Media. Il primo foglio di lavoro contiene grafici, e l’ultimo foglio di lavoro ha un’immagine, come mostrato nelle schermate di seguito.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|

### **Processo di conversione**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Se il foglio contiene formule, è meglio chiamare il metodo [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) subito prima di esportare il foglio in PDF. Questo assicura che i valori dipendenti dalla formula siano ricalcolati e che i valori corretti siano visualizzati nel PDF.

{{% /alert %}}

### **Risultato**

Quando il codice sopra è stato eseguito, viene creato un file PDF nella cartella Files della directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Nota che gli header e i footer sono mantenuti anche nel file PDF di output.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|
