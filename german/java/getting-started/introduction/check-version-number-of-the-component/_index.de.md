---
title: Versionsnummer des Komponenten überprüfen
type: docs
weight: 70
url: /de/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

In einigen Fällen möchten Sie vielleicht wissen, welche Version des Produkts Sie haben. Oft erstellen wir neue Korrekturen (Fehlerkorrekturen für die Benutzerszenarien, auf die sie hinweisen) und veröffentlichen sie in den Foren, wenn sie dringend benötigt werden. Die Versionsnummer besteht aus der Hauptversionsnummer, der Nebenversionsnummer und der Hotfix-Version. Alle definierten Komponenten müssen Ganzzahlen sein, die größer oder gleich 0 sind. Das Format der Versionsnummer ist wie folgt:

Hauptneben.hotfix , wir können einen Teil um 1 erhöhen und eine neue Version erstellen. Normalerweise erhöhen wir den letzten Teil um 1 und erstellen eine neue Korrektur, um sie in die Foren für die Benutzer zu posten.

Dieses Dokument beschreibt einige Möglichkeiten, die installierte Version des Komponenten zu überprüfen.

{{% /alert %}} 
## **Überprüfen der Versionsnummer**
### **1) Manueller Weg**
Wenn Sie die Java-Version/Korrektur (Aspose.Cells for Java) haben, können Sie die Aspose.Cells-Bibliotheks-Jar-Datei entpacken, die MANIFEST-Datei mit dem Editor öffnen und nach dem Zeichenfolgenwert "Specification-Version:" suchen, um seinen Wert zu überprüfen.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Abbildung:** Überprüfen der Versionsnummer der Java-Korrektur
### **2) Verwendung der APIs**
Sie können auch die folgenden APIs verwenden, um die Versionsnummer des Produkts zu erhalten.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

