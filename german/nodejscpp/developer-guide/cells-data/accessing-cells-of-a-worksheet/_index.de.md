---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Dieser Artikel zeigt, wie man den maximalen Anzeigebereich des Arbeitsblatts erhält und Zellen über die API Aspose.Cells for Node.js via C++ zugreift.
keywords: Hol Cell Objekt, Zugriff auf Zellen, Holen Sie sich den maximalen Anzeigebereich des Arbeitsblatts. 
---

{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die im Wesentlichen in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Bestandteil eines Arbeitsblatts, der zum Aufbau des gesamten Arbeitsblatts als Abfolge von Zeilen und Spalten verwendet wird. Bevor wir versuchen, Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugang zu seinen Zellen erhalten. In diesem Thema werden wir einige grundlegende Ansätze zur Laufzeit Zugriff auf Arbeitsblattzellen mit Aspose.Cells for Node.js via C++ diskutieren.

{{% /alert %}}

## **Wie man auf Zellen zugreift**

Aspose.Cells for Node.js via C++ stellt eine Klasse bereit, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Wir können die Sammlung [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) verwenden, um Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells for Node.js via C++ bietet drei grundlegende Ansätze, um Zellen in einem Arbeitsblatt zuzugreifen:

1. Verwenden des Zellnamens
2. Verwendung von Zeilen- und Spaltenindex einer Zelle.
1. Verwenden eines Zellindexes in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung

**WICHTIG:** Es wurde erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, daher müssen Sie sich keine Sorgen um Leistungsverluste machen, egal welchen Ansatz Sie verwenden.

### **So erhalten Sie ein Zellenobjekt anhand des Zellnamens**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie ihren Zellnamen als Index an die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) übergeben.

Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, ist die Anzahl der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung null. Wenn Sie diesen Ansatz zum Zugriff auf eine Zelle verwenden, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, wird das Zellenobjekt in der Sammlung zurückgegeben; andernfalls wird ein neues [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Objekt erstellt, das Objekt der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung hinzugefügt und dann das Objekt zurückgegeben. Dieser Ansatz ist die einfachste Möglichkeit, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist im Vergleich zu anderen Ansätzen der langsamste.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zeilen- und Spaltenindexes der Zelle**

Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) übergeben.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **So erhalten Sie ein Zellenobjekt anhand des Zellindexes in der Zellensammlung**

Eine Zelle kann auch durch Übergabe des numerischen Index der Zelle an die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung abgerufen werden.

Wenn Sie diesen Ansatz zum Zugriff auf Zellen verwenden, kann eine Ausnahme ausgelöst werden, wenn der numerische Index der Zelle außerhalb des gültigen Bereichs liegt. Dieser Ansatz ist der schnellste, um auf die Zellen zuzugreifen, aber eine wichtige Sache zu wissen ist, dass der numerische Index nach Hinzufügen neuer Zellen zur [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung geändert werden kann. Die Zellenobjekte in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung sind intern nach Zeilen- und Spaltenindizes sortiert.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **So erhalten Sie die maximale Anzeigebereich des Arbeitsblatts**

Aspose.Cells for Node.js via C++ für Node.js via C++ ermöglicht es Entwicklern, den maximalen Anzeige-Bereich eines Arbeitsblatts zuzugreifen. Der maximale Anzeigebereich – der Bereich der Zellen zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts kopieren, auswählen oder anzeigen möchten.

Sie können den maximalen Anzeigebereich eines Arbeitsblatts mithilfe von [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) abrufen. Der folgende Beispielcode veranschaulicht, wie auf die [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)-Eigenschaft zugegriffen wird.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
