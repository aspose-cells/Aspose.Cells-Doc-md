---
title: Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie
linktitle: Rich-Formatierungstext
type: docs
weight: 40
url: /de/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie auf die Teile des Rich-Texts der Zelle zugreifen und diese aktualisieren. Zu diesem Zweck können Sie verwenden[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) und[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methoden. Diese Methoden werden das Array von zurückgeben und akzeptieren[**Schrifteinstellung**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)Objekte, mit denen Sie auf verschiedene Eigenschaften von Schriftarten wie Schriftartname, Schriftfarbe, Fettschrift usw. zugreifen und diese aktualisieren können.

{{% /alert %}}

## **Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie**

 Der folgende Code demonstriert die Verwendung von[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) und[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methode mit der[Excel-Quelldatei](5112369.xlsx)die Sie über den angegebenen Link herunterladen können. Die Excel-Quelldatei hat einen Rich-Text in der Zelle A1. Es hat 3 Teile und jeder Teil hat eine andere Schriftart. Das folgende Code-Snippet greift auf diese Teile zu und aktualisiert den ersten Teil mit einem neuen Schriftartnamen. Schließlich speichert es die Arbeitsmappe als[Excel-Datei ausgeben](5112366.xlsx) . Wenn Sie es öffnen, werden Sie feststellen, dass sich die Schriftart des ersten Teils des Textes geändert hat**"Arial"**.

### C#-Code, um auf die Teile von Rich Text von Cell zuzugreifen und sie zu aktualisieren

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Vom Beispielcode generierte Konsolenausgabe

 Hier ist die Konsolenausgabe des obigen Beispielcodes mit der[Excel-Quelldatei](5112369.xlsx).

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

