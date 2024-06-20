---
title: Arbeitsblatt des Diagramms abrufen
type: docs
weight: 80
url: /de/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über einen Diagrammverweis zugreifen. Aspose.Cells bietet die [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)-Eigenschaft, die den Verweis auf das Arbeitsblatt zurückgibt, das das Diagramm enthält.

{{% /alert %}}

## Beispiel

Im folgenden Beispiel ist gezeigt, wie die [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)-Eigenschaft verwendet wird. Der Code druckt zunächst den Namen des Arbeitsblatts, greift dann auf das erste Diagramm auf dem Arbeitsblatt zu. Danach wird erneut der Arbeitsblattname gedruckt, mithilfe der [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)-Eigenschaft.

### Java-Code zum Zugreifen auf das Arbeitsblatt des Diagramms

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Von der Beispiellösung generierte Konsolenausgabe

Nachfolgend finden Sie die Konsolenausgabe, die der Beispielcode ergibt. Wie Sie sehen können, gibt es sowohl beim ersten als auch beim zweiten Mal den gleichen Arbeitsblattnamen aus.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
