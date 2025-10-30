---
title: Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest
type: docs
weight: 370
url: /de/python-net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie beim Rendern von Tabellenkalkulationen in HTML die Standardschriftart festlegen. Verwenden Sie hierfür [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name). Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabellenkalkulation ungültige oder nicht vorhandene Schriftarten aufweisen. Dann werden diese Zellen in einer Schriftart gerendert, die mit der Eigenschaft [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) festgelegt ist.

{{% /alert %}}

## Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in HTML

Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt einen Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt die Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Dann speichert er die Arbeitsmappe in HTML, indem er verschiedene Standardschriftart-Namen wie Courier New, Arial, Times New Roman usw. festlegt.

Der Screenshot zeigt die Auswirkung des Festlegens verschiedener Standardschriftartnamen über die [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name)-Eigenschaft.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Der Code generiert die [Ausgabe-HTML-Datei mit Courier New](5115516), die [Ausgabe-HTML mit Arial](5115518) und die [Ausgabe-HTML-Datei mit Times New Roman](5115517).

## Beispielcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetDefaultFontWhileRendering-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
