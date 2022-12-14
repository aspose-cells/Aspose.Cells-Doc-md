---
title: Seitenumbrüche verwalten
type: docs
weight: 30
url: /de/net/managing-page-breaks/
---
{{% alert color="primary" %}}

Ein Seitenumbruch ist per Definition eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Mit Excel können Benutzer Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einfügen.

Die Position der Zelle, an der der Seitenumbruch hinzugefügt wird, die Seite beendet wird und die restlichen Daten nach dem Seitenumbruch beim Drucken auf die nächste Seite gedruckt werden. Vereinfacht gesagt unterteilen Seitenumbrüche Ihr Arbeitsblatt nach Ihren Vorgaben in mehrere Seiten. Sie können Ihren Arbeitsblättern auch zur Laufzeit Seitenumbrüche hinzufügen, indem Sie Aspose.Cells verwenden. Mit Aspose.Cells können Entwickler zwei Arten von Seitenumbrüchen hinzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im Rest der Diskussion werden wir beschreiben, wie Sie mit Aspose.Cells horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Die Klasse stellt eine breite Palette von Eigenschaften und Methoden bereit, die zum Verwalten eines Arbeitsblatts verwendet werden.

 Um die Seitenumbrüche hinzuzufügen, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**HorizontaleSeitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) und[**VertikaleSeitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Eigenschaften.

 Das[**HorizontaleSeitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) und[**VertikaleSeitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Eigenschaften sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zum Verwalten horizontaler und vertikaler Seitenumbrüche.

### **Seitenumbrüche hinzufügen**

 Um einem Arbeitsblatt einen Seitenumbruch hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die aufrufen[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) und[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) Methoden. Jeder**Hinzufügen** Die Methode übernimmt den Namen der Zelle, in der der Umbruch hinzugefügt werden soll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

In den Modi Seitenumbruchvorschau oder Druckvorschau können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

### **Löschen aller Seitenumbrüche**

 Um alle Seitenumbrüche in einem Arbeitsblatt zu löschen, rufen Sie die auf[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) und[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) Sammlungen[**Klar()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)Methoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Entfernen bestimmter Seitenumbrüche**

 Um einen bestimmten Seitenumbruch zu entfernen, rufen Sie die[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) und[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) Methoden. Jeder**EntfernenBei**-Methode nimmt den Index des Seitenumbruchs, der entfernt werden soll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Wichtig zu wissen**

 Wenn Sie einstellen**FitToPages** Eigenschaften (dh[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) und[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) in den Seiteneinrichtungseinstellungen sind die Seitenumbrucheinstellungen betroffen. Wenn Sie also das Arbeitsblatt drucken, werden die Seitenumbrucheinstellungen nicht berücksichtigt, obwohl sie noch festgelegt sind.
