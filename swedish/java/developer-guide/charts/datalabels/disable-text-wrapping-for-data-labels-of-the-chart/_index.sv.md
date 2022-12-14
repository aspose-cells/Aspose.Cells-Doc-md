---
title: Inaktivera textbrytning för dataetiketter i diagrammet
type: docs
weight: 60
url: /sv/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 tillåter användare att radbryta eller packa upp text inuti ett diagrams dataetiketter. Som standard är dataetikettens text radbruten.

{{% /alert %}}

Aspose.Cells tillhandahåller[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metod. Satt till**Sann** eller**Falsk** för att aktivera eller inaktivera textbrytning på dataetiketter.

 Använd på samma sätt[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)metod för att ta reda på om en dataetikett redan är inslagen.

Den här skärmdumpen visar ett exempel på en Microsoft Excel-fil som innehåller ett diagram där texten till dataetiketterna är inlindade. Som du kan se kan du kontrollera eller rensa**Slå in text i form** alternativet i avsnittet ALIGNMENT på panelen Formatera dataetiketter i Microsoft Excel 2013.

**Slå in dataetiketter**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 Exempelkoden som följer läser in exempelfilen i Microsoft Excel med Aspose.Cells och inaktiverar dataetiketttextbrytning med hjälp av[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)metod. När koden exekveras ser diagrammet ut så här. Den tidigare raderade texten är nu uppackad.

**Visar endast dataetiketter på en rad**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
