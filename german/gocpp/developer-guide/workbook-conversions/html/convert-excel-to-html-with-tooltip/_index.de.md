---
title: Excel in HTML mit Tooltip konvertieren mit C++
linktitle: Excel in HTML mit Tooltip konvertieren
type: docs
weight: 200
url: /de/go-cpp/convert-excel-to-html-with-tooltip/
description: Excel in HTML konvertieren, während Tooltips mit Aspose.Cells und C++ hinzugefügt werden.
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text im generierten HTML abgeschnitten ist und Sie möchten den vollständigen Text als Tooltip beim Hover-Ereignis anzeigen. Aspose.Cells unterstützt dies durch Bereitstellung der [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/)-Eigenschaft. Das Setzen der [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/)-Eigenschaft auf **true** fügt den vollständigen Text als Tooltip im generierten HTML hinzu.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Das folgende Code-Beispiel lädt die [Quellexcel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit Tooltip.

Beispielcode

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
