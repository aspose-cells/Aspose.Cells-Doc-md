---
title: X axel vs. Kategori axel
description: Lär dig hur man skiljer mellan X axeln och kategoraxeln i Aspose.Cells för Python via .NET. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, samt hur man konfigurerar dem efter behov.
keywords: Aspose.Cells för Python via .NET, X axel, kategori axel, skillnad, användning, egenskaper, konfiguration.
type: docs
weight: 180
url: /sv/python-net/X-axis-vs-category-axis/
---

## **Möjliga användningsscenario**
Det finns olika typer av X-axlar. Medan Y-axeln är en Värde typ axel kan X-axeln vara en Kategori typ axel eller en Värde typ axel. Genom att använda en Värde-axel behandlas datan som kontinuerligt varierande numerisk data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Genom att använda en Kategori-axel behandlas datan som en följd av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i följden. Exemplet nedan illustrerar skillnaden mellan Värde- och Kategori-axlar.
Vår provdata visas i [provtabellfilen](sample.png) nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som Kategorier eller som Värden. Observera att siffrorna inte är jämnt fördelade, och de förekommer inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)

## **Hantera X- och Kategori-axeln som i Microsoft Excel**
Vi kommer att visa dessa data på två typer av diagram, det första diagrammet är XY (Spridnings) diagram X som Värde axel, det andra diagrammet är linjediagram X som Kategori axel.

![todo:image_alt_text](compare.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-X-axis-vs-category-axis.py" >}}
