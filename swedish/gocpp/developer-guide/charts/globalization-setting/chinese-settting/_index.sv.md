---
title: Konvertera diagram till bild för Kina regionen med Golang via C++
linktitle: Ställ in kinesisk region
description: Lär dig hur du använder Aspose.Cells for C++ för att ställa in kinesisk konfiguration för diagram. Vår guide visar hur du konfigurerar diagram för att stödja kinesiska tecken och format, inklusive teckensnitt, storlekar, texts riktningar och mer.
keywords: Aspose.Cells for C++, diagram, kinesisk konfiguration, teckensnitt, teckenstorlek, textriktning, stöd.
type: docs
weight: 9
url: /sv/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.

{{% /alert %}}

## **Definierar en arvs klass**

 Första steget, du måste definiera en klass "ChartChineseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/). 
 Sedan, genom att överskrida relaterade funktioner, kan du ställa in texten på diagrammets element på ditt eget språk.

Kodexempel:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

## **Slutsats**

I det här exemplet, om du inte ställer in kinesisk region för ett diagram, kan följande diagramelement renderas på det vanliga språket, såsom engelska.
Efter ovanstående åtgärd kan vi få en utmatningsdiagrambild med kinesisk region.

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|
| :- | :- | :- |
|Axel Titel Namn|坐标轴标题|Axis Title|
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|
|Diagram Titel Namn|图表标题|Chart Title|
|Legend Öka Namn|增加|Increase|
|Legend Minska Namn|减少|Decrease|
|Legend Total Namn|汇总|Total|
|Annat Namn|其他|Other|
|Serienamn|系列|Series|
