---
title: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Un salto di pagina è un punto nel testo in cui finisce una pagina e inizia la successiva. Microsoft Excel può aggiungere salti di pagina in qualsiasi cella selezionata in un foglio di lavoro.
La pagina termina nella cella in cui è stato aggiunto il salto di pagina e tutti i dati dopo il salto di pagina vengono stampati sulla pagina successiva. In parole semplici, i salti di pagina dividono i fogli di calcolo in più pagine. È anche possibile aggiungere salti di pagina ai fogli di lavoro in esecuzione utilizzando Aspose.Cells. Aspose.Cells supporta due tipi di salti di pagina:

- orizzontale
- verticale.

Questo articolo descrive come aggiungere salti di pagina orizzontali o verticali nei fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells e i salti di pagina**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe {0} che fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per aggiungere i salti di pagina, utilizzare la {1} della classe {2} e le proprietà {3} e {4}.

Le proprietà [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) e [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) sono infatti insiemi che possono contenere diversi salti di pagina. Ogni insieme contiene diversi metodi per gestire i salti di pagina orizzontali e verticali. Come utilizzare questi metodi è discusso di seguito.

## **Aggiunta dei salti di pagina**

Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserire interruzioni di pagina verticali e orizzontali nella cella specificata chiamando i metodi **Aggiungi** delle collezioni [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Ogni metodo **Aggiungi** richiede il nome della cella in cui deve essere aggiunta l'interruzione di pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

In modalità anteprima interruzione di pagina o anteprima di stampa, è possibile vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}

## **Cancellazione di tutte le interruzioni di pagina**

Per cancellare tutte le interruzioni di pagina in un foglio di lavoro, chiamare i metodi **Cancella** delle collezioni [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Rimozione di specifiche interruzioni di pagina**

Per rimuovere una specifica interruzione di pagina nel foglio di lavoro, chiamare i metodi **removeAt** delle collezioni [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Ogni metodo **removeAt** richiederà l'indice dell'interruzione di pagina da rimuovere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Importante da sapere**: Quando si impostano le proprietà di adattamento alla pagina (cioè [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) e [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) nelle impostazioni di configurazione della pagina), le impostazioni di interruzione pagina sono influenzate, quindi, se si stampa il foglio di lavoro, le impostazioni di interruzione pagina non saranno considerate anche se esistono ancora nel file.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
