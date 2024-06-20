---
title: Formen zwischen Arbeitsblättern kopieren
type: docs
weight: 250
url: /de/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Manchmal müssen Sie verschiedene Bilder, Diagramme und andere Zeichenobjekte je nach Bedarf in verschiedene Arbeitsblätter kopieren. Aspose.Cells unterstützt das Kopieren von Formen zwischen Arbeitsblättern. Die Diagramme, Bilder und andere Objekte werden mit höchster Genauigkeit kopiert.

Sie könnten Office Automation ausprobieren, aber das hat seine eigenen Nachteile. Es gibt mehrere Gründe und Probleme, z. B. Sicherheit, Stabilität, Skalierbarkeit, Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste darin besteht, dass Microsoft selbst dringend davon abrät, Office-Automatisierung aus Softwarelösungen.

In diesem Artikel erstellen wir eine Konsolenanwendung, führen das Kopieren von Bildern, Diagrammen und anderen Zeichenobjekten zwischen Arbeitsblättern eines Arbeitsmappen mit wenigen und einfachsten Codezeilen mithilfe von Aspose.Cells durch.

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis dafür vermitteln, wie Formen (Bilder, Diagramme, Steuerelemente und andere Zeichenobjekte) zwischen Arbeitsblättern kopiert werden.

{{% /alert %}}

## **Kopieren von Formen**

Dieser Artikel erklärt, wie:

- [Bild von einem Arbeitsblatt in ein anderes kopieren](/cells/de/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Kopieren Sie ein Diagramm von einem Arbeitsblatt auf ein anderes](/cells/de/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Kopieren Sie Steuerelemente und andere Zeichenobjekte von einem Arbeitsblatt auf ein anderes](/cells/de/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

#### **Schritt 1: Erstellen eines Arbeitsbuchs mit Bild und Diagramm in Microsoft Excel**

1. Erstellen Sie ein neues Arbeitsbuch in Microsoft Excel.
1. Fügen Sie ein Bild auf das erste Arbeitsblatt und ein Diagramm auf das zweite Arbeitsblatt ein.

   Die folgenden Screenshots zeigen die beiden Vorlagenarbeitsblätter, die in Microsoft Excel erstellt wurden.

   **Arbeitsblatt 'Diagramm' mit Diagramm**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Arbeitsblatt 'Bild' mit Bild**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Kopieren Sie nun das Bild im Arbeitsblatt mit dem Namen 'Bild' auf das letzte Arbeitsblatt 'Ergebnis'.

#### **Schritt 2: Download von Aspose.Cells.Zip**

1. [Aspose.Cells for Java herunterladen](https://downloads.aspose.com/cells/java).
1. Entpacken Sie es auf Ihrem Entwicklungscomputer.

   Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.

#### **Schritt 3: Erstellen eines Projekts**

Sie können entweder ein Projekt mit einem Java-Editor, z. B. Eclipse, erstellen oder ein einfaches Programm mit einem Notepad erstellen.

#### **Schritt 4: Klassenpfad hinzufügen**

Um einen Klassenpfad in Eclipse festzulegen, führen Sie bitte die folgenden Schritte aus:

1. Extrahieren Sie die Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
1. Setzen Sie den Klassenpfad des Projekts in Eclipse:
1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie dann auf Menüs Projekt-Eigenschaften.
1. Wählen Sie im linken Bereich des Popup-Fensters "Java Build Path" aus, wählen Sie dann die Registerkarte "Bibliotheken" aus, klicken Sie auf "JARs hinzufügen" oder "Externe JARs hinzufügen", um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und fügen Sie sie zu den Erstellungspfaden hinzu.
1. Schreiben Sie eine Anwendung, um die APIs der Aspose-Komponenten aufzurufen.

Oder Sie können ihn zur Laufzeit im DOS-Prompt in Windows festlegen. Zum Beispiel:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Schritt 5: Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

Im Folgenden finden Sie den Code, um die Aufgabe zu erledigen. Er kopiert ein Bild vom Arbeitsblatt mit dem Namen 'Bild' auf das Arbeitsblatt 'Ergebnis'.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Ergebnis Aufgabe 1:**

Nach Ausführung des obigen Codes wird das Bild aus dem Arbeitsblatt "Bild" nun in das letzte Arbeitsblatt "Ergebnis" kopiert

**Arbeitsblatt "Ergebnis" mit kopiertem Bild**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Aufgabe 2: Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes**

#### **Schritt 1: Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes**

Im Folgenden ist der tatsächlich verwendete Code des Komponenten zur Durchführung der Aufgabe aufgeführt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Ergebnis Aufgabe 2**

Nach Ausführung des obigen Codes wird das Diagramm aus dem Arbeitsblatt "Diagramm" in das Arbeitsblatt "Ergebnis" kopiert. Bitte beachten Sie den folgenden Schnappschuss des Ergebnis-Arbeitsblatts.

**Arbeitsblatt "Ergebnis" mit kopiertem Bild und Diagramm**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Aufgabe 3: Kopieren von Steuerelementen und anderen Zeichenobjekten von einem Arbeitsblatt auf ein anderes**

**Arbeitsblatt "Steuerelement" mit Textfeld und Oval**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Bitte beachten Sie die folgenden einfachen Schritte, die Sie ausführen müssen, um Ihre gewünschten Ergebnisse zu erzielen.

#### **Schritt 1: Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Im Folgenden finden Sie den von der Komponente verwendeten Code zur Durchführung der Aufgabe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Ergebnis Aufgabe 3**

Nach Ausführung des obigen Codes werden die Steuerelemente aus dem Arbeitsblatt "Steuerelement" nun in das Arbeitsblatt "Ergebnis" kopiert. Bitte sehen Sie sich den folgenden Schnappschuss von "Ergebnis" an.

**Arbeitsblatt "Ergebnis" mit kopiertem Textfeld und Oval**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Fazit**

Dieser Artikel hat gezeigt, wie man verschiedene Formen wie Bilder, Diagramme und andere Zeichenobjekte zwischen Verwendungen von Aspose.Cells kopiert. Hoffentlich wird es Ihnen einige Einblicke geben, und Sie werden in der Lage sein, diese Optionen gemäß Ihren unterschiedlichen Szenarien zu nutzen.

Aspose.Cells kann mehr Flexibilität als andere Lösungen bieten und bietet eine herausragende Geschwindigkeit, Effizienz und Zuverlässigkeit, um spezifische Geschäftsanforderungen zu erfüllen. Die Ergebnisse zeigen, dass Aspose.Cells von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert hat.

Wir heißen Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) herzlich willkommen.
