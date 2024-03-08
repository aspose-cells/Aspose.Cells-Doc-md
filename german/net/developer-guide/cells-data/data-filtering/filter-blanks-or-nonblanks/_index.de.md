---
title: So filtern Sie Leerzeichen oder Nicht-Leerzeichen
type: docs
weight: 85
url: /de/net/how-to-filter-blanks-and-non-blanks/
description: Erfahren Sie, wie Sie Leerzeichen und Nicht-Leerzeichen mithilfe von Aspose.Cells for .NET API filtern.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Mögliche Nutzungsszenarien**
Das Filtern von Daten in Excel ist ein wertvolles Werkzeug, das die Datenanalyse, -erkundung und -präsentation verbessert, indem es Benutzern ermöglicht, sich anhand ihrer Kriterien auf bestimmte Teilmengen von Daten zu konzentrieren, wodurch der gesamte Datenbearbeitungs- und Interpretationsprozess effizienter und effektiver wird.

##  **So filtern Sie Leerzeichen oder Nicht-Leerzeichen in Excel**
In Excel können Sie mithilfe der Filteroptionen ganz einfach Leerzeichen oder Nicht-Leerzeichen filtern. So können Sie es machen:

###  **So filtern Sie Leerzeichen in Excel**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie im Menüband auf die Registerkarte „Daten“.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche „Filter“. Dadurch werden dem ausgewählten Bereich Filterpfeile hinzugefügt.
1. Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer „Leerzeichen“ und klicken Sie auf „OK“. Dadurch werden nur die leeren Zellen in dieser Spalte angezeigt.
<br>
<image src="2.png" width="70%" />
1. Das Ergebnis wie folgt:
<br>
<image src="3.png" width="70%" />

###  **So filtern Sie Nicht-Leerzeichen in Excel**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Nicht-Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie im Menüband auf die Registerkarte „Daten“.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche „Filter“. Dadurch werden dem ausgewählten Bereich Filterpfeile hinzugefügt.
1. Nicht-Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Nicht-Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer „Keine Leerzeichen“ oder „Benutzerdefiniert“ und legen Sie die Bedingungen entsprechend fest. OK klicken. Dadurch werden nur die Zellen angezeigt, die in dieser Spalte nicht leer sind.
<br>
<image src="4.png" width="70%" />
1. Das Ergebnis wie folgt:
<br>
<image src="5.png" width="70%" />

##  **So filtern Sie Leerzeichen mit Aspose.Cells**
 Wenn eine Spalte Text enthält, sodass nur wenige Zellen leer sind, und ein Filter erforderlich ist, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind,[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) Und[AutoFilter.AddFilter(int fieldIndex, String-Kriterien)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) Funktionen können wie unten gezeigt verwendet werden.

 Bitte sehen Sie sich den folgenden Beispielcode an, der das lädt[Beispiel-Excel-Datei](sample.xlsx) die einige Dummy-Daten enthält. Der Beispielcode verwendet drei Methoden zum Filtern von Leerzeichen. Anschließend wird die Arbeitsmappe als gespeichert[Excel-Datei ausgeben](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **So filtern Sie Nicht-Leerzeichen mit Aspose.Cells**

 Bitte sehen Sie sich den folgenden Beispielcode an, der das lädt[Beispiel-Excel-Datei](sample.xlsx)die einige Dummy-Daten enthält. Rufen Sie nach dem Laden der Datei die auf[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) Funktion zum Filtern nicht leerer Daten und zum abschließenden Speichern der Arbeitsmappe unter[Excel-Datei ausgeben](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

