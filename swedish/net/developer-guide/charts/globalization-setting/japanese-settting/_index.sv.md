---
title: Konvertera diagram till bild för japansk region
linktitle: Ställ in japansk region
type: docs
weight: 10
url: /sv/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

I det här avsnittet kommer vi att visa dig hur du ställer in japansk region för ett diagram.

{{% /alert %}}

##  **Definierar en arvsklass**

 Första steget måste du definiera en klass "ChartJapaneseSettings" som ärver från[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Sedan, genom att skriva om de relaterade funktionerna, kan du ställa in texten i diagramelementen på ditt eget språk.
Kodexempel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Konfigurera japansk inställning för diagram**

I det här steget kommer du att använda klassen "ChartJapaneseSettings" som du definierade i föregående steg.
Kodexempel:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Sedan kan du se effekten i utdatabilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

##  **Slutsats**

I det här exemplet, om du inte anger japansk region för ett diagram, kan följande diagramelement återges på standardspråket, till exempel engelska.
Efter ovanstående operation kan vi få en utdatadiagrambild med japansk region.

|**Element som stöds**|**Värde i detta exempel**|**standardvärde i engelsk miljö**|
| :- | :- | :- |
|Axeltitelnamn|軸タイトル|Axeltitel|
|Axelenhetsnamn|百,千...|Hundra, tusentals...|
|Diagramtitelnamn|グラフ タイトル|Diagramtitel|
|Förklaring Öka namn|ぞうか|Öka|
|Förklaring Minska namn|削減|Minska|
|Legend Totalt namn|すべての|Total|
|Annat namn|その他|Övrig|
|Seriens namn|シリーズ|Serier|
