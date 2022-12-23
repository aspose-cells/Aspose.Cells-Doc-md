---
title: Disattiva l'esportazione degli script dei frame e delle proprietà del documento
type: docs
weight: 410
url: /it/java/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}} 

 Aspose.Cells esporta gli script dei frame e le proprietà del documento durante la conversione di una cartella di lavoro in HTML. La versione 8.6.0 di Aspose.Cells for Java introduce un'opzione che consente facoltativamente di disabilitare l'esportazione degli script dei frame e delle proprietà del documento. Si prega di utilizzare il[HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) property per disabilitare l'esportazione.

{{% /alert %}} 
## **Disattiva l'esportazione degli script dei frame e delle proprietà dei documenti**
Il seguente codice di esempio consente di disabilitare l'esportazione di script di frame e proprietà del documento. Dopo aver convertito una cartella di lavoro in HTML, il file di output non conterrà script di frame e proprietà del documento.

Ecco un codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
