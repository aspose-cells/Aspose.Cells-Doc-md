---
title: Inaktivera Exportering av Ramskript och Dokumentegenskaper
type: docs
weight: 310
url: /sv/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET exporterar ram-skript och dokumentegenskaper när en arbetsbok konverteras till HTML. Version 8.6.0 av Aspose.Cells för Python via .NET introducerar ett alternativ som tillåter dig att tillfälligt inaktivera export av ram-skript och dokumentegenskaper. Använd HtmlSaveOptions.ExportFrameScriptsAndProperties-egenskapen för att inaktivera exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
