---
title: Hur man skapar Lagerdiagram
description: Aktie diagram är en specifik typ av diagram som används för att spåra förändringar i priset på handlade tillgångar. I den här avsnittet kommer vi att visa dig hur du enkelt skapar olika typer av aktie diagram med hjälp av Aspose.Cells API er. Specifikt kommer vi att täcka följande typer av aktie diagram Hög Låg Stäng (HLC) aktie diagram, Öppen Hög Låg Stäng (OHLC) diagram, Volym Hög Låg Stäng (VHLC) aktie diagram och Volym Öppen Hög Låg Stäng (VOHLC) aktie diagram. 
keywords: Skapa Aktie diagram, Aspose.Cells, Marknadsdata Visualisering, Aktiemarknadsanalys, Steg för steg guide.
type: docs
weight: 71
url: /sv/net/how-to-create-stock-charts/
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

Följande dataset visar den dagliga handelsinformationen för en aktie. Vi kommer att använda dessa data för att skapa fyra typer av aktie-diagram: Hög-Låg-Stäng (HLC) aktie-diagram, Öppen-Hög-Låg-Stäng (OHLC) diagram, Volym-Hög-Låg-Stäng (VHLC) aktie-diagram och Volym-Öppen-Hög-Låg-Stäng (VOHLC) aktie-diagram. 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="csharp" >}}
