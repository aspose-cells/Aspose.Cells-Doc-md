---
title: Disabilita l Esportazione degli Script Frame e delle Proprietà del Documento
type: docs
weight: 410
url: /it/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells esporta gli script frame e le proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells for Java introduce un'opzione che ti consente di disabilitare facoltativamente l'esportazione degli script frame e delle proprietà del documento. Si prega di utilizzare la proprietà [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) per disabilitare l'esportazione.

{{% /alert %}} 
## **Disabilita l'esportazione degli script frame e delle proprietà del documento**
Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

Ecco un codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
{{< app/cells/assistant language="java" >}}
