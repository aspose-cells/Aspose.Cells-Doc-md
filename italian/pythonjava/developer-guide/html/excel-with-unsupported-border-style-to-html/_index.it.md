---
title: Excel con stile di bordo non supportato in HTML
type: docs
weight: 80
url: /it/python-java/excel-with-unsupported-border-style-to/
---

## **Excel con stile di bordo non supportato in HTML**
Microsoft Excel supporta alcuni tipi di bordi tratteggiati non supportati dai browser Web. Quando tali file vengono convertiti in HTML utilizzando Aspose.Cells, quei bordi vengono rimossi. Tuttavia, Aspose.Cells for Python via Java supporta la visualizzazione di bordi simili con la proprietà [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). È possibile impostare il valore della proprietà [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) su **True** per esportare i bordi non supportati.

Il codice di esempio seguente carica il [file Excel di esempio](sampleExportSimilarBorderStyle.xlsx) che contiene alcuni bordi non supportati come mostrato nella schermata seguente. La schermata illustra ulteriormente l'effetto della proprietà [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) all'interno dell'[HTML di output](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
