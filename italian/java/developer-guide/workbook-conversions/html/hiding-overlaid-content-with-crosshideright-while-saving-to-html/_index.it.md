---
title: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Possibili Scenari di Utilizzo**

Quando si salva il file Excel in HTML, è possibile specificare diversi tipi di attraversamenti per le stringhe delle celle. Per impostazione predefinita, Aspose.Cells genera l'HTML come da Microsoft Excel ma quando si cambia il [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) in [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT) allora nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o sovrapponibili alla stringa della cella.

## **Nascondere il Contenuto Sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il codice di esempio seguente carica il [file Excel di esempio](64716916.xlsx) e lo salva in [HTML di output](64716915.zip) dopo aver impostato il [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) come [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT). La schermata spiega come [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT) influisce sull'HTML di output predefinito.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
{{< app/cells/assistant language="java" >}}
