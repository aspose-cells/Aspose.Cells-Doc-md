---
title: Inaktivera textrader för dataetiketter i diagrammet
type: docs
weight: 60
url: /sv/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 låter användare rada upp eller rada ur texten i diagrammets datamarkörer. Som standard är texten i datamarkörerna raderad.

{{% /alert %}}

Aspose.Cells tillhandahåller metoden [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Ange **True** eller **False** för att aktivera eller inaktivera textradering på datamarkörerna respektive.

På liknande sätt använder du [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metoden för att ta reda om en datamarkör redan är raderad.

Denna skärmbild visar en provfil från Microsoft Excel som innehåller ett diagram där datamarkörernas text är raderad. Som du kan se kan du markera eller avmarkera alternativet **Rada in text i form** i avsnittet ALIGNMENT i panelen Format Datalabels i Microsoft Excel 2013.

**Rada in datamarkörer**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Följande exempelkod laddar den provfilen från Microsoft Excel med hjälp av Aspose.Cells och inaktiverar textradering på datamarkörerna med hjälp av [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metoden. När koden har exekverats ser diagrammet ut så här. Den tidigare radade texten är nu uradad.

**Visa datamarkörer på en rad endast**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
