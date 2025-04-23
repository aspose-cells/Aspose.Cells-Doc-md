---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Die Position der Zelle, an der der Seitenumbruch hinzugefügt wird, markiert das Ende der Seite und alle restlichen Daten nach dem Seitenumbruch werden auf der nächsten Seite gedruckt, während des Druckvorgangs. Einfach ausgedrückt, Seitenumbrüche teilen Ihr Arbeitsblatt entsprechend Ihren Spezifikationen in mehrere Seiten. Unter Verwendung von Aspose.Cells können Entwickler auch zur Laufzeit Seitenumbrüche zu ihren Arbeitsblättern hinzufügen. Aspose.Cells ermöglicht Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook), die eine Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden. Um Seitenumbrüche hinzuzufügen, verwenden Sie die Methode [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse.

### **Seitenumbrüche hinzufügen**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
