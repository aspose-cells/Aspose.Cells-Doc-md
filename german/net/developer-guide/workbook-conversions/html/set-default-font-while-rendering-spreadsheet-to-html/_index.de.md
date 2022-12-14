---
title: Legen Sie die Standardschriftart fest, während die Tabelle in HTML gerendert wird
type: docs
weight: 370
url: /de/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells ermöglicht es Ihnen, die Standardschriftart festzulegen, während die Tabelle in HTML gerendert wird. Bitte verwenden Sie die[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) für diesen Zweck. Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabelle ungültige oder nicht vorhandene Schriftarten enthalten. Dann werden diese Zellen in einer mit angegebenen Schriftart gerendert[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) Eigentum.

{{% /alert %}}

## Legen Sie die Standardschriftart fest, während die Tabelle in HTML gerendert wird

Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt seine Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Anschließend wird die Arbeitsmappe in HTML gespeichert, indem verschiedene Standardschriftnamen wie Courier New, Arial, Times New Roman usw. festgelegt werden.

 Der Screenshot zeigt den Effekt des Festlegens verschiedener Standardschriftnamen über[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)Eigentum.

![todo: Bild_alt_Text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Der Code generiert die[HTML-Datei mit Courier New ausgeben](5115516) , das[Ausgabe von HTML mit Arial](5115518) , und die[HTML-Datei mit Times New Roman ausgeben](5115517).

## Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
