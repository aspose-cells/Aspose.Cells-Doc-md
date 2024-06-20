---
title: Formatting Smart Markers
type: docs
weight: 20
url: /de/java/formatting-smart-markers/
---

## **Stil-Attribut kopieren**
Manchmal möchten Sie beim Verwenden von Smart Markern den Stil der Zelle kopieren, die die Smart-Marker-Tags enthält. Sie können das Attribut CopyStyle der Smart Marker-Tags zu diesem Zweck verwenden.
### **Kopieren von Stilen aus Zellen mit Smart Markern**
Dieses Beispiel verwendet eine einfache Vorlage Microsoft Excel-Datei mit zwei Markern in den Zellen A2 und B2. Der in die Zelle B2 eingefügte Marker verwendet das Attribut CopyStyle, während der Marker in Zelle A2 dies nicht tut. Wenden Sie einfache Formatierungen an (zum Beispiel, setzen Sie die Schriftfarbe auf **rot** und setzen Sie die Zellfüllfarbe auf **gelb**).

Dieses Beispiel verwendet eine [Vorlagendatei](template1.xlsx) mit einigen Markern in den Zellen. Beim Ausführen des Codes kopiert Aspose.Cells die Formatierung auf alle Datensätze in Spalte B, behält jedoch die Formatierung in Spalte A nicht bei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Benutzerdefinierte Beschriftungen hinzufügen**
### **Einführung**
Bei der Arbeit mit der Smart Markers-Gruppendatenfunktion müssen Sie manchmal Ihre eigenen benutzerdefinierten Beschriftungen zur Zusammenfassungszeile hinzufügen. Sie möchten auch den Spaltennamen mit dieser Beschriftung verknüpfen, z. B. "Summe der Aufträge". Aspose.Cells bietet die Attribute Label und LabelPosition, sodass Sie Ihre benutzerdefinierten Beschriftungen in den Smart Markers platzieren können, während Sie diese mit den Zwischensummenzeilen in den Gruppendaten verknüpfen.
### **Hinzufügen benutzerdefinierter Beschriftungen zum Verknüpfen mit den Zwischensummenzeilen in Smart Markers**
In diesem Beispiel wird eine [Vorlagendatei](template.xlsx) mit einigen Markern in den Zellen verwendet. Wenn der Code ausgeführt wird, fügt Aspose.Cells einigen Zusammenfassungszeilen für die gruppierten Daten benutzerdefinierte Beschriftungen hinzu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
