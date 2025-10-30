---
title: Ändern Sie das Format einer Zelle
linktitle: Ändern Sie das Format einer Zelle
description: So verwenden Sie die Aspose.Cells Bibliothek in Node.js via C++, um die Formatierung von Zellen einschließlich Schriftart, Farbe, Rand usw. zu ändern. Durch Anpassen dieser Eigenschaften haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellenformatierung, Node.js via C++, Schriftart, Farbe, Rand
type: docs
weight: 20
url: /de/nodejs-cpp/how-to-change-format-of-cell/
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


## **So ändern Sie das Format einer Zelle mit Node.js**

Um das Format einer Zelle mit Aspose.Cells zu ändern, können Sie die folgenden Methoden verwenden:
1. [Cell.setStyle(Style)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)
2. [Cell.setStyle(Style, explicitFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-boolean-)
3. [Cell.setStyle(Style, StyleFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-styleflag-)


## **Beispielcode**
In diesem Beispiel erstellen wir ein Excel-Arbeitsbuch, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und holen zwei Zellen («A2» und «B3»). Dann holen wir den Stil der Zelle, setzen verschiedene Formatierungsoptionen (z. B. Schriftfarbe, fett) und ändern das Format der Zelle. Schließlich speichern wir das Arbeitsbuch in eine neue Datei.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ChangeFormat.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
