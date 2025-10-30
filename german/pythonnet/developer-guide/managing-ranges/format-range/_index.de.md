---
title: Bereiche formatieren
type: docs
weight: 105
url: /de/python-net/how-to-format-a-range/
description: Dieser Artikel beschreibt, wie Bereiche mit der Aspose.Cells für Python via .NET Bibliothek formatiert werden.
keywords: Python Excel Bibliothek, Python Wie man einen Bereich formatiert, Python Wie man Bereiche formatiert.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie einen Stil auf einen Bereich anwenden möchten, können Sie die Bereichsformatierung verwenden.

## **Wie formatiert man einen Bereich in Excel**

Um einen Zellenbereich in Excel zu formatieren, können Sie die von Excel bereitgestellten integrierten Formatierungsoptionen verwenden. So formatieren Sie einen Zellenbereich direkt in Excel:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die den zu formatierenden Bereich enthält.

2. Wählen Sie den zu formatierenden Zellenbereich aus. Sie können klicken und ziehen, um den Bereich auszuwählen, oder Sie können Tastenkombinationen wie Umschalttaste + Pfeiltasten verwenden, um die Auswahl zu erweitern.

3. Wenn der Bereich ausgewählt ist, klicken Sie mit der rechten Maustaste auf den ausgewählten Bereich und wählen Sie "Zellen formatieren" im Kontextmenü aus. Alternativ können Sie zum Start-Tab im Excel-Ribbon gehen, auf die Dropdown-Liste "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.

4. Das Dialogfeld "Zellen formatieren" wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf den ausgewählten Bereich angewendet werden sollen. Sie können beispielsweise den Schriftstil, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Nachdem Sie die gewünschten Formatierungsänderungen vorgenommen haben, klicken Sie auf die Schaltfläche "OK", um die Formatierung auf den ausgewählten Bereich anzuwenden.


## **So formatieren Sie einen Bereich mit C#**

Um einen Bereich mit Aspose.Cells zu formatieren, können Sie die folgenden Methoden verwenden:
1. [Range.apply_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)
2. [Range.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style)
3. [Range.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style-bool)


## **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und definieren zwei Bereiche ("A1:C3" und "A4:C5"). Dann erstellen wir neue Stile, setzen verschiedene Formatierungsoptionen (z.B. Schriftfarbe, Fett) und wenden den Stil auf den Bereich an. Schließlich speichern wir die Arbeitsmappe in eine neue Datei.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-FormatRanges.py" >}}
{{< app/cells/assistant language="python-net" >}}
