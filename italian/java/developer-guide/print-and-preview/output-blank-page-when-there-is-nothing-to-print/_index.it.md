---
title: Genera una pagina vuota quando non c è nulla da stampare
type: docs
weight: 80
url: /it/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Se il foglio è vuoto, allora Aspose.Cells non stamperà nulla quando si esporta il foglio di lavoro in immagine. Puoi cambiare questo comportamento utilizzando la proprietà [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint). Quando imposti [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) a **true**, stamperà la pagina vuota.

## **Output Pagina Bianca quando non c'è Nulla da Stampare**

Il seguente codice di esempio crea il libro di lavoro vuoto che ha un foglio di lavoro vuoto e rende il foglio di lavoro vuoto in un'immagine dopo aver impostato la proprietà [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) come **true**. Di conseguenza, genera la pagina vuota in quanto non c'è nulla da stampare che puoi vedere di seguito.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
