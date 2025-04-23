---
title: Bereiche von Excel kopieren
linktitle: Bereiche kopieren
type: docs
weight: 105
url: /de/net/copy-ranges-of-Excel/
---

## **Einführung**

In Excel können Sie einen Bereich auswählen, den Bereich kopieren und ihn mit spezifischen Optionen in dasselbe Arbeitsblatt, in andere Arbeitsblätter oder in andere Dateien einfügen.

## **Bereiche mit Aspose.Cells kopieren**

Aspose.Cells bietet einige Überladungsmethoden für [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) an, um den Bereich zu kopieren.
Und [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) kopiert nur den Stil des Bereichs; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) kopiert nur den Wert des Bereichs.

## **Bereich kopieren**

Erstellen von zwei Bereichen: Der Quellbereich, der Zielbereich, dann Kopieren des Quellbereichs in den Zielbereich mit der Range.Copy-Methode.

Siehe den folgenden Code:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Bereich mit Optionen einfügen**

Aspose.Cells unterstützt das Einfügen des Bereichs mit einem spezifischen Typ.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Nur Daten des Bereichs kopieren**
Sie können auch die Daten mit der Range.CopyData-Methode wie folgt kopieren:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Erweiterte Themen**
- [Zeilenhöhen des Quellbereichs in den Zielbereich kopieren](/cells/de/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
