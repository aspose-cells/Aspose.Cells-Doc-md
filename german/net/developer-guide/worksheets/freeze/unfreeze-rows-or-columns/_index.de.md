---
title: Freigeben von Zeilen oder Spalten
linktitle: Scheiben auftauen
type: docs
weight: 190
url: /de/net/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie Zeilen, Spalten oder Bereiche von Excel-Arbeitsblättern programmgesteuert mithilfe der Bibliothek C# mit .NET API freigeben.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie die Fixierung von Zeilen, Spalten und Fenstern aufheben.
Wenn Arbeitsblätter in den Excel-Dateien eingefroren sind, möchten wir sie manchmal entsperren oder eingefrorene Zeilen, Spalten oder Bereiche anpassen.

{{% /alert %}}

##  **In Excel**

1. Klicken Sie auf die Registerkarte „Ansicht“ > „Fenster einfrieren“ > „Fenster einfrieren“.

**![Fenster in Excel freigeben](Unfreeze-Panes.png)**




##  **Entsperren Sie Zeilen, Spalten oder Bereiche mit Aspose.Cells für .Net**
 Es ist einfach, Fenster mit Aspose.Cells für .Net freizugeben. Bitte nutzen Sie die[**Arbeitsblatt.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)Methode zum Entsperren von Scheiben.

1. Arbeitsmappe erstellen, um die eingefrorene Datei zu öffnen.
2. Geben Sie die Fixierung der Fenster mit der Methode Worksheet.UnFreezePanes() frei.
3. Speichern Sie die Datei.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Beigefügt[Beispiel einer Excel-Quelldatei](Frozen.xlsx).
