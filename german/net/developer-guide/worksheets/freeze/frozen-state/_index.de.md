---
title: So überprüfen Sie den Frozen State ohne Excel.
linktitle: Gefrorener Zustand
type: docs
weight: 190
url: /de/net/how-to-check-frozen-state-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie mithilfe der Bibliothek C# und .NET API den eingefrorenen Status eines Excel-Arbeitsblatts programmgesteuert überprüfen.
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie den eingefrorenen Zustand eines Excel-Arbeitsblatts programmgesteuert überprüfen.
Wir können einfach herausfinden, ob das Arbeitsblatt in MS Excel eingefroren oder geteilt ist. Aber gibt es eine Möglichkeit, mit CSharp herauszufinden, ob es eingefroren oder geteilt ist?
Wir können es einfach mit Aspose.Cells für .Net machen.
{{% /alert %}}

##  **Sind Fensterscheiben eingefroren?**
Mit Aspose.Cells für .Net können wir prüfen, ob das Fenster eingefroren ist und wie viele Zeilen und Spalten gesperrt sind.

 Bitte nutzen Sie die[**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) Eigenschaft, um den Zustand von Fensterscheiben zu überprüfen
 und erhält gesperrte Zeilen und Spalten mit[**Arbeitsblatt.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)Methode.
1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist.
3. Ruft die gesperrte Zeile und die gesperrten Spalten ab

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}