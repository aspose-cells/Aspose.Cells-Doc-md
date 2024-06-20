---
title: Excel in HTML mit Tooltip konvertieren
type: docs
weight: 200
url: /de/python-net/convert-excel-to-html-with-tooltip/
description: Dieses Thema zeigt, wie Sie Excel mithilfe von Aspose.Cells for Python via NET mit Tooltip in HTML konvertieren können.
keywords: Python Excel in HTML mit Tooltip konvertieren, Python Excel in HTML mit Tooltip konvertieren via NET, Python via NET Excel in HTML mit Tooltip, Python Arbeitsmappe in HTML mit Tooltip.
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text in dem generierten HTML abgeschnitten ist und Sie den vollständigen Text als Tooltip bei einem Hover-Ereignis anzeigen möchten. Aspose.Cells unterstützt dies durch Bereitstellung der [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)-Eigenschaft. Wenn die [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)-Eigenschaft auf **true** gesetzt wird, wird der vollständige Text als Tooltip im generierten HTML hinzugefügt.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Das folgende Beispielskript lädt die [Quell-Excel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit dem Tooltip.

Beispielcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
