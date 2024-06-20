---
title: Esportare uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel supporta alcuni tipi di bordi tratteggiati non supportati dai browser Web. Quando si converte un file Excel di questo tipo in HTML usando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può supportare anche la visualizzazione di bordi simili con la proprietà [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle). Si prega di impostare il suo valore su **true** e i bordi non supportati verranno esportati anche nel file HTML.

## **Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web**

Il codice di esempio seguente carica il [file Excel di esempio](64716832.xlsx) che contiene alcuni bordi non supportati come mostrato nella seguente schermata. La schermata illustra inoltre l'effetto della proprietà [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) all'interno dell'[HTML di output](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
