---
title: Smart Marker formatieren
type: docs
weight: 20
url: /de/java/formatting-smart-markers/
---
##  **Stilattribut kopieren**
Manchmal möchten Sie bei der Verwendung von Smart Markern den Stil der Zelle kopieren, die die Smart Marker-Tags enthält. Zu diesem Zweck können Sie das CopyStyle-Attribut der Tags des Smart Markers verwenden.
###  **Kopieren von Stilen aus Cells mit Smart Markers**
 In diesem Beispiel wird eine einfache Excel-Vorlage Microsoft mit zwei Markierungen in den Zellen A2 und B2 verwendet. Die in Zelle B2 eingefügte Markierung verwendet das CopyStyle-Attribut, die Markierung in Zelle A2 hingegen nicht. Wenden Sie einfache Formatierungen an (stellen Sie beispielsweise die Schriftfarbe auf ein).**Rot** und setzen Sie die Zellenfüllfarbe auf *Gelb**).

 In diesem Beispiel wird a verwendet[Vorlagendatei](template1.xlsx)mit ein paar Markierungen in den Zellen. Beim Ausführen des Codes kopiert Aspose.Cells die Formatierung in alle Datensätze in Spalte B, behält jedoch die Formatierung in Spalte A nicht bei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


##  **Benutzerdefinierte Etiketten hinzufügen**
###  **Einführung**
Beim Arbeiten mit der Gruppierungsdatenfunktion von Smart Markers müssen Sie manchmal Ihre eigenen benutzerdefinierten Beschriftungen zur Zusammenfassungszeile hinzufügen. Sie möchten auch den Namen der Spalte mit dieser Bezeichnung verketten, z. B. „Zwischensumme der Bestellungen“. Aspose.Cells bietet Ihnen die Attribute „Label“ und „LabelPosition“, sodass Sie Ihre benutzerdefinierten Beschriftungen in den Smart Markers platzieren und gleichzeitig mit den Zwischensummenzeilen in Gruppierungsdaten verketten können.
###  **Hinzufügen benutzerdefinierter Beschriftungen zur Verkettung mit den Zwischensummenzeilen in Smart Markers**
 In diesem Beispiel wird a verwendet[Vorlagendatei](template.xlsx) mit ein paar Markierungen in den Zellen. Beim Ausführen des Codes fügt Aspose.Cells den Zusammenfassungszeilen für die gruppierten Daten einige benutzerdefinierte Beschriftungen hinzu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
