---
title: Konvertera diagram till bild för japansk region
description: Lär dig hur man använder Aspose.Cells for .NET sätter den japanska konfigurationen för diagrammet. Vår guide kommer att demonstrera hur man konfigurerar diagram för att stödja japanska tecken och formatering, inklusive teckensnitt, storlek, textriktning och mer.
keywords: Aspose.Cells for .NET, Diagram, Japansk konfiguration, teckensnitt, teckenstorlek, textriktning, stöd.
linktitle: Ställ in japansk region
type: docs
weight: 10
url: /sv/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in japansk region för ett diagram.

{{% /alert %}}

## **Definierar en arvs klass**

Första steget, du behöver definiera en klass "ChartJapaneseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Sedan, genom att omdefiniera relaterade funktioner, kan du ange texten i diagramelementen på ditt eget sprak.
Kodexempel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Konfigurera japanska inställningar för diagram**

I detta steg kommer du att använda klassen "ChartJapaneseSetttings" som du definierade i det föregående steget.
Kodexempel:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

## **Slutsats**

I det här exemplet, om du inte anger japansk region för ett diagram, kan följande diagramelement renderas på standardspråket, såsom engelska.
Efter ovanstående operation kan vi få en utdata-diagrambild med japansk region.

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|
| :- | :- | :- |
|axeltitelnamn|軸タイトル|Axeltitel|
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|
|diagramtitelnamn|グラフ タイトル|Diagramtitel|
|legend öka namn|ぞうか|Ökning|
|legend minskning namn|削減|Minskning|
|legend totalt namn|すべての|Totalt|
|annat namn|その他|Övrigt|
|Serienamn|シリーズ|Serie|
