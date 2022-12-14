---
title: Seitenumbrüche verwalten
type: docs
weight: 30
url: /de/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Ein Seitenumbruch ist eine Stelle im Text, an der eine Seite endet und die nächste beginnt. Microsoft Excel kann Seitenumbrüche an jeder ausgewählten Zelle in einem Arbeitsblatt hinzufügen.
Die Seite endet an der Zelle, an der der Seitenumbruch hinzugefügt wird, und alle Daten nach dem Seitenumbruch werden auf der nächsten Seite gedruckt. In einfachen Worten, Seitenumbrüche teilen Arbeitsblätter in mehrere Seiten auf. Es ist auch möglich, mit Aspose.Cells zur Laufzeit Seitenumbrüche zu Arbeitsblättern hinzuzufügen. Aspose.Cells unterstützt zwei Arten von Seitenumbrüchen:

- horizontal
- vertikal.

In diesem Artikel wird beschrieben, wie Sie mithilfe von Aspose.Cells horizontale oder vertikale Seitenumbrüche in Arbeitsblätter einfügen.

{{% /alert %}}

## **Aspose.Cells & Seitenumbrüche**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse, die eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern bereitstellt. Um die Seitenumbrüche hinzuzufügen, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**HorizontaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) und[**VertikaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)Eigenschaften.

 Das[**HorizontaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) und[**VertikaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)Eigenschaften sind in der Tat Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zum Verwalten horizontaler und vertikaler Seitenumbrüche. Wie diese Methoden verwendet werden, wird unten diskutiert.

## **Seitenumbrüche hinzufügen**

 Um einem Arbeitsblatt einen Seitenumbruch hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die aufrufen[**HorizontaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und[**VertikaleSeitenumbrüche**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) Sammlungen**Hinzufügen** Methoden. Jeder**Hinzufügen**-Methode nimmt den Zellennamen, an dem der Seitenumbruch hinzugefügt werden soll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

In den Modi Seitenumbruchvorschau oder Druckvorschau können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

## **Löschen aller Seitenumbrüche**

 Um alle Seitenumbrüche in einem Arbeitsblatt zu löschen, rufen Sie die auf[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) Sammlungen**Klar**Methoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Entfernen bestimmter Seitenumbrüche**

 Um einen bestimmten Seitenumbruch im Arbeitsblatt zu entfernen, rufen Sie die auf[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) und[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) Sammlungen**entfernenBei** Methoden. Jeder**entfernenBei**-Methode nimmt den Index des zu entfernenden Seitenumbruchs.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Wichtig zu wissen** : Wenn Sie die Seitenanpassungseigenschaften festlegen (d. h[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) und[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) in den Seiteneinrichtungseinstellungen sind die Seitenumbrucheinstellungen betroffen, sodass beim Drucken des Arbeitsblatts die Seitenumbrucheinstellungen nicht berücksichtigt werden, obwohl sie noch in der Datei vorhanden sind.

{{% /alert %}}
