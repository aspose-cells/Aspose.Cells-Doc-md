---
title: Excel in HTML mit Tooltip konvertieren
type: docs
weight: 150
url: /de/java/convert-excel-to-html-with-tooltip/
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text im generierten HTML abgeschnitten ist und Sie den vollständigen Text als Tooltip beim Hover-Ereignis anzeigen möchten. Aspose.Cells unterstützt dies, indem es die [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)-Eigenschaft bereitstellt. Durch Einstellen der [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)-Eigenschaft auf **true** wird der vollständige Text als Tooltip im generierten HTML hinzugefügt.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Der folgende Codeausschnitt lädt die [Quell-Excel-Datei](AddTooltipToHtmlSample.xlsx) und generiert die [Ausgabe-HTML-Datei](AddTooltipToHtmlSample_out.zip) mit dem Tooltip.

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
{{< app/cells/assistant language="java" >}}
