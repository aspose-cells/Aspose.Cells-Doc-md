---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/python-net/autofit-rows-and-columns/
description: Dieser Artikel zeigt, wie man Reihen, Spalten, Reihen zusammengeführter Zellen und eine Zeile in einem Zellenbereich mittels der Aspose.Cells für Python via .NET API automatisch anpasst.
keywords: Python Excel Bibliothek, Python Autofit Reihen, Python Autofit Spalten, Python Autofit Reihe in einem Zellenbereich, Python Autofit Reihen zusammengeführter Zellen.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, die Breite und Höhe von Zellen entsprechend ihrem Inhalt automatisch anzupassen. Diese Funktion steht auch über Aspose.Cells für Python via .NET zur Verfügung, so dass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.

{{% /alert %}}

## **Automatische Anpassung**

Aspose.Cells für Python via .NET bietet eine [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. Dieser Artikel beschäftigt sich mit der Verwendung der [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse zur automatischen Anpassung von Reihen oder Spalten.

### **AutoFit Zeile - Einfach**

Der einfachste Ansatz, um die Breite und Höhe einer Zeile automatisch anzupassen, ist das Aufrufen der Methode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Die Methode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) erhält einen Zeilenindex (der zu ändernden Zeile) als Parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Wie man eine Zeile in einem Zellenbereich automatisch anpasst**

Eine Zeile besteht aus vielen Spalten. Aspose.Cells für Python via .NET ermöglicht Entwicklern, eine Zeile anhand des Inhalts in einem Zellenbereich innerhalb der Zeile automatisch anzupassen, indem sie eine überladene Version der Methode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) aufrufen. Diese Methode nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

Die Methode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) prüft die Inhalte aller Spalten in der Zeile und passt dann die Zeile automatisch an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Wie man eine Spalte in einem Zellenbereich automatisch anpasst**

Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Zellenbereich in der Spalte automatisch anzupassen, indem eine überladene Version der Methode [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) aufgerufen wird, die die folgenden Parameter verwendet:

- **Spaltenindex**, der Index der zu automatisch anzupassenden Spalte.
- **Erster Zeilenindex**, der Index der ersten Zeile der Spalte.
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.

Die [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte dann automatisch an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Wie man Zeilen für zusammengeführte Zellen automatisch anpasst**

Mit Aspose.Cells for Python via .NET ist es möglich, Zeilen auch für Zellen automatisch anzupassen, die mithilfe der API [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) zusammengeführt wurden. Die Klasse [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) bietet die Eigenschaft [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/), die zum automatischen Anpassen von Zeilen für zusammengeführte Zellen verwendet werden kann. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) akzeptiert eine [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype)-Auflistung, die die folgenden Elemente enthält.

- NONE: Zusammengeführte Zellen ignorieren.
- FIRST_LINE: Erweitert nur die Höhe der ersten Zeile.
- LAST_LINE: Erweitert nur die Höhe der letzten Zeile.
- EACH_LINE: Erweitert nur die Höhe jeder Zeile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

Sie können auch die überladenen Versionen der [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions)- und [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions)-Methoden verwenden, die einen Bereich von Zeilen/Spalten und eine Instanz von [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend Ihrer gewünschten [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) automatisch anzupassen.

Die Signaturen der genannten Methoden lauten wie folgt:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) Optionen)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Wichtig zu wissen**

{{% alert color="primary" %}}

Wenn eine Zelle zusammengeführt ist, werden die AutoFit-Methoden nicht angewendet, was dasselbe Verhalten wie in Microsoft Excel ist. Sie können dies umgehen, indem Sie die Autofilter-API verwenden. Außerdem werden die [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)-Methode nicht angewendet, wenn der Text in einer Zelle umgebrochen ist. Eine weitere Sache, die Sie wissen müssen, ist, dass die *AutoFit*-Methoden zeitintensiv sind. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.

{{% /alert %}}

## **Erweiterte Themen**
- [Automatisches Anpassen von Zeilen für zusammengeführte Zellen](/cells/de/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
