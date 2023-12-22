---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/net/autofit-rows-and-columns/
description: In diesem Artikel wird gezeigt, wie Sie Zeilen, Spalten, Zeilen zusammengeführter Zellen und Zeilen in einem Zellbereich mit Aspose.Cells for .NET API automatisch anpassen.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht Benutzern die automatische Anpassung der Breite und Höhe von Zellen entsprechend ihrem Inhalt. Diese Funktion ist auch über Aspose.Cells verfügbar, sodass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.

{{% /alert %}}

##  **Automatische Anpassung**

Aspose.Cells bietet a[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Die Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Dieser Artikel befasst sich mit der Verwendung von[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse, um Zeilen oder Spalten automatisch anzupassen.

###  **AutoFit-Reihe – einfach**

 Der einfachste Ansatz zur automatischen Größenanpassung der Breite und Höhe einer Zeile ist der Aufruf von[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) Methode. Der[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)Die Methode benötigt einen Zeilenindex (der Zeile, deren Größe geändert werden soll) als Parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **So passen Sie eine Zeile automatisch in einen Bereich von Cells ein**

 Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf dem Inhalt in einem Bereich von Zellen innerhalb der Zeile automatisch anzupassen, indem sie eine überladene Version von aufrufen[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Methode. Es werden folgende Parameter benötigt:

- *Zeilenindex**, der Index der Zeile, die automatisch angepasst werden soll.
- *Index der ersten Spalte**, der Index der ersten Spalte der Zeile.
- *Index der letzten Spalte**, der Index der letzten Spalte der Zeile.

 Der[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Die Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile dann automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **So passen Sie eine Spalte automatisch in einen Bereich von Cells ein**

 Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Bereich von Zellen in der Spalte automatisch anzupassen, indem eine überladene Version von aufgerufen wird[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Methode, die die folgenden Parameter annimmt:

- *Spaltenindex**, der Index der Spalte, die automatisch angepasst werden soll.
- *Index der ersten Zeile**, der Index der ersten Zeile der Spalte.
- *Index der letzten Zeile**, der Index der letzten Zeile der Spalte.

 Der[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Die Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte dann automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **So passen Sie Zeilen für zusammengeführte Zeilen automatisch an Cells**

 Mit Aspose.Cells ist es möglich, Zeilen auch für Zellen automatisch anzupassen, die mit dem zusammengeführt wurden[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Klasse bietet[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) Eigenschaft, die zum automatischen Anpassen von Zeilen für verbundene Zellen verwendet werden kann.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)akzeptiert[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) aufzählbar, das die folgenden Mitglieder hat.

- Keine: Zusammengeführte Zellen ignorieren.
- FirstLine: Erweitert nur die Höhe der ersten Zeile.
- LastLine: Erweitert nur die Höhe der letzten Zeile.
- EachLine: Erweitert nur die Höhe jeder Zeile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Sie können auch versuchen, die überladenen Versionen von zu verwenden[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) Methoden, die einen Bereich von Zeilen/Spalten und eine Instanz davon akzeptieren[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) um die ausgewählten Zeilen/Spalten automatisch an Ihre Wünsche anzupassen[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)entsprechend.

Die Signaturen der oben genannten Methoden lauten wie folgt:

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Optionen)
1.  AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Optionen)

{{% /alert %}}

##  **Wichtig zu wissen**

{{% alert color="primary" %}}

Wenn eine Zelle zusammengeführt wird, werden die AutoFit-Methoden nicht angewendet, was dem gleichen Verhalten wie in Microsoft Excel entspricht. Sie können dies umgehen, indem Sie den automatischen Filter API verwenden. Wenn der Text in einer Zelle außerdem umbrochen wird, wird der[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) Methode wird ebenfalls nicht angewendet. Eine andere Sache, die Sie wissen müssen, ist, dass die*AutoFit*Methoden sind zeitaufwändig. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung sicherzustellen.

{{% /alert %}}

##  **Vorabthemen**
- [Zeilen automatisch anpassen für zusammengeführte Zeilen Cells](/cells/de/net/autofit-rows-for-merged-cells/)
