---
title: Daten filtern
type: docs
weight: 80
url: /de/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb, Filter, Daten filtern, Datenfilterung
description: Dieser Artikel führt ein, wie man Daten in GridWeb filtert.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb bietet die Funktionen für Auto-Filter und benutzerdefinierten Datenfilter. Diese Funktionen ermöglichen es Ihnen, nur die Elemente in einem Arbeitsblatt auszuwählen, die Sie in einer Liste anzeigen möchten. Darüber hinaus können Sie Elemente in einer Liste nach festgelegten Kriterien filtern. Filtern Sie Texte, Zahlen oder Datumsangaben mit den Filterfunktionen.

{{% /alert %}} 
## **Arbeiten mit Filtern**
Verwenden Sie die Methode AddAutoFilter des Arbeitsblatts, um den Auto-Filter für ein Arbeitsblatt zu aktivieren. Diese Methode akzeptiert die Zeilen- sowie Start- und Endspalten-Indizes.

Um den benutzerdefinierten Filter zu aktivieren, verwenden Sie die Methode AddCustomFilter des Arbeitsblatts, die den Zeilenindex akzeptiert, auf den der Filter angewendet werden soll, sowie die benutzerdefinierten Filterkriterien.

Das untenstehende Beispiel implementiert sowohl Auto- als auch benutzerdefinierte Datenfilter. Im Beispiel wird die Auto-Filterfunktion aktiviert und die gefilterten Zeilen werden auf der Grundlage bestimmter Kriterien gesucht.

**Eingabe: Die Datenliste im ersten Arbeitsblatt** 

![todo:image_alt_text](filter-data_1.jpg)

**Ausgabe: Auto-Filter-Funktion aktivieren** 

![todo:image_alt_text](filter-data_2.jpg)
### **Auto-Filter**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Benutzerdefinierter Datenfilter**
**Benutzerdefinierte gefilterte Daten basierend auf den Kriterien** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
