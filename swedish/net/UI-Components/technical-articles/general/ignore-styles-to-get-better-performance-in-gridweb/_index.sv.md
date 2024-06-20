---
title: Ignorera stilar för bättre prestanda i GridWeb
type: docs
weight: 1060
url: /sv/net/aspose-cells-gridweb/ignorestylewithnodata
description: Den här artikeln beskriver hur man använder IgnoreStyleWithNoData för bättre prestanda i GridWeb.
keywords: GridWeb,performance
---

## **Möjliga användningsscenario**
Använd [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)-egenskapen för att ladda färre nödvändiga rader/kolumner från arbetsbok.

## **Få bättre prestanda vid inläsning av arbetsbok**
Var god kontrollera den [provexempelfil](largerowswithstyle.xlsx) 

När du ställer in IgnoreStyleWithNoData = true;

Som du kan se, visas rader (till 15) och kolumner (till L), det kommer inte att visa de sista kontinuerliga raderna och kolumnerna utan data i celler. Laddningstiden blir således mindre.

![arbetsbok med ignorera stil](ignorestyletrue.png)


När IgnoreStyleWithNoData = false; (standardvärdet är false)

Som du kan se, visas mycket fler rader (till 500) och kolumner (till CZ)

Från rad 16 till rad 500 har vissa av cellerna fått bode rstyle, men innehåller ingen data.

Från kolumn M till kolumn CZ har vissa av cellerna fått bode rstyle, men innehåller ingen data.

![arbetsbok utan ignorera stil](ignorestylefalse.png)



