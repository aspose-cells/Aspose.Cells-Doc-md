---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel bietet eine gute Funktion, um die Breite und Höhe einer Zelle entsprechend ihrem Inhalt automatisch anzupassen. Diese Funktion ist auch für Aspose.Cells-Benutzer verfügbar, mit der Möglichkeit, die Abmessungen einer Zelle zur Laufzeit automatisch anzupassen.

{{% /alert %}} 
## **Automatische Anpassung**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Dieser Artikel befasst sich mit der Verwendung von[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse zum automatischen Anpassen von Zeilen oder Spalten.
### **AutoFit Row - Einfach**
 Der einfachste Ansatz zur automatischen Größenanpassung der Breite und Höhe einer Zeile ist der Aufruf von the[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) Methode. Das[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\))-Methode nimmt einen Zeilenindex (der Zeile, deren Größe geändert werden soll) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Row in einem Bereich von Cells**
 Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf dem Inhalt in einem Bereich von Zellen innerhalb der Zeile automatisch anzupassen, indem eine überladene Version von aufgerufen wird[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) Methode. Es nimmt die folgenden Parameter:

- **Zeilenindex**, der Index der Zeile, die automatisch angepasst werden soll.
- **Index der ersten Spalte**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

 Das[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))-Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile dann automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **AutoFit-Spalte - Einfach**
 Die einfachste Möglichkeit, die Breite und Höhe einer Spalte automatisch anzupassen, ist der Aufruf von the[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse'[autoFitSpalte](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) Methode. Das[autoFitSpalte](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))-Methode nimmt den Spaltenindex (der Spalte, deren Größe geändert werden soll) als Parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit-Spalte in einem Bereich von Cells**
 Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Bereich von Zellen in der Spalte automatisch anzupassen, indem eine überladene Version von aufgerufen wird[autoFitSpalte](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\))-Methode, die die folgenden Parameter akzeptiert:

- **Spaltenindex**, stellt den Index der Spalte dar, deren Inhalt automatisch angepasst werden muss
- **Index der ersten Zeile**, stellt den Index der ersten Zeile der Spalte dar
- **Letzter Zeilenindex**, stellt den Index der letzten Zeile der Spalte dar

 Das[autoFitSpalte](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\))-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte dann automatisch an.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Zeilen automatisch anpassen für zusammengeführt Cells**
Mit Aspose.Cells ist es möglich, Zeilen auch für Zellen automatisch anzupassen, die mit dem verbunden wurden[AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)Klasse bietet[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)Eigenschaft, die zum automatischen Anpassen von Zeilen für verbundene Zellen verwendet werden kann.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)akzeptiert[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)aufzählbar, die die folgenden Mitglieder hat.

- [KEINER](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Verbundene Zellen ignorieren.
- [ERSTE LINIE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Erweitert nur die Höhe der ersten Zeile.
- [LETZTE LINIE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Erweitert nur die Höhe der letzten Zeile.
- [JEDE ZEILE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Erweitert nur die Höhe jeder Zeile.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Sie können auch die überladenen Versionen von verwenden[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) Methoden, die eine Reihe von Zeilen/Spalten und eine Instanz von akzeptieren[AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) um die ausgewählten Zeilen/Spalten automatisch mit den gewünschten anzupassen[AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)entsprechend.

Die Signaturen der oben genannten Methoden sind wie folgt:

1.  autoFitRows(int startRow, int endRow,[AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)Optionen)
1.  autoFitColumns(int ersteSpalte, int letzteSpalte,[AutoFitter-Optionen](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)Optionen)
## **Wichtig zu wissen**
{{% alert color="primary" %}} 

 Wenn eine Zelle zusammengeführt wird, dann die*AutoFit* Methoden werden nicht angewendet, was das gleiche Verhalten wie in Microsoft Excel ist. Wenn der Text in einer Zelle umbrochen wird, wird außerdem die[autoFitSpalte](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) )-Methode wird ebenfalls nicht angewendet. Eine andere Sache, die Sie wissen müssen, ist, dass die*AutoFit*Methoden sind zeitaufwändig. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung sicherzustellen.

{{% /alert %}}
