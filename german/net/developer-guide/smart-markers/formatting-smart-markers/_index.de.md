---
title: Formatting Smart Markers
type: docs
weight: 20
url: /de/net/formatting-smart-markers/
---

## **Stil-Attribut kopieren**
Manchmal möchten Sie beim Verwenden von Smart Markern den Stil der Zelle kopieren, die die Smart-Marker-Tags enthält. Sie können das Attribut CopyStyle der Smart Marker-Tags zu diesem Zweck verwenden.
### **Kopieren von Stilen aus Zellen mit Smart Markern**
Dieses Beispiel verwendet eine einfache Vorlage Microsoft Excel-Datei mit zwei Markern in den Zellen A2 und B2. Der in die Zelle B2 eingefügte Marker verwendet das Attribut CopyStyle, während der Marker in Zelle A2 dies nicht tut. Wenden Sie einfache Formatierungen an (zum Beispiel, setzen Sie die Schriftfarbe auf **rot** und setzen Sie die Zellfüllfarbe auf **gelb**).

Beim Ausführen des Codes kopiert Aspose.Cells die Formatierung in alle Datensätze in der Spalte B, behält jedoch die Formatierung in Spalte A nicht bei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Benutzerdefinierte Beschriftungen hinzufügen**
### **Einführung**
Bei der Arbeit mit der Smart Markers-Gruppendatenfunktion müssen Sie manchmal Ihre eigenen benutzerdefinierten Beschriftungen zur Zusammenfassungszeile hinzufügen. Sie möchten auch den Spaltennamen mit dieser Beschriftung verknüpfen, z. B. "Summe der Aufträge". Aspose.Cells bietet die Attribute Label und LabelPosition, sodass Sie Ihre benutzerdefinierten Beschriftungen in den Smart Markers platzieren können, während Sie diese mit den Zwischensummenzeilen in den Gruppendaten verknüpfen.
### **Hinzufügen benutzerdefinierter Beschriftungen zum Verknüpfen mit den Zwischensummenzeilen in Smart Markers**
Dieses Beispiel verwendet eine [Datendatei](96927971.xlsx) und eine [Vorlagendatei](96927972.xlsx) mit einigen Markern in den Zellen. Beim Ausführen des Codes fügt Aspose.Cells den Zusammenfassungszeilen für die gruppierten Daten einige benutzerdefinierte Beschriftungen hinzu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
