---
title: Inaktivera Exportering av Ramskript och Dokumentegenskaper
type: docs
weight: 410
url: /sv/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells exporterar ramskript och dokumentegenskaper vid konvertering av en arbetsbok till HTML. Version 8.6.0 av Aspose.Cells for Java inför ett alternativ som låter dig valfritt inaktivera exportering av ramskript och dokumentegenskaper. Vänligen använd egenskapen [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) för att inaktivera exporten.

{{% /alert %}} 
## **Inaktivera export av ramskript och dokumentegenskaper**
Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

Här är ett exempel på kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
{{< app/cells/assistant language="java" >}}
