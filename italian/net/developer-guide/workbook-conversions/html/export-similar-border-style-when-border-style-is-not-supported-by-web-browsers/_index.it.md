---
title: Esportare uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando converti tale file di Excel in HTML utilizzando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può anche supportare la visualizzazione di tali bordi con la proprietà [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle). Imposta il suo valore su **true** e i bordi non supportati verranno esportati anche nel file HTML.

## **Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web**

Il codice di esempio seguente carica il [file di Excel di esempio](64716806.xlsx) che contiene alcuni bordi non supportati come mostrato nella seguente schermata. La schermata illustra ulteriormente l'effetto della proprietà [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) all'interno dell'HTML [generato](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
