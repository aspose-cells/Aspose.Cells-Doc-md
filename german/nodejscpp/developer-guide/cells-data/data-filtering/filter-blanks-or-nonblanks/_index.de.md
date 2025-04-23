---
title: Wie filtert man leere oder nicht leere Felder
type: docs
weight: 85
url: /de/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Erfahren Sie, wie Sie Leerzellen und Nicht Leerzellen mithilfe der API Aspose.Cells for Node.js via C++ filtern.
keywords: Leere Felder filtern, Nicht leere Felder filtern, Leere Felder im Arbeitsblatt filtern, Nicht leere Felder im Arbeitsblatt filtern, Leere Felder in Excel filtern, Nicht leere Felder in Excel filtern, Leere und Nicht leere Felder in Excel filtern
---

## **Mögliche Verwendungsszenarien**
Die Filterung von Daten in Excel ist ein wertvolles Werkzeug, das die Datenanalyse, Exploration und Präsentation verbessert, indem Benutzer sich auf bestimmte Datenuntergruppen konzentrieren können, die auf ihren Kriterien basieren. Dadurch wird der gesamte Prozess der Datenmanipulation und -interpretation effizienter und effektiver.

## **Wie man leere oder nicht leere Felder in Excel filtert**
In Excel können Sie ganz einfach leere oder nicht leere Felder mithilfe der Filteroptionen filtern. Hier erfahren Sie, wie es geht:

### **Wie man Leerzeichen in Excel filtert**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie zum Register "Daten" im Menüband.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche "Filter". Dadurch werden Filterpfeile zum ausgewählten Bereich hinzugefügt.
1. Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer "Leerzeichen" und klicken Sie auf OK. Dies zeigt nur die leeren Zellen in dieser Spalte an.
<br>
<image src="2.png" width="70%" />
1. Das Ergebnis lautet wie folgt:
<br>
<image src="3.png" width="70%" />

### **Wie man Nicht-Leerzeichen in Excel filtert**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Nicht-Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie zum Register "Daten" im Menüband.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche "Filter". Dadurch werden Filterpfeile zum ausgewählten Bereich hinzugefügt.
1. Nicht-Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Nicht-Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer "Nicht-Leerzeichen" oder "Benutzerdefiniert" und legen Sie die Bedingungen entsprechend fest. Klicken Sie auf OK. Dies zeigt nur die Zellen an, die in dieser Spalte nicht leer sind.
<br>
<image src="4.png" width="70%" />
1. Das Ergebnis lautet wie folgt:
<br>
<image src="5.png" width="70%" />

## **So filtern Sie Leerzellen mit Aspose.Cells for Node.js via C++**
Wenn eine Spalte Text enthält, sodass einige Zellen leer sind, und Sie nur die Zeilen auswählen möchten, in denen leere Zellen vorhanden sind, können die Funktionen [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) und [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) wie unten demonstriert verwendet werden. 

Bitte sehen Sie sich den folgenden Beispielcode an, der die [Beispiel-Excel-Datei](sample.xlsx) lädt, die einige Dummy-Daten enthält. Der Beispielcode verwendet drei Methoden, um Leerzeichen zu filtern. Anschließend speichert er die Arbeitsmappe als [ausgabe Excel-Datei](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **So filtern Sie Nicht-Leerzellen mit Aspose.Cells for Node.js via C++**

Siehe den folgenden Beispielcode, der die [Beispiel-Excel-Datei](sample.xlsx) lädt, die einige Dummy-Daten enthält. Nach dem Laden der Datei rufen Sie die Funktion [AutoFilter.matchNonBlanks(Nummer)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) auf, um Nicht-Leerzellen zu filtern, und speichern die Arbeitsmappe schließlich als [Ausgabe-Excel-Datei](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

