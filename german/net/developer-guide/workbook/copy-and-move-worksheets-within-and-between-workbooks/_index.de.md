---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben
type: docs
weight: 80
url: /de/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Anzahl von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie z.B. mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Genauigkeit kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die Anfangsschritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xlsx (3 Tabellenblätter).
- SecondWorkbook.xlsx (1 Tabellenblatt).

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Laden Sie Aspose.Cells for .NET herunter](https://downloads.aspose.com/cells/net).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio.Net.
   1. Erstellen Sie eine neue Konsolenanwendung.
1. Fügen Sie Verweise hinzu:
   1. Fügen Sie dem Projekt einen Verweis auf Aspose.Cells hinzu.
      Fügen Sie beispielsweise einen Verweis auf ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu.
1. Kopieren Sie das Tabellenblatt innerhalb einer Arbeitsmappe.
   Das erste Beispiel kopiert das erste Tabellenblatt (Kopie) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Kopie innerhalb von FirstWorkbook.xlsx mit dem Namen Last Sheet kopiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Verschieben eines Arbeitsblatts innerhalb eines Arbeitsmappes**

Der untenstehende Code zeigt, wie man ein Arbeitsblatt von einer Position in einer Arbeitsmappe an eine andere verschiebt. Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben vom Index 1 auf den Index 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes kopiert das Arbeitsblatt namens Kopie in SecondWorkbook.xlsx mit dem Namen Blatt2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben von FirstWorkbook.xlsx nach SecondWorkbook.xlsx mit dem Namen Blatt3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
