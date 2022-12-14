---
title: Formen zwischen Arbeitsblättern kopieren
type: docs
weight: 250
url: /de/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

Manchmal müssen Sie je nach Bedarf verschiedene Bilder, Diagramme und andere Zeichnungsobjekte in verschiedene Arbeitsblätter kopieren. Aspose.Cells unterstützt das Kopieren von Formen zwischen Arbeitsblättern. Die Diagramme, Bilder und andere Objekte werden mit höchster Präzision kopiert.

Sie könnten Office Automation ausprobieren, aber das hat seine eigenen Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit, Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste darin besteht, dass Microsoft selbst dringend von der Office-Automatisierung durch Softwarelösungen abrät.

In diesem Artikel erstellen wir eine Konsolenanwendung, führen das Kopieren von Bildern, Diagrammen und anderen Zeichenobjekten zwischen Arbeitsblättern einer Arbeitsmappe mit wenigen und einfachsten Codezeilen unter Verwendung von Aspose.Cells durch.

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis dafür vermitteln, wie Formen (Bilder, Diagramme, Steuerelemente und andere Zeichenobjekte) zwischen Arbeitsblättern kopiert werden.

{{% /alert %}}

## **Formen kopieren**

In diesem Artikel wird erläutert, wie Sie:

- [Kopieren Sie ein Bild von einem Arbeitsblatt auf ein anderes](/cells/de/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Kopieren Sie ein Diagramm von einem Arbeitsblatt in ein anderes](/cells/de/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Kopieren Sie Steuerelemente und andere Zeichnungsobjekte von einem Arbeitsblatt in ein anderes](/cells/de/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Kopieren eines Bildes von einem Arbeitsblatt in ein anderes**

#### **Schritt 1: Erstellen einer Arbeitsmappe mit Bild und Diagramm in Microsoft Excel**

1. Erstellt eine neue Arbeitsmappe in Microsoft Excel.
1. Fügen Sie ein Bild auf dem ersten Arbeitsblatt und ein Diagramm auf dem zweiten Arbeitsblatt hinzu.

 Die folgenden Screenshots zeigen die beiden in Microsoft Excel erstellten Vorlagenarbeitsblätter.

   **Arbeitsblatt „Diagramm“ mit Diagramm**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_1.png)

**Arbeitsblatt „Bild“ mit Bild**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_2.png)

Kopieren Sie nun das Bild im Arbeitsblatt „Bild“ in das letzte Arbeitsblatt „Ergebnis“.

#### **Schritt 2: Laden Sie Aspose.Cells.Zip herunter**

1. [Herunterladen Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Entpacken Sie es auf Ihrem Entwicklungscomputer.

 Alle[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.

#### **Schritt 3: Erstellen Sie ein Projekt**

Sie können entweder ein Projekt mit einem Java-Editor erstellen, z. B. Eclipse, oder ein einfaches Programm mit einem NotePad erstellen.

#### **Schritt 4: Klassenpfad hinzufügen**

Um einen Klassenpfad mit Eclipse festzulegen, führen Sie bitte die folgenden Schritte aus:

1. Extrahieren Sie Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
1. Legen Sie den Klassenpfad des Projekts in Eclipse fest:
1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie dann auf Menüs Projekt-Eigenschaften.
1. Wählen Sie „Java Build Path“ auf der linken Seite des Popup-Fensters, wählen Sie dann die Registerkarte „Bibliotheken“, klicken Sie auf „JARs hinzufügen“ oder „Externe JARs hinzufügen“, um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und sie dem Build hinzuzufügen Pfade.
1. Schreiben Sie eine Anwendung, um APIs der Komponenten von Aspose aufzurufen.

Oder Sie können es zur Laufzeit an der DOS-Eingabeaufforderung in Windows einstellen. Beispiel:

javac -classpath %classpath%;e:\Aspose.Cells.jar; Klassenname .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Klassenname

#### **Schritt 5: Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

Im Folgenden finden Sie den Code zum Ausführen der Aufgabe. Es kopiert ein Bild aus dem Arbeitsblatt „Bild“ in das Arbeitsblatt „Ergebnis“.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Ergebnis Aufgabe 1:**

Nach Ausführung des obigen Codes wird nun das Bild aus dem Arbeitsblatt „Bild“ in das letzte Arbeitsblatt „Ergebnis“ kopiert

**Arbeitsblatt „Ergebnis“ mit kopiertem Bild**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_3.png)

### **Aufgabe 2: Kopieren eines Diagramms von einem Arbeitsblatt in ein anderes**

#### **Schritt 1: Kopieren Sie ein Diagramm von einem Arbeitsblatt in ein anderes**

Es folgt der eigentliche Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Ergebnisaufgabe 2**

Nach Ausführung des obigen Codes wird das Diagramm aus dem Arbeitsblatt „Diagramm“ in das Arbeitsblatt „Ergebnis“ kopiert. Bitte sehen Sie sich den folgenden Schnappschuss des resultierenden Arbeitsblatts an.

**Arbeitsblatt „Ergebnis“ mit kopiertem Bild und Diagramm**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_4.png)

### **Aufgabe 3: Kopieren von Steuerelementen und anderen Zeichenobjekten von einem Arbeitsblatt in ein anderes**

**Arbeitsblatt „Kontrolle“ mit Textfeld und Oval**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_5.png)

Bitte beachten Sie die folgenden einfachen Schritte, die Sie ausführen müssen, um die gewünschten Ergebnisse zu erzielen.

#### **Schritt 1: Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Das Folgende ist der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Ergebnisaufgabe 3**

Nach dem Ausführen des obigen Codes werden nun die Kontrollen aus dem Arbeitsblatt „Kontrolle“ in das Arbeitsblatt „Ergebnis“ kopiert. Bitte sehen Sie sich den folgenden Schnappschuss von „Ergebnis“ an.

**Arbeitsblatt „Ergebnis“ mit kopiertem Textfeld und Oval**

![todo: Bild_alt_Text](copy-shapes-between-worksheets_6.png)

## **Fazit**

Dieser Artikel hat gezeigt, wie Sie verschiedene Formen wie Bilder, Diagramme und andere Zeichnungsobjekte zwischen der Verwendung von Aspose.Cells kopieren können. Hoffentlich gibt es Ihnen einen Einblick und Sie können diese Optionen entsprechend Ihren verschiedenen Szenarien nutzen.

Aspose.Cells kann mehr Flexibilität als andere Lösungen bieten und bietet hervorragende Geschwindigkeit, Effizienz und Zuverlässigkeit, um spezifische Anforderungen von Geschäftsanwendungen zu erfüllen. Die Ergebnisse zeigen, dass Aspose.Cells von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert hat.

 Wir freuen uns sehr über Ihre Fragen, Kommentare und Anregungen im[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).
