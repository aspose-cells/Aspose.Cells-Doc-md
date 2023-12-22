---
title: Formatbereiche
type: docs
weight: 105
url: /de/net/how-to-format-a-range/
---
##  **Mögliche Nutzungsszenarien**
Wenn Sie einen Stil auf einen Bereich anwenden müssen, können Sie die Bereichsformatierung verwenden.

##  **So formatieren Sie einen Bereich in Excel**

Um einen Zellbereich in Excel zu formatieren, können Sie die integrierten Formatierungsoptionen von Excel verwenden. So können Sie einen Zellbereich direkt in Excel formatieren:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die den Bereich enthält, den Sie formatieren möchten.

2. Wählen Sie den Zellbereich aus, den Sie formatieren möchten. Sie können klicken und ziehen, um den Bereich auszuwählen, oder Sie können Tastaturkürzel wie Umschalt + Pfeiltasten verwenden, um die Auswahl zu erweitern.

3. Sobald der Bereich ausgewählt ist, klicken Sie mit der rechten Maustaste auf den ausgewählten Bereich und wählen Sie „Cells formatieren“ aus dem Kontextmenü. Alternativ können Sie im Excel-Menüband zur Registerkarte „Startseite“ gehen, in der Gruppe „Cells“ auf das Dropdown-Menü „Format“ klicken und „Cells formatieren“ auswählen.

4. Das Dialogfeld „Cells formatieren“ wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf den ausgewählten Bereich angewendet werden sollen. Sie können beispielsweise den Schriftstil, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Nachdem Sie die gewünschten Formatierungsänderungen vorgenommen haben, klicken Sie auf die Schaltfläche „OK“, um die Formatierung auf den ausgewählten Bereich anzuwenden.


##  **So formatieren Sie einen Bereich mit C#**

Um einen Bereich mit Aspose.Cells zu formatieren, können Sie die folgenden Methoden verwenden:
1. [Range.ApplyStyle(Stilstil, StyleFlag-Flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Stilstil)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Stilstil)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und definieren zwei Bereiche („A1:C3“ und „A4:C5“). Anschließend erstellen wir neue Stile, legen verschiedene Formatierungsoptionen fest (z. B. Schriftfarbe, Fettdruck) und wenden den Stil auf den Bereich an. Abschließend speichern wir die Arbeitsmappe in einer neuen Datei.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
