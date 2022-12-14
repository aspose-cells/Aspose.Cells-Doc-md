---
title: Disattiva l'esportazione degli script dei frame e delle proprietà del documento
type: docs
weight: 310
url: /it/net/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}}

Aspose.Cells esporta gli script dei frame e le proprietà dei documenti durante la conversione di una cartella di lavoro in HTML. La versione 8.6.0 di Aspose.Cells for .NET introduce un'opzione che consente facoltativamente di disabilitare l'esportazione degli script dei frame e delle proprietà dei documenti. Utilizzare la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties per disabilitare l'esportazione.

{{% /alert %}}

## **Disattiva l'esportazione degli script dei frame e delle proprietà dei documenti**

Il seguente codice di esempio consente di disabilitare l'esportazione di script di frame e proprietà del documento. Dopo aver convertito una cartella di lavoro in HTML, il file di output non conterrà script di frame e proprietà del documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
