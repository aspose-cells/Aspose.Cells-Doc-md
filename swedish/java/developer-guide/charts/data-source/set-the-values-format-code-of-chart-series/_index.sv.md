---
title: Ställ in värdeformatets kod för diagramserien
type: docs
weight: 60
url: /sv/java/set-the-values-format-code-of-chart-series/
---
## **Möjliga användningsscenarier**

Du kan ställa in värdeformatkoden för diagramserier med hjälp av[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)fast egendom. Den här egenskapen är inte bara användbar för serier som är baserade på intervallet i kalkylbladet utan fungerar också bra för serier som skapats med en rad värden.

## **Ställ in värdeformatets kod för diagramserien**

Följande exempelkod lägger till en serie i det tomma diagrammet som inte har några serier tidigare. Den lägger till serien med hjälp av arrayen av värden. När den väl lägger till serien, formaterar den den med koden $#,##0 med hjälp av[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)egendom och talet 10 000 blir 10 000 $. Skärmdumpen visar effekten av koden på[exempel på Excel-fil](51740736.xlsx)och[utdata Excel-fil](51740735.xlsx)efter avrättningen.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-SetValuesFormatCodeOfChartSeries.java" >}}
