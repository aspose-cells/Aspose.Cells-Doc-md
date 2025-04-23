---
title: Diagramm durch Verarbeitung von Smart Markers generieren
description: Erfahren Sie, wie Sie Diagramme mit intelligenten Markierungen mithilfe von Aspose.Cells for .NET generieren. Unser Leitfaden zeigt Ihnen, wie Sie intelligente Markierungen und deren Eigenschaften verarbeiten, um das Aussehen und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for .NET, Diagrammerstellung, intelligente Markierungen, Aussehen, Benutzerfreundlichkeit, Verarbeitung.
type: docs
weight: 2100
url: /de/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Aspose.Cells-APIs bieten die [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)-Klasse zum Arbeiten mit Smart Markers, bei der die Formatierung und Formeln in den Designer-Arbeitsmappen platziert und dann mit der [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)-Klasse verarbeitet werden, um die Daten gemäß den angegebenen Smart Markern auszufüllen. Es ist auch möglich, Excel-Diagramme durch Verarbeitung von Smart Markern zu erstellen, was die folgenden Schritte erfordert.

- Erstellung der Designer-Arbeitsmappe
- Verarbeitung des Designer-Arbeitsblatts gegen die angegebene Datenquelle
- Erstellung eines Diagramms basierend auf den befüllten Daten

{{% /alert %}}

## Erstellung des Designer-Arbeitsblatts

Ein Designer-Arbeitsblatt ist eine einfache Excel-Datei, die mit der Microsoft Excel-Applikation oder Aspose.Cells-APIs erstellt wurde und visuelles Formatieren, Formeln und intelligente Markierungen enthält, in der die Inhalte zur Laufzeit befüllt werden können.

Um der Einfachheit willen werden wir das Designer-Arbeitsblatt unter Verwendung der Aspose.Cells for .NET-API erstellen und es später gegen eine dynamisch erstellte Datenquelle für Demon-zwecke verarbeiten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Verarbeitung des Designer-Arbeitsblatts

Um das Designer-Arbeitsblatt zu verarbeiten, muss man eine Datenquelle haben, die den Smart Markers im Designer-Arbeitsblatt entspricht. Zum Beispiel haben wir einen Smart Marker-Eintrag als &=Sales.Year erstellt, der die Spalte Year in der DataTable Sales repräsentiert. Falls eine entsprechende Spalte in der Datenquelle nicht vorhanden ist, überspringen die Aspose.Cells-APIs die Verarbeitung für diesen bestimmten Smart Marker, und infolgedessen werden die Daten für den speziellen Smart Marker nicht befüllt.

Um diesen Anwendungsfall zu demonstrieren, werden wir die Datenquelle von Grund auf erstellen und sie dann gegen das im vorherigen Schritt erstellte Designer-Arbeitsblatt verarbeiten. In einem Echtzeitszenario könnten jedoch bereits Daten für eine weitere Verarbeitung verfügbar sein, sodass Sie die Erstellung der Datenquelle überspringen können, wenn bereits Daten verfügbar sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Die Verarbeitung von Smart Markern ist recht einfach, wie im folgenden Code-Snippet demonstriert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

Das obige Code-Snippet verwendet die vorhandene Instanz der [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse, die im ersten Schritt erstellt wurde. Wenn Sie die Designer-Arbeitsblattdatei bereits auf der Festplatte oder im Speicher haben, können Sie eine Instanz der [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse erstellen, indem Sie das vorhandene Designer-Arbeitsblatt laden.

{{% /alert %}}

## Erstellung eines Diagramms

Sobald die Daten vorhanden sind, müssen wir nur noch ein Diagramm auf Basis der Datenquelle erstellen. Um das Beispiel einfach zu halten, werden wir die [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)-Methode verwenden, damit wir das Diagramm nicht weiter konfigurieren müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
