---
title: Converti il file XLSX nel formato PDF
type: docs
weight: 30
url: /it/python-net/convert-xlsx-file-to-pdf-format/
description: Scopri come convertire il file XLSX nel formato PDF con Aspose.Cells for Python via .NET API.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF (Portable Document Format) rappresenta i documenti indipendentemente dal software, dall'hardware e dal sistema operativo utilizzati per creare tali documenti. Un file PDF può contenere documenti con qualsiasi combinazione di testo, grafica e immagini in modo indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio del file originale.

 A volte è necessario convertire un file Excel Microsoft in PDF. Per questo è necessaria una soluzione veloce, sicura, precisa e affidabile che ti consenta di distribuire i documenti PDF in tutto il mondo. Esistono numerosi strumenti di conversione in grado di eseguire questa attività. Ma devi assicurarti che il layout del documento Excel originale venga mantenuto nel file di output PDF. Immagini, grafici, forme, formattazione dei dati, caratteri, attributi, colori, impostazioni di impostazione della pagina, orientamento del testo, bordi, grafici ecc. devono essere visualizzati in modo accurato e preciso.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Excel Microsoft (contenente immagini, grafici, formattazione ecc.) può essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in Visual Studio.Net che converte un file Excel in PDF utilizzando Aspose.Cells for Python via .NET API. La conversione viene eseguita con un elevato grado di precisione e accuratezza.

{{% /alert %}}

##  **Conversione di Excel in PDF**

In questo esempio viene utilizzato un file Excel (SampleInput.xlsx) come modello. La cartella di lavoro contiene fogli di lavoro con grafici e immagini. Ogni foglio di lavoro contiene diversi tipi di formati utilizzando caratteri, attributi, colori, effetti di ombreggiatura e bordi. C'è un istogramma nel primo foglio di lavoro e un'immagine nell'ultimo.

###  **Il file Excel modello**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come Media. Il primo foglio di lavoro contiene grafici e l'ultimo foglio di lavoro contiene un'immagine come mostrato di seguito negli screenshot.

|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet1.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet3.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|

###  **Processo di conversione**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) subito prima di eseguire il rendering del foglio di calcolo su PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}

###  **Risultato**

Una volta eseguito il codice precedente, viene creato un file PDF nella cartella File nella directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Tieni presente che le intestazioni e i piè di pagina vengono conservati anche nel file di output PDF.

|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted1.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted3.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|
