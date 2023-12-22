---
title: Ändern Sie das Format einer Zelle
description: So verwenden Sie die Bibliothek Aspose.Cells in C#, um die Formatierung von Zellen zu ändern, einschließlich Schriftart, Farbe, Rahmen usw. Durch Anpassen dieser Eigenschaften haben Sie mehr Kontrolle darüber, wie Zellen aussehen und angezeigt werden.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /de/net/how-to-change-format-of-cell/
---
##  **Mögliche Nutzungsszenarien**
Wenn Sie bestimmte Daten hervorheben möchten, können Sie den Stil der Zellen ändern.

##  **So ändern Sie das Format einer Zelle in Excel**

Um das Format einer einzelnen Zelle in Excel zu ändern, gehen Sie folgendermaßen vor:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die die Zelle enthält, die Sie formatieren möchten.

2. Suchen Sie die Zelle, die Sie formatieren möchten.

3. Klicken Sie mit der rechten Maustaste auf die Zelle und wählen Sie im Kontextmenü „Cells formatieren“. Alternativ können Sie die Zelle auswählen und im Excel-Menüband zur Registerkarte „Startseite“ wechseln, in der Gruppe „Cells“ auf das Dropdown-Menü „Format“ klicken und „Cells formatieren“ auswählen.

4. Das Dialogfeld „Cells formatieren“ wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf die ausgewählte Zelle angewendet werden sollen. Sie können beispielsweise den Schriftstil, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Nachdem Sie die gewünschten Formatierungsänderungen vorgenommen haben, klicken Sie auf die Schaltfläche „OK“, um die Formatierung auf die ausgewählte Zelle anzuwenden.


##  **So ändern Sie das Format einer Zelle mit C#**

Um das Format einer Zelle mit Aspose.Cells zu ändern, können Sie die folgenden Methoden verwenden:
1. [Cell.SetStyle(Stilstil)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Stilstil, Bool ExplicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Stilstil, StyleFlag-Flagge)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und erhalten zwei Zellen („A2“ und „B3“). Anschließend ermitteln wir den Stil der Zelle, legen verschiedene Formatierungsoptionen fest (z. B. Schriftfarbe, Fettdruck) und ändern das Format der Zelle. Abschließend speichern wir die Arbeitsmappe in einer neuen Datei.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
