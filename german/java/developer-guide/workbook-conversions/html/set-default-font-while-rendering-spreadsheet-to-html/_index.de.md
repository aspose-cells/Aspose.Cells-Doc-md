---
title: Legen Sie die Standardschriftart fest, während die Tabelle in HTML gerendert wird
type: docs
weight: 830
url: /de/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells ermöglicht es Ihnen, die Standardschriftart festzulegen, während die Tabelle in HTML gerendert wird. Bitte verwenden Sie die[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)für diesen Zweck. Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabelle ungültige oder nicht vorhandene Schriftarten enthalten. Dann werden diese Zellen in einer mit angegebenen Schriftart gerendert[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) Eigentum.

{{% /alert %}} 
## **Legen Sie die Standardschriftart fest, während die Tabelle in HTML gerendert wird**
Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt seine Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Anschließend wird die Arbeitsmappe in HTML gespeichert, indem verschiedene Standardschriftnamen wie Courier New, Arial, Times New Roman usw. festgelegt werden.

 Der Screenshot zeigt den Effekt des Festlegens verschiedener Standardschriftnamen über[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)Eigentum.

![todo: Bild_alt_Text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Der Code generiert die[HTML-Datei mit Courier New ausgeben](5472568) , das[Ausgabe von HTML mit Arial](5472567) und die[HTML-Datei mit Times New Roman ausgeben](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
