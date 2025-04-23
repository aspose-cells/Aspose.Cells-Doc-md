---
title: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi di croce per le stringhe delle celle. Per impostazione predefinita, Aspose.Cells per Python via .NET genera HTML secondo Microsoft Excel, ma quando cambi il tipo di croce in [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/), allora nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o coprono la stringa della cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il seguente codice di esempio carica il [file Excel di esempio](64716894.xlsx) e lo salva in [HTML di output](64716893.zip) dopo aver impostato [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) come [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). La schermata mostra come [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) influisce sull'HTML di output rispetto all'output predefinito.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
