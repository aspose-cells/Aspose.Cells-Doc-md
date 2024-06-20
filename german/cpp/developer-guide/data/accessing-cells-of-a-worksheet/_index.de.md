---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die im Wesentlichen in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Bestandteil eines Arbeitsblatts, der dazu verwendet wird, das gesamte Arbeitsblatt als Abfolge von Zeilen und Spalten aufzubauen. Bevor wir versuchen, Daten aus einem Arbeitsblatt abzurufen, müssten wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze zur Laufzeitzugriff auf Arbeitsblattzellen erörtern, die Aspose.Cells verwendet.

{{% /alert %}} 
## **Zugriff auf Zellen**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Wir können die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung verwenden, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt:

1. Verwendung des Zellnamens.
2. Verwendung von Zeilen- und Spaltenindex einer Zelle.
3. Verwendung eines Zellenindexes in der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung

{{% alert color="primary" %}} 

Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, daher müssen Sie sich keine Sorgen um Leistungsverschlechterung machen, welchen Ansatz Sie auch wählen.

{{% /alert %}} 
### **Verwendung des Zellnamens**
Entwickler können auf eine bestimmte Zelle zugreifen, indem sie ihren Zellnamen an die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse als Index übergeben.

Wenn Sie am Anfang ein leeres Arbeitsblatt erstellen, ist die Anzahl der Elemente in der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist. Wenn ja, wird das Zellenobjekt in der Sammlung zurückgegeben, andernfalls wird ein neues [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Objekt erstellt, das Objekt zur [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung hinzugefügt und dann dieses Objekt zurückgegeben. Dieser Ansatz ist der einfachste Weg, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist im Vergleich zu anderen Ansätzen der langsamste.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Verwenden von Zeilen- und Spaltenindex der Zelle**
Entwickler können auf eine bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse übergeben. Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**
Aspose.Cells ermöglicht es Entwicklern, auf den maximalen Anzeigebereich eines Arbeitsblatts zuzugreifen. Der maximale Anzeigebereich - der Bereich von Zellen zwischen der ersten und der letzten Zelle mit Inhalt - ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

Sie können den maximalen Anzeigebereich eines Arbeitsblatts mithilfe der [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)-Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung abrufen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
