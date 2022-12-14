---
title: Esporta uno stile del bordo simile quando lo stile del bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Possibili scenari di utilizzo**

Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando converti un file Excel di questo tipo in HTML utilizzando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può anche supportare la visualizzazione di tali bordi con[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) proprietà. Si prega di impostare il suo valore come**VERO**e anche i bordi non supportati verranno esportati in un file HTML.

## **Esporta uno stile del bordo simile quando lo stile del bordo non è supportato dai browser web**

Il codice di esempio seguente carica il file[esempio di file Excel](64716806.xlsx) che contiene alcuni bordi non supportati come mostrato nello screenshot seguente. Lo screenshot illustra ulteriormente l'effetto di[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)proprietà all'interno del[output HTML](64716804.zip).

![cose da fare:immagine_alt_testo](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
