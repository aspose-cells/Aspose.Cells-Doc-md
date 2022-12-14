---
title: Kopieren und verschieben Sie Arbeitsblätter innerhalb und zwischen Arbeitsmappen
type: docs
weight: 80
url: /de/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie beispielsweise mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter inklusive Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und andere Objekte werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Kopieren und Verschieben von Arbeitsblättern**

### **Kopieren eines Arbeitsblatts innerhalb einer Arbeitsmappe**

Die ersten Schritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xlsx (3 Arbeitsblätter).
- SecondWorkbook.xlsx (1 Arbeitsblatt).

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installieren Sie es auf Ihrem Entwicklungscomputer.
 Alle[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. Erstellen Sie ein Projekt:
 1. Starten Sie Visual Studio.Net.
 1. Erstellen Sie eine neue Konsolenanwendung.
1. Referenzen hinzufügen:
 1. Fügen Sie dem Projekt einen Verweis auf Aspose.Cells hinzu.
 Fügen Sie beispielsweise einen Verweis auf ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu
1. Kopieren Sie das Arbeitsblatt in eine Arbeitsmappe
 Das erste Beispiel kopiert das erste Arbeitsblatt (Copy) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Copy mit dem Namen Last Sheet in FirstWorkbook.xlsx kopiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Verschieben eines Arbeitsblatts innerhalb einer Arbeitsmappe**

Der folgende Code zeigt, wie ein Arbeitsblatt von einer Position in einer Arbeitsmappe zu einer anderen verschoben wird. Durch Ausführen des Codes wird das Arbeitsblatt mit dem Namen Move from index 1 to index 2 in FirstWorkbook.xlsx verschoben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt mit dem Namen „Copy is“ in „SecondWorkbook.xlsx“ mit dem Namen „Sheet2“ kopiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt mit dem Namen „Move from FirstWorkbook.xlsx“ nach „SecondWorkbook.xlsx“ mit dem Namen „Sheet3“ verschoben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
