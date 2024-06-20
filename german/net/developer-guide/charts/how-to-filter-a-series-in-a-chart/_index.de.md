---
title: Drei Methoden zum Filtern von Diagrammdaten
description: Erfahren Sie, wie Sie Diagramme in Excel mit Aspose.Cells for .NET filtern. Unser umfassender Leitfaden wird Ihnen zeigen, wie Sie Filter auf Diagramme anwenden, Diagrammelemente anpassen und Datenanalysetools für bessere Einblicke und fundierte Entscheidungen nutzen.
keywords: Aspose.Cells for .NET, Filtern von Diagrammen in Excel, Datenanalyse, Entscheidungsfindung, Visualisierung.
type: docs
weight: 2210
url: /de/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Herausfiltern von Reihen, um ein Diagramm zu rendern**

### **Schritte zum Filtern von Reihen aus einem Diagramm in Excel**
In Excel können wir bestimmte Reihen aus einem Diagramm herausfiltern, sodass diese herausgefilterten Reihen im Diagramm nicht angezeigt werden. Das ursprüngliche Diagramm ist in **Abbildung 1** dargestellt. Wenn wir jedoch **Testreihe2** und **Testreihe4** herausfiltern, wird das Diagramm wie in **Abbildung 2** angezeigt.

In Aspose.Cells können wir eine ähnliche Operation durchführen. Für eine [Beispiel](seriesFiltered.xlsx)-Datei wie diese, wenn wir **Testreihe2** und **Testreihe4** herausfiltern möchten, können wir den folgenden Code ausführen. Zusätzlich werden wir zwei Listen führen: eine ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) Liste, um alle ausgewählten Reihen zu speichern, und eine weitere ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)), um die gefilterten Reihen zu speichern.

Bitte **beachten** Sie, dass im Code, wenn wir **chart.NSeries[0].IsFiltered = true;** setzen, wird die erste Reihe in [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) entfernt und an der entsprechenden Position innerhalb von [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) platziert. Anschließend wird das vorherige **NSeries[1]** zum neuen ersten Element in der Liste und alle folgenden Reihen werden um eine Position nach vorne verschoben. Das bedeutet, dass wenn wir dann **chart.NSeries[1].IsFiltered = true;** ausführen, entfernen wir effektiv die ursprüngliche dritte Reihe. Dies kann manchmal zu Verwirrung führen, daher empfehlen wir, die Operation im Code zu befolgen, die Reihen von hinten nach vorne löscht.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Filtern Sie die Daten mithilfe einer Tabelle und lassen Sie das Diagramm sich ändern.**

Die Verwendung einer Tabelle ist ähnlich wie Methode 2, die Verwendung eines Bereichs, aber Sie haben mit Tabellen Vorteile gegenüber Bereichen. Wenn Sie Ihren Bereich in eine Tabelle ändern und Daten hinzufügen, wird das Diagramm automatisch aktualisiert. Mit einem Bereich müssten Sie die Datenquelle ändern.

### **Als Tabelle formatieren in Excel**

Klicken Sie in Ihre Daten und verwenden Sie **STRG + T** oder gehen Sie zum Register **Start**, **Als Tabelle formatieren**

![todo:image_alt_text](Figure4.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](TableFilters.xlsx) und zeigt dieselbe Funktion unter Verwendung von Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
