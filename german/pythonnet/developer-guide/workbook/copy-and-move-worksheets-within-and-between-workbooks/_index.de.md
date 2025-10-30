---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben
type: docs
weight: 80
url: /de/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Anzahl von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie z.B. mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells for Python via .NET unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter inklusive Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und andere Objekte werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die Anfangsschritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xlsx (3 Tabellenblätter).
- SecondWorkbook.xlsx (1 Tabellenblatt).

1. Laden Sie Aspose.Cells für Python via .NET herunter und installieren Sie es:
   1. [Download Aspose.Cells for Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Erstellen Sie ein Projekt und fügen Sie Verweise hinzu:   
1. Kopieren Sie das Tabellenblatt innerhalb einer Arbeitsmappe.
   Das erste Beispiel kopiert das erste Tabellenblatt (Kopie) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Kopie innerhalb von FirstWorkbook.xlsx mit dem Namen Last Sheet kopiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Verschieben eines Arbeitsblatts innerhalb eines Arbeitsmappes**

Der untenstehende Code zeigt, wie man ein Arbeitsblatt von einer Position in einer Arbeitsmappe an eine andere verschiebt. Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben vom Index 1 auf den Index 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes kopiert das Arbeitsblatt namens Kopie in SecondWorkbook.xlsx mit dem Namen Blatt2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben von FirstWorkbook.xlsx nach SecondWorkbook.xlsx mit dem Namen Blatt3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
{{< app/cells/assistant language="python-net" >}}
