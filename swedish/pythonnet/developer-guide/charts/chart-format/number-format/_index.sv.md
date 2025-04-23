---
title: Ange värdenas formatkod för diagramserier
description: Lär dig hur man ställer in värdeformatkoden för diagramserier i Aspose.Cells för Python via .NET. Vår guide hjälper dig att förstå hur man formaterar diagramseriedata med rätt formatkod, så att du kan presentera dina data noggrant och professionellt.
keywords: Aspose.Cells för Python via .NET, diagramserier, värdeformatkod, formatering, dataframställning, noggrannhet, professionalism.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/python-net/set-the-values-format-code-of-chart-series/
---

## **Möjliga användningsscenario**
Du kan ställa in värdeformatkoden för diagramserier med hjälp av [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) egenskapen. Denna egenskap är inte bara användbar för serien som är baserad på området inuti kalkylbladet utan fungerar också väl för serien som skapats med en värde-array.

## **Ställ in värdenas formatkod för diagramserier**
Følgende exempel kod lägger till en serie i ett tomt diagram som inte hade någon serie tidigare. Den lägger till serien med hjälp av värdearrayen. När serien har lagts till formateras den med koden $#,##0 med egenskapen [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code), och numret 10000 blir $10,000. Skärmbilden visar effekten av koden på [exempel-Excelfilen](51740712.xlsx) och [utdata-Excelfilen](51740713.xlsx) efter körning.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
