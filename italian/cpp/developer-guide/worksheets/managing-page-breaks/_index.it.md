---
title: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui termina una pagina e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunto il salto di pagina, la pagina finisce e tutti i dati dopo il salto di pagina vengono stampati sulla pagina successiva durante la stampa. In parole semplici, i salti di pagina dividono il foglio di lavoro in più pagine in base alle specifiche. È anche possibile aggiungere salti di pagina ai fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di salti di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come è possibile aggiungere interruzioni di pagina orizzontali o verticali ai fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 
## **Interruzioni di pagina**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di metodi utilizzati per gestire un foglio di lavoro. Per aggiungere i salti di pagina, utilizzare il metodo [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Aggiunta dei salti di pagina**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
