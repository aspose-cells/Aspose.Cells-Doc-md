---
title: Seitenumbrüche verwalten
type: docs
weight: 30
url: /de/net/managing-page-breaks/
description: Dieser Artikel enthält Beispielcode und erläutert, wie Sie mithilfe der Bibliothek C#, API oder .NET programmgesteuert Seitenumbrüche hinzufügen, Seitenumbrüche löschen oder bestimmte Seitenumbrüche in Excel-Arbeitsblättern löschen.
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

Laut Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Mit Excel können Benutzer Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einfügen.

Die Position der Zelle, in der der Seitenumbruch eingefügt wird, die Seite endet und die restlichen Daten nach dem Seitenumbruch beim Drucken auf der nächsten Seite gedruckt werden. Vereinfacht ausgedrückt unterteilen Seitenumbrüche Ihr Arbeitsblatt entsprechend Ihren Vorgaben in mehrere Seiten. Sie können Ihren Arbeitsblättern auch zur Laufzeit Seitenumbrüche hinzufügen, indem Sie Aspose.Cells verwenden. Aspose.Cells ermöglicht Entwicklern das Hinzufügen von zwei Arten von Seitenumbrüchen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion beschreiben wir, wie Sie mit Aspose.Cells horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter einfügen können.

{{% /alert %}}

##  **Seitenumbrüche**

Aspose.Cells bietet a[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die eine Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Die Klasse stellt eine breite Palette von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts bereit.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Horizontale Seitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) Und[**Vertikale Seitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Eigenschaften.

 Der[**Horizontale Seitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) Und[**Vertikale Seitenumbrüche**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Eigenschaften sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zum Verwalten horizontaler und vertikaler Seitenumbrüche.

###  **Seitenumbrüche hinzufügen**

 Um einen Seitenumbruch in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie aufrufen[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) Und[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) Methoden. Jede**Hinzufügen** Die Methode übernimmt den Namen der Zelle, in der der Umbruch eingefügt werden soll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

In der Seitenumbruchvorschau oder der Druckvorschau können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

###  **Alle Seitenumbrüche löschen**

 Um alle Seitenumbrüche in einem Arbeitsblatt zu löschen, rufen Sie auf[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) Und[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) Sammlungen'[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)Methoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **Entfernen eines bestimmten Seitenumbruchs**

 Um einen bestimmten Seitenumbruch zu entfernen, rufen Sie auf[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) Und[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) Methoden. Jede**RemoveAt**Die Methode verwendet den Index des Seitenumbruchs, der entfernt werden soll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **Wichtig zu wissen**

 Wenn Sie einstellen**FitToPages** Eigenschaften (d. h[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) Und[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) in den Seiteneinrichtungseinstellungen sind die Seitenumbrucheinstellungen betroffen. Wenn Sie also das Arbeitsblatt drucken, werden die Seitenumbrucheinstellungen nicht berücksichtigt, obwohl sie noch festgelegt sind.
