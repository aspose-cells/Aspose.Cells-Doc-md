---
title: Sätt värdeformatkod för Diagramserie med Golang via C++
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/go-cpp/set-the-values-format-code-of-chart-series/
description: Lär dig hur du ställer in värden formatkod för diagramserier i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du formaterar dina diagramdataserier med rätt formatkod för att presentera data noggrant och professionellt.
keywords: Aspose.Cells for C++, diagramserier, värden formatkod, formatering, datapresentation, noggrannhet, professionalism.
---

## **Möjliga användningsscenario**
Du kan ställa in värdeformatkoden för diagramserien med hjälp av [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/)-egenskapen. Denna egenskap är inte bara användbar för serien som är baserad på området inuti kalkbladet utan fungerar också bra för serien skapad med en array av värden.

## **Ställ in värdenas formatkod för diagramserier**
Följande exempel kod lägger till en serie i ett tomt diagram som inte hade någon serie tidigare. Den lägger till serien med hjälp av en array av värden. När den har lagt till serien formaterar den den med kod `$#,##0` med hjälp av [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/)-egenskapen och numret `10000` blir `$10,000`. Skärmbilden visar effekten av koden på [exempel Excel-fil](51740712.xlsx) och [utdata Excel-fil](51740713.xlsx) efter körning.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
