---
title: Seitenumbrüche verwalten
type: docs
weight: 30
url: /de/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Ein Seitenumbruch ist per Definition eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Mit Excel können Benutzer Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einfügen.

Die Position der Zelle, an der der Seitenumbruch hinzugefügt wird, die Seite beendet wird und alle restlichen Daten nach dem Seitenumbruch während des Druckens auf der nächsten Seite gedruckt werden. Vereinfacht gesagt unterteilen Seitenumbrüche Ihr Arbeitsblatt nach Ihren Vorgaben in mehrere Seiten. Sie können Ihren Arbeitsblättern auch zur Laufzeit Seitenumbrüche hinzufügen, indem Sie Aspose.Cells verwenden. Mit Aspose.Cells können Entwickler zwei Arten von Seitenumbrüchen hinzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im Rest der Diskussion werden wir beschreiben, wie Sie mit Aspose.Cells horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter einfügen können.

{{% /alert %}} 
## **Seitenumbrüche**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) die eine Excel-Datei darstellt. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Die Klasse bietet eine breite Palette von Methoden zum Verwalten eines Arbeitsblatts. Um die Seitenumbrüche hinzuzufügen, verwenden Sie die[Seitenumbrüche hinzufügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Klasse.
### **Seitenumbrüche hinzufügen**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
