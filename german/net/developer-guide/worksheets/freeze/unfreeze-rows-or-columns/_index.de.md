---
title: Zeilen oder Spalten fixieren
linktitle: Fenster fixieren
type: docs
weight: 190
url: /de/net/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie Zeilen, Spalten oder Fenster von Excel Arbeitsblättern programmgesteuert mithilfe der C# Bibliothek und der .NET API wieder fixieren.
keywords: Fenster fixieren, Zeilen fixieren, Spalten fixieren, Fenster nicht fixieren.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man Zeilen, Spalten und Fenster entfrostet. Wenn Arbeitsblätter in den Excel-Dateien eingefroren sind, möchten wir manchmal das Arbeitsblatt entfrosten oder eingefrorene Zeilen, Spalten oder Fenster anpassen.


## **In Excel**

1. Klicken Sie auf die Registerkarte Ansicht > Fenster fixieren > Fenster nicht fixieren.

**![Fenster nicht fixieren in Excel](Unfreeze-Panes.png)**




## **Unfreezen von Zeilen, Spalten oder Bereichen mit Aspose.Cells für .NET**
Mit Aspose.Cells for .NET ist es einfach, Fenster zu entfrieren. Bitte verwenden Sie die [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)-Methode zum Entfrieren der Fenster.

1. Arbeitsmappe erstellen, um die gefrorene Datei zu öffnen.
2. Entfrieren von Fenstern mit der Methode Worksheet.UnFreezePanes().
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Angehängte [Beispiel-Excel-Quelldatei](Frozen.xlsx).
{{< app/cells/assistant language="csharp" >}}
