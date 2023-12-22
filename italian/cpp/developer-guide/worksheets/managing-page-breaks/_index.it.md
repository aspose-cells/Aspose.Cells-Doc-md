---
title: Gestione delle interruzioni di pagina
type: docs
weight: 30
url: /it/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Secondo la definizione, un'interruzione di pagina è un punto nel flusso di testo in cui finisce una pagina e inizia quella successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, la pagina viene terminata e tutti i restanti dati dopo l'interruzione di pagina vengono stampati sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il tuo foglio di lavoro in più pagine in base alle tue specifiche. Puoi anche aggiungere interruzioni di pagina ai tuoi fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come aggiungere interruzioni di pagina orizzontali o verticali nei tuoi fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 
##  **Interruzioni di pagina**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) che rappresenta un file Excel. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fornisce un'ampia gamma di metodi utilizzati per gestire un foglio di lavoro. Per aggiungere le interruzioni di pagina, utilizzare il[AggiungiPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe.
###  **Aggiunta di interruzioni di pagina**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
