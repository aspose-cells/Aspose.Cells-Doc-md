---
title: Converti il file XLSX nel formato PDF
type: docs
weight: 30
url: /it/net/convert-xlsx-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) rappresenta i documenti indipendentemente dal software, dall'hardware e dal sistema operativo utilizzato per creare tali documenti. Un file PDF può essere costituito da documenti con qualsiasi combinazione di testo, grafica e immagini in modo indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio del file originale.

 volte, è necessario convertire un file Excel Microsoft in PDF. Per questo, è necessaria una soluzione rapida, sicura, accurata e affidabile che consenta di distribuire documenti PDF in tutto il mondo. Esistono numerosi strumenti di conversione che possono eseguire questa operazione. Ma devi assicurarti che il layout del documento Excel originale sia mantenuto nel file di output PDF. Immagini, grafici, forme, formattazione dei dati, caratteri, attributi, colori, impostazioni di configurazione della pagina, orientamento del testo, bordi, grafici ecc. devono essere riprodotti in modo accurato e preciso.[Aspose.Cells](https://products.aspose.com/cells/net/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Excel Microsoft (contenente immagini, grafici, formattazione ecc.) può essere convertito in PDF. A tal fine, viene mostrato come creare una semplice applicazione console in Visual Studio.Net che converte un file Excel in PDF utilizzando Aspose.Cells API. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

##  **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. La cartella di lavoro contiene fogli di lavoro con grafici e immagini. Ogni foglio di lavoro contiene diversi tipi di formati utilizzando caratteri, attributi, colori, effetti di ombreggiatura e bordi. C'è un istogramma sul primo foglio di lavoro e un'immagine sull'ultimo.

###  **Il file modello Excel**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come Media. Il primo foglio di lavoro ha grafici e l'ultimo foglio di lavoro ha un'immagine come mostrato di seguito negli screenshot.

|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|

###  **Processo di conversione**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)appena prima di eseguire il rendering del foglio di calcolo in PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}

###  **Risultato**

Quando il codice precedente è stato eseguito, viene creato un file PDF nella cartella File nella directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Si noti che anche le intestazioni e i piè di pagina vengono mantenuti nel file di output PDF.

|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![cose da fare:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|
