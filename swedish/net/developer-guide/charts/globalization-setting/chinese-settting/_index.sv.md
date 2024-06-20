---
title: Konvertera diagram till bild för kinesisk region
description: Lär dig hur man använder Aspose.Cells for .NET sätter kinesisk konfiguration för diagram. Vår guide kommer att demonstrera hur man konfigurerar diagram för att stödja kinesiska tecken och format, inklusive teckensnitt, storlekar, textriktningar och mer.
keywords: Aspose.Cells for .NET, Diagram, Kinesisk konfiguration, Teckensnitt, Teckenstorlek, Textriktning, Stöd.
linktitle: Ställ in kinesisk region
type: docs
weight: 9
url: /sv/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.

{{% /alert %}}

## **Definierar en arvs klass**

Första steget, du behöver definiera en klass "ChartChineseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Sedan, genom att omdefiniera relaterade funktioner, kan du ange texten i diagramelementen på ditt eget sprak.
Kodexempel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Konfigurera kinesiska inställningar för diagram**

I det här steget kommer du att använda klassen "ChartChineseSetttings" du har definierat i det föregående steget.
Kodexempel:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

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
