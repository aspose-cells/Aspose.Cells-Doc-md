---
title: Convertire un Workbook Excel in PDF
type: docs
weight: 80
url: /it/cpp/convert-excel-workbook-to-pdf/
---

## **Conversione di un Workbook Excel in PDF**
I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}} 

Aspose.Cells scrive direttamente le informazioni sull'API e sul numero di versione nei documenti di output. Ad esempio, al renderizzare il Documento in PDF, Aspose.Cells for C++ popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad esempio 'Aspose.Cells v18.5.0'.

{{% /alert %}} 
### **Conversione Diretta**
Aspose.Cells supporta la conversione da fogli elettronici a PDF in modo indipendente da altri software. Basta salvare un file Excel in PDF utilizzando il [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) e il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) fornisce il membro dell'enumerazione [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) che converte i file nativi di Excel nel formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Istanziare un oggetto della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
3. Eseguire qualsiasi lavoro (inserire dati, applicare formattazione, inserire formule, inserire immagini o altri oggetti grafici, ecc.) sul foglio di calcolo utilizzando le API di Aspose.Cells.
4. Quando il codice del foglio di calcolo è completo, chiamare il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi selezionare il valore rilevante PDF (un valore predefinito) dall'enumerazione SaveFormat per generare il documento PDF finale.

Si prega di vedere il seguente codice di esempio, il [file di Excel di esempio](67338368.xlsx) e il [PDF di output](67338369.pdf) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Conversione Avanzata**
Si può anche optare per utilizzare la classe [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) per impostare diversi attributi per la conversione. Impostare diverse proprietà della classe **PdfSaveOptions** consente di controllare le impostazioni di stampa, font, sicurezza e compressione per il PDF di output. La proprietà più importante è [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) che consente di salvare i file Excel come file PDF/A conformi.
#### **Salvataggio del foglio di lavoro in file PDF/A compilati**
Il seguente frammento di codice dimostra come utilizzare la classe **PdfSaveOptions** per salvare i file Excel in formato PDF/A conforme

Si prega di consultare il seguente codice di esempio e il suo [file PDF di output](67338370.pdf) per il riferimento.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Imposta l'ora di creazione del PDF**
Con la classe **IPdfSaveOptions**, è possibile ottenere o impostare l'ora di creazione del PDF.

Si prega di consultare il seguente codice di esempio e il suo [file PDF di output](67338371.pdf) per il riferimento.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
