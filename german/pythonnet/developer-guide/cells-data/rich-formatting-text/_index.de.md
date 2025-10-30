---
title: Zugriff und Aktualisierung der Teile von Rich Text einer Zelle
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Erfahren Sie, wie Sie über die Aspose.Cells für Python via .NET API auf die Teile des Rich Texts einer Zelle zugreifen und diese aktualisieren können.
keywords: Python Excel Bibliothek, Zugriff und Aktualisierung von Rich Text einer Zelle in Python, Abrufen von Rich Text einer Zelle in Python, Bearbeiten von Rich Text einer Zelle in Python, Zugriff auf Rich Text einer Zelle in Python, Aktualisierung von Rich Text einer Zelle in Python, Änderung von Rich Text einer Zelle in Python.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ermöglicht es Ihnen, auf die Teile des Rich Texts der Zelle zuzugreifen und diese zu aktualisieren. Hierfür können Sie die [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#)- und [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list)-Methoden verwenden. Diese Methoden geben ein Array von [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)-Objekten zurück und akzeptieren dieses, mit dem Sie verschiedene Eigenschaften der Schrift wie Schriftart, Schriftfarbe, Fettdruck usw. zugreifen und aktualisieren können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code zeigt die Verwendung der [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#)- und [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list)-Methoden anhand der [Quelldatei Excel](5112369.xlsx), die Sie über den bereitgestellten Link herunterladen können. Die Quelldatei Excel enthält einen Rich-Text in der Zelle A1. Es hat 3 Teile, und jeder Teil hat eine andere Schriftart. Der folgende Codeausschnitt greift auf diese Teile zu und aktualisiert den ersten Teil mit einer neuen Schriftart. Abschließend speichert er die Arbeitsmappe als [Ausgabedatei Excel](5112366.xlsx). Wenn Sie es öffnen, werden Sie feststellen, dass die Schriftart des ersten Teils des Textes auf **"Arial"** geändert wurde.

### C#-Code zum Zugriff und zur Aktualisierung der Teile des Rich Texts einer Zelle

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
