---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 40
url: /de/net/copying-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten durch die Aspose.Cells for .NET API kopiert.
keywords: C# Wie man Zeilen und Spalten kopiert, Zeilen in C# kopiert, Spalten in C# kopiert, Wie man Zeilen und Spalten mithilfe von Aspose.Cells for .NET einfügt, Mehrere Zeilen und Spalten einfügt, Wie man eine einzelne Zeile oder Spalte kopiert und einfügt.
---

## **Einführung**

Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.
Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten, einschließlich Formeln - mit aktualisierten Verweisen - und Werten, Kommentare, Formatierungen, versteckte Zellen, Bilder und andere Zeichenobjekte ebenfalls kopiert.

## **Wie man Zeilen und Spalten mit Microsoft Excel kopiert**

1. Wählen Sie die zu kopierende Zeile oder Spalte aus.
1. Zum Kopieren von Zeilen oder Spalten klicken Sie auf **Kopieren** in der **Standard**-Symbolleiste oder drücken Sie **STRG**+**C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Position aus, an der Sie Ihre Auswahl kopieren möchten.
1. Beim Kopieren von Zeilen oder Spalten klicken Sie auf **Kopierte Zellen** im **Einfügen**-Menü.

{{% alert color="primary" %}}

Wenn Sie auf **Einfügen** in der **Standard**-Symbolleiste klicken oder **STRG**+**V** drücken, anstatt ein Befehl im **Einfügen**-Menü zu klicken, werden die Inhalte der Zielzellen ersetzt.

{{% /alert %}}

## **Wie man Zeilen und Spalten mit Paste-Optionen mit Microsoft Excel einfügt**

1. Wählen Sie die Zellen aus, die die Daten oder andere Attribute enthalten, die Sie kopieren möchten.
1. Klicken Sie auf der Registerkarte Start auf **Kopieren**.
1. Klicken Sie auf die erste Zelle im Bereich, in dem Sie das, was Sie kopiert haben, **einfügen** möchten.
1. Klicken Sie auf der Registerkarte Start auf den Pfeil neben **Einfügen**, und wählen Sie dann **Inhalt einfügen** aus.
1. Wählen Sie die **Optionen**, die Sie möchten.

## **Wie man Zeilen und Spalten mit der Verwendung von Aspose.Cells for .NET kopiert**

## **Wie man einzelne Zeilen kopiert**

Aspose.Cells bietet die [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) Methode der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse an. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werten, Kommentaren, Zellformatierungen, versteckten Zellen, Bildern und anderen Zeichenobjekten von der Quellzeile zur Zielzeile.

Die Methode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) akzeptiert die folgenden Parameter:

- das Quell-[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Objekt,
- den Index der Quellzeile, und
- den Index der Zielzeile.

Verwenden Sie diese Methode zum Kopieren einer Zeile innerhalb eines Blatts oder zu einem anderen Blatt. Die Methode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) funktioniert ähnlich wie Microsoft Excel. Sie müssen beispielsweise nicht explizit die Höhe der Zielzeile festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es wird eine Vorlagen-Excel-Datei verwendet, und die zweite Zeile (vollständig mit Daten, Formatierung, Kommentaren, Bildern usw.) wird in die 12. Zeile im selben Arbeitsblatt eingefügt.

Sie können den Schritt überspringen, der die Höhe der Quellzeile mit der Methode [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) ermittelt und dann mit der Methode [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) die Höhe der Zielzeile festlegt, da die Methode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) automatisch die Zeilenhöhe übernimmt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Beim Kopieren von Zeilen ist es wichtig, darauf hinzuweisen, dass damit verbundene Bilder, Diagramme oder andere Zeichenobjekte genauso wie bei Microsoft Excel behandelt werden:

1. Wenn der Quellzeilenindex 5 beträgt, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Startzeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}}

## **Wie man Mehrere Zeilen kopiert**

Sie können auch mehrere Zeilen auf ein neues Ziel kopieren, während die Methode [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), die einen zusätzlichen Parameter vom Typ Ganzzahl akzeptiert, verwendet wird, um die Anzahl der zu kopierenden Quellzeilen anzugeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Wie man Spalten kopiert**

Aspose.Cells bietet die Methode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) der Klasse [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), diese Methode kopiert alle Arten von Daten, einschließlich Formeln - mit aktualisierten Referenzen - und Werten, Kommentaren, Zellformaten, versteckten Zellen, Bildern und anderen Zeichenobjekten von der Quellspalte in die Zielspalte.

Die Methode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) akzeptiert die folgenden Parameter:

- das Quell-[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Objekt,
- Quellspaltenindex, und
- der Zielspaltenindex.

Verwenden Sie die Methode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn), um eine Spalte innerhalb eines Blatts oder zu einem anderen Blatt zu kopieren.

Dieses Beispiel kopiert eine Spalte aus einem Arbeitsblatt und fügt sie in ein Arbeitsblatt in einer anderen Arbeitsmappe ein.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Wie man mehrere Spalten kopiert**

Ähnlich wie die [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)-Methode bieten die Aspose.Cells-APIs auch die [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)-Methode, um mehrere Quellspalten an eine neue Position zu kopieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Wie man Zeilen und Spalten mit Einfügeoptionen einfügt**

Aspose.Cells bietet jetzt [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) bei Verwendung der Funktionen [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) und [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Es ermöglicht, ähnlich wie in Excel, die geeignete Einfügeoption festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
