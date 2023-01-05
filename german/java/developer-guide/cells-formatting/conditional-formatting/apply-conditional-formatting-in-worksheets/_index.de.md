---
title: Wenden Sie bedingte Formatierung in Arbeitsblättern an
type: docs
weight: 40
url: /de/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie Sie einer Reihe von Zellen in einem Arbeitsblatt eine bedingte Formatierung hinzufügen.

Die bedingte Formatierung ist eine erweiterte Funktion in Microsoft Excel, mit der Sie Formate auf einen Bereich von Zellen anwenden und diese Formatierung abhängig vom Wert der Zelle oder dem Wert einer Formel ändern können. Beispielsweise kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte für einen positiven Wert grün sein. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Wenn der Wert der Zelle die Formatbedingung nicht erfüllt, wird die Standardformatierung der Zelle verwendet.

Es ist möglich, bedingte Formatierung mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Dafür gibt es mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund für die Suche nach einer anderen Lösung ist, dass Microsoft selbst dringend von Office Automation für Softwarelösungen abrät.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung erstellen und Zellen mit ein paar einfachsten Codezeilen mit Aspose.Cells API bedingt formatieren.

{{% /alert %}}

## **Arbeiten mit bedingter Formatierung**

Dieser Artikel behandelt die folgenden Aufgaben:

1. [Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf dem Zellenwert](/cells/de/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf einer Formel](/cells/de/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Aufgabe 1: Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf dem Wert von Cell**

1. **Laden Sie Aspose.Cells.zip herunter und installieren Sie es**:
   1. [Download](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
 Alle Aspose-Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. **Erstellen Sie ein Projekt**.
 Erstellen Sie entweder ein Projekt mit einem Java Editor wie Eclipse oder erstellen Sie ein einfaches Programm mit einem Texteditor.
1. **Klassenpfad hinzufügen**.
 Um einen Klassenpfad mit Eclipse festzulegen, führen Sie bitte die folgenden Schritte aus:
1. Extrahieren Sie Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
 1. Legen Sie den Klassenpfad des Projekts in Eclipse fest:
 1. Wählen Sie Ihr Projekt in Eclipse aus und wählen Sie dann aus**Eigenschaften** von dem**Projekt** Speisekarte.
 1. Wählen Sie links im Dialog „Java Build Path“ aus.
 1. Auf der**Bibliotheken** Registerkarte, auswählen**JARs hinzufügen** oder**Fügen Sie externe JARs hinzu** um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und sie zu Erstellungspfaden hinzuzufügen.
 1. Anwendung schreiben, um APIs der Komponenten von Aspose aufzurufen.
 Oder Sie können den Pfad zur Laufzeit an einer DOS-Eingabeaufforderung in Windows festlegen.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Wenden Sie die bedingte Formatierung basierend auf dem Zellenwert an**.
 Unten ist der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Es wendet eine bedingte Formatierung auf eine Zelle an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „A1“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die auf A1 angewendete bedingte Formatierung hängt vom Zellenwert ab. Wenn der Zellenwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot. Bitte sehen Sie sich die folgenden Screenshots der generierten XLS-Datei an.

**Ausgabe einer Excel-Datei mit einem A1-Wert kleiner als 50**

![todo: Bild_alt_Text](apply-conditional-formatting-in-worksheets_1.png)

**Excel-Datei mit A1 zwischen 50 und 100 ausgeben**

![todo: Bild_alt_Text](apply-conditional-formatting-in-worksheets_2.png)

### **Aufgabe 2: Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf einer Formel**

1. **Bedingte Formatierung je nach Formel anwenden**.
 Unten ist der tatsächliche Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Es wendet die bedingte Formatierung auf „B3“ an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „B3“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung hängt von der Formel ab, die den Wert von „B3“ als Summe von B1 & B2 berechnet. Bitte sehen Sie sich die folgenden Screenshots der generierten XLS-Datei an.

**Excel-Datei mit B3-Wert kleiner als 100 ausgeben**

![todo: Bild_alt_Text](apply-conditional-formatting-in-worksheets_3.png)

**Excel-Datei mit B3 größer als 100 ausgeben**

![todo: Bild_alt_Text](apply-conditional-formatting-in-worksheets_4.png)

### **Fazit**

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie Sie bedingte Formatierung auf Zellen in einem Arbeitsblatt mit Aspose.Cells API anwenden. Hoffentlich gibt er Ihnen einen Einblick, damit Sie diese Optionen in Ihren eigenen Szenarien verwenden können.

Aspose.Cells bietet große Flexibilität für Lösungen und bietet hervorragende Geschwindigkeit, Effizienz und Zuverlässigkeit, um spezifische Anforderungen von Geschäftsanwendungen zu erfüllen. Aspose.Cells profitiert von jahrelanger Forschung, Design und sorgfältiger Abstimmung.

 Wir freuen uns über Ihre Fragen, Kommentare und Anregungen im[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine umgehende Antwort.

{{% /alert %}}
