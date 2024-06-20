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
Der einfachste Ansatz zum automatischen Anpassen der Breite und Höhe einer Zeile besteht darin, die Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) der Klasse [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Arbeitsblatt) aufzurufen. Die Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) erfordert einen Zeilenindex (der zu ändernden Zeile) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Zeile in einem Bereich von Zellen**
Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf dem Inhalt in einem Bereich von Zellen in der Zeile automatisch anzupassen, indem sie eine überladene Version der Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) aufrufen. Sie nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

Die Methode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) überprüft den Inhalt aller Spalten in der Zeile und passt dann die Zeile automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Spalten automatisch anpassen - Einfach**
Der einfachste Weg, die Breite und Höhe einer Spalte automatisch anzupassen, besteht darin, die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) aufzurufen. Die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) nimmt den Spaltenindex (der zu ändernden Spalte) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Spalten in einem Zellenbereich automatisch anpassen**
Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Zellenbereich in der Spalte automatisch anzupassen, indem eine überladene Version der Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) aufgerufen wird, die die folgenden Parameter annimmt:

- **Spaltenindex**, stellt den Index der Spalte dar, deren Inhalt automatisch angepasst werden soll
- **Index der ersten Zeile**, stellt den Index der ersten Zeile der Spalte dar
- **Index der letzten Zeile**, stellt den Index der letzten Zeile der Spalte dar

Die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) überprüft den Inhalt aller Zeilen in der Spalte und passt dann die Spalte automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Automatisches Anpassen von Zeilen für zusammengeführte Zellen**
Mit Aspose.Cells ist es möglich, auch für zusammengeführte Zellen mit der API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) die Zeilen automatisch anzupassen. Die Klasse [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) bietet die Eigenschaft [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), die verwendet werden kann, um Zeilen für zusammengeführte Zellen automatisch anzupassen. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) akzeptiert das Enum [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) mit folgenden Elementen:

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Zusammengeführte Zellen ignorieren.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Nur die Höhe der ersten Zeile erweitern.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Nur die Höhe der letzten Zeile erweitern.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Nur die Höhe jeder Zeile erweitern.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Sie können auch die überladenen Versionen der Methoden [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) und [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) verwenden, die einen Bereich von Zeilen/Spalten und eine Instanz von [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) annehmen, um die ausgewählten Zeilen/Spalten entsprechend mit den gewünschten [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) automatisch anzupassen.

Die Signaturen der genannten Methoden lauten wie folgt:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Wichtig zu wissen**
{{% alert color="primary" %}} 

Wenn eine Zelle zusammengeführt ist, werden die *AutoFit*-Methoden nicht angewendet, was dem gleichen Verhalten wie in Microsoft Excel entspricht. Darüber hinaus wird die Methode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) auch nicht angewendet, wenn der Text in einer Zelle umgebrochen ist. Etwas, das Sie auch wissen müssen, ist, dass die *AutoFit*-Methoden zeitaufwändig sind. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.

{{% /alert %}}
