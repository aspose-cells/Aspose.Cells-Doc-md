---
title: Ange värdenas formatkod för diagramserier
description: Lär dig att ställa in värdenas formatkod för diagramserier i Aspose.Cells for .NET. Vår guide hjälper dig att förstå hur man formaterar dina diagramseriedata med lämplig formatkod, vilket gör det möjligt för dig att presentera dina data på ett korrekt och professionellt sätt.
keywords: Aspose.Cells for .NET, diagramserier, värdenas formatkod, formatering, datapresentation, noggrannhet, professionalism.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/net/set-the-values-format-code-of-chart-series/
---

## **Möjliga användningsscenario**
Du kan ställa in värdenas formatkod för diagramserier med hjälp av egenskapen [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). Denna egenskap är inte bara användbar för serier som är baserade på området inuti arbetsbladet utan fungerar också bra för serier skapade med en array av värden.
## **Ställ in värdenas formatkod för diagramserier**
Följande provkod lägger till en serie i det tomma diagrammet som inte har någon serie tidigare. Den lägger till serien med hjälp av en array av värden. När det lägger till serien formaterar det den med koden $#,##0 med hjälp av egenskapen [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) och talet 10000 blir $10,000. Skärmdumpen visar effekten av koden på [prov Excel-filen](51740712.xlsx) och [utdata Excel-filen](51740713.xlsx) efter utförande.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
{{< app/cells/assistant language="csharp" >}}
