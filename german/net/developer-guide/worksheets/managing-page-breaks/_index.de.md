---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/net/managing-page-breaks/
description: In diesem Artikel finden Sie Beispielscode und Erläuterungen, wie man Seiteumbrüche in Excel Arbeitsblättern programmgesteuert mit der C# API oder der .NET Bibliothek hinzufügen, löschen oder spezielle Seiteumbrüche entfernen kann.
keywords: Seiteumbrüche c#, Excel Seiteumbrüche c#, speziellen Seiteumbruch c# löschen, spezieller Seiteumbruch c# löschen
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Der Ort der Zelle, an dem der Seitenumbruch hinzugefügt wird, die Seite endet und der Rest der Daten nach dem Seitenumbruch auf der nächsten Seite gedruckt wird, während des Druckens. Einfach ausgedrückt, teilen Seitenumbrüche Ihr Arbeitsblatt gemäß Ihren Spezifikationen in mehrere Seiten auf. Sie können auch zur Laufzeit Seitenumbrüche zu Ihren Arbeitsblättern mit Aspose.Cells hinzufügen. Aspose.Cells ermöglicht Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells stellt eine Klasse bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine Sammlung von [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) und [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Die Eigenschaften [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) und [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen.

### **Seitenumbrüche hinzufügen**

Um einen Seitenumbruch in ein Arbeitsblatt einzufügen, fügen Sie vertikale und horizontale Seitenumbrüche in die angegebene Zelle ein, indem Sie die Methoden [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) und [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) aufrufen. Jede **Hinzufügen**-Methode nimmt den Namen der Zelle, an der der Umbruch hinzugefügt werden soll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

### **Alle Seitenumbrüche löschen**

Um alle Seitenumbrüche in einem Arbeitsblatt zu löschen, rufen Sie die Methoden [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear) der Sammlungen [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) und [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) auf.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Bestimmten Seitenumbruch entfernen**

Um einen bestimmten Seitenumbruch zu entfernen, rufen Sie die Methoden [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) und [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) auf. Jede **Entfernen an**-Methode nimmt den Index des zu entfernenden Seitenumbruchs.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Wichtig zu wissen**

Wenn Sie **Passend für Seiten**-Eigenschaften festlegen (d. h. [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) und [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) in den Seiteneinrichtungseinstellungen, werden die Seitenumbrucheinstellungen beeinflusst. Daher werden die Seitenumbrucheinstellungen beim Drucken des Arbeitsblatts nicht berücksichtigt, obwohl sie immer noch eingestellt sind.
