---
title: Bereichsdaten mit Stil in C++ kopieren
linktitle: Bereichsdaten mit Format kopieren
type: docs
weight: 610
url: /de/go-cpp/copy-range-data-with-style/
description: Bereichsdaten einschließlich Zellformatierungen in Excel Dateien mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/cpp/copy-range-data-only/) erklärt, wie man Zellendaten zwischen Bereichen kopiert. Dieser Artikel demonstriert, wie man Zellbereiche beim Erhalt ihrer Formatierungen mit Aspose.Cells for C++ kopiert.

{{% /alert %}}

Aspose.Cells bietet Klassen und Methoden für die Arbeit mit Bereichen, einschließlich [**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) und [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Dieses Beispiel demonstriert, wie man:

1. Ein Arbeitsbuch erstellt
1. Zellen mit Daten füllt
1. Ein [**Range**](https://reference.aspose.com/cells/go-cpp/range/) erstellt
1. Ein [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekt erstellt und konfiguriert
1. Stil auf den Bereich anwenden
1. Einen zweiten Bereich erstellen
1. Formatierten Daten zwischen Bereichen kopieren

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
