---
title: Excel in HTML mit Tooltip konvertieren
type: docs
weight: 200
url: /de/net/convert-excel-to-html-with-tooltip/
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text in dem generierten HTML abgeschnitten ist und Sie den vollständigen Text als Tooltip bei einem Hover-Ereignis anzeigen möchten. Aspose.Cells unterstützt dies durch Bereitstellung der [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)-Eigenschaft. Wenn die [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)-Eigenschaft auf **true** gesetzt wird, wird der vollständige Text als Tooltip im generierten HTML hinzugefügt.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Das folgende Beispielskript lädt die [Quell-Excel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit dem Tooltip.

Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
