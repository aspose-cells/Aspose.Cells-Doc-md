---
title: Gestione delle interruzioni di pagina
type: docs
weight: 30
url: /it/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Un'interruzione di pagina è un punto nel testo in cui finisce una pagina e inizia quella successiva. Microsoft Excel può aggiungere interruzioni di pagina in qualsiasi cella selezionata in un foglio di lavoro.
La pagina termina nella cella in cui viene aggiunta l'interruzione di pagina e tutti i dati dopo l'interruzione di pagina vengono stampati nella pagina successiva. In parole semplici, le interruzioni di pagina dividono i fogli di lavoro in più pagine. È anche possibile aggiungere interruzioni di pagina ai fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells supporta due tipi di interruzioni di pagina:

- orizzontale
- verticale.

Questo articolo descrive come aggiungere interruzioni di pagina orizzontali o verticali nei fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells e interruzioni di pagina**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class che fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per aggiungere le interruzioni di pagina, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**Interruzioni di pagina orizzontali**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) e[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)proprietà.

 Il[**Interruzioni di pagina orizzontali**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) e[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)le proprietà sono infatti raccolte che possono contenere diverse interruzioni di pagina. Ogni raccolta contiene diversi metodi per la gestione delle interruzioni di pagina orizzontali e verticali. Come vengono utilizzati questi metodi è discusso di seguito.

## **Aggiunta di interruzioni di pagina**

 Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserisci interruzioni di pagina verticali e orizzontali nella cella specificata chiamando il metodo[**Interruzioni di pagina orizzontali**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collezioni'**Aggiungere** metodi. A testa**Aggiungere**Il metodo accetta il nome della cella in cui deve essere aggiunta l'interruzione di pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

Nelle modalità Anteprima interruzione di pagina o Anteprima di stampa, puoi vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}

## **Cancellazione di tutte le interruzioni di pagina**

 Per cancellare tutte le interruzioni di pagina in un foglio di lavoro, chiama il metodo[**OrizzontalePageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collezioni'**Chiaro**metodi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Rimozione di un'interruzione di pagina specifica**

 Per rimuovere un'interruzione di pagina specifica nel foglio di lavoro, chiama il metodo[**OrizzontalePageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) e[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collezioni'**removeAt** metodi. A testa**removeAt**metodo prenderà l'indice dell'interruzione di pagina da rimuovere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Importante da sapere** : quando si imposta l'adattamento alle proprietà della pagina (ovvero[**FitToPagesAlto**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) e[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) nelle impostazioni di configurazione della pagina, le impostazioni dell'interruzione di pagina sono interessate, quindi, se si stampa il foglio di lavoro, le impostazioni dell'interruzione di pagina non vengono considerate sebbene esistano ancora nel file.

{{% /alert %}}
