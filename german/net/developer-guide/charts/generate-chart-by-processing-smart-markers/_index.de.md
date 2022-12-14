---
title: Erstellen Sie ein Diagramm, indem Sie Smart-Marker verarbeiten
type: docs
weight: 2100
url: /de/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells APIs bieten die[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)Klasse, um mit Smart Markern zu arbeiten, bei denen die Formatierungen und Formeln in den Designer-Tabellen platziert und dann verarbeitet werden[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)Klasse, um die Daten gemäß den angegebenen Smart Markern aufzufüllen. Es ist auch möglich, Excel-Diagramme durch die Verarbeitung von Smart Markern zu erstellen, was die folgenden Schritte erfordert.

- Erstellung von Designer-Tabellenkalkulationen
- Verarbeitung des Designer-Arbeitsblatts anhand der angegebenen Datenquelle
- Erstellung von Diagrammen basierend auf ausgefüllten Daten

{{% /alert %}}

## Erstellung einer Designer-Tabelle

Eine Designer-Tabelle ist eine einfache Excel-Datei, die mit der Excel-Anwendung Microsoft oder den APIs Aspose.Cells erstellt wurde und die visuelle Formatierung, Formeln und intelligente Markierungen enthält, in die der Inhalt zur Laufzeit eingefügt werden kann.

Der Einfachheit halber erstellen wir das Designer-Arbeitsblatt mit Aspose.Cells for .NET API und verarbeiten es später zu Demonstrationszwecken gegen eine dynamisch erstellte Datenquelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Designer-Tabelle verarbeiten

Um das Designer-Arbeitsblatt zu verarbeiten, muss man über eine Datenquelle verfügen, die den in dem Designer-Arbeitsblatt verwendeten Smart Markern entspricht. Beispielsweise haben wir einen Smart-Marker-Eintrag als &=Sales.Year erstellt, der die Year-Spalte in der DataTable Sales darstellt. Falls eine entsprechende Spalte in der Datenquelle nicht verfügbar ist, überspringen die Aspose.Cells-APIs die Verarbeitung für diese bestimmte Smart-Markierung, und folglich werden die Daten für die bestimmte Smart-Markierung nicht ausgefüllt.

Um diesen Anwendungsfall zu demonstrieren, erstellen wir die Datenquelle von Grund auf neu und verarbeiten sie mit der im vorherigen Schritt erstellten Designer-Tabelle. In einem Echtzeitszenario könnten Daten jedoch bereits zur weiteren Verarbeitung verfügbar sein, sodass Sie die Erstellung einer Datenquelle überspringen können, wenn bereits Daten verfügbar sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Die Verarbeitung von Smart Markern ist recht einfach, wie das folgende Code-Snippet zeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Das obige Code-Snippet verwendet die vorhandene Instanz von[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die im ersten Schritt erstellt wurde. Wenn Sie die Designer-Tabellenkalkulationsdatei bereits auf der Festplatte oder im Speicher haben, können Sie eine Instanz davon erstellen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, indem Sie das vorhandene Designer-Arbeitsblatt laden.

{{% /alert %}}

## Erstellung von Diagrammen

 Sobald die Daten vorhanden sind, müssen wir nur noch ein Diagramm basierend auf der Datenquelle erstellen. Um das Beispiel einfach zu halten, verwenden wir die[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)-Methode, sodass wir das Diagramm nicht weiter konfigurieren müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
