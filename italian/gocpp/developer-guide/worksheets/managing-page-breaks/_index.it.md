---
title: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui termina una pagina e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunto il salto di pagina, la pagina finisce e tutti i dati dopo il salto di pagina vengono stampati sulla pagina successiva durante la stampa. In parole semplici, i salti di pagina dividono il foglio di lavoro in più pagine in base alle specifiche. È anche possibile aggiungere salti di pagina ai fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di salti di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come è possibile aggiungere interruzioni di pagina orizzontali o verticali ai fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Interruzioni di pagina**

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) che permette l’accesso a ogni foglio di lavoro nel file Excel.

Una scheda di lavoro è rappresentata dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre un'ampia serie di metodi per gestire un foglio di lavoro. Per aggiungere i interruzioni di pagina, utilizza il metodo [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).

### **Aggiunta dei salti di pagina**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
