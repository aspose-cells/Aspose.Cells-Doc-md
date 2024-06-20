---
title: Inaktivera Exportering av Ramskript och Dokumentegenskaper
type: docs
weight: 310
url: /sv/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells exporterar ramscript och dokumentegenskaper vid konvertering av en arbetsbok till HTML. Version 8.6.0 av Aspose.Cells for .NET introducerar ett alternativ som tillåter dig att valfritt inaktivera export av ramscript och dokumentegenskaper. Använd egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties för att inaktivera exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
