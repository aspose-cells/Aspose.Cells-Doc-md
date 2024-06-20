---
title: Ange värdenas formatkod för diagramserier
description: Lär dig hur man ställer in värdenas formatkod för diagramserier i Aspose.Cells for Java. Vår guide hjälper dig att förstå hur du formaterar dina diagramseriedata med rätt formatkod, vilket gör det möjligt för dig att presentera dina data på ett korrekt och professionellt sätt.
keywords: Aspose.Cells for Java, diagramserier, värdenas formatkod, formatering, datapresentation, noggrannhet, professionalism.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/java/set-the-values-format-code-of-chart-series/
---

## **Möjliga användningsscenario**
Du kan ställa in värdenas formatkod för diagramserier med hjälp av metoden [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-). Denna metod är inte bara användbar för serien som är baserad på området inne i arbetsbladet utan fungerar också bra för serien skapad med en matris av värden.
## **Ställ in värdenas formatkod för diagramserier**
Följande exempelkod lägger till en serie i det tomma diagrammet som inte har några serier innan. Den lägger till serien med hjälp av matris av värden. När den har lagt till serien formaterar den den med koden $#,##0 med hjälp av metoden [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) och numret 10000 blir $10,000. Skärmdumpen visar effekten av koden på [prov Excel-fil](51740712.xlsx) och [utdata Excel-fil](51740713.xlsx) efter utförande.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
