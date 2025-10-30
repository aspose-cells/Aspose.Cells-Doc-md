---
title: Zugriff und Aktualisierung der Teile von Rich Text einer Zelle
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lernen Sie, wie man über die API Aspose.Cells for Node.js via C++ auf und aktualisiert die Abschnitte des Rich Texts in einer Zelle zugreift.
keywords: Zugriff und Aktualisierung des Rich Texts einer Zelle, Abrufen des Rich Texts einer Zelle, Rich Text einer Zelle bearbeiten, Rich Text einer Zelle abrufen, Rich Text einer Zelle aktualisieren, Rich Text einer Zelle ändern
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ ermöglicht den Zugriff auf und die Aktualisierung der Abschnitte des Rich-Texts einer Zelle. Zu diesem Zweck können Sie die Methoden [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) und [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) verwenden. Diese Methoden geben und akzeptieren ein Array von [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-Objekten, mit denen Sie verschiedene Eigenschaften der Schriftart wie Schriftname, Schriftfarbe, Fett usw. zugreifen und aktualisieren können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code demonstriert die Verwendung der Methoden [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) und [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) mit der Quelldatei im Excel-Format, die Sie über den bereitgestellten Link herunterladen können. Die Quelldatei enthält in Zelle A1 einen Rich-Text mit 3 Abschnitten, die jeweils eine andere Schriftart haben. Das folgende Code-Snippet greift auf diese Abschnitte zu und aktualisiert den ersten Abschnitt mit einem neuen Schriftartnamen. Schließlich speichert es die Arbeitsmappe als Ausgabedatei. Beim Öffnen wird die Schriftart des ersten Textabschnitts auf **"Arial"** geändert.

### Node.js-Code zum Zugriff und zur Aktualisierung der Abschnitte des Rich-Texts in einer Zelle

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

{{< app/cells/assistant language="nodejs-cpp" >}}
