---
title: Bereiche von Excel kopieren
linktitle: Bereiche kopieren
type: docs
weight: 105
url: /de/python-net/copy-ranges-of-excel/
description: In diesem Artikel wird beschrieben, wie man Bereiche von Excel mit der Aspose.Cells for Python via .NET Bibliothek kopiert.
keywords: Python Excel Bibliothek, Wie man Bereiche von Excel kopiert, Wie man nur Datenbereiche mit der Python Excel Bibliothek kopiert, Wie man Bereiche mit Optionen einfügt, Wie man nur Daten des Bereichs kopiert.
---

## **Einführung**

In Excel können Sie einen Bereich auswählen, den Bereich kopieren und ihn mit spezifischen Optionen in dasselbe Arbeitsblatt, in andere Arbeitsblätter oder in andere Dateien einfügen.

## **Bereiche kopieren mit der Aspose.Cells für Python Excel-Bibliothek**

Aspose.Cells for Python via .NET bietet einige Überlastungsmethoden, um den Bereich zu kopieren.
Und [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) nur den Kopierstil des Bereichs; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) nur den Kopierwert des Bereichs

## **Bereich kopieren**

Erstellen zweier Bereiche: Quellbereich, Zielbereich, und dann Quellbereich in Zielbereich mit Methode [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) kopieren.

Siehe den folgenden Code:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Bereich mit Optionen einfügen**

Aspose.Cells for Python via .NET unterstützt das Einfügen des Bereichs mit bestimmtem Typ.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Nur Daten des Bereichs kopieren**
Sie können die Daten auch mit der Methode [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) wie folgt kopieren:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Erweiterte Themen**
- [Zeilenhöhen des Quellbereichs in den Zielbereich kopieren](/cells/de/python-net/copy-row-heights-of-source-range-to-destination-range/)


