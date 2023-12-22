---
title: Converti la cartella di lavoro di Excel in PDF
type: docs
weight: 80
url: /it/cpp/convert-excel-workbook-to-pdf/
---
##  **Conversione della cartella di lavoro Excel in PDF**
I file PDF sono ampiamente utilizzati per scambiare documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Excel Microsoft in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}} 

 Aspose.Cells scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, durante il rendering del documento su PDF, Aspose.Cells for C++ popola il campo**Applicazione** campo con valore 'Aspose.Cells' e**PDF Produttore** campo con valore, ad esempio 'Aspose.Cells v18.5.0'.

Tieni presente che non puoi chiedere a Aspose.Cells for C++ di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}} 
###  **Conversione diretta**
Aspose.Cells supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Salva semplicemente un file Excel su PDF utilizzando il file[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)classe'[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metodo. IL[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)il metodo fornisce il file[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)membro di enumerazione che converte i file Excel nativi nel formato PDF.

Segui i passaggi seguenti per convertire direttamente i fogli di calcolo Excel nel formato PDF:

1.  Istanziare un oggetto di[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)class chiamando il suo costruttore vuoto.
1. Puoi aprire/caricare un file modello esistente o saltare questo passaggio se stai creando la cartella di lavoro da zero.
1. Esegui qualsiasi operazione (inserisci dati, applica formattazione, imposta formule, inserisci immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells.
1.  Una volta completato il codice del foglio di calcolo, chiamare il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)classe'[Salva](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metodo per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi seleziona PDF pertinente (un valore predefinito) dall'enumerazione SaveFormat per generare il documento finale PDF

 Si prega di consultare il seguente codice di esempio, its[file Excel di esempio](67338368.xlsx) E[uscita PDF](67338369.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Conversione avanzata**
Puoi anche scegliere di utilizzare il file[PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)classe per impostare attributi diversi per la conversione. Impostazione di diverse proprietà di**PdfSaveOptions** ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output PDF. La proprietà più importante è[ImpostaConformità](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)che consente di salvare i file Excel in file PDF conformi a PDF/A.
####  **Salvataggio della cartella di lavoro in file conformi PDF/A**
Il frammento di codice seguente illustra come utilizzare il file**PdfSaveOptions**classe per salvare i file Excel nel formato compatibile PDF/A PDF

 Si prega di consultare il seguente codice di esempio e il suo[uscita PDF](67338370.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Imposta l'ora di creazione PDF**
Con il**IPdfSaveOptions** class, puoi ottenere o impostare l'ora di creazione PDF.

 Si prega di consultare il seguente codice di esempio e il suo[uscita PDF](67338371.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
