---
title: Converti un file XLS in formato PDF
type: docs
weight: 30
url: /it/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) rappresenta i documenti indipendentemente dal software, dall'hardware e dal sistema operativo utilizzato per crearli. Un file PDF può essere costituito da documenti con qualsiasi combinazione di testo, grafica e immagini in modo indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio del file originale.

 volte, è necessario convertire un file Microsoft Excel in PDF. Per questo, hai bisogno di una soluzione veloce, sicura, accurata e affidabile che ti consenta di distribuire documenti PDF in tutto il mondo. Esistono numerosi strumenti di conversione che possono eseguire questa operazione. Ma devi assicurarti che il layout del documento Excel originale sia mantenuto nel file PDF di output. Le immagini, la formattazione dei dati, i caratteri, gli attributi, i colori, le impostazioni di configurazione della pagina, l'orientamento del testo, i bordi, i grafici ecc. devono essere resi in modo accurato e preciso.[Aspose.Cells](https://products.aspose.com/cells/net/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Microsoft Excel (contenente immagini, grafici, formattazione ecc.) può essere convertito in PDF. A tal fine, viene mostrato come creare una semplice applicazione console in Visual Studio.Net che converte un file Excel in PDF utilizzando l'API Aspose.Cells. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

## **Conversione da Excel a PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. La cartella di lavoro contiene fogli di lavoro con grafici e immagini. Ogni foglio di lavoro contiene diversi tipi di formati utilizzando caratteri, attributi, colori, effetti di ombreggiatura e bordi. C'è un istogramma sul primo foglio di lavoro e un'immagine sull'ultimo.

### **Il file modello Excel**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come Media. Il primo foglio di lavoro ha grafici e l'ultimo foglio di lavoro ha un'immagine come mostrato di seguito negli screenshot.

|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet1.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet3.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|

### **Processo di conversione**

1. Scarica e installa Aspose.Cells:
 1. Scarica Aspose.Cells for .NET.
 1. Installalo sul tuo computer di sviluppo.
1. Crea un progetto e aggiungi i riferimenti:
 1. Avviare Visual Studio.Net.
 1. Creare una nuova applicazione console.
 1. Aggiungere un riferimento a …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Aggiungi il codice di conversione al progetto:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare Workbook.CalculateFormula() appena prima di eseguire il rendering del foglio di calcolo in PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}

### **Risultato**

quando il codice precedente è stato eseguito, viene creato un file PDF nella cartella File nella directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Si noti che anche intestazioni e piè di pagina vengono mantenuti nel file PDF di output.

|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted1.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
| Il primo foglio di lavoro**(Previsioni di vendita)**| Il secondo foglio di lavoro**(Rapporto delle vendite)**|
|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted3.png)|![cose da fare:immagine_alt_testo](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Il terzo foglio di lavoro**(Inserimento dati)**| L'ultimo foglio di lavoro**(Immagine)**|
