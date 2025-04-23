---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben
type: docs
weight: 20
url: /de/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Anzahl von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie z.B. mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Genauigkeit kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

In diesem Artikel wird erklärt, wie Sie Aspose.Cells verwenden, um:

- [Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Ein Arbeitsblatt innerhalb einer Arbeitsmappe verschieben](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Ein Arbeitsblatt zwischen Arbeitsmappen kopieren](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Ein Arbeitsblatt zwischen Arbeitsmappen verschieben](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die Anfangsschritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xls (3 Arbeitsblätter)
- SecondWorkbook.xls (1 Arbeitsblatt).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Aspose.Cells for Java herunterladen](https://downloads.aspose.com/cells/java).
   1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen:
   1. Erstellen Sie ein Projekt mit einem Java-Editor wie Eclipse oder erstellen Sie ein einfaches Programm mit einem Texteditor.
1. Einen Klassenpfad hinzufügen:
   1. Extrahieren Sie die Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
   1. Setzen Sie den Klassenpfad des Projekts in Eclipse:
      1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie auf die Menüs **Projekt** und dann **Eigenschaften**.
      1. Wählen Sie **Java Build Path** auf der linken Seite des Dialogs aus und wählen Sie dann den Registerkarte Bibliotheken aus.
      1. Klicken Sie auf **JARs hinzufügen** oder **Externe JARs hinzufügen**, um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und in die Build-Pfade aufzunehmen.

{{% alert color="primary" %}}

Alternativ können Sie den Klassenpfad zur Laufzeit in einem DOS-Prompt unter Windows festlegen.
Zum Beispiel:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Arbeitsblatt innerhalb einer Arbeitsmappe kopieren:
   Nachstehend ist der verwendete Code, um die Aufgabe abzuschließen. Damit wird das Arbeitsblatt Kopie innerhalb von ErsteArbeitsmappe.xls kopiert.

Durch Ausführen des Codes wird das Arbeitsblatt mit dem neuen Namen Letztes Blatt von ErsteArbeitsmappe.xls verschoben.

**Ausgabedatei**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Bewegen eines Arbeitsblatts innerhalb einer Arbeitsmappe**

Im Folgenden finden Sie den Code, der zur Durchführung der Aufgabe verwendet wird.

Die Ausführung des Codes verschiebt das Arbeitsblatt "Move" vom Index 1 auf den Index 2 in der Datei FirstWorkbook.xls.

**Ausgabedatei**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt "Copy" mit dem neuen Namen "Sheet2" in die Datei SecondWorkbook.xls kopiert.

**Ausgabedatei**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Durch Ausführen des Codes wird das Arbeitsblatt "Move" aus FirstWorkbook.xls in SecondWorkbook.xls mit dem neuen Namen "Sheet3" verschoben.

**Ausgabe FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Ausgabe SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Fazit**

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie Arbeitsblätter innerhalb und zwischen Arbeitsmappen mithilfe von Aspose.Cells kopiert und verschoben werden.

Aspose.Cells hat von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert. Wir freuen uns über Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells-Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine prompte Antwort.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
