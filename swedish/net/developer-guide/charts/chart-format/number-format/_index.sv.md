---
title: Ställ in värdeformatets kod för diagramserien
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/net/set-the-values-format-code-of-chart-series/
---
## **Möjliga användningsscenarier**
Du kan ställa in värdeformatkoden för diagramserier med hjälp av[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)fast egendom. Den här egenskapen är inte bara användbar för serien som är baserad på intervallet i kalkylbladet utan fungerar också bra för serien som skapats med en rad värden.
## **Ställ in värdeformatets kod för diagramserien**
Följande exempelkod lägger till en serie i det tomma diagrammet som inte har några serier tidigare. Den lägger till serien med hjälp av arrayen av värden. När den väl lägger till serien, formaterar den den med koden $#,##0 med hjälp av[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)egendom och talet 10 000 blir 10 000 $. Skärmdumpen visar effekten av koden på[exempel på Excel-fil](51740712.xlsx) och[utdata Excel-fil](51740713.xlsx) efter avrättningen.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
