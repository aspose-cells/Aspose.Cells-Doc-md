---
title: Ställ in värdeformatets kod för diagramserien
description: Lär dig hur du ställer in värdeformatkoden för diagramserier i Aspose.Cells for Java. Vår guide hjälper dig att förstå hur du formaterar dina diagramseriedata med hjälp av rätt formatkod, så att du kan presentera dina data korrekt och professionellt.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/java/set-the-values-format-code-of-chart-series/
---
##  **Möjliga användningsscenarier**
Du kan ställa in värdeformatkoden för diagramserier med hjälp av[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) metod. Den här metoden är inte bara användbar för serien som är baserad på intervallet inuti kalkylbladet utan fungerar också bra för serien som skapats med en rad värden.
##  **Ställ in värdeformatets kod för diagramserien**
 Följande exempelkod lägger till en serie i det tomma diagrammet som inte har några serier tidigare. Den lägger till serien med hjälp av arrayen av värden. När den väl lägger till serien, formaterar den den med koden $#,##0 med hjälp av[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) metod och talet 10 000 blir 10 000 $. Skärmdumpen visar effekten av koden på[exempel på Excel-fil](51740712.xlsx) och[utdata Excel-fil](51740713.xlsx) efter avrättningen.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
