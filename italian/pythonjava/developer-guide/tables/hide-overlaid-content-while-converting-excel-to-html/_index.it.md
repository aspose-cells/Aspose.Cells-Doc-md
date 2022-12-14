---
title: Nascondi il contenuto sovrapposto durante la conversione di Excel in HTML
type: docs
weight: 40
url: /it/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Nascondi il contenuto sovrapposto durante la conversione di Excel in HTML**
Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi incrociati per le stringhe di celle. Per impostazione predefinita, Aspose.Cells genera HTML come per Microsoft Excel ma quando si modifica il[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)a[ATTRAVERSO_NASCONDERE_GIUSTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)quindi nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o sovrapposte alla stringa di cella.

Il codice di esempio seguente carica il file[esempio di file Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)e lo salva in[output HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)dopo aver impostato il[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)come[ATTRAVERSO_NASCONDERE_GIUSTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Lo screenshot spiega come[ATTRAVERSO_NASCONDERE_GIUSTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)influisce sull'output HTML dall'output predefinito.

![cose da fare:immagine_alt_testo](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
