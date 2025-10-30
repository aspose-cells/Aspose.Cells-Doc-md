---
title: Ändern Sie das Format einer Zelle mit Golang via C++
linktitle: Ändern Sie das Format einer Zelle
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um die Formatierung von Zellen zu ändern, einschließlich Schriftart, Farbe, Rahmen usw. Durch Anpassen dieser Eigenschaften haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellenformatierung, C++, Schriftart, Farbe, Rahmen
type: docs
weight: 20
url: /de/go-cpp/how-to-change-format-of-cell/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie bestimmte Daten hervorheben möchten, können Sie den Stil der Zellen ändern.

## **Wie man das Format einer Zelle in Excel ändert**

Um das Format einer einzelnen Zelle in Excel zu ändern, befolgen Sie diese Schritte:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die die Zelle enthält, die Sie formatieren möchten.

2. Suchen Sie die Zelle, die Sie formatieren möchten.

3. Klicken Sie mit der rechten Maustaste auf die Zelle und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie die Zelle auswählen, zum Register Start in der Excel-Befehlsleiste gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.

4. Das Dialogfeld "Zellen formatieren" wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf die ausgewählte Zelle angewendet werden sollen. Sie können z.B. die Schriftart, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Klicken Sie nach dem Anwenden der gewünschten Formatierungsänderungen auf die Schaltfläche "OK", um die Formatierung auf die ausgewählte Zelle anzuwenden.

## **Wie ändert man das Format einer Zelle mit C++**

Um das Format einer Zelle mit Aspose.Cells zu ändern, können Sie die folgenden Methoden verwenden:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)

## **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und erhalten zwei Zellen ("A2" und "B3"). Dann holen wir uns den Stil der Zelle, setzen verschiedene Formatierungsoptionen (z.B. Schriftfarbe, fett) und ändern das Format der Zelle. Schließlich speichern wir die Arbeitsmappe in einer neuen Datei.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeFormat.go" >}}
