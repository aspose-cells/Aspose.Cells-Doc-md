---
title: Ändern Sie das Format einer Zelle
description: So verwenden Sie die Aspose.Cells für Python via .NET Bibliothek, um die Formatierung von Zellen einschließlich Schriftart, Farbe, Rahmen usw. zu ändern. Durch Anpassen dieser Eigenschaften haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells für Python via .NET Bibliothek, Zellenformatierung, Python, Schriftart, Farbe, Rahmen
type: docs
weight: 20
url: /de/python-net/how-to-change-format-of-cell/
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


## **So ändern Sie das Format einer Zelle mit C#**

Um das Format einer Zelle mit Aspose.Cells für Python via .NET zu ändern, können Sie die folgenden Methoden verwenden:
1. [Cell.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style)
2. [Cell.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-bool)
3. [Cell.set_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-aspose.cells.StyleFlag)


## **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und erhalten zwei Zellen ("A2" und "B3"). Dann holen wir uns den Stil der Zelle, setzen verschiedene Formatierungsoptionen (z.B. Schriftfarbe, fett) und ändern das Format der Zelle. Schließlich speichern wir die Arbeitsmappe in einer neuen Datei.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-change-format.py" >}}

{{< app/cells/assistant language="python-net" >}}
