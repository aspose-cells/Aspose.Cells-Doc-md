---
title: Skapa Volym Öppen Hög Låg Stäng (VOHLC) Aktiediagram
type: docs
weight: 183
url: /sv/java/create-volume-high-low-close-stock-chart/
description: Hur man skapar en volym hög låg slutföra (VHLC) Lagerdiagram, hur man lägger till en Volym Hög Låg Slutför (VHLC) Lagerdiagram, hur man genererar en Volym Hög Låg Slutför (VHLC) Lagerdiagram.
keywords: Lägg till Volym Hög Låg Slutför (VHLC) Lagerdiagram, Skapa Volym Hög Låg Slutför (VHLC) Lagerdiagram, Generera Volym Hög Låg Slutför (VHLC) Lagerdiagram.
---

## **Möjliga användningsscenario**
Det tredje aktiediagrammet vi ska titta på är Volym Hög Låg Stäng-diagrammet. Det är återigen viktigt att upprepa att data måste vara i rätt ordning. Om du behöver omorganisera din datatabell, bör du göra det innan du skapar ditt diagram.
Detta diagram inkluderar en kolumn för volym omedelbart efter den första (kategori) kolumnen, och diagrammen inkluderar ett kolumnsdiagram på primäraxeln som visar denna volym, medan priserna flyttas till sekundäraxeln.

![todo:image_alt_text](data.png)
## **Volym-Öppen-Hög-Låg-Stäng (VOHLC) aktiediagram**

![todo:image_alt_text](sample.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Volume-Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
{{< app/cells/assistant language="java" >}}
