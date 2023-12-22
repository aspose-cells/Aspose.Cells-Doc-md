---
title: Drei Methoden zum Filtern von Diagrammdaten
description: Erfahren Sie, wie Sie Diagramme in Excel mithilfe von Aspose.Cells for .NET filtern. Unser umfassender Leitfaden zeigt, wie Sie Filter auf Diagramme anwenden, Diagrammelemente anpassen und Datenanalysetools verwenden, um bessere Einblicke und eine fundierte Entscheidungsfindung zu erhalten.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /de/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Serien herausfiltern, um ein Diagramm zu rendern**

###  **Schritte zum Filtern von Reihen aus einem Diagramm in Excel**
 In Excel können wir bestimmte Reihen aus einem Diagramm herausfiltern, was dazu führt, dass diese gefilterten Reihen nicht im Diagramm angezeigt werden. Das Originaldiagramm ist in dargestellt**Abbildung 1**. Wenn wir jedoch **Testseries2** und *Testseries4**, das Diagramm wird wie in *Abbildung 2** dargestellt angezeigt.

 In Aspose.Cells können wir einen ähnlichen Vorgang durchführen. Für ein[Probe](seriesFiltered.xlsx) Datei wie diese, wenn wir herausfiltern wollen**Testreihe2** und *Testseries4** können wir den folgenden Code ausführen. Darüber hinaus werden wir zwei Listen führen: eine ([NSerie](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/))-Liste zum Speichern aller ausgewählten Serien und einer weiteren ([GefilterteNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)), um die gefilterte Serie zu speichern.

Bitte**Notiz** das im Code, wenn wir es einstellen**chart.NSeries[0].IsFiltered = true;**, die erste Serie in [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) wird entfernt und an der entsprechenden Position in [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) platziert. Anschließend wurde die vorherige **NSeries[1]** wird zum neuen ersten Element in der Liste und alle folgenden Serien werden um eine Position nach vorne verschoben. Das heißt, wenn wir dann *chart.NSeries[1].IsFiltered = true;** ausführen, entfernen wir effektiv die ursprüngliche dritte Serie. Dies kann manchmal zu Verwirrung führen. Wir empfehlen daher, der Operation im Code zu folgen, die Serien vom Ende bis zum Anfang löscht.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

###  **Beispielcode**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Filtern Sie die Daten und lassen Sie das Diagramm sich ändern**

Das Filtern Ihrer Daten ist eine hervorragende Möglichkeit, Diagrammfilter mit vielen Daten zu verwalten. Wenn Sie die Daten filtern, ändert sich das Diagramm. Ein Problem, das wir angehen müssen, besteht darin, sicherzustellen, dass das Diagramm auf dem Bildschirm bleibt. Beim Filtern werden ausgeblendete Zeilen angezeigt, und gelegentlich befindet sich das Diagramm in diesen ausgeblendeten Zeilen.

![todo:image_alt_text](Figure3.png)

###  **Schritte zur Verwendung von Datenfiltern zum Ändern des Diagramms in Excel**

1. Klicken Sie in Ihren Datenbereich.
 2. Klicken Sie auf**Daten** Klicken Sie auf die Registerkarte „Filter“ und aktivieren Sie „Filter“, indem Sie auf „Filter“ klicken. Ihre Kopfzeile verfügt über Dropdown-Pfeile.
 3. Erstellen Sie ein Diagramm, indem Sie zu gehen**Einfügen** Klicken Sie auf die Registerkarte und wählen Sie ein Säulendiagramm aus.
4. Filtern Sie nun Ihre Daten mithilfe der Dropdown-Pfeile in den Daten. Verwenden Sie nicht die Diagrammfilter.

###  **Beispielcode**
Der folgende Beispielcode zeigt die gleiche Funktion mit Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Filtern Sie die Daten mithilfe einer Tabelle und lassen Sie das Diagramm ändern**

Die Verwendung einer Tabelle ähnelt Methode 2, bei der ein Bereich verwendet wird, Tabellen haben jedoch Vorteile gegenüber Bereichen. Wenn Sie Ihren Bereich in eine Tabelle ändern und Daten hinzufügen, wird das Diagramm automatisch aktualisiert. Bei einem Bereich müssen Sie die Datenquelle ändern.

###  **Als Tabelle in Excel formatieren**

 Klicken Sie in Ihre Daten und verwenden Sie sie**STRG + T** oder verwenden Sie die Registerkarte „Startseite“.**Als Tabelle formatieren**

![todo:image_alt_text](Figure4.png)

###  **Beispielcode**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](TableFilters.xlsx) zeigt das gleiche Merkmal mit Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}