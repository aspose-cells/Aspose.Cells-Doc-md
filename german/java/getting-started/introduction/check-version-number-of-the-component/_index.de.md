---
title: Überprüfen Sie die Versionsnummer der Komponente
type: docs
weight: 70
url: /de/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

In einigen Fällen fragen Sie sich vielleicht, welche Version des Produkts Sie haben. Oft bauen wir neue Fixes (Fehlerbehebungen für die Benutzerszenarien, auf die sie hinweisen) und posten sie in den Foren, wenn sie dringend benötigt werden. Die Versionsnummer besteht aus der Hauptversionsnummer, der Nebenversionsnummer und der Hotfix-Versionsnummer. Alle definierten Komponenten müssen ganze Zahlen größer oder gleich 0 sein. Das Format der Versionsnummer ist wie folgt:

major.minor.hotfix , können wir einen Teil um 1 erhöhen und eine neue Version erstellen. Normalerweise erhöhen wir den letzten Teil um 1 und bauen einen neuen Fix, um ihn für die Benutzer in die Foren zu stellen.

Dieses Dokument beschreibt einige Möglichkeiten, um zu überprüfen, welche Version der Komponente auf Ihrem System installiert ist.

{{% /alert %}} 
## **Überprüfung der Versionsnummer**
### **1) Manueller Weg**
Wenn Sie Version/Fix Java (Aspose.Cells for Java) haben, können Sie die Aspose.Cells-Bibliotheks-JAR-Datei entpacken, die MANIFEST-Datei mit Notepad öffnen und nach der Zeichenfolge suchen, z. B. „Specification-Version:“, um ihren Wert zu überprüfen.

![todo: Bild_alt_Text](check-version-number-of-the-component_1.png)


**Figur:** Überprüfen der Versionsnummer des Fixes Java
### **2) Verwenden der APIs**
Sie können auch die folgenden APIs verwenden, um die Versionsnummer des Produkts abzurufen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

