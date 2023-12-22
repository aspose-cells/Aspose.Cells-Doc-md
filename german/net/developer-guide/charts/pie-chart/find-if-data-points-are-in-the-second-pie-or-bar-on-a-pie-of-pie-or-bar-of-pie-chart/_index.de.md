---
title: Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken eines Kreisdiagramms oder Balkendiagramms befinden
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET herausfinden, ob sich Datenpunkte im zweiten Kreis oder Balken eines Kreisdiagramms oder Balkendiagramms befinden. Unser Leitfaden zeigt, wie Sie den sekundären Kreis oder Balken in einem zusammengesetzten Diagramm identifizieren und darauf zugreifen, sodass Sie die Daten effektiv analysieren und bearbeiten können.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Mögliche Nutzungsszenarien**
 Sie können herausfinden, ob sich Datenpunkte einer Reihe im zweiten Kreis befinden*Kuchen vom Kuchen* Diagramm oder in der Leiste von*Stück Kuchen* Diagramm unter Aspose.Cells. Bitte verwenden Sie die[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)Eigenschaft, es zu bestimmen.

 Bitte laden Sie die herunter[Beispiel-Excel-Datei](5115193.xlsx)Wird im folgenden Beispielcode verwendet und sehen Sie sich die Konsolenausgabe an. Wenn Sie die öffnen[Beispiel-Excel-Datei](5115193.xlsx) Sie werden feststellen, dass alle Datenpunkte, die kleiner als 10 sind, innerhalb der Leiste von liegen*Stück Kuchen*Diagramm, wie auch in der Konsolenausgabe angezeigt.
##  **Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken eines Kreisdiagramms oder Balkendiagramms befinden**
 Der folgende Beispielcode zeigt, wie Sie herausfinden, ob sich Datenpunkte im zweiten Kreis oder Balken auf a befinden*Kuchen vom Kuchen* oder*Stück Kuchen*Diagramm.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Konsolenausgabe**
 Sehen Sie sich bitte die folgende Konsolenausgabe an, die nach der Ausführung des obigen Beispielcodes mit generiert wurde[Beispiel-Excel-Datei](5115193.xlsx) . Wenn[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)Ist *falsch**, liegt der Datenpunkt innerhalb des Kuchens, oder wenn *wahr**, dann liegt der Datenpunkt innerhalb des Balkens.



{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
