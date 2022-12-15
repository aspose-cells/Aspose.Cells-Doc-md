---
title: Excel con stile del bordo non supportato in HTML
type: docs
weight: 80
url: /it/python-java/excel-with-unsupported-border-style-to/
---
## **Excel con stile del bordo non supportato in HTML**
Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando tali file vengono convertiti in HTML utilizzando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells for Python via Java supporta la visualizzazione di bordi simili con[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)proprietà. Puoi impostare il valore di[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) proprietà a**Vero** per esportare bordi non supportati.

Il codice di esempio seguente carica il file[esempio di file Excel](sampleExportSimilarBorderStyle.xlsx)che contiene alcuni bordi non supportati come mostrato nello screenshot seguente. Lo screenshot illustra ulteriormente l'effetto di[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)proprietà all'interno del[output HTML](outputExportSimilarBorderStyle.zip).

![cose da fare:immagine_alt_testo](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
