---
title: Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie
linktitle: Text mit reichhaltiger Formatierung
type: docs
weight: 40
url: /de/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Erfahren Sie, wie Sie auf die Rich-Text-Teile von Cell über Aspose.Cells for .NET API zugreifen und diese aktualisieren.
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells ermöglicht Ihnen den Zugriff auf und die Aktualisierung der Teile des Rich-Textes der Zelle. Zu diesem Zweck können Sie verwenden[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) Und[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methoden. Diese Methoden geben das Array von zurück und akzeptieren es[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)Objekte, mit denen Sie auf verschiedene Eigenschaften der Schriftart zugreifen und diese aktualisieren können, z. B. den Namen der Schriftart, die Schriftfarbe, die Fettschrift usw.

{{% /alert %}}

##  **Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie**

 Der folgende Code demonstriert die Verwendung von[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) Und[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methode mit der[Quell-Excel-Datei](5112369.xlsx) die Sie über den bereitgestellten Link herunterladen können. Die Excel-Quelldatei enthält einen Rich-Text in der Zelle A1. Es besteht aus 3 Teilen und jeder Teil hat eine andere Schriftart. Der folgende Codeausschnitt greift auf diese Teile zu und aktualisiert den ersten Teil mit einem neuen Schriftartnamen. Schließlich wird die Arbeitsmappe als gespeichert[Excel-Datei ausgeben](5112366.xlsx). Wenn Sie es öffnen, werden Sie feststellen, dass die Schriftart des ersten Teils des Textes in *„Arial“** geändert wurde.

###  C#-Code für den Zugriff und die Aktualisierung der Rich-Text-Teile von Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Durch den Beispielcode generierte Konsolenausgabe

 Hier ist die Konsolenausgabe des obigen Beispielcodes unter Verwendung von[Quell-Excel-Datei](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

