---
title: Daten filtern
type: docs
weight: 80
url: /de/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb bietet Autofilter- und benutzerdefinierte Datenfilterfunktionen. Mit diesen Funktionen können Sie nur die Elemente in einem Arbeitsblatt auswählen, die Sie in einer Liste anzeigen möchten. Darüber hinaus können Sie Artikel in einer Liste nach festgelegten Kriterien filtern. Filtern Sie Text, Zahlen oder Daten mit den Filterfunktionen.

{{% /alert %}} 
## **Arbeiten mit Filtern**
Verwenden Sie die Arbeitsblatt-AddAutoFilter-Methode, um den automatischen Filter für ein Arbeitsblatt zu aktivieren. Diese Methode akzeptiert die Zeilen-, Start- und Endspaltenindizes.

Um einen benutzerdefinierten Filter zu aktivieren, verwenden Sie die AddCustomFilter-Methode des Arbeitsblatts, die den Zeilenindex, auf den der Filter angewendet werden soll, und die benutzerdefinierten Filterkriterien akzeptiert.

Das folgende Beispiel implementiert sowohl automatische als auch benutzerdefinierte Datenfilter. Im Beispiel ist die automatische Filterfunktion aktiviert und gefilterte Zeilen werden basierend auf einigen Kriterien durchsucht.

**Eingabe: die Datenliste im ersten Arbeitsblatt** 

![todo: Bild_alt_Text](filter-data_1.jpg)

**Ausgabe: Autofilter-Funktion aktivieren** 

![todo: Bild_alt_Text](filter-data_2.jpg)
### **Automatischer Filter**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Benutzerdefinierter Datenfilter**
**Benutzerdefinierte gefilterte Daten basierend auf den Kriterien** 

![todo: Bild_alt_Text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
