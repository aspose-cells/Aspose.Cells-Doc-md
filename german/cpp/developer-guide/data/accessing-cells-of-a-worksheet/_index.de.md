---
title: Zugriff auf Cells eines Arbeitsblatts
type: docs
weight: 10
url: /de/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der zum Aufbau des gesamten Arbeitsblatts als Folge von Zeilen und Spalten verwendet wird. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. In diesem Thema besprechen wir daher einige grundlegende Ansätze für den Zugriff auf Arbeitsblattzellen zur Laufzeit mithilfe von Aspose.Cells.

{{% /alert %}} 
##  **Zugriff auf Cells**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das eine Excel-Datei darstellt. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Wir können benutzen[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt:

1. Zellennamen verwenden.
1. Verwenden des Zeilen- und Spaltenindex einer Zelle.
1.  Verwenden eines Zellindex im[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung

{{% alert color="primary" %}} 

Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering. Machen Sie sich also keine Sorgen über Leistungseinbußen, egal welchen Ansatz Sie verwenden.

{{% /alert %}} 
###  **Verwenden Sie den Namen Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie ihren Zellennamen an übergeben[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse als Index.

 Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, beträgt die Anzahl der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung ist Null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird geprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, wird das Zellobjekt in der Sammlung zurückgegeben, andernfalls wird ein neues erstellt[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) Objekt, fügt das Objekt dem hinzu[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung und gibt dann dieses Objekt zurück. Dieser Ansatz ist der einfachste Weg, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber im Vergleich zu anderen Ansätzen ist er der langsamste.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Verwenden des Zeilen- und Spaltenindex von Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die übergeben[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse. Dieser Ansatz funktioniert auf die gleiche Weise wie der erste Ansatz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**
Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich – der Zellbereich zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts kopieren, auswählen oder in einem Bild anzeigen müssen.

Den maximalen Anzeigebereich eines Arbeitsblatts können Sie über erreichen[MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
