---
title: Inaktivera export av ramskript och dokumentegenskaper
type: docs
weight: 310
url: /sv/net/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}}

Aspose.Cells exporterar ramskript och dokumentegenskaper samtidigt som en arbetsbok konverteras till HTML. 8.6.0-versionen av Aspose.Cells for .NET introducerar ett alternativ som låter dig valfritt inaktivera export av ramskript och dokumentegenskaper. Använd egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties för att inaktivera exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod låter dig inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript och dokumentegenskaper.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
