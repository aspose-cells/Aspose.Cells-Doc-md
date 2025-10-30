---
title: Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web con Golang via C++
linktitle: Esportare uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Impara come esportare stili di bordo simili quando non supportati dai browser web usando Aspose.Cells con Golang via C++.
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel supporta alcuni tipi di bordi a tratteggio che non sono supportati dai browser web. Quando converti un file Excel di questo tipo in HTML usando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può anche supportare la visualizzazione di tali bordi usando la proprietà [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/). Imposta il suo valore su **true** e i bordi non supportati verranno esportati anche nel file HTML.

## **Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web**

Il seguente esempio di codice carica il [file Excel di esempio](64716806.xlsx) che contiene alcuni bordi non supportati come mostrato nella schermata successiva. La schermata illustra inoltre l'effetto della proprietà [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) all'interno dell'[output HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
