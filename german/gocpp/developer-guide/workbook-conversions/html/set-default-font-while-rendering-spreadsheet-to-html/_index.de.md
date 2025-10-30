---
title: Setze die Standardschriftart beim Rendern von Tabellen in HTML mit Golang via C++
linktitle: Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest
type: docs
weight: 370
url: /de/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Lernen Sie, wie man die Standard Schriftart beim Rendern von Tabellen nach HTML mit Aspose.Cells for C++ festlegt.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, die Standardschriftart beim Rendern einer Tabelle nach HTML festzulegen. Verwenden Sie dazu [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/). Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabelle ungültige oder nicht vorhandene Schriftarten haben. Diese Zellen werden dann in einer mit [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) festgelegten Schriftart gerendert.

{{% /alert %}}

## Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in HTML

Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt einen Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt die Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Dann speichert er die Arbeitsmappe in HTML, indem er verschiedene Standardschriftart-Namen wie Courier New, Arial, Times New Roman usw. festlegt.

Das Screenshot zeigt die Auswirkung der Einstellung verschiedener Standard-Schriftartnamen über die Eigenschaft [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Der Code generiert die [Ausgabe-HTML-Datei mit Courier New](5115516), die [Ausgabe-HTML mit Arial](5115518) und die [Ausgabe-HTML-Datei mit Times New Roman](5115517).

## Beispielcode

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
