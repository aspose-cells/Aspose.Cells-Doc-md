---
title: Converti il file XLSX nel Formato PDF
type: docs
weight: 30
url: /it/python-net/convert-xlsx-file-to-pdf-format/
description: Scopri come convertire il file XLSX nel formato PDF con Aspose.Cells for Python via .NET API.
keywords: Converte il file XLSX nel formato PDF con Python, Converti xlsx in pdf usando Python, Python xlsx in pdf, Salva xlsx in pdf in python, xlsx in formato pdf in Python
---

{{% alert color="primary" %}}

Il formato PDF (Portable Document Format) rappresenta documenti in modo indipendente dal software, dall'hardware e dal sistema operativo utilizzati per crearli. Un file PDF può contenere una combinazione qualsiasi di testo, grafica e immagini in maniera indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio rispetto al file originale.

A volte è necessario convertire un file Microsoft Excel in PDF. Per questo, è necessaria una soluzione rapida, sicura, accurata e affidabile che consenta di distribuire documenti PDF in tutto il mondo. Ci sono numerosi strumenti di conversione che possono svolgere questo compito. Ma devi assicurarti che la struttura del documento Excel originale venga mantenuta nel file PDF di output. Immagini, grafici, forme, formattazione dati, caratteri, attributi, colori, impostazioni di impaginazione della pagina, orientamento del testo, bordi, grafici, ecc. dovrebbero essere renderizzati in modo accurato e preciso. [Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Microsoft Excel (contenente immagini, grafici, formattazione ecc.) possa essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in Visual Studio.Net che converte un file Excel in PDF utilizzando Aspose.Cells for Python via .NET API. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

## **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. Il workbook contiene fogli di lavoro con grafici e immagini. Ogni foglio di lavoro contiene diversi tipi di formati utilizzando caratteri, attributi, colori, effetti di sfumatura e bordi. C'è un grafico a colonne sul primo foglio di lavoro e un'immagine sull'ultimo.

### **Il file Excel di modello**

Il file di modello ha tre fogli di lavoro, compresi grafici e immagini come Media. Il primo foglio di lavoro ha grafici e l'ultimo foglio di lavoro ha un'immagine come mostrato di seguito negli screenshot.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|

### **Processo di conversione**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) subito prima di rendere il foglio di calcolo in PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che vengano visualizzati i valori corretti nel PDF.

{{% /alert %}}

### **Risultato**

Quando il codice sopra è stato eseguito, viene creato un file PDF nella cartella Files della directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Nota che gli header e i footer sono mantenuti anche nel file PDF di output.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|
{{< app/cells/assistant language="python-net" >}}
