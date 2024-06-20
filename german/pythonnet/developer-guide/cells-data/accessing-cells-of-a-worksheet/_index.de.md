---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/python-net/accessing-cells-of-a-worksheet/
description: Dieser Artikel zeigt, wie Sie den maximalen Anzeigebereich des Arbeitsblatts erhalten und auf Zellen durch die Aspose.Cells für Python via .NET API zugreifen.
keywords: Python Excel Bibliothek, Zell Objekt abrufen, auf Zellen zugreifen, Wie Sie das Zell Objekt nach Zeilen & Spaltenindex der Zelle erhalten, Wie Sie das Zell Objekt nach Zellindex in Zellensammlung erhalten, Wie Sie das Zell Objekt nach Zeilen & Spaltenindex der Zelle erhalten, Höchsten Anzeigebereich des Arbeitsblatts erhalten. 
---

{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Bestandteil eines Arbeitsblatts, der verwendet wird, um das gesamte Arbeitsblatt als Sequenz von Zeilen und Spalten zu erstellen. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssten wir Zugriff auf seine Zellen erhalten. In diesem Thema werden wir daher einige grundlegende Ansätze zur Laufzeitzugriff auf Arbeitsblattzellen mithilfe von Aspose.Cells für Python via .NET diskutieren.

{{% /alert %}}

## **Wie man auf Zellen zugreift**

Aspose.Cells für Python via .NET stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), zur Verfügung, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Wir können die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung verwenden, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells für Python via .NET bietet drei grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt:

1. Verwenden des Zellnamens
2. Verwendung von Zeilen- und Spaltenindex einer Zelle.
1. Verwenden eines Zellindexes in der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung

**WICHTIG:** Es wurde erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, daher müssen Sie sich keine Sorgen um Leistungsverluste machen, egal welchen Ansatz Sie verwenden.

### **So erhalten Sie ein Zellenobjekt anhand des Zellnamens**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie ihren Zellnamen als Index an die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) übergeben.

Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, ist die Anzahl der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung null. Wenn Sie diesen Ansatz zum Zugriff auf eine Zelle verwenden, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, wird das Zellenobjekt in der Sammlung zurückgegeben; andernfalls wird ein neues [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Objekt erstellt, das Objekt der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung hinzugefügt und dann das Objekt zurückgegeben. Dieser Ansatz ist die einfachste Möglichkeit, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist im Vergleich zu anderen Ansätzen der langsamste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zeilen- und Spaltenindexes der Zelle**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) übergeben.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zellindexes in der Zellensammlung**

Eine Zelle kann auch durch Übergabe des numerischen Index der Zelle an die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung abgerufen werden.

Wenn Sie diesen Ansatz zum Zugriff auf Zellen verwenden, kann eine Ausnahme ausgelöst werden, wenn der numerische Index der Zelle außerhalb des gültigen Bereichs liegt. Dieser Ansatz ist der schnellste, um auf die Zellen zuzugreifen, aber eine wichtige Sache zu wissen ist, dass der numerische Index nach Hinzufügen neuer Zellen zur [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung geändert werden kann. Die Zellenobjekte in der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung sind intern nach Zeilen- und Spaltenindizes sortiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **So erhalten Sie die maximale Anzeigebereich des Arbeitsblatts**

Aspose.Cells für Python via .NET ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich - der Bereich von Zellen zwischen der ersten und der letzten Zelle mit Inhalt - ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

Sie können den maximalen Anzeigebereich eines Arbeitsblatts mithilfe von [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/) abrufen. Der folgende Beispielcode veranschaulicht, wie auf die [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)-Eigenschaft zugegriffen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
