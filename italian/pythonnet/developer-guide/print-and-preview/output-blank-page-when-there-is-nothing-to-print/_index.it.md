---
title: Genera una pagina vuota quando non c è nulla da stampare
type: docs
weight: 90
url: /it/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Se il foglio è vuoto, Aspose.Cells per Python via .NET non stamperà nulla quando esporti il foglio come immagine. Puoi modificare questo comportamento usando la proprietà [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print). Quando la imposterai su **true**, stamperà la pagina vuota.

## **Output Pagina Bianca quando non c'è Nulla da Stampare**

Il seguente codice di esempio crea il workbook vuoto che ha un foglio di lavoro vuoto e rende il foglio di lavoro vuoto in un'immagine dopo aver impostato la proprietà [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) come **true**. Di conseguenza, genera la pagina vuota poiché non c'è nulla da stampare, come puoi vedere nell'immagine sotto.

![todo:image_alt_text](1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

