---
title: Seitenumbrüche verwalten
type: docs
weight: 30
url: /de/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Laut Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Mit Excel können Benutzer Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einfügen.

Die Position der Zelle, in der der Seitenumbruch eingefügt wird, die Seite endet und alle restlichen Daten nach dem Seitenumbruch beim Drucken auf der nächsten Seite gedruckt werden. Vereinfacht ausgedrückt unterteilen Seitenumbrüche Ihr Arbeitsblatt entsprechend Ihren Vorgaben in mehrere Seiten. Sie können Ihren Arbeitsblättern auch zur Laufzeit Seitenumbrüche hinzufügen, indem Sie Aspose.Cells verwenden. Aspose.Cells ermöglicht Entwicklern das Hinzufügen von zwei Arten von Seitenumbrüchen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion beschreiben wir, wie Sie mit Aspose.Cells horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter einfügen können.

{{% /alert %}} 
##  **Seitenumbrüche**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) das eine Excel-Datei darstellt. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Die Klasse bietet eine breite Palette von Methoden zum Verwalten eines Arbeitsblatts. Um die Seitenumbrüche hinzuzufügen, verwenden Sie die[Seitenumbrüche hinzufügen](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse.
###  **Seitenumbrüche hinzufügen**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
