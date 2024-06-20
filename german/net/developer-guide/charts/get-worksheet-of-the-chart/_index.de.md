---
title: Arbeitsblatt des Diagramms abrufen
description: Erfahren Sie, wie Sie das mit einem Excel Diagramm verbundene Arbeitsblatt mithilfe von Aspose.Cells for .NET abrufen können. Unser Leitfaden zeigt Ihnen, wie Sie auf das Arbeitsblatt zugreifen und Operationen zum Manipulieren der zugrunde liegenden Daten des Diagramms durchführen können.
keywords: Aspose.Cells for .NET, Excel Diagramme, Arbeitsblätter, Datenmanipulation, zugrunde liegende Daten, Operationen.
type: docs
weight: 1000
url: /de/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über einen Diagrammverweis zugreifen. Aspose.Cells bietet die [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)-Eigenschaft, die den Verweis auf das Arbeitsblatt zurückgibt, das das Diagramm enthält.

{{% /alert %}}

Im folgenden Beispiel ist gezeigt, wie die [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)-Eigenschaft verwendet wird. Der Code druckt zunächst den Namen des Arbeitsblatts, greift dann auf das erste Diagramm auf dem Arbeitsblatt zu. Danach wird erneut der Arbeitsblattname gedruckt, mithilfe der [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)-Eigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Unten ist die Konsolenausgabe, die das Beispiel des Codes ergibt. Wie Sie sehen können, druckt es den Arbeitsblattnamen beide Male gleich aus.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
