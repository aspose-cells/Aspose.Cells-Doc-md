---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/net/autofit-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen, Spalten, Zeilen von zusammengeführten Zellen und Zeilen in einem Zellenbereich mittels der Aspose.Cells for .NET API automatisch anpasst.
keywords: Zeilen automatisch anpassen, Spalten automatisch anpassen, Zeile in einem Zellenbereich automatisch anpassen, Zeilen von zusammengeführten Zellen automatisch anpassen
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, die Breite und Höhe von Zellen automatisch an den Inhalt anzupassen. Diese Funktion ist auch über Aspose.Cells verfügbar, so dass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.

{{% /alert %}}

## **Automatische Anpassung**

Aspose.Cells stellt eine [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse bereit, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine breite Palette von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. Dieser Artikel beschäftigt sich mit der Verwendung der [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse zum automatischen Anpassen von Zeilen oder Spalten.

### **AutoFit Zeile - Einfach**

Der einfachste Ansatz, um die Breite und Höhe einer Zeile automatisch anzupassen, ist das Aufrufen der Methode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Die Methode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) erhält einen Zeilenindex (der zu ändernden Zeile) als Parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Wie man eine Zeile in einem Zellenbereich automatisch anpasst**

Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf dem Inhalt in einem Zellenbereich innerhalb der Zeile automatisch anzupassen, indem eine überladene Version der [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)-Methode aufgerufen wird. Sie nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

Die Methode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) prüft die Inhalte aller Spalten in der Zeile und passt dann die Zeile automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Wie man eine Spalte in einem Zellenbereich automatisch anpasst**

Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Zellenbereich in der Spalte automatisch anzupassen, indem eine überladene Version der Methode [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) aufgerufen wird, die die folgenden Parameter verwendet:

- **Spaltenindex**, der Index der zu automatisch anzupassenden Spalte.
- **Erster Zeilenindex**, der Index der ersten Zeile der Spalte.
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.

Die [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte dann automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Wie man Zeilen für zusammengeführte Zellen automatisch anpasst**

Mit Aspose.Cells ist es möglich, Zeilen auch für Zellen, die mit der [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)-API zusammengeführt wurden, automatisch anzupassen. Die [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)-Klasse bietet eine [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)-Eigenschaft, die zum automatischen Anpassen von Zeilen für zusammengeführte Zellen verwendet werden kann. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) akzeptiert eine [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)-Aufzählung, die die folgenden Elemente enthält.

- None: Zusammengeführte Zellen ignorieren.
- FirstLine: Erweitert nur die Höhe der ersten Zeile.
- LastLine: Erweitert nur die Höhe der letzten Zeile.
- EachLine: Erweitert nur die Höhe jeder Zeile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

Sie können auch die überladenen Versionen der [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows)- und [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)-Methoden verwenden, die einen Bereich von Zeilen/Spalten und eine Instanz von [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend Ihrer gewünschten [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) automatisch anzupassen.

Die Signaturen der genannten Methoden lauten wie folgt:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) Optionen)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) Optionen)

{{% /alert %}}

## **Wichtig zu wissen**

{{% alert color="primary" %}}

Wenn eine Zelle zusammengeführt ist, werden die AutoFit-Methoden nicht angewendet, was dasselbe Verhalten wie in Microsoft Excel ist. Sie können dies umgehen, indem Sie die Autofilter-API verwenden. Außerdem werden die [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)-Methode nicht angewendet, wenn der Text in einer Zelle umgebrochen ist. Eine weitere Sache, die Sie wissen müssen, ist, dass die *AutoFit*-Methoden zeitintensiv sind. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.

{{% /alert %}}

## **Erweiterte Themen**
- [Automatisches Anpassen von Zeilen für zusammengeführte Zellen](/cells/de/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
