---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /de/java/aspose-cells-java-for-jython/
---

## **Einführung**

### **Was ist Jython?**

Jython ist eine Java-Implementierung von Python, die Ausdruckskraft mit Klarheit kombiniert. Jython ist frei für kommerzielle und nicht-kommerzielle Nutzung und wird mit dem Quellcode verteilt. Jython ergänzt Java und eignet sich besonders für die folgenden Aufgaben:

- **Eingebettetes Skripting** - Java-Programmierer können die Jython-Bibliotheken zu ihrem System hinzufügen, um Endbenutzern das Schreiben einfacher oder komplizierter Skripte zu ermöglichen, die der Anwendung Funktionalität hinzufügen.
- **Interaktive Experimente** - Jython bietet einen interaktiven Interpreter, der zur Interaktion mit Java-Paketen oder zur Interaktion mit laufenden Java-Anwendungen verwendet werden kann. Dies ermöglicht es Programmierern, jedes Java-System mithilfe von Jython zu experimentieren und zu debuggen.
- **Schnelle Anwendungsentwicklung** - Python-Programme sind typischerweise 2-10-mal kürzer als das entsprechende Java-Programm. Dies führt direkt zu einer erhöhten Produktivität der Programmierer. Die nahtlose Interaktion zwischen Python und Java ermöglicht Entwicklern, beide Sprachen sowohl während der Entwicklung als auch beim Versand von Produkten frei zu mischen.

### **Aspose.Cells for Java**

Aspose.Cells for Java ist eine fortgeschrittene Klassenbibliothek für Java, die es Ihnen ermöglicht, eine große Bandbreite von Dokumentenverarbeitungsaufgaben direkt in Ihrem Java durchzuführen
Anwendungen.

Aspose.Cells for Java unterstützt die Verarbeitung von Zellen (DOC, DOCX, OOXML, RTF), HTML, OpenDocument, PDF, EPUB, XPS, SWF und alle Bildformate. Mit Aspose.Cells können Sie
Dokumente generieren, ändern und konvertieren, ohne Microsoft Cells zu verwenden.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java für Jython ist ein Projekt, das Aspose.Cells for Java API-Verwendungsbeispiele in Jython demonstriert/bereitstellt.

## **Systemanforderungen und unterstützte Plattformen**

### **Systemanforderungen**

- Jython 2.7.0

- Java 1.5 oder höher installiert
- Aspose.Cells-Komponente heruntergeladen
- Jython 2.7.0

### **Unterstützte Plattformen**

**Folgende Plattformen werden unterstützt:**

- Aspose.Cells 15.4 und höher.
- Java-IDE (Eclipse, NetBeans...)

## **Herunterladen der Installation und Nutzung**

### **Herunterladen**

**Beispielsdownloads von Social-Coding-Websites**

Die folgenden Versionen von laufenden Beispielen sind zum Download auf allen unten genannten Social-Coding-Sites verfügbar:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Download Aspose.Cells for Java-Komponente**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installation**

- Platziere die heruntergeladene Aspose.Cells for Java-JAR-Datei im "lib"-Verzeichnis.
- Ersetze "your-lib" durch den heruntergeladenen JAR-Dateinamen in der _*init*_.py-Datei.

### **Verwendung**

Du kannst das HelloWorld-Dokument mit folgendem Beispielcode erstellen:

{{< highlight java >}}

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

## **Unterstützung, Erweitern und Beitrag leisten**

### **Unterstützung**

Von den allerersten Tagen von Aspose an wussten wir, dass es nicht ausreichen würde, unseren Kunden einfach gute Produkte anzubieten. Wir mussten auch guten Service liefern. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Eigenart der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht sie zu schaffen.

Deshalb bieten wir kostenlosen Support an. Jeder, der unsere Produkte verwendet, egal ob sie sie gekauft haben oder eine Evaluierung durchführen, verdient unsere volle Aufmerksamkeit und Respekt.

Du kannst jegliche Probleme oder Vorschläge im Zusammenhang mit Aspose.Cells Java für Jython über eine der folgenden Plattformen melden:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Ausweiten und Beitrag leisten**

Aspose.Cells Java für Jython ist Open Source und der Quellcode ist auf den unten aufgeführten großen sozialen Coding-Websites verfügbar. Entwickler sind dazu ermutigt, den Quellcode herunterzuladen und durch Vorschläge oder das Hinzufügen neuer Funktionen oder die Verbesserung bestehender dazu beizutragen, damit auch andere davon profitieren können.

### **Quellcode**

Sie können den neuesten Quellcode von einem der folgenden Standorte erhalten

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
