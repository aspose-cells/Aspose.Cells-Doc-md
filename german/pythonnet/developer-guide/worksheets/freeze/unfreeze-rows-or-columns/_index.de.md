---
title: Zeilen oder Spalten fixieren
linktitle: Fenster fixieren
type: docs
weight: 190
url: /de/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie Zeilen, Spalten oder Fenster von Excel Arbeitsblättern programmgesteuert mit Aspose.Cells für Python via .NET APIs entsperren.
keywords: Python Excel Bibliothek, Python Fenster entsperren, Python Wie man Zeilen entsperrt, Python wie man Spalten entsperrt, Python wie man Fenster entriegelt.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man Zeilen, Spalten und Fenster entfrostet. Wenn Arbeitsblätter in den Excel-Dateien eingefroren sind, möchten wir manchmal das Arbeitsblatt entfrosten oder eingefrorene Zeilen, Spalten oder Fenster anpassen.


## **Wie man Zeilen oder Spalten in Excel entsperrt**

1. Klicken Sie auf die Registerkarte Ansicht > Fenster fixieren > Fenster nicht fixieren.

**![Fenster nicht fixieren in Excel](Unfreeze-Panes.png)**




## **Wie man Zeilen, Spalten oder Fenster mit der Aspose.Cells für Python Excel-Bibliothek entsperrt**
Das Aufheben des Einfrierens von Fenstern ist mit Aspose.Cells für Python via .NET einfach. Bitte verwenden Sie die [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/)-Methode, um die Fenster zu entsperren.

1. Arbeitsmappe erstellen, um die gefrorene Datei zu öffnen.
2. Entfrieren von Fenstern mit der Methode Worksheet.UnFreezePanes().
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Angehängte [Beispiel-Excel-Quelldatei](Frozen.xlsx).
