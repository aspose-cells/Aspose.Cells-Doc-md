---
title: Zugriff und Aktualisierung der Teile von Rich Text einer Zelle
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Lernen Sie, wie Sie über die Aspose.Cells for .NET API auf Teile des Rich Texts einer Zelle zugreifen und diese aktualisieren können.
keywords: Zugriff und Aktualisierung des Rich Texts einer Zelle, Abrufen des Rich Texts einer Zelle, Rich Text einer Zelle bearbeiten, Rich Text einer Zelle abrufen, Rich Text einer Zelle aktualisieren, Rich Text einer Zelle ändern
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie auf die Teile des Rich-Texts einer Zelle zugreifen und diese aktualisieren. Hierfür können Sie die [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) und [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methoden verwenden. Diese Methoden geben ein Array von [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)-Objekten zurück und akzeptieren dieses, mit dem Sie verschiedene Eigenschaften der Schriftart wie Schriftartname, Schriftfarbe, Fettgedrucktheit usw. ändern können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code zeigt die Verwendung der [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)- und [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)-Methode mit der [Quelldatei Excel](5112369.xlsx), die Sie über den bereitgestellten Link herunterladen können. Die Quelldatei Excel enthält einen Rich-Text in der Zelle A1. Es hat 3 Teile, und jeder Teil hat eine andere Schriftart. Der folgende Codeschnipsel greift auf diese Teile zu und aktualisiert den ersten Teil mit einem neuen Schriftartnamen. Schließlich speichert es die Arbeitsmappe als [Ausgabedatei Excel](5112366.xlsx). Wenn Sie es öffnen, werden Sie feststellen, dass sich die Schriftart des ersten Teils des Textes zu **"Arial"** geändert hat.

### C#-Code zum Zugriff und zur Aktualisierung der Teile des Rich Texts einer Zelle

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielscodes unter Verwendung der [Quelldatei Excel](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

{{< app/cells/assistant language="csharp" >}}
