---
title: Disabilita l esportazione di script di frame e proprietà del documento con Golang via C++
type: docs
weight: 310
url: /it/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Disabilita l esportazione di script di frame e proprietà del documento usando Aspose.Cells con Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells esporta script di frame e proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells for C++ introduce un'opzione che ti permette di disattivare opzionalmente l'esportazione di script di frame e proprietà del documento. Usa la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties per disattivare l'esportazione.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
