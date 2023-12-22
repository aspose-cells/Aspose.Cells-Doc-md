---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Manchmal benötigen Sie mehrere Arbeitsblätter mit gemeinsamen Formatierungen und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Ein Arbeitsblatt mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten wird mit höchster Präzision kopiert.

{{% /alert %}} 
##  **Verschieben oder Kopieren von Blättern mit Microsoft Excel**
Im Folgenden sind die Schritte aufgeführt, die zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel erforderlich sind.

1. Um Blätter in eine andere Arbeitsmappe zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1.  Auf der**Bearbeiten** Klicken Sie im Menü auf *Blatt verschieben oder kopieren**.
1. Im**Buchen** Klicken Sie im Dialogfeld auf die Arbeitsmappe, um die Blätter zu erhalten.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf *Neues Buch**.
1. Im**Vor Blatt** Klicken Sie im Feld auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1.  Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie das aus**Erstellen Sie eine Kopie** Kontrollkästchen.
###  **Kopieren Sie Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells**
 Aspose.Cells stellt eine überladene Methode bereit[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)Dies wird verwendet, um der Sammlung ein Arbeitsblatt hinzuzufügen und Daten aus einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode verwendet den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts. Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Verschieben Sie Arbeitsblätter innerhalb der Arbeitsmappe**
 Aspose.Cells bietet eine Methode[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)mit dem ein Arbeitsblatt an eine andere Stelle in derselben Tabelle verschoben werden kann. Die Methode verwendet den Zielarbeitsblattindex als Parameter. Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle in der Arbeitsmappe verschieben.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
