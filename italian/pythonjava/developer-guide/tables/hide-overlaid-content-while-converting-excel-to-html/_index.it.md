---
title: Nascondi Contenuto Sovrapposto durante la conversione di Excel in HTML
type: docs
weight: 40
url: /it/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Nascondi Contenuto Sovrapposto durante la conversione di Excel in HTML**
Quando si salva il file Excel in HTML, è possibile specificare diversi tipi di incrocio per le stringhe delle celle. Per impostazione predefinita, Aspose.Cells genera HTML come da Microsoft Excel ma quando si modifica l'opzione [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) in [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) allora nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o sovrapponendosi alla stringa della cella.

Il seguente codice di esempio carica il [file Excel di esempio](sampleHidingOverlaidContentWithCrossHideRight.xlsx) e lo salva in [HTML di output](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) dopo aver impostato l'opzione [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) come [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). La schermata mostra come [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) influisce sull'HTML di output rispetto all'output predefinito.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
