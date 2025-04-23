---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Ein Seitenumbruch ist ein Ort im Text, an dem eine Seite endet und die nächste beginnt. Microsoft Excel kann Seitenumbrüche an einer beliebigen ausgewählten Zelle in einem Arbeitsblatt hinzufügen.
Die Seite endet an der Zelle, an der der Seitenumbruch hinzugefügt wird, und alle Daten nach dem Seitenumbruch werden auf der nächsten Seite gedruckt. Mit anderen Worten, Seitenumbrüche teilen Arbeitsblätter in mehrere Seiten auf. Es ist auch möglich, Seitenumbrüche in Arbeitsblätter zur Laufzeit mit Aspose.Cells hinzuzufügen. Aspose.Cells unterstützt zwei Arten von Seitenumbrüchen:

- horizontal
- vertikal.

In diesem Artikel wird beschrieben, wie horizontale oder vertikale Seitenumbrüche in Arbeitsblätter mithilfe von Aspose.Cells hinzugefügt werden.

{{% /alert %}}

## **Aspose.Cells & Seitenumbrüche**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält ein [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), das den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert, die eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern bietet. Um Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) und [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

Die Eigenschaften [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) und [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) sind tatsächlich Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen. Wie diese Methoden verwendet werden, wird unten diskutiert.

## **Seitenumbrüche hinzufügen**

Um einen Seitenumbruch in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die **Hinzufügen**-Methoden der Sammlungen [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) aufrufen. Jede **Hinzufügen**-Methode nimmt den Zellnamen entgegen, an dem der Seitenumbruch hinzugefügt werden soll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

## **Alle Seitenumbrüche löschen**

Um alle Seitenumbrüche in einem Arbeitsblatt zu löschen, rufen Sie die **Löschen**-Methoden der Sammlungen [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) auf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Bestimmten Seitenumbruch entfernen**

Um einen bestimmten Seitenumbruch im Arbeitsblatt zu entfernen, rufen Sie die **removeAt**-Methoden der Sammlungen [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) auf. Jede **removeAt**-Methode nimmt den Index des zu entfernenden Seitenumbruchs entgegen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Wichtig zu wissen**: Wenn Sie die Eigenschaften zum Anpassen des Seitenfits (also [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) und [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) in den Seiteneinrichtungs-Einstellungen) einstellen, werden die Einstellungen für Seitenumbrüche beeinflusst. Wenn Sie das Arbeitsblatt drucken, werden die Seitensprung- Einstellungen nicht berücksichtigt, obwohl sie noch in der Datei vorhanden sind.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
