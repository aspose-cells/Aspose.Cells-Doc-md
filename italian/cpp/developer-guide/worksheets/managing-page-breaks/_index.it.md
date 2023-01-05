---
title: Gestione delle interruzioni di pagina
type: docs
weight: 30
url: /it/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui una pagina finisce e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, la pagina viene terminata e tutti gli altri dati dopo l'interruzione di pagina vengono stampati sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il foglio di lavoro in più pagine in base alle tue specifiche. Puoi anche aggiungere interruzioni di pagina ai tuoi fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come aggiungere interruzioni di pagina orizzontali o verticali nei fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 
## **Interruzioni di pagina**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)fornisce una vasta gamma di metodi utilizzati per gestire un foglio di lavoro. Per aggiungere le interruzioni di pagina, utilizzare il[Aggiungi interruzioni di pagina](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe.
### **Aggiunta di interruzioni di pagina**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
