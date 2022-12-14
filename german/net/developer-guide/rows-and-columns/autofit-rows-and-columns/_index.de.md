---
title: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Mit Excel können Benutzer die Breite und Höhe von Zellen entsprechend ihrem Inhalt automatisch anpassen. Diese Funktion ist auch über Aspose.Cells verfügbar, sodass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.

{{% /alert %}}

## **Automatische Anpassung**

Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Dieser Artikel befasst sich mit der Verwendung von[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse zum automatischen Anpassen von Zeilen oder Spalten.

### **AutoFit Row - Einfach**

 Der einfachste Ansatz zur automatischen Größenanpassung der Breite und Höhe einer Zeile ist der Aufruf von the[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) Methode. Das[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)-Methode nimmt einen Zeilenindex (der Zeile, deren Größe geändert werden soll) als Parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **AutoFit Row in einem Bereich von Cells**

 Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf dem Inhalt in einem Bereich von Zellen innerhalb der Zeile automatisch anzupassen, indem eine überladene Version von aufgerufen wird[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Methode. Es nimmt die folgenden Parameter:

- **Zeilenindex**, der Index der Zeile, die automatisch angepasst werden soll.
- **Index der ersten Spalte**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

 Das[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)-Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile dann automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **AutoFit-Spalte in einem Bereich von Cells**

 Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf dem Inhalt in einem Bereich von Zellen in der Spalte automatisch anzupassen, indem eine überladene Version von aufgerufen wird[**Spalte automatisch anpassen**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Methode, die die folgenden Parameter akzeptiert:

- **Spaltenindex**der Index der Spalte, die automatisch angepasst werden soll.
- **Index der ersten Zeile**, der Index der ersten Zeile der Spalte.
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.

 Das[**Spalte automatisch anpassen**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte dann automatisch an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Zeilen automatisch anpassen für zusammengeführt Cells**

 Mit Aspose.Cells ist es möglich, Zeilen auch für Zellen automatisch anzupassen, die mit dem verbunden wurden[**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Klasse bietet[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) Eigenschaft, die zum automatischen Anpassen von Zeilen für verbundene Zellen verwendet werden kann.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)akzeptiert[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) aufzählbar, die die folgenden Mitglieder hat.

- Keine: Verbundene Zellen ignorieren.
- FirstLine: Erweitert nur die Höhe der ersten Zeile.
- LastLine: Erweitert nur die Höhe der letzten Zeile.
- EachLine: Erweitert nur die Höhe jeder Zeile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Sie können auch versuchen, die überladenen Versionen von zu verwenden[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Spalten automatisch anpassen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) Methoden, die eine Reihe von Zeilen/Spalten und eine Instanz von akzeptieren[**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) um die ausgewählten Zeilen/Spalten automatisch an die gewünschten anzupassen[**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)entsprechend.

Die Signaturen der oben genannten Methoden lauten wie folgt:

1.  AutoFitRows(int startRow, int endRow,[**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Optionen)
1. AutoFitColumns(int ersteSpalte, int letzteSpalte,[**AutoFitter-Optionen**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)Optionen)

{{% /alert %}}

## **Wichtig zu wissen**

{{% alert color="primary" %}}

 Wenn eine Zelle zusammengeführt wird, werden die AutoFit-Methoden nicht angewendet, was das gleiche Verhalten wie in Microsoft Excel ist. Sie können dies umgehen, indem Sie den Autofilter API verwenden. Außerdem wird, wenn der Text in einer Zelle umgebrochen wird, die[**Spalte automatisch anpassen**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) Methode wird auch nicht angewendet. Eine andere Sache, die Sie wissen müssen, ist, dass die*AutoFit*Methoden sind zeitaufwändig. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung sicherzustellen.

{{% /alert %}}

## **Themen vorantreiben**
- [Zeilen automatisch anpassen für zusammengeführt Cells](/cells/de/net/autofit-rows-for-merged-cells/)
