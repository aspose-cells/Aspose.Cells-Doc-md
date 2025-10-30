---
title: Bereichsdaten mit Format kopieren
type: docs
weight: 610
url: /de/python-net/copy-range-data-with-style/
description: Dieser Artikel beschreibt, wie Sie Bereichsdaten mit Stil mit der Aspose.Cells for Python via .NET Bibliothek kopieren können.
keywords: Python Excel Bibliothek, Python Wie man Bereichsdaten mit Stil kopiert, Python Wie man Bereichsdaten mit Stil mit Python Excel Bibliothek kopiert.
---

{{% alert color="primary" %}}

[Kopieren von Bereichsdaten nur](/cells/de/python-net/copy-range-data-only/) erklärt, wie die Daten aus einem Zellenbereich in einen anderen Bereich kopiert werden. Insbesondere werden dabei auch neue Stile auf die kopierten Zellen angewendet. Aspose.Cells für Python via .NET kann auch einen Bereich einschließlich der Formatierung kopieren. Dieser Artikel erklärt, wie das funktioniert.

{{% /alert %}}

Aspose.Cells für Python via .NET bietet eine Reihe von Klassen und Methoden zum Arbeiten mit Bereichen, zum Beispiel, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) und [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Dieses Beispiel:

1. Erstellt ein Arbeitsblatt.
1. Füllt eine Anzahl von Zellen im ersten Arbeitsblatt mit Daten.
1. Erstellt ein [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Erstellt ein [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wendet den Stil auf den Datenbereich an.
1. Erstellt einen zweiten Zellenbereich.
1. Kopiert Daten mit Formatierung aus dem ersten Bereich in den zweiten Bereich.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
