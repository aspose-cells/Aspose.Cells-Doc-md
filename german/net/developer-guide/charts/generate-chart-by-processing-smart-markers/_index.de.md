---
title: Generieren Sie ein Diagramm durch die Verarbeitung intelligenter Markierungen
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Diagramme mit Smart Markers erstellen. Unser Leitfaden zeigt Ihnen, wie Sie Smart Markers und deren Eigenschaften verarbeiten, um das Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /de/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells APIs stellen die bereit[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) Klasse zum Arbeiten mit Smart Markers, wobei die Formatierungen und Formeln in den Designer-Tabellen platziert und dann damit verarbeitet werden[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)Klasse, um die Daten gemäß den angegebenen Smart Markern zu füllen. Es ist auch möglich, Excel-Diagramme durch die Verarbeitung von Smart Markers zu erstellen, wofür die folgenden Schritte erforderlich sind.

- Erstellung einer Designer-Tabelle
- Verarbeitung der Designer-Tabelle anhand der angegebenen Datenquelle
- Erstellung eines Diagramms basierend auf ausgefüllten Daten

{{% /alert %}}

##  Erstellung einer Designer-Tabelle

Eine Designer-Tabelle ist eine einfache Excel-Datei, die mit der Excel-Anwendung Microsoft oder den APIs Aspose.Cells erstellt wurde und die visuelle Formatierung, Formeln und Smart Marker enthält, wobei der Inhalt zur Laufzeit ausgefüllt werden kann.

Der Einfachheit halber erstellen wir die Designer-Tabelle mit Aspose.Cells for .NET API und verarbeiten sie später zu Demonstrationszwecken anhand einer dynamisch erstellten Datenquelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

##  Verarbeitung einer Designer-Tabelle

Um die Designer-Tabelle zu verarbeiten, muss eine Datenquelle vorhanden sein, die den in der Designer-Tabelle verwendeten Smart Markers entspricht. Beispielsweise haben wir einen Smart Marker-Eintrag als &=Sales.Year erstellt, der die Spalte „Jahr“ in der DataTable „Sales“ darstellt. Falls eine entsprechende Spalte in der Datenquelle nicht verfügbar ist, überspringen die Aspose.Cells-APIs die Verarbeitung für diesen bestimmten Smart Marker und die Daten für den bestimmten Smart Marker werden daher nicht ausgefüllt.

Um diesen Anwendungsfall zu demonstrieren, erstellen wir die Datenquelle von Grund auf und verarbeiten sie anhand der im vorherigen Schritt erstellten Designer-Tabelle. In einem Echtzeitszenario könnten jedoch bereits Daten zur weiteren Verarbeitung verfügbar sein, sodass Sie die Erstellung einer Datenquelle überspringen können, wenn Daten bereits verfügbar sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Die Verarbeitung von Smart Markern ist recht einfach, wie der folgende Codeausschnitt zeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Das obige Code-Snippet verwendet die vorhandene Instanz von[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die im ersten Schritt erstellt wurde. Wenn Sie die Designer-Tabellenkalkulationsdatei bereits auf der Festplatte oder im Speicher haben, können Sie eine Instanz davon erstellen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse durch Laden der vorhandenen Designer-Tabelle.

{{% /alert %}}

##  Erstellung eines Diagramms

 Sobald die Daten vorhanden sind, müssen wir nur noch ein Diagramm basierend auf der Datenquelle erstellen. Um das Beispiel einfach zu halten, verwenden wir das[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)Methode, sodass wir das Diagramm nicht weiter konfigurieren müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
