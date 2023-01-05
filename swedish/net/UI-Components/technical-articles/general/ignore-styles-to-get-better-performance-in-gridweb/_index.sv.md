---
title: Ignorera stilar för att få bättre prestanda i GridWeb
type: docs
weight: 1060
url: /sv/net/aspose-cells-gridweb/ignorestylewithnodata
description: Den här artikeln beskriver hur du använder IgnoreStyleWithNoData för att få bättre prestanda för Aspose.Cells.GridWeb-biblioteket.
keywords: performance
---
## **Möjliga användningsscenarier**
 Snälla använd[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)egenskap för att läsa in färre nödvändiga rader/kolumner från arbetsboken.
 
## **Få bättre prestanda när arbetsboken laddas**
 Vänligen kontrollera[exempel på excel-fil](largerowswithstyle.xlsx) 

När satt IgnoreStyleWithNoData = true;

Som du kan se visar den rader (till 15) och kolumner (till L), den kommer inte att visa de sista raderna och kolumnerna utan data i cellerna. Därför blir laddningstiden kortare.

![arbetsbok med ignorera stil](ignorestyletrue.png)


När inställt IgnoreStyleWithNoData = false;(standardvärdet är false)

Som du kan se visar den mycket fler rader (till 500) och kolumner (till CZ)

Från rad 16 till rad 500 har några av cellerna angett boderstilen, men cellerna innehåller inga data.

Från kolumn M till kolumn CZ har några av cellerna angett boderstilen, men cellerna innehåller inga data.

![arbetsbok utan att ignorera stil](ignorestylefalse.png)
 
 
 