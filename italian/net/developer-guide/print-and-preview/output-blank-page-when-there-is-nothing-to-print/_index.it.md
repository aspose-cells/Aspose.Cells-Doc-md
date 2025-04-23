---
title: Genera una pagina vuota quando non c è nulla da stampare
type: docs
weight: 90
url: /it/net/output-blank-page-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Se il foglio è vuoto, allora Aspose.Cells non stamperà nulla quando si esporta il foglio di lavoro in un'immagine. È possibile modificare questo comportamento utilizzando la proprietà [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint). Quando la imposti su **true**, stamperà la pagina vuota.

## **Output Pagina Bianca quando non c'è Nulla da Stampare**

Il seguente codice di esempio crea il workbook vuoto che ha un foglio di lavoro vuoto e rende il foglio di lavoro vuoto in un'immagine dopo aver impostato la proprietà [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) come **true**. Di conseguenza, genera la pagina vuota poiché non c'è nulla da stampare, come puoi vedere nell'immagine sotto.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
