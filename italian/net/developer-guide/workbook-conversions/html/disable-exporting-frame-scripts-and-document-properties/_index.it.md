---
title: Disabilita l Esportazione degli Script Frame e delle Proprietà del Documento
type: docs
weight: 310
url: /it/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells esporta script frame e proprietà del documento durante la conversione di un documento Excel in HTML. La versione 8.6.0 di Aspose.Cells for .NET introduce un'opzione che consente di disabilitare facoltativamente l'esportazione di script frame e proprietà del documento. Si prega di utilizzare la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties per disabilitare l'esportazione.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
