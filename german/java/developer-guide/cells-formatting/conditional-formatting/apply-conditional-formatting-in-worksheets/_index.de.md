---
title: Bedingte Formatierung in Arbeitsblättern anwenden
type: docs
weight: 40
url: /de/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie bedingte Formatierung auf eine Zellenreihe in einem Arbeitsblatt angewendet wird.

Bedingte Formatierung ist eine fortgeschrittene Funktion in Microsoft Excel, die es ermöglicht, Formate auf eine Zellenreihe anzuwenden und diese Formatierung je nach dem Wert der Zelle oder dem Wert einer Formel zu ändern. Zum Beispiel kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte grün sein, um einen positiven Wert hervorzuheben. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Erfüllt der Wert der Zelle die Formatbedingung nicht, wird das Standardformat der Zelle verwendet.

Es ist möglich, bedingte Formatierungen mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Es gibt mehrere Gründe und Probleme, die damit verbunden sind: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund, nach einer anderen Lösung zu suchen, ist, dass Microsoft selbst die Nutzung von Office Automation für Softwarelösungen nachdrücklich ablehnt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, bedingte Formatierung auf Zellen mit einigen einfachsten Zeilen Code mithilfe der Aspose.Cells API hinzufügt.

{{% /alert %}}

## **Arbeiten mit bedingter Formatierung**

Dieser Artikel behandelt die folgenden Aufgaben:

1. [Mit Aspose.Cells bedingte Formatierung basierend auf Zellenwert anwenden](/cells/de/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Mit Aspose.Cells bedingte Formatierung basierend auf einer Formel anwenden](/cells/de/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Aufgabe 1: Mit Aspose.Cells bedingte Formatierung basierend auf Zellenwert anwenden**

1. **Laden Sie Aspose.Cells.zip herunter und installieren Sie es**: 
   1. [Herunterladen](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
      Alle Aspose-Komponenten arbeiten im Installationsmodus nur als Testversion. Die Testversion hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. **Ein Projekt erstellen**.
   Erstellen Sie entweder ein Projekt mit einem Java-Editor wie Eclipse oder erstellen Sie ein einfaches Programm mit einem Texteditor.
1. **Fügen Sie den Klassenpfad hinzu**.
   Um einen Klassenpfad in Eclipse festzulegen, führen Sie bitte die folgenden Schritte aus:
   1. Extrahieren Sie die Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
   1. Setzen Sie den Klassenpfad des Projekts in Eclipse:
      1. Wählen Sie Ihr Projekt in Eclipse aus und wählen Sie dann **Eigenschaften** im **Projekt**-Menü aus.
      1. Wählen Sie links in dem Dialogfeld "Java-Build-Pfad" aus.
      1. Wählen Sie auf der Registerkarte **Bibliotheken** **JARs hinzufügen** oder **Externe JARs hinzufügen**, um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und in den Build-Pfaden hinzuzufügen.
   1. Schreiben Sie eine Anwendung, um die APIs der Aspose-Komponenten aufzurufen.
      Alternativ können Sie den Pfad über eine Eingabeaufforderung in Windows während der Laufzeit festlegen.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Bedingte Formatierung basierend auf Zellwert anwenden**.
   Im Folgenden finden Sie den vom Komponenten verwendeten Code, um die Aufgabe zu erledigen. Er wendet bedingte Formatierung auf einer Zelle an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle "A1" im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die bedingte Formatierung, die auf A1 angewendet wird, hängt vom Zellwert ab. Wenn der Zellwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot. Bitte sehen Sie sich die folgenden Screenshots der generierten XLS-Datei an.

**Ausgabedatei Excel mit einem Wert von A1 kleiner als 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**Ausgabedatei Excel mit einem Wert von A1 zwischen 50 und 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Aufgabe 2: Mit Aspose.Cells bedingte Formatierung basierend auf einer Formel anwenden**

1. **Bedingte Formatierung abhängig von einer Formel anwenden**.
   Im Folgenden finden Sie den tatsächlichen Code, der von der Komponente verwendet wird, um die Aufgabe zu erledigen. Er wendet bedingte Formatierung auf “B3” an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle "B3" im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die bedingte Formatierung, die angewendet wird, hängt von der Formel ab, die den Wert von "B3" als Summe von B1 & B2 berechnet. Bitte sehen Sie sich die folgenden Screenshots der generierten XLS-Datei an.

**Ausgabedatei Excel mit einem Wert von B3 kleiner als 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**Ausgabedatei Excel mit einem Wert von B3 größer als 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Fazit**

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie die bedingte Formatierung von Zellen in einem Arbeitsblatt mit der Aspose.Cells API angewendet wird. Hoffentlich vermittelt er Ihnen Einblicke, damit Sie diese Optionen in Ihren eigenen Szenarien verwenden können.

Aspose.Cells bietet eine hohe Flexibilität für Lösungen und bietet herausragende Geschwindigkeit, Effizienz und Zuverlässigkeit, um spezifische Anwendungsanforderungen zu erfüllen. Aspose.Cells profitiert von Jahren der Forschung, des Designs und der sorgfältigen Abstimmung.

Wir begrüßen Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine schnelle Antwort.

{{% /alert %}}
