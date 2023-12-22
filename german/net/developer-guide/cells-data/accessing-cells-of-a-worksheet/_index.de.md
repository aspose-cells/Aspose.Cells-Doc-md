---
title: Zugriff auf Cells eines Arbeitsblatts
type: docs
weight: 10
url: /de/net/accessing-cells-of-a-worksheet/
description: In diesem Artikel wird gezeigt, wie Sie über Aspose.Cells for .NET API den maximalen Anzeigebereich von Arbeitsblättern und Zugriffszellen erreichen.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der zum Aufbau des gesamten Arbeitsblatts als Folge von Zeilen und Spalten verwendet wird. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. In diesem Thema besprechen wir daher einige grundlegende Ansätze für den Zugriff auf Arbeitsblattzellen zur Laufzeit mithilfe von Aspose.Cells.

{{% /alert %}}

##  **So erreichen Sie Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das eine Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Dies ermöglicht den Zugriff auf jedes Arbeitsblatt in der Excel-Datei. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Wir können benutzen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt:

1. Verwendung des Zellennamens.
1. Verwenden des Zeilen- und Spaltenindex einer Zelle.
1.  Verwenden eines Zellindex im[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung

**WICHTIG:**Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering. Machen Sie sich also keine Sorgen über Leistungseinbußen, egal welchen Ansatz Sie verwenden.

###  **So erhalten Sie das Cell-Objekt anhand des Cell-Namens**

 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie ihren Zellennamen an übergeben[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse als Index.

 Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, beträgt die Anzahl der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung ist Null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird geprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, wird das Zellobjekt in der Sammlung zurückgegeben, andernfalls wird ein neues erstellt[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Objekt, fügt das Objekt dem hinzu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung und gibt dann das Objekt zurück. Dieser Ansatz ist der einfachste Weg, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber im Vergleich zu anderen Ansätzen ist er der langsamste.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **So erhalten Sie den Cell-Objekt-nach-Zeilen- und Spaltenindex von Cell**

 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die übergeben[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

Dieser Ansatz funktioniert auf die gleiche Weise wie der erste Ansatz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **So erhalten Sie das Cell-Objekt nach Cell-Index in der Cells-Sammlung**

 Auf eine Zelle kann auch zugegriffen werden, indem der numerische Index der Zelle an übergeben wird[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung.

Wenn Sie diesen Ansatz für den Zugriff auf Zellen verwenden, kann eine Ausnahme ausgelöst werden, wenn der numerische Index der Zelle außerhalb des gültigen Bereichs liegt. Dieser Ansatz ist der schnellste, um auf die Zellen zuzugreifen. Es ist jedoch wichtig zu wissen, dass sich der numerische Index ändern kann, wenn Sie diesen Ansatz für den Zugriff auf ein Zellobjekt verwenden, nachdem dem Objekt neue Zellen hinzugefügt wurden[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Die Zellobjekte in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Die Sammlung wird intern nach Zeilen- und Spaltenindizes sortiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **So erhalten Sie den maximalen Anzeigebereich des Arbeitsblatts**

Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich – der Zellbereich zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts kopieren, auswählen oder in einem Bild anzeigen müssen.

Den maximalen Anzeigebereich eines Arbeitsblatts können Sie über erreichen[**Arbeitsblatt.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Der folgende Beispielcode veranschaulicht den Zugriff auf[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
