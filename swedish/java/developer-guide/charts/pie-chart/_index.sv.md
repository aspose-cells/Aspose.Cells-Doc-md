---
title: Skapa cirkeldiagram med ledarlinjer
linktitle: Cirkeldiagram
type: docs
weight: 170
url: /sv/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Den här artikeln förklarar hur man skapar ett cirkeldiagram med ledarlinjer från grunden medan du använder Aspose.Cells for Java API. I Excel är alternativet 'Visa ledarlinjer' inställt som standard, så när du skapar ett cirkeldiagram i Excel visas ledarlinjerna. Men när du skapar en liknande graf med Aspose.Cells API måste du explicit ställa in [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines) -egenskapen.

{{% /alert %}}

## **Skapa cirkeldiagram med ledarlinjer**

För att demonstrera användningen av Aspose.Cells for Java API för att skapa ett cirkeldiagram med ledarlinjer kommer vi först att skapa en ny [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) och ange lite data som kommer att fungera som datorkälla för serier. När datan är på plats kommer vi att lägga till en [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) av typ [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) till diagramkollectionen och ställa in dess olika aspekter för att få önskad diagramvy.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Följande cirkeldiagram**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Relaterade artiklar

- [Skapa och anpassa diagram](/cells/sv/java/creating-and-customizing-charts/)
- [Diagramformatering](/cells/sv/java/chart-formatting/)
{{< app/cells/assistant language="java" >}}
