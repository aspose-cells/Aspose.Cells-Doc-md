---
title: Konvertera diagram till bild för den kinesiska regionen
description: Lär dig hur du använder Aspose.Cells for .NET ställer in kinesisk konfiguration för sjökort. Vår guide kommer att visa hur du konfigurerar diagram för att stödja kinesiska tecken och format, inklusive teckensnitt, storlekar, textanvisningar och mer.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Ställ in kinesisk region
type: docs
weight: 9
url: /sv/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.

{{% /alert %}}

##  **Definierar en arvsklass**

 Första steget måste du definiera en klass "ChartChineseSettings" som ärver från[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Sedan, genom att skriva om de relaterade funktionerna, kan du ställa in texten i diagramelementen på ditt eget språk.
Kodexempel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Konfigurera kinesiska inställning för diagram**

I det här steget kommer du att använda klassen "ChartChineseSettings" som du definierade i föregående steg.
Kodexempel:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Sedan kan du se effekten i utdatabilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

##  **Slutsats**

I det här exemplet, om du inte ställer in kinesisk region för ett diagram, kan följande diagramelement återges på standardspråket, till exempel engelska.
Efter operationen ovan kan vi få en utdatadiagrambild med den kinesiska regionen.

|**Element som stöds**|**Värde i detta exempel**|**standardvärde i engelsk miljö**|
| :- | :- | :- |
|Axeltitelnamn|坐标轴标题|Axeltitel|
|Axelenhetsnamn|百,千...|Hundra, tusentals...|
|Diagramtitelnamn|图表标题|Diagramtitel|
|Förklaring Öka namn|增加|Öka|
|Förklaring Minska namn|减少|Minska|
|Legend Totalt namn|汇总|Total|
|Annat namn|其他|Övrig|
|Seriens namn|系列|Serier|
