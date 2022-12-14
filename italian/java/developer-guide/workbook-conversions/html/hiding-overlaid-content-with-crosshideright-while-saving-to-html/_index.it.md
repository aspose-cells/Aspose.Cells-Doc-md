---
title: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Possibili scenari di utilizzo**

Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi incrociati per le stringhe di celle. Per impostazione predefinita, Aspose.Cells genera HTML come per Microsoft Excel ma quando si modifica il[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)a[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)quindi nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o sovrapposte alla stringa di cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il codice di esempio seguente carica il file[esempio di file Excel](64716916.xlsx)e lo salva in[output HTML](64716915.zip)dopo aver impostato il[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)come[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Lo screenshot spiega come[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)influisce sull'output HTML dall'output predefinito.

![cose da fare:immagine_alt_testo](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
