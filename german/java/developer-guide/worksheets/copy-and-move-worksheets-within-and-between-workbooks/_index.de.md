---
title: Kopieren und verschieben Sie Arbeitsblätter innerhalb und zwischen Arbeitsmappen
type: docs
weight: 20
url: /de/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie beispielsweise mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter inklusive Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und andere Objekte werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Kopieren und Verschieben von Arbeitsblättern**

In diesem Artikel wird erläutert, wie Sie Aspose.Cells verwenden, um:

- [Kopieren Sie ein Arbeitsblatt innerhalb einer Arbeitsmappe](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Verschieben Sie ein Arbeitsblatt innerhalb einer Arbeitsmappe](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Kopieren Sie ein Arbeitsblatt zwischen Arbeitsmappen](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Verschieben Sie ein Arbeitsblatt zwischen Arbeitsmappen](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Kopieren eines Arbeitsblatts innerhalb einer Arbeitsmappe**

Die ersten Schritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xls (3 Arbeitsblätter)
- SecondWorkbook.xls (1 Arbeitsblatt).

  **FirstWorkbook.xls**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
 Alle[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. Erstellen Sie ein Projekt:
 1. Erstellen Sie ein Projekt mit einem Java-Editor wie Eclipse oder erstellen Sie ein einfaches Programm mit einem Texteditor.
1. Klassenpfad hinzufügen:
1. Extrahieren Sie Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
 1. Legen Sie den Klassenpfad des Projekts in Eclipse fest:
 1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie auf Menüs**Projekt** , dann**Eigenschaften**.
 1. Wählen**Java Erstellungspfad** auf der linken Seite des Dialogs, dann wählen Sie die Registerkarte Bibliotheken,
 1. Klicken Sie auf**JARs hinzufügen** oder**Fügen Sie externe JARs hinzu** um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und sie zu Erstellungspfaden hinzuzufügen.

{{% alert color="primary" %}}

Oder Sie können den Klassenpfad zur Laufzeit in einer DOS-Eingabeaufforderung auf Windows festlegen.
Zum Beispiel:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Arbeitsblatt innerhalb einer Arbeitsmappe kopieren:
 Unten ist der Code, der von verwendet wird, um die Aufgabe auszuführen. Es kopiert das Arbeitsblatt Copy innerhalb von FirstWorkbook.xls.

Durch Ausführen des Codes wird das Arbeitsblatt mit dem Namen „Copy“ innerhalb von „FirstWorkbook.xls“ mit dem neuen Namen „Last Sheet“ verschoben.

**Ausgabedatei**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Verschieben eines Arbeitsblatts in einer Arbeitsmappe**

Nachfolgend finden Sie den Code, der zum Ausführen der Aufgabe verwendet wird.

Durch Ausführen des Codes wird das Arbeitsblatt Move von Index 1 nach Index 2 in FirstWorkbook.xls verschoben.

**Ausgabedatei**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt Copy nach SecondWorkbook.xls mit dem neuen Namen Sheet2 kopiert.

**Ausgabedatei**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt zum Verschieben von „FirstWorkbook.xls“ in „SecondWorkbook.xls“ mit dem neuen Namen „Sheet3“ verschoben.

**Geben Sie FirstWorkbook.xls aus**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Geben Sie SecondWorkbook.xls aus**

![todo: Bild_alt_Text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Fazit**

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie Arbeitsblätter innerhalb und zwischen Arbeitsmappen mithilfe von Aspose.Cells kopieren und verschieben.

 Aspose.Cells hat von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert. Wir freuen uns über Ihre Fragen, Kommentare und Anregungen unter[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine zeitnahe Antwort.

{{% /alert %}}
