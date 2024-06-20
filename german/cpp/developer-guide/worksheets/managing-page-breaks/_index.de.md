---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Die Position der Zelle, an der der Seitenumbruch hinzugefügt wird, markiert das Ende der Seite und alle restlichen Daten nach dem Seitenumbruch werden auf der nächsten Seite gedruckt, während des Druckvorgangs. Einfach ausgedrückt, Seitenumbrüche teilen Ihr Arbeitsblatt entsprechend Ihren Spezifikationen in mehrere Seiten. Unter Verwendung von Aspose.Cells können Entwickler auch zur Laufzeit Seitenumbrüche zu ihren Arbeitsblättern hinzufügen. Aspose.Cells ermöglicht Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells einfügen können.

{{% /alert %}} 
## **Seitenumbrüche**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) -Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) -Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine große Auswahl an Methoden, um Arbeitsblätter zu verwalten. Um Seitenumbrüche hinzuzufügen, verwenden Sie die Methode [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) der Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Seitenumbrüche hinzufügen**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
