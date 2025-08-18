---
title: Drei Methoden zum Filtern von Diagrammdaten
description: Lernen Sie, wie Sie mit Aspose.Cells für Python via .NET Diagramme in Excel filtern. Unser umfassender Leitfaden zeigt, wie man Filter auf Diagramme anwendet, Diagrammelemente anpasst und Datenanalyse Tools für bessere Erkenntnisse und fundierte Entscheidungen nutzt.
keywords: Aspose.Cells für Python via .NET, Diagramme in Excel filtern, Datenanalyse, Entscheidungsfindung, Visualisierung.
type: docs
weight: 2210
url: /de/python-net/filtering-charts-in-excel/
---


## **1. Herausfiltern von Reihen, um ein Diagramm zu rendern**

### **Schritte zum Filtern von Reihen aus einem Diagramm in Excel**
In Excel können wir bestimmte Reihen aus einem Diagramm herausfiltern, sodass diese herausgefilterten Reihen im Diagramm nicht angezeigt werden. Das ursprüngliche Diagramm ist in **Abbildung 1** dargestellt. Wenn wir jedoch **Testreihe2** und **Testreihe4** herausfiltern, wird das Diagramm wie in **Abbildung 2** angezeigt.

In Aspose.Cells für Python via .NET können wir eine ähnliche Operation durchführen. Für eine [Beispieldatei](seriesFiltered.xlsx) wie diese, wenn wir **Testseries2** und **Testseries4** herausfiltern möchten, können wir den folgenden Code ausführen. Zusätzlich verwalten wir zwei Listen: eine ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)) zum Speichern aller ausgewählten Serien und eine andere ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)) zur Speicherung der gefilterten Serien.

Bitte **beachten** Sie, dass im Code, wenn wir **chart.nSeries[0].is_filtered = TRUE;** setzen, die erste Serie in [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) entfernt und an der entsprechenden Stelle in [filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/) platziert wird. Danach wird die vorherige **nSeries[1]** das neue erste Element in der Liste, und alle folgenden Serien verschieben sich um eine Position. Das bedeutet, wenn wir dann **chart.nSeries[1].is_filtered = TRUE;** ausführen, entfernen wir effektiv die ursprüngliche dritte Serie. Dies kann manchmal verwirrend sein, daher empfehlen wir, die Operation im Code zu befolgen, die Serien vom Ende zum Anfang löscht.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

## **2. Filtern Sie die Daten und lassen Sie das Diagramm sich ändern**

Das Filtern Ihrer Daten ist eine großartige Möglichkeit, mit vielen Daten Diagrammfilter umzugehen. Wenn Sie die Daten filtern, ändert sich das Diagramm. Ein Problem, dem wir begegnen werden, ist sicherzustellen, dass das Diagramm auf dem Bildschirm bleibt. Beim Filtern erhalten Sie ausgeblendete Zeilen und gelegentlich wird das Diagramm in diesen versteckten Zeilen sein.

![todo:image_alt_text](Figure3.png)

### **Schritte zum Verwenden von Datenfiltern zum Ändern des Diagramms in Excel**

1. Klicken Sie innerhalb Ihres Datenbereichs.
2. Klicken Sie auf die Registerkarte **Daten** und aktivieren Sie Filter, indem Sie auf Filter klicken. Ihre Kopfzeile wird Dropdown-Pfeile haben.
3. Erstellen Sie ein Diagramm, indem Sie zum **Einfügen**-Tab gehen und ein Säulendiagramm auswählen.
4. Filtern Sie nun Ihre Daten mithilfe der Dropdown-Pfeile in den Daten. Verwenden Sie nicht die Diagrammfilter.

### **Beispielcode**
Der folgende Beispielcode zeigt dieselbe Funktion unter Verwendung von Aspsoe.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Filtern Sie die Daten mithilfe einer Tabelle und lassen Sie das Diagramm sich ändern.**

Die Verwendung einer Tabelle ist ähnlich wie Methode 2, die Verwendung eines Bereichs, aber Sie haben mit Tabellen Vorteile gegenüber Bereichen. Wenn Sie Ihren Bereich in eine Tabelle ändern und Daten hinzufügen, wird das Diagramm automatisch aktualisiert. Mit einem Bereich müssten Sie die Datenquelle ändern.

### **Als Tabelle formatieren in Excel**

Klicken Sie in Ihre Daten und verwenden Sie **STRG + T** oder gehen Sie zum Register **Start**, **Als Tabelle formatieren**

![todo:image_alt_text](Figure4.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](TableFilters.xlsx) und zeigt dieselbe Funktion unter Verwendung von Aspsoe.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
