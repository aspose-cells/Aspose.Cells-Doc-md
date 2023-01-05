---
title: Formatieren von intelligenten Markierungen
type: docs
weight: 20
url: /de/net/formatting-smart-markers/
---
## **Stilattribut kopieren**
Wenn Sie intelligente Markierungen verwenden, möchten Sie manchmal den Stil der Zelle kopieren, die die intelligenten Markierungs-Tags enthält. Zu diesem Zweck können Sie das Attribut CopyStyle der Tags des Smart Markers verwenden.
### **Kopieren von Styles aus Cells mit Smart Markern**
 Dieses Beispiel verwendet eine einfache Vorlage Microsoft Excel-Datei mit zwei Markierungen in den A2- und B2-Zellen. Die in Zelle B2 eingefügte Markierung verwendet das CopyStyle-Attribut, die Markierung in Zelle A2 hingegen nicht. Wenden Sie eine einfache Formatierung an (stellen Sie beispielsweise die Schriftfarbe auf**rot** und stellen Sie die Zellenfüllfarbe auf ein**gelb**).

Beim Ausführen des Codes kopiert Aspose.Cells die Formatierung in alle Datensätze in Spalte B, behält aber die Formatierung in Spalte A nicht bei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Hinzufügen von benutzerdefinierten Etiketten**
### **Einführung**
Beim Arbeiten mit der Datengruppierungsfunktion von Smart Markers müssen Sie manchmal Ihre eigenen benutzerdefinierten Beschriftungen zur Zusammenfassungszeile hinzufügen. Sie möchten auch den Namen der Spalte mit diesem Label verketten, z. B. „Sub Total of Orders“. Aspose.Cells bietet Ihnen Label- und LabelPosition-Attribute, sodass Sie Ihre benutzerdefinierten Labels in den Smart Markern platzieren können, während Sie sie mit den Zwischensummenzeilen beim Gruppieren von Daten verketten.
### **Hinzufügen benutzerdefinierter Beschriftungen zur Verkettung mit den Zwischensummenzeilen in Smart Markers**
Dieses Beispiel verwendet a[Datendatei](96927971.xlsx) und ein[Vorlagendatei](96927972.xlsx) mit ein paar Markern in den Zellen. Beim Ausführen des Codes fügt Aspose.Cells einige benutzerdefinierte Bezeichnungen zu den Zusammenfassungszeilen für die gruppierten Daten hinzu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
