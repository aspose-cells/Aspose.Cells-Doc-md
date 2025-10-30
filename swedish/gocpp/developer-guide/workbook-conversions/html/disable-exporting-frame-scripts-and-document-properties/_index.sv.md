---
title: Inaktivera export av Frame Scripts och Dokumentegenskaper med Golang via C++
type: docs
weight: 310
url: /sv/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Inaktivera export av frame skript och dokumentegenskaper med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells exporterar frame scripts och dokumentegenskaper när en arbetsbok konverteras till HTML. Version 8.6.0 av Aspose.Cells for C++ introducerar ett alternativ som tillåter att du valfritt inaktiverar export av frame scripts och dokumentegenskaper. Använd egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties för att inaktivera exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
