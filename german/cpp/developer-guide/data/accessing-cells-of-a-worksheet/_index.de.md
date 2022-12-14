---
title: Zugriff auf Cells eines Arbeitsblatts
type: docs
weight: 10
url: /de/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der verwendet wird, um das gesamte Arbeitsblatt als eine Folge von Zeilen und Spalten zu erstellen. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze für den Zugriff auf Arbeitsblattzellen zur Laufzeit mit Aspose.Cells erörtern.

{{% /alert %}} 
## **Zugriff auf Cells**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) die eine Excel-Datei darstellt. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Wir können benutzen[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt:

1. Zellname verwenden.
1. Verwenden des Zeilen- und Spaltenindex einer Zelle.
1.  Verwenden eines Zellenindex in der[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung

{{% alert color="primary" %}} 

Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, machen Sie sich also keine Sorgen über Leistungseinbußen, egal welchen Ansatz Sie verwenden.

{{% /alert %}} 
### **Verwendung des Namens Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie ihren Zellennamen an die übergeben[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Klasse als Index.

 Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, wird die Anzahl von[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung ist null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, gibt es das Zellobjekt in der Sammlung zurück, andernfalls erstellt es ein neues[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Objekt, fügt das Objekt dem hinzu[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung und gibt dann dieses Objekt zurück. Dieser Ansatz ist der einfachste Weg, um auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber im Vergleich zu anderen Ansätzen ist er der langsamste.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Verwenden des Zeilen- und Spaltenindex von Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die übergeben[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Klasse. Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**
Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich – der Zellbereich zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

 Mit können Sie auf den maximalen Anzeigebereich eines Arbeitsblatts zugreifen[MaxDisplayIRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) Methode der[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
