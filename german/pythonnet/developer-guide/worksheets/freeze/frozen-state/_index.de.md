---
title: Wie man den fixierten Zustand ohne Excel überprüft
linktitle: Einfrierungsstatus
type: docs
weight: 190
url: /de/python-net/how-to-check-frozen-state-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie den fixierten Zustand eines Excel Tabellenblatts programmgesteuert überprüfen können, indem Sie Aspose.Cells für Python via .NET APIs verwenden.
keywords: Python Excel Bibliothek, Python Wie man den fixierten Zustand ohne Excel überprüft, Den fixiert Zustand ohne Excel in Python überprüfen.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie Sie den fixierten Zustand eines Excel-Tabellenblatts programmgesteuert überprüfen können. Wir können einfach feststellen, ob das Tabellenblatt in MS Excel eingefroren oder aufgeteilt ist. Aber gibt es eine Möglichkeit zu prüfen, ob es mit CSharp eingefroren oder aufgeteilt ist. Wir können dies ganz einfach mit Aspose.Cells für Python via .NET tun.

## **Wie man den fixierten Zustand überprüft**
Mit Aspose.Cells für Python via .NET können wir überprüfen, ob das Fenster eingefroren ist und wie viele Zeilen und Spalten gesperrt sind.

Bitte verwenden Sie die [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/)-Eigenschaft, um den Zustand der Fensterscheiben zu überprüfen 
und sperren Sie Zeilen und Spalten mit der [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any)-Methode.
1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist.
3. Erhalten Sie die gesperrten Zeilen und Spalten

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
