---
title: Aspose.Cells Java für Jython
type: docs
weight: 70
url: /de/java/aspose-cells-java-for-jython/
---
## **Einführung**

### **Was ist Jyton?**

Jython ist eine Java-Implementierung von Python, die Ausdruckskraft mit Klarheit verbindet. Jython ist sowohl für die kommerzielle als auch für die nicht-kommerzielle Nutzung frei verfügbar und wird mit Quellcode verteilt. Jython ist komplementär zu Java und eignet sich besonders für folgende Aufgaben:

- **Eingebettete Skripterstellung** - Java Programmierer können die Jython-Bibliotheken zu ihrem System hinzufügen, damit Endbenutzer einfache oder komplizierte Skripte schreiben können, die der Anwendung Funktionalität hinzufügen.
- **Interaktives Experimentieren** - Jython bietet einen interaktiven Interpreter, der zur Interaktion mit Java-Paketen oder mit laufenden Java-Anwendungen verwendet werden kann. Dies ermöglicht Programmierern, jedes Java-System mit Jython zu experimentieren und zu debuggen.
- **Schnelle Anwendungsentwicklung** Python-Programme sind in der Regel 2-10 Mal kürzer als das entsprechende Java-Programm. Dies führt direkt zu einer erhöhten Programmiererproduktivität. Die nahtlose Interaktion zwischen Python und Java ermöglicht es Entwicklern, die beiden Sprachen sowohl während der Entwicklung als auch beim Versand von Produkten frei zu mischen.

### **Aspose.Cells for Java**

Aspose.Cells for Java ist eine erweiterte Klassenbibliothek for Java, mit der Sie eine große Auswahl an Dokumentenverarbeitungsaufgaben direkt in Ihrem Java ausführen können
Anwendungen.

Aspose.Cells for Java unterstützt die Verarbeitung von Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF und allen Bildformaten. Mit Aspose.Cells geht das
Erstellen, ändern und konvertieren Sie Dokumente ohne Microsoft Cells.

### **Aspose.Cells Java für Jython**

Aspose.Cells Java für Jython ist ein Projekt, das die Verwendungsbeispiele Aspose.Cells for Java API in Jython demonstriert / bereitstellt.

## **Systemanforderungen und unterstützte Plattformen**

### **System Anforderungen**

**Im Folgenden sind die Systemanforderungen für die Verwendung von Aspose.Cells Java für Jython aufgeführt:**

- Java 1.5 oder höher installiert
- Komponente Aspose.Cells heruntergeladen
- Jython 2.7.0

### **Unterstützte Plattformen**

**Im Folgenden sind die unterstützten Plattformen aufgeführt:**

- Aspose.Cells 15.4 und höher.
- Java IDE (Eclipse, NetBeans ...)

## **Installation und Verwendung herunterladen**

### **wird heruntergeladen**

**Laden Sie Beispiele von Social-Coding-Websites herunter**

Die folgenden Versionen von Laufbeispielen stehen auf allen unten genannten Social-Coding-Sites zum Download zur Verfügung:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Laden Sie die Komponente Aspose.Cells for Java herunter**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installieren**

- Platzieren Sie die heruntergeladene JAR-Datei Aspose.Cells for Java im Verzeichnis „lib“.
- Ersetzen Sie „your-lib“ durch den heruntergeladenen JAR-Dateinamen in der Datei _*init*_.py.

### **Verwenden**

Sie können ein HelloWorld-Dokument mit folgendem Beispielcode erstellen:

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Unterstützen, erweitern und beitragen**

### **Die Unterstützung**

Von den ersten Tagen der Aspose wussten wir, dass es nicht ausreichen würde, unseren Kunden nur gute Produkte zu geben. Wir mussten auch einen guten Service bieten. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Macke in der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht um sie zu erschaffen.

Aus diesem Grund bieten wir kostenlosen Support an. Jeder, der unser Produkt verwendet, ob er es gekauft hat oder eine Bewertung verwendet, verdient unsere volle Aufmerksamkeit und unseren Respekt.

Sie können alle Probleme oder Vorschläge im Zusammenhang mit Aspose.Cells Java für Jython über eine der folgenden Plattformen protokollieren:

- [GitHub](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Erweitern und beitragen**

Aspose.Cells Java für Jython ist Open Source und sein Quellcode ist auf den unten aufgeführten wichtigen Social-Coding-Websites verfügbar. Entwickler werden ermutigt, den Quellcode herunterzuladen und einen Beitrag zu leisten, indem sie neue Funktionen vorschlagen oder hinzufügen oder die vorhandenen verbessern, damit auch andere davon profitieren können.

### **Quellcode**

Den neuesten Quellcode erhalten Sie von einer der folgenden Stellen

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
