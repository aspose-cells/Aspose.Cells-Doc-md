---
title: Disabilita l Esportazione degli Script Frame e delle Proprietà del Documento
type: docs
weight: 310
url: /it/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET esporta script di frame e proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells per Python via .NET introduce un'opzione che permette di disattivare opzionalmente l'esportazione di script di frame e proprietà del documento. Per favore, utilizza la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties per disattivare l'esportazione.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
