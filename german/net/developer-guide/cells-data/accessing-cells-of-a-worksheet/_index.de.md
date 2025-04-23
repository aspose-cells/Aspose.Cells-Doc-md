---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/net/accessing-cells-of-a-worksheet/
description: Dieser Artikel zeigt, wie Sie den maximalen Anzeigebereich des Arbeitsblatts erhalten und auf die Zellen über die Aspose.Cells for .NET API zugreifen.
keywords: Hol Cell Objekt, Zugriff auf Zellen, Holen Sie sich den maximalen Anzeigebereich des Arbeitsblatts. 
---

{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die im Wesentlichen in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Bestandteil eines Arbeitsblatts, der dazu verwendet wird, das gesamte Arbeitsblatt als Abfolge von Zeilen und Spalten aufzubauen. Bevor wir versuchen, Daten aus einem Arbeitsblatt abzurufen, müssten wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze zur Laufzeitzugriff auf Arbeitsblattzellen erörtern, die Aspose.Cells verwendet.

{{% /alert %}}

## **Wie man auf Zellen zugreift**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält ein [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), das den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Wir können die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung verwenden, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet drei grundlegende Ansätze, um auf Zellen in einem Arbeitsblatt zuzugreifen:

1. Verwenden des Zellnamens
2. Verwendung von Zeilen- und Spaltenindex einer Zelle.
1. Verwenden eines Zellindexes in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung

**WICHTIG:** Es wurde erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, daher müssen Sie sich keine Sorgen um Leistungsverluste machen, egal welchen Ansatz Sie verwenden.

### **So erhalten Sie ein Zellenobjekt anhand des Zellnamens**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie ihren Zellnamen als Index an die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) übergeben.

Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, ist die Anzahl der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung null. Wenn Sie diesen Ansatz zum Zugriff auf eine Zelle verwenden, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, wird das Zellenobjekt in der Sammlung zurückgegeben; andernfalls wird ein neues [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Objekt erstellt, das Objekt der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung hinzugefügt und dann das Objekt zurückgegeben. Dieser Ansatz ist die einfachste Möglichkeit, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist im Vergleich zu anderen Ansätzen der langsamste.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zeilen- und Spaltenindexes der Zelle**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) übergeben.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zellindexes in der Zellensammlung**

Eine Zelle kann auch durch Übergabe des numerischen Index der Zelle an die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung abgerufen werden.

Wenn Sie diesen Ansatz zum Zugriff auf Zellen verwenden, kann eine Ausnahme ausgelöst werden, wenn der numerische Index der Zelle außerhalb des gültigen Bereichs liegt. Dieser Ansatz ist der schnellste, um auf die Zellen zuzugreifen, aber eine wichtige Sache zu wissen ist, dass der numerische Index nach Hinzufügen neuer Zellen zur [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung geändert werden kann. Die Zellenobjekte in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung sind intern nach Zeilen- und Spaltenindizes sortiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **So erhalten Sie die maximale Anzeigebereich des Arbeitsblatts**

Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich - der Bereich der Zellen zwischen der ersten und der letzten Zelle mit Inhalt - ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

Sie können den maximalen Anzeigebereich eines Arbeitsblatts mithilfe von [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) abrufen. Der folgende Beispielcode veranschaulicht, wie auf die [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)-Eigenschaft zugegriffen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
