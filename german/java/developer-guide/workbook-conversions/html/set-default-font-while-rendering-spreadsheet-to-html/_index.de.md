---
title: Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest
type: docs
weight: 830
url: /de/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells ermöglicht es Ihnen, die Standardschriftart beim Rendern der Tabellenkalkulation in HTML festzulegen. Verwenden Sie dazu die [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) zu diesem Zweck. Diese Eigenschaft ist nützlich, wenn in einer Tabellenkalkulation Zellen mit ungültigen oder nicht vorhandenen Schriftarten vorhanden sind. Dann werden diese Zellen in einer mit der [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) Eigenschaft angegebenen Schriftart gerendert.

{{% /alert %}} 
## **Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest**
Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt einen Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt die Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Dann speichert er die Arbeitsmappe in HTML, indem er verschiedene Standardschriftart-Namen wie Courier New, Arial, Times New Roman usw. festlegt.

Der Screenshot zeigt die Auswirkung des Festlegens verschiedener Standardschriftart-Namen über die [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) Eigenschaft.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Der Code generiert die [Ausgabe HTML-Datei mit Courier New](5472568), die [Ausgabe HTML-Datei mit Arial](5472567) und die [Ausgabe HTML-Datei mit Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
