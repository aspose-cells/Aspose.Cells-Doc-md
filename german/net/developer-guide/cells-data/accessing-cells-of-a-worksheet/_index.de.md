---
title: Zugriff auf Cells eines Arbeitsblatts
type: docs
weight: 10
url: /de/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der verwendet wird, um das gesamte Arbeitsblatt als eine Folge von Zeilen und Spalten zu erstellen. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze für den Zugriff auf Arbeitsblattzellen zur Laufzeit mit Aspose.Cells erörtern.

{{% /alert %}}

## **Zugriff auf Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Wir können benutzen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt:

1. Verwenden des Zellennamens.
1. Verwenden des Zeilen- und Spaltenindex einer Zelle.
1.  Verwenden eines Zellenindex in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung

**WICHTIG:**Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, machen Sie sich also keine Sorgen über Leistungseinbußen, egal welchen Ansatz Sie verwenden.

### **Verwendung des Namens Cell**

 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie ihren Zellennamen an die übergeben[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse als Index.

 Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, wird die Anzahl der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung ist null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, gibt es das Zellobjekt in der Sammlung zurück, andernfalls erstellt es ein neues[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Objekt, fügt das Objekt dem hinzu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung und gibt dann das Objekt zurück. Dieser Ansatz ist der einfachste Weg, um auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber im Vergleich zu anderen Ansätzen ist er der langsamste.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Verwenden des Zeilen- und Spaltenindex von Cell**

 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die übergeben[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Verwenden des Cell-Index in der Cells-Sammlung**

 Auf eine Zelle kann auch zugegriffen werden, indem der numerische Index der Zelle an die übergeben wird[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung.

 Wenn Sie diesen Ansatz verwenden, um auf Zellen zuzugreifen, kann eine Ausnahme ausgelöst werden, wenn der numerische Index der Zelle außerhalb des zulässigen Bereichs liegt. Dieser Ansatz ist der schnellste, um auf die Zellen zuzugreifen, aber es ist wichtig zu wissen, dass sich der numerische Index ändern kann, wenn Sie diesen Ansatz verwenden, um auf ein Zellenobjekt zuzugreifen, nachdem neue Zellen hinzugefügt wurden[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Die Zellobjekte in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung sind intern nach Zeilen- und Spaltenindizes sortiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**

Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich – der Zellbereich zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

 Mit können Sie auf den maximalen Anzeigebereich eines Arbeitsblatts zugreifen[**Arbeitsblatt.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Der folgende Beispielcode veranschaulicht den Zugriff auf die[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
