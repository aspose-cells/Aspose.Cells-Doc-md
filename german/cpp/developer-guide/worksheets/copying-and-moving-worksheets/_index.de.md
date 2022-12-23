---
title: Kopieren und Verschieben von Arbeitsblättern
type: docs
weight: 10
url: /de/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamen Formatierungen und Daten. Wenn Sie beispielsweise mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Ein Arbeitsblatt mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten wird mit höchster Präzision kopiert.

{{% /alert %}} 
## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**
Im Folgenden sind die Schritte zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel aufgeführt.

1. Um Blätter in eine andere Arbeitsmappe zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1.  Auf der**Bearbeiten** Menü, klicken**Blatt verschieben oder kopieren**.
1.  Im**Buchen** Klicken Sie im Dialogfeld auf die Arbeitsmappe, um die Blätter zu erhalten.
1.  Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf**Neues Buch**.
1.  Im**Vor Blatt** klicken Sie auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1.  Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie aus**Erstellen Sie eine Kopie** Kontrollkästchen.
### **Kopieren Sie Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells**
 Aspose.Cells bietet eine überladene Methode[HinzufügenKopie()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)die verwendet wird, um der Sammlung ein Arbeitsblatt hinzuzufügen und Daten aus einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts. Das folgende Beispiel zeigt, wie Sie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopieren.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **Arbeitsblätter innerhalb der Arbeitsmappe verschieben**
 Aspose.Cells stellt eine Methode bereit[Ziehen nach()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)die verwendet wird, um ein Arbeitsblatt an eine andere Stelle in derselben Tabelle zu verschieben. Die Methode nimmt den Index des Zielarbeitsblatts als Parameter. Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle innerhalb der Arbeitsmappe verschieben.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}
