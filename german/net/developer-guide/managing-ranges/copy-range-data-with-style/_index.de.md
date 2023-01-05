---
title: Bereichsdaten mit Stil kopieren
type: docs
weight: 610
url: /de/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/net/copy-range-data-only/) erklärt, wie man die Daten aus einem Zellbereich in einen anderen Bereich kopiert. Insbesondere wurde ein neuer Stilsatz auf die kopierten Zellen angewendet. Aspose.Cells kann auch einen Bereich komplett mit Formatierung kopieren. Dieser Artikel erklärt, wie.

{{% /alert %}}

Aspose.Cells bietet eine Reihe von Klassen und Methoden für die Arbeit mit Bereichen, z. B.[**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) und[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Dieses Beispiel:

1. Erstellt eine Arbeitsmappe.
1. Füllt eine Reihe von Zellen im ersten Arbeitsblatt mit Daten.
1.  Erstellt ein[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Erstellt ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt mit angegebenen Formatierungsattributen.
1. Wendet den Stil auf den Datenbereich an.
1. Erstellt einen zweiten Zellbereich.
1. Kopiert Daten mit der Formatierung aus dem ersten Bereich in den zweiten Bereich.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
