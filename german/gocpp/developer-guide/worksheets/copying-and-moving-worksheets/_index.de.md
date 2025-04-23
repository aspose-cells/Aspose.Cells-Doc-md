---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/go-cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Ein Arbeitsblatt einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und andere Objekte werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Die folgenden Schritte sind beim Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel beteiligt.

1. Um Blätter zu einem anderen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Klicken Sie im Dialogfeld **Zu Arbeitsbuch** auf das Arbeitsbuch, um die Blätter zu empfangen.
1. Um die ausgewählten Blätter in ein neues Arbeitsbuch zu verschieben oder zu kopieren, klicken Sie auf **Neues Buch**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.

### **Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells kopieren**

Aspose.Cells bietet eine überladene Methode [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/), die verwendet wird, um ein Arbeitsblatt zu der Sammlung hinzuzufügen und Daten von einem bestehenden Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quell-Arbeitsblatts als Parameter. Die andere Version verwendet den Namen des Quell-Arbeitsblatts. Das folgende Beispiel zeigt, wie ein bestehendes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**

Aspose.Cells bietet die Methode [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/), um ein Arbeitsblatt an einen anderen Ort im selben Spreadsheet zu verschieben. Diese Methode nimmt den Ziel-Arbeitsblattindex als Parameter. Das folgende Beispiel zeigt, wie ein Arbeitsblatt an eine andere Stelle innerhalb der Arbeitsmappe verschoben wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
