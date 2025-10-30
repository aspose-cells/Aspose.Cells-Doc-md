---
title: Esportare uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando converti un tale file Excel in HTML usando Aspose.Cells per Python via .NET, tali bordi vengono rimossi. Tuttavia, Aspose.Cells per Python via .NET può anche supportare la visualizzazione di tali bordi con la proprietà [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style). Impostane il valore su **true** e i bordi non supportati verranno anch'essi esportati nel file HTML.

## **Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web**

Il codice di esempio seguente carica il [file di Excel di esempio](64716806.xlsx) che contiene alcuni bordi non supportati come mostrato nella seguente schermata. La schermata illustra ulteriormente l'effetto della proprietà [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) all'interno dell'HTML [generato](64716804.zip).

![todo:image_alt_text](1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
