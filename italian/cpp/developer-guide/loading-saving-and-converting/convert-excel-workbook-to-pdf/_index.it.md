---
title: Converti la cartella di lavoro di Excel in PDF
type: docs
weight: 80
url: /it/cpp/convert-excel-workbook-to-pdf/
---
## **Conversione della cartella di lavoro di Excel in PDF**
I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}} 

 Aspose.Cells scrive direttamente le informazioni sull'API e il numero di versione nei documenti di output. Ad esempio, dopo aver convertito Documento in PDF, Aspose.Cells for C++ popola il**Applicazione** campo con valore 'Aspose.Cells' e**Produttore PDF** campo con valore, ad esempio 'Aspose.Cells v18.5.0'.

Si prega di notare che non è possibile incaricare Aspose.Cells for C++ di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}} 
### **Conversione diretta**
Aspose.Cells supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il formato[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)classe'[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo. Il[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo fornisce il[SalvaFormato_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)membro di enumerazione che converte i file Excel nativi in formato PDF.

Segui i passaggi seguenti per convertire direttamente i fogli di calcolo Excel in formato PDF:

1.  Istanziare un oggetto di[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)class chiamando il suo costruttore vuoto.
1. Puoi aprire/caricare un file modello esistente o saltare questo passaggio se stai creando la cartella di lavoro da zero.
1. Eseguire qualsiasi lavoro (dati di input, applicare formattazione, impostare formule, inserire immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells.
1.  Quando il codice del foglio di calcolo è completo, chiama il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)classe'[Salva](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metodo per salvare il foglio di calcolo.

Il formato del file deve essere PDF, quindi seleziona il PDF pertinente (un valore predefinito) dall'enumerazione SaveFormat per generare il documento PDF finale

 Si prega di vedere il seguente codice di esempio, its[esempio di file Excel](67338368.xlsx) e[uscita PDF](67338369.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **Conversione avanzata**
Puoi anche scegliere di utilizzare il[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)class per impostare diversi attributi per la conversione. Impostazione di diverse proprietà del file**IPdfSaveOptions** class ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per il PDF di output. La proprietà più importante è[SetCompliance](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)che consente di salvare i file Excel in file PDF compatibili con PDF/A.
#### **Salvataggio della cartella di lavoro in file PDF/A conformi**
Il seguente frammento di codice illustra come utilizzare il**IPdfSaveOptions**class per salvare i file Excel in formato PDF compatibile con PDF/A

 Si prega di vedere il seguente codice di esempio e il suo[uscita PDF](67338370.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **Imposta l'ora di creazione del PDF**
Con il**IPdfSaveOptions** class, è possibile ottenere o impostare l'ora di creazione del PDF.

 Si prega di vedere il seguente codice di esempio e il suo[uscita PDF](67338371.pdf) per tua referenza.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
