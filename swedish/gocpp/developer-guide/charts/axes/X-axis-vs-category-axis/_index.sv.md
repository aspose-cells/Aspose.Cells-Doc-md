---
title: X Axel Vs. KategorAxel med Golang via C++
linktitle: X axel vs. Kategori axel
description: Lär dig att särskilja mellan X axeln och kategorilänken i Aspose.Cells for C++. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, samt hur du konfigurerar dem efter dina behov.
keywords: Aspose.Cells for C++, X axel, kategorilänk, skillnad, användning, egenskaper, konfiguration.
type: docs
weight: 180
url: /sv/go-cpp/X-axis-vs-category-axis/
---

## **Möjliga användningsscenario**
Det finns olika typer av X-axlar. Medan Y-axeln är en Värde typ axel kan X-axeln vara en Kategori typ axel eller en Värde typ axel. Genom att använda en Värde-axel behandlas datan som kontinuerligt varierande numerisk data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Genom att använda en Kategori-axel behandlas datan som en följd av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i följden. Exemplet nedan illustrerar skillnaden mellan Värde- och Kategori-axlar.
Vår provdata visas i [provtabellfilen](sample.png) nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som Kategorier eller som Värden. Observera att siffrorna inte är jämnt fördelade, och de förekommer inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)

## **Hantera X- och Kategori-axeln som i Microsoft Excel**
Vi kommer visa denna data på två typer av diagram, det första är XY (Scatter) diagram med X som värdeaxel, det andra är linjediagram med X som kategorilänk.

![todo:image_alt_text](compare.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-XAxisVsCategoryAxis.go" >}}
