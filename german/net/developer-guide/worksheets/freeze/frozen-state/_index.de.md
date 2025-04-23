---
title: Wie überprüfen Sie den Einfrierungsstatus ohne Excel.
linktitle: Einfrierungsstatus
type: docs
weight: 190
url: /de/net/how-to-check-frozen-state-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie programmgesteuert den Einfrierungsstatus des Excel Arbeitsblatts mit C# Bibliothek und .NET API überprüfen können.

---

## **Einführung**

In diesem Artikel erfahren Sie, wie man den eingefrorenen Zustand des Excel-Arbeitsblatts programmgesteuert prüft. Wir können in MS Excel einfach herausfinden, ob das Arbeitsblatt eingefroren oder gespalten ist. Aber gibt es eine Möglichkeit, dies mit C# herauszufinden? Mit Aspose.Cells für .NET können wir es ganz einfach tun.

## **Sind Fensterscheiben eingefroren?**
Mit Aspose.Cells für .Net können wir überprüfen, ob das Fenster eingefroren ist und wie viele Zeilen und Spalten gesperrt sind.

Bitte verwenden Sie die [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/)-Eigenschaft, um den Zustand der Fensterscheiben zu überprüfen 
und sperren Sie Zeilen und Spalten mit der [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)-Methode.
1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist.
3. Erhalten Sie die gesperrten Zeilen und Spalten

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
{{< app/cells/assistant language="csharp" >}}
