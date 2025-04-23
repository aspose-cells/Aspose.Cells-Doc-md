---
title: Hur man skapar Lagerdiagram
type: docs
weight: 71
url: /sv/java/how-to-create-stock-charts/
description: Hur man skapar en lagerdiagram, hur man lägger till ett lagerdiagram, hur man genererar ett lagerdiagram.
keywords: Lägg till lagerdiagram, Skapa lagerdiagram, Generera lagerdiagram.
---

{{% alert color="primary" %}}

Detta avsnitt kommer att berätta för dig hur man skapar ett lagerdiagram, vilket inkluderar fyra typer:
- **HLC** – Hög-Låg-Stäng.
- **OHLC** – Öppen-Hög-Låg-Stäng.
- **VHLC** – Volym-Hög-Låg-Stäng.
- **VOHLC** – Volym-Öppen-Hög-Låg-Stäng.

{{% /alert %}}

## **Vad är lagerdiagram?**

Lagerdiagram är ett specifikt diagram som används för att spåra förändringarna i pris på handlade tillgångar. Tillgångar som varor, aktier och kryptovalutor. De låter dig se höga och låga värden över tiden, tillsammans med öppnings- och stängningsvärden i ett diagram. Aspose.Cells erbjuder 4 lagerdiagram och för att använda dessa måste du ha rätt uppsättning data tillgänglig och du måste välja kolumnerna i rätt ordning.

Nedan visas en uppsättning data som visar daglig handelsinformation för en aktie. Vi kommer att använda denna data för att skapa var och en av de 4 lagerdiagram som finns i Aspose.Cells. 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="java" >}}
