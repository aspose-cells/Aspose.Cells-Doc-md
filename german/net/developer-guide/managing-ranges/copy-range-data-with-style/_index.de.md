---
title: Bereichsdaten mit Format kopieren
type: docs
weight: 610
url: /de/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/net/copy-range-data-only/) erläutert, wie die Daten eines Zellenbereichs in einen anderen Bereich kopiert werden können. Insbesondere wird ein neuer Satz von Formatierungen auf die kopierten Zellen angewendet. Aspose.Cells kann auch einen Bereich einschließlich Formatierung kopieren. Dieser Artikel erklärt wie.

{{% /alert %}}

Aspose.Cells bietet eine Reihe von Klassen und Methoden zum Arbeiten mit Bereichen, beispielsweise [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) und [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Dieses Beispiel:

1. Erstellt ein Arbeitsblatt.
1. Füllt eine Anzahl von Zellen im ersten Arbeitsblatt mit Daten.
1. Erstellt ein [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Erstellt ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wendet den Stil auf den Datenbereich an.
1. Erstellt einen zweiten Zellenbereich.
1. Kopiert Daten mit Formatierung aus dem ersten Bereich in den zweiten Bereich.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
