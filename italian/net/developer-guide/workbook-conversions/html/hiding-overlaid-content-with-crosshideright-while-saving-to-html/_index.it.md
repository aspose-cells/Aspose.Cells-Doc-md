---
title: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possibili Scenari di Utilizzo**

Quando si salva il file Excel in HTML, è possibile specificare diversi tipi di incrocio per le stringhe delle celle. Per impostazione predefinita, Aspose.Cells genera HTML come da Microsoft Excel ma quando si cambia il tipo di incrocio in [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), allora nasconde tutte le stringhe sul lato destro della cella che si sovrappongono o si sovrappongono alla stringa della cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il seguente codice di esempio carica il [file Excel di esempio](64716894.xlsx) e lo salva in [HTML di output](64716893.zip) dopo aver impostato [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) come [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). La schermata mostra come [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) influisce sull'HTML di output rispetto all'output predefinito.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
