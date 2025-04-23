---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel bietet eine gute Funktion zum automatischen Anpassen der Breite und Höhe einer Zelle gemäß ihrem Inhalt. Diese Funktion steht auch Aspose.Cells-Benutzern mit der Möglichkeit zur Verfügung, die Abmessungen einer Zelle zur Laufzeit automatisch anzupassen.

{{% /alert %}} 
## **Automatische Anpassung**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht.

Eine Arbeitsmappe wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. In diesem Artikel wird die Verwendung der [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse zum automatischen Anpassen von Zeilen oder Spalten behandelt.
### **AutoFit Zeile - Einfach**
Der direkteste Ansatz zur automatischen Anpassung der Breite und Höhe einer Zeile besteht darin, die Methode [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) aufzurufen. Die Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Zeile in einem Bereich von Zellen**
Eine Zeile besteht aus vielen Spalten. Aspose.Cells erlaubt Entwicklern, eine Zeile automatisch an den Inhalt innerhalb eines Zellbereichs anzupassen, indem eine überladene Version der Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) aufgerufen wird. Diese Methode nimmt folgende Parameter:

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

Die Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) prüft die Inhalte aller Spalten in der Zeile und passt die Zeile automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Spalten automatisch anpassen - Einfach**
Der einfachste Weg, die Breite und Höhe einer Spalte automatisch anzupassen, ist die Verwendung der Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) der [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) akzeptiert den Spaltenindex (der Spalte, die angepasst werden soll) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Spalten in einem Zellenbereich automatisch anpassen**
Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf den Inhalt in einem Zellbereich in der Spalte anzupassen, indem eine überladene Version der [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) Methode aufgerufen wird, die folgende Parameter akzeptiert:

- **Spaltenindex**, stellt den Index der Spalte dar, deren Inhalt automatisch angepasst werden soll
- **Index der ersten Zeile**, stellt den Index der ersten Zeile der Spalte dar
- **Index der letzten Zeile**, stellt den Index der letzten Zeile der Spalte dar

Die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) überprüft die Inhalte aller Zeilen in der Spalte und passt die Spalte entsprechend automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Automatisches Anpassen von Zeilen für zusammengeführte Zellen**
Mit Aspose.Cells ist es möglich, auch für zusammengeführte Zellen mit der API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) die Zeilen automatisch anzupassen. Die Klasse [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) bietet die Eigenschaft [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), die verwendet werden kann, um Zeilen für zusammengeführte Zellen automatisch anzupassen. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) akzeptiert das Enum [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) mit folgenden Elementen:

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Zusammengeführte Zellen ignorieren.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): Erweitert nur die Höhe der ersten Zeile.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): Erweitert nur die Höhe der letzten Zeile.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): Erweitert nur die Höhe jeder Zeile.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Sie können auch die überladenen Versionen von [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) verwenden, die einen Bereich von Zeilen/Spalten und eine Instanz von [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend den gewünschten [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) automatisch anzupassen.

Die Signaturen der genannten Methoden lauten wie folgt:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Wichtig zu wissen**
{{% alert color="primary" %}} 

Wenn eine Zelle zusammengeführt ist, werden die *AutoFit*-Methoden nicht angewendet, was das gleiche Verhalten wie in Microsoft Excel ist. Außerdem wird die [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) Methode ebenfalls nicht angewendet, wenn der Text in einer Zelle umbrochen ist. Eine weitere wichtige Information ist, dass die *AutoFit*-Methoden zeitaufwendig sind. Daher sollten Sie diese Methoden so sparsam wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
