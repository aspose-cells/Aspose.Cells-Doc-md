---
title: Escludere Stili Non Utilizzati durante la conversione da Excel a HTML
type: docs
weight: 30
url: /it/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**
I file di Microsoft Excel possono contenere molti stili non utilizzati. Quando questi file vengono esportati nel formato HTML, gli stili non utilizzati verranno esportati. Ciò comporta un aumento delle dimensioni dell'HTML di output. Aspose.Cells for Python via Java supporta l'esclusione di questi stili durante la conversione del file Excel in HTML. A tale scopo, l'API fornisce la proprietà [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles). Impostando il valore della proprietà [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) su **True** verranno esclusi tutti gli stili non utilizzati dall'HTML di output.

La schermata seguente mostra gli stili non utilizzati nel file HTML che verranno rimossi impostando il valore della proprietà [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) su **True**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Il codice di esempio seguente dimostra la rimozione degli stili non utilizzati durante la conversione da Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
